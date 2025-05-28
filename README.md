# LLM TOPIX

> A comprehensive web platform for LLM and generative AI news, featuring analysis and insights from major LLM providers (Gemini, ChatGPT, Claude).

[![Built with TDD](https://img.shields.io/badge/Built%20with-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![Code Coverage](https://img.shields.io/badge/Coverage-90%25+-brightgreen.svg)](#testing)
[![Performance](https://img.shields.io/badge/API%20Response-<50ms-blue.svg)](#performance-requirements)
[![Accessibility](https://img.shields.io/badge/WCAG-2.1%20AA-blue.svg)](#accessibility)

## 🎯 Project Overview

LLM TOPIX is designed to be the definitive source for LLM and generative AI news, built with enterprise-grade architecture and strict Test-Driven Development principles. Our platform delivers curated content with performance, accessibility, and security at its core.

### Key Features

#### 🚀 Phase 1 (Current - MVP)
- ✅ **Latest Articles Display**: Homepage showcasing the 5 most recent LLM news articles
- ✅ **Responsive Article Cards**: Clean, accessible cards with title, summary (100 chars), publication date, and source
- ✅ **Performance Optimized**: Sub-50ms API responses and <16ms frontend interactions
- ✅ **Accessibility First**: WCAG 2.1 AA compliant with keyboard navigation and screen reader support
- ✅ **RESTful API**: Robust error handling with standardized response formats
- ✅ **Complete TDD Implementation**: Comprehensive test coverage following RED → GREEN → REFACTOR methodology

#### 🔮 Phase 2 (Planned)
- [ ] **Advanced Search & Filtering**: Content discovery with multiple filter criteria
- [ ] **User Authentication**: Personalized preferences and reading history
- [ ] **LLM Document Analysis**: AI-powered summarization and insights
- [ ] **Real-time Updates**: Live news feeds with push notifications
- [ ] **Content Management System**: Admin interface for content curation

## 🛠 Technology Stack

### Frontend Architecture
- **Framework**: Next.js 14+ with TypeScript (Strict Mode)
- **UI Library**: React 18+ with functional components and hooks
- **Styling**: CSS Modules with performance optimization
- **Type Safety**: Branded types and comprehensive TypeScript interfaces
- **Testing**: Jest with React Testing Library
- **Performance**: React.memo, useMemo, and component optimization

### Backend Architecture
- **Framework**: Python Flask with SQLAlchemy ORM
- **Language**: Python 3.11+ with comprehensive type hints
- **Database**: PostgreSQL 15+ with optimized indexing
- **API Design**: RESTful endpoints with standardized error responses
- **Performance Monitoring**: Built-in execution time tracking
- **Testing**: PyTest with 90%+ coverage requirement

### Development & Operations
- **Containerization**: Docker with multi-service docker-compose setup
- **Dependency Management**: Poetry (Python), npm (Node.js)
- **Code Quality**: Black, Flake8, MyPy (Python); ESLint, Prettier (TypeScript)
- **Version Control**: Git with Conventional Commits specification
- **CI/CD**: GitHub Actions with automated testing and deployment

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:
- **Docker** and **Docker Compose** (latest stable versions)
- **Git** for version control
- **Make** (optional, for convenience scripts)

### Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/Be114/LLM_TOPIX.git
cd LLM_TOPIX

# 2. Make scripts executable
chmod +x scripts/*.sh

# 3. Setup development environment (initializes database, installs dependencies)
./scripts/setup.sh

# 4. Start all services in development mode
docker-compose up -d

# 5. Verify setup by running tests
./scripts/test.sh

# 6. View logs (optional)
docker-compose logs -f
```

### Development Scripts

Our project includes convenient development scripts for common tasks:

```bash
# Start development environment
./scripts/setup.sh

# Run all tests (backend + frontend)
./scripts/test.sh

# Run specific test suites
./scripts/test.sh backend    # Backend tests only
./scripts/test.sh frontend   # Frontend tests only
./scripts/test.sh lint       # Code quality checks

# Development server management
docker-compose up -d         # Start all services
docker-compose down          # Stop all services
docker-compose restart      # Restart services
```

### Access Points

Once the setup is complete, access the application at:

- **🌐 Frontend Application**: http://localhost:3000
- **⚡ Backend API**: http://localhost:5000
- **💚 Health Check**: http://localhost:5000/health
- **📰 Latest Articles API**: http://localhost:5000/api/articles/latest
- **📊 API Documentation**: http://localhost:5000/docs (if available)

## 🏗 Project Architecture

```
LLM_TOPIX/
├── 🗄️ backend/                    # Flask API Server
│   ├── app/
│   │   ├── 📊 models/              # SQLAlchemy data models
│   │   │   ├── article.py          # Article model with optimized queries
│   │   │   └── __init__.py
│   │   ├── 🔧 services/            # Business logic layer
│   │   │   ├── article_service.py  # Article operations with performance monitoring
│   │   │   ├── formatters.py       # Data formatting utilities
│   │   │   └── __init__.py
│   │   ├── 🛤️ routes/              # API endpoint definitions
│   │   │   ├── articles.py         # Article-related endpoints
│   │   │   └── __init__.py
│   │   ├── ⚙️ config/              # Configuration management
│   │   │   ├── constants.py        # Application constants
│   │   │   ├── database.py         # Database configuration
│   │   │   └── __init__.py
│   │   ├── 🔧 utils/               # Utility functions
│   │   │   ├── response_helpers.py # Standardized API responses
│   │   │   └── __init__.py
│   │   ├── exceptions.py           # Custom exception hierarchy
│   │   └── app.py                  # Application factory
│   ├── 🧪 tests/                   # Backend test suite
│   │   ├── test_api_endpoints.py   # Integration tests
│   │   ├── test_article_service.py # Unit tests
│   │   └── __init__.py
│   ├── pyproject.toml              # Poetry configuration
│   └── Dockerfile                  # Backend container definition
├── 🎨 frontend/                    # Next.js Application
│   ├── src/
│   │   ├── 🧩 components/          # React components
│   │   │   ├── ArticleCard.tsx     # Article display component
│   │   │   ├── ArticleCard.module.css
│   │   │   └── __tests__/          # Component tests
│   │   │       └── ArticleCard.test.tsx
│   │   ├── 📄 pages/               # Next.js pages (auto-routing)
│   │   ├── 🏷️ types/               # TypeScript type definitions
│   │   │   └── article.ts          # Article-related types and interfaces
│   │   └── 🔧 utils/               # Frontend utilities
│   ├── 🧪 tests/                   # Frontend test configuration
│   ├── package.json                # npm configuration
│   ├── next.config.js              # Next.js configuration
│   ├── tsconfig.json               # TypeScript configuration
│   ├── jest.setup.js               # Jest test setup
│   └── Dockerfile                  # Frontend container definition
├── 🗃️ database/                    # Database schema and migrations
│   └── init.sql                    # Initial database schema
├── 📜 scripts/                     # Development and deployment scripts
│   ├── setup.sh                    # Environment setup
│   └── test.sh                     # Test execution
├── 🐳 docker-compose.yml           # Multi-service container orchestration
├── 📖 CLAUDE.md                    # Development constitution and guidelines
└── 📝 README.md                    # This file
```

## 📡 API Documentation

Our API follows RESTful principles with consistent response formats and comprehensive error handling.

### Base Information
- **Base URL**: `http://localhost:5000/api`
- **Response Format**: JSON
- **Authentication**: Not required for current endpoints
- **Rate Limiting**: Not implemented (Phase 2)

### Core Endpoints

#### `GET /api/articles/latest`
Retrieves the 5 most recent LLM and AI news articles.

**Parameters**: None

**Success Response** (200):
```json
[
  {
    "id": 1,
    "title": "Breaking: GPT-5 Architecture Revealed",
    "summary_truncated": "OpenAI unveils revolutionary architecture improvements in their latest model, featuring enhanced reasoning...",
    "published_at": "2024-01-15T10:30:00Z",
    "source_url": "https://example.com/gpt5-architecture"
  },
  {
    "id": 2,
    "title": "Google Announces Gemini Ultra 2.0",
    "summary_truncated": "Google's latest multimodal AI model shows significant improvements in code generation and mathematics...",
    "published_at": "2024-01-14T15:45:00Z",
    "source_url": "https://example.com/gemini-ultra-2"
  }
  // ... 3 more articles
]
```

**Error Responses**:
- **503 Service Unavailable**: Database connection issues
  ```json
  {
    "error": "Database service unavailable",
    "message": "Please try again later"
  }
  ```
- **500 Internal Server Error**: Unexpected server errors
  ```json
  {
    "error": "Internal server error",
    "message": "An unexpected error occurred"
  }
  ```

#### `GET /health`
Health check endpoint for monitoring service availability.

**Success Response** (200):
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "database": "connected",
    "api": "operational"
  }
}
```

### Response Standards

All API responses follow consistent formatting:

- **Success responses**: Direct data or wrapped in appropriate structure
- **Error responses**: Include error type, user-friendly message, and relevant details
- **HTTP status codes**: Semantic and consistent usage
- **Timestamps**: ISO 8601 format (UTC)
- **Performance**: All endpoints target <50ms response time

## 🧪 Testing

Our testing strategy follows Test-Driven Development (TDD) principles with comprehensive coverage across all layers.

### Testing Philosophy

We implement the complete TDD cycle:
1. **🔴 RED**: Write failing tests that describe desired functionality
2. **🟢 GREEN**: Implement minimal code to make tests pass  
3. **🔵 REFACTOR**: Improve code quality while maintaining test coverage

### Running Tests

```bash
# Run complete test suite
./scripts/test.sh

# Backend tests only (PyTest)
./scripts/test.sh backend

# Frontend tests only (Jest)
./scripts/test.sh frontend

# Code quality and linting
./scripts/test.sh lint

# Coverage report
./scripts/test.sh coverage
```

### Test Coverage Requirements

- **Minimum Coverage**: 90% for all modules
- **Unit Tests**: All business logic methods and components
- **Integration Tests**: API endpoints and database interactions
- **Performance Tests**: Response time validation (<50ms backend, <16ms frontend)
- **Accessibility Tests**: WCAG 2.1 AA compliance verification

### Test Organization

#### Backend Testing (PyTest)
```python
# Example test structure
class TestArticleService:
    def test_get_latest_articles_returns_five_articles(self):
        """Verify correct number of articles returned."""
        
    def test_get_latest_articles_performance_requirement(self):
        """Ensure response time under 50ms."""
        
    def test_get_latest_articles_handles_database_error(self):
        """Test graceful error handling."""
```

#### Frontend Testing (Jest + React Testing Library)
```typescript
// Example component test
describe('ArticleCard Component', () => {
  describe('UI Display', () => {
    test('renders article information correctly', () => {
      // Test implementation
    });
  });
  
  describe('Accessibility', () => {
    test('has proper ARIA attributes', () => {
      // Accessibility verification
    });
  });
  
  describe('Performance', () => {
    test('renders within 16ms budget', () => {
      // Performance validation
    });
  });
});
```

## 🚀 Performance Requirements

Our platform is built with performance as a first-class concern:

### Backend Performance
- **🎯 API Response Time**: <50ms for data retrieval endpoints
- **📊 Database Queries**: <10ms execution time with proper indexing
- **📈 Monitoring**: Built-in performance tracking with automated warnings
- **🔍 Profiling**: Execution time logging for all service methods

### Frontend Performance
- **⚡ UI Interactions**: <16ms for smooth 60fps interactions
- **📦 Bundle Size**: <1MB compressed JavaScript
- **🖼️ Image Optimization**: Lazy loading and responsive images
- **♿ Accessibility**: Optimized for screen readers and keyboard navigation

### Performance Monitoring

```python
# Example performance monitoring (backend)
def get_latest_articles(self) -> List[Dict[str, Any]]:
    start_time = time.time()
    try:
        # Business logic
        return articles
    finally:
        execution_time = (time.time() - start_time) * 1000
        if execution_time > PERFORMANCE_THRESHOLD_MS:
            logger.warning(f"Slow operation: {execution_time:.2f}ms")
```

## 🔒 Security

Security is integrated throughout our architecture with multiple layers of protection:

### Input Validation
- **Backend**: Comprehensive validation using Marshmallow schemas
- **Frontend**: Client-side validation with server-side verification
- **Database**: Parameterized queries preventing SQL injection

### Data Protection
- **XSS Prevention**: React's built-in escaping + DOMPurify for HTML content
- **CSRF Protection**: Token-based validation for state-changing operations
- **CORS Configuration**: Strict origin and method restrictions

### Configuration Security
- **Environment Variables**: All sensitive configuration externalized
- **Secret Management**: No hardcoded credentials or API keys
- **Database Security**: Connection encryption and access controls

### Security Headers
```python
# Example security configuration
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

## 🤝 Contributing

We welcome contributions! Please follow our established development workflow:

### Development Workflow

1. **📋 Issues**: Start by creating or claiming an issue
2. **🌿 Branching**: Create feature branch following naming conventions
3. **🔴 TDD Process**: Write tests first, then implementation
4. **✅ Quality Checks**: Ensure all tests pass and code quality standards are met
5. **📝 Pull Request**: Submit PR with detailed description and test coverage
6. **👀 Review**: Code review by team members
7. **🚀 Merge**: Merge after approval and CI/CD validation

### Branch Naming Conventions
- `feat/description-of-feature` - New functionality
- `fix/description-of-bug` - Bug fixes
- `refactor/description-of-refactor` - Code improvements
- `docs/description-of-docs` - Documentation updates
- `chore/description-of-chore` - Maintenance tasks

### Commit Message Format
We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer(s)]
```

**Examples**:
```bash
feat(articles): add pagination support to latest articles API
fix(frontend): resolve memory leak in ArticleCard component
docs(readme): update API documentation with new endpoints
```

### Pull Request Checklist
- [ ] All tests pass (`./scripts/test.sh`)
- [ ] Code coverage maintains 90%+ threshold
- [ ] Performance requirements met (<50ms backend, <16ms frontend)
- [ ] Code follows style guidelines in [CLAUDE.md](CLAUDE.md)
- [ ] Documentation updated for new features
- [ ] No new security vulnerabilities introduced
- [ ] Accessibility requirements maintained (WCAG 2.1 AA)

### Development Guidelines

For comprehensive development standards, architectural decisions, and best practices, please refer to our [**Development Constitution (CLAUDE.md)**](CLAUDE.md). This document covers:

- 📝 Coding standards and naming conventions
- 🏗️ Architecture and design principles  
- 🔒 Security guidelines and best practices
- 🧪 Testing strategies and requirements
- 📊 Performance optimization techniques
- 🔄 Git workflow and branch management
- 📦 Dependency management protocols

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with ❤️ using Test-Driven Development principles
- Powered by the latest in web technology and AI innovation
- Accessibility guidelines based on WCAG 2.1 AA standards
- Performance benchmarks inspired by Google Web Vitals

---

**🚀 Ready to explore the future of LLM and AI news?**

[Get Started](#quick-start) | [View Live Demo](http://localhost:3000) | [API Docs](#api-documentation) | [Contributing Guidelines](#contributing)

---

<div align="center">

**Built with Test-Driven Development principles**  
*Generated with [Claude Code](https://claude.ai/code)*

</div>