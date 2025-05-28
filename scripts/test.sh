#!/bin/bash

# LLM TOPIX Test Runner Script
# This script runs all tests for both backend and frontend

set -e

echo "🧪 Running LLM TOPIX test suite..."

# Function to run backend tests
run_backend_tests() {
    echo "🐍 Running backend tests..."
    cd backend
    
    # Ensure test database is ready
    export TEST_DATABASE_URL="postgresql://postgres:password@localhost:5433/llm_topix_test"
    
    # Setup test database schema
    poetry run python -c "
from app.models.article import Base
from app.config.database import get_test_database_url
from sqlalchemy import create_engine

engine = create_engine(get_test_database_url())
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print('Test database schema created!')
"
    
    # Run pytest with coverage
    poetry run pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html
    
    cd ..
    echo "✅ Backend tests completed!"
}

# Function to run frontend tests
run_frontend_tests() {
    echo "⚛️ Running frontend tests..."
    cd frontend
    
    # Run Jest tests
    npm test -- --coverage --watchAll=false
    
    cd ..
    echo "✅ Frontend tests completed!"
}

# Function to run linting
run_linting() {
    echo "🔍 Running code quality checks..."
    
    # Backend linting
    echo "🐍 Checking backend code quality..."
    cd backend
    poetry run black --check .
    poetry run flake8 .
    poetry run mypy app/
    cd ..
    
    # Frontend linting
    echo "⚛️ Checking frontend code quality..."
    cd frontend
    npm run lint
    cd ..
    
    echo "✅ Code quality checks completed!"
}

# Parse command line arguments
case "${1:-all}" in
    backend)
        run_backend_tests
        ;;
    frontend)
        run_frontend_tests
        ;;
    lint)
        run_linting
        ;;
    all)
        run_linting
        run_backend_tests
        run_frontend_tests
        ;;
    *)
        echo "Usage: $0 [backend|frontend|lint|all]"
        echo "  backend  - Run only backend tests"
        echo "  frontend - Run only frontend tests"
        echo "  lint     - Run only linting and code quality checks"
        echo "  all      - Run all tests and checks (default)"
        exit 1
        ;;
esac

echo ""
echo "🎉 All tests completed successfully!"
echo "📊 Coverage reports:"
echo "  - Backend: backend/htmlcov/index.html"
echo "  - Frontend: frontend/coverage/lcov-report/index.html"