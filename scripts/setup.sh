#!/bin/bash

# LLM TOPIX Development Environment Setup Script
# This script sets up the complete development environment

set -e

echo "🚀 Setting up LLM TOPIX development environment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cat > .env << EOF
# Database Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/llm_topix_dev
TEST_DATABASE_URL=postgresql://postgres:password@localhost:5433/llm_topix_test

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1

# Frontend Configuration
BACKEND_URL=http://localhost:5000
NODE_ENV=development
EOF
fi

# Start database services
echo "🐘 Starting PostgreSQL databases..."
docker-compose up -d postgres postgres_test

# Wait for databases to be ready
echo "⏳ Waiting for databases to be ready..."
until docker-compose exec postgres pg_isready -U postgres; do
    sleep 2
done

echo "⏳ Waiting for test database to be ready..."
until docker-compose exec postgres_test pg_isready -U postgres; do
    sleep 2
done

# Setup backend
echo "🐍 Setting up backend environment..."
cd backend

# Install Poetry if not already installed
if ! command -v poetry &> /dev/null; then
    echo "📦 Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
poetry install

# Run database migrations (create tables)
echo "🗄️ Setting up database schema..."
poetry run python -c "
from app.models.article import Base, Article
from app.config.database import get_database_url
from sqlalchemy import create_engine

engine = create_engine(get_database_url())
Base.metadata.create_all(engine)
print('Database schema created successfully!')
"

cd ..

# Setup frontend
echo "⚛️ Setting up frontend environment..."
cd frontend

# Install Node.js dependencies
if [ -f package-lock.json ]; then
    echo "📦 Installing Node.js dependencies..."
    npm ci
else
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

cd ..

echo "✅ Environment setup completed!"
echo ""
echo "🎯 Next steps:"
echo "  1. Run 'docker-compose up -d' to start all services"
echo "  2. Backend API will be available at http://localhost:5000"
echo "  3. Frontend will be available at http://localhost:3000"
echo "  4. Run tests with './scripts/test.sh'"
echo ""
echo "🔧 Development commands:"
echo "  - Start services: docker-compose up -d"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop services: docker-compose down"
echo "  - Run tests: ./scripts/test.sh"