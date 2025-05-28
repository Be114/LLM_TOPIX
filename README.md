# LLM TOPIX - AI News Platform

A comprehensive web platform for LLM and generative AI news, featuring analysis of major LLM providers (Gemini, ChatGPT, Claude). Built with strict Test-Driven Development (TDD) principles.

## Tech Stack

- **Frontend**: Next.js 14+ with TypeScript
- **Backend**: Python Flask with SQLAlchemy ORM  
- **Database**: PostgreSQL 15+
- **Testing**: Jest (Frontend), PyTest (Backend)
- **Containerization**: Docker with docker-compose

## Features

### Phase 1 (Current - MVP)
- ✅ Display latest 5 LLM news articles on homepage
- ✅ Article cards with title, summary (100 chars), date, source
- ✅ Responsive design with accessibility support
- ✅ RESTful API with error handling
- ✅ Complete TDD implementation (RED → GREEN → REFACTOR)

### Phase 2 (Planned)
- [ ] Article search and filtering
- [ ] User authentication and preferences
- [ ] LLM document analysis and summarization
- [ ] Real-time news feeds and notifications

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd LLM_TOPIX

# Setup development environment
chmod +x scripts/*.sh
./scripts/setup.sh

# Start all services
docker-compose up -d

# Run tests
./scripts/test.sh
```

### Access Points
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Health**: http://localhost:5000/health
- **Latest Articles**: http://localhost:5000/api/articles/latest

## Development

### TDD Workflow
This project follows strict TDD principles:

1. **RED**: Write failing tests first
2. **GREEN**: Implement minimal code to pass tests  
3. **REFACTOR**: Improve code quality while maintaining tests

### Code Standards
- **Python**: PEP 8 with Black formatter, type hints mandatory
- **TypeScript**: Strict mode, ESLint + Prettier
- **Testing**: 90%+ code coverage required
- **Documentation**: Google-style docstrings

### Running Tests
```bash
# All tests
./scripts/test.sh

# Backend only
./scripts/test.sh backend

# Frontend only  
./scripts/test.sh frontend

# Code quality checks
./scripts/test.sh lint
```

## API Documentation

### GET /api/articles/latest
Returns the 5 most recent articles.

**Response:**
```json
[
  {
    "title": "Article Title",
    "summary_truncated": "Article summary...",
    "published_at": "2024-01-15T10:30:00Z",
    "source_url": "https://example.com/article"
  }
]
```

**Error Responses:**
- `503`: Database unavailable
- `500`: Internal server error

## Contributing

1. Follow TDD workflow (RED → GREEN → REFACTOR)
2. Ensure all tests pass: `./scripts/test.sh`
3. Follow code standards in `CLAUDE.md`
4. Use Conventional Commits format
5. Maintain 90%+ test coverage

## Architecture

```
/
├── backend/              # Flask API server
│   ├── app/
│   │   ├── models/       # SQLAlchemy models
│   │   ├── services/     # Business logic
│   │   ├── routes/       # API endpoints
│   │   └── config/       # Configuration
│   └── tests/            # Backend tests
├── frontend/             # Next.js application
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── types/        # TypeScript types
│   │   └── pages/        # Next.js pages
│   └── tests/            # Frontend tests
├── database/             # Database schemas & migrations
├── scripts/              # Development scripts
└── docker/               # Docker configurations
```

## Performance Requirements

- **Backend API**: <50ms response time
- **Frontend UI**: <16ms for 60fps interactions  
- **Database**: <10ms query execution
- **Bundle Size**: <1MB compressed

## Security

- Input validation and sanitization
- SQL injection prevention via parameterized queries
- XSS protection with output encoding
- CORS properly configured
- Rate limiting on API endpoints

---

**Built with Test-Driven Development principles**  
**Generated with [Claude Code](https://claude.ai/code)**