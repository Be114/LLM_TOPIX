# LLM TOPIX Development Constitution

## Project Overview
LLM TOPIX is a comprehensive web platform for LLM and generative AI news, featuring document analysis for major LLM providers (Gemini, ChatGPT, Claude). This project follows strict Test-Driven Development (TDD) principles.

## Architecture Stack
- **Frontend**: Next.js 14+ with TypeScript (Strict Mode)
- **Backend**: Python Flask with SQLAlchemy ORM
- **Database**: PostgreSQL 15+
- **Testing**: Jest (Frontend), PyTest (Backend)
- **Dependency Management**: Poetry (Python), npm/yarn (Node.js)
- **Containerization**: Docker with docker-compose
- **CI/CD**: GitHub Actions

## Coding Standards

### Python (Backend)
- **Style**: PEP 8 compliant with Black formatter
- **Type Hints**: Mandatory for all functions and class methods
- **Docstrings**: Google-style docstrings for all public methods
- **Error Handling**: Custom exception classes, never bare except clauses
- **Security**: Input validation, SQL injection prevention, XSS protection

### TypeScript (Frontend)
- **Mode**: Strict TypeScript with no implicit any
- **Style**: Prettier + ESLint configuration
- **Components**: Functional components with React Hooks
- **Props**: Explicit interface definitions for all props
- **Accessibility**: WCAG 2.1 AA compliance mandatory

## TDD Principles
1. **RED**: Write failing tests first
2. **GREEN**: Implement minimal code to pass tests
3. **REFACTOR**: Improve code quality while maintaining test coverage

## Database Design Principles
- **Normalization**: 3NF minimum
- **Indexing**: Performance-optimized indexes on frequently queried columns
- **Constraints**: Proper foreign key relationships and data validation
- **Migrations**: Version-controlled schema changes

## Security Requirements
- Input sanitization and validation
- SQL injection prevention via parameterized queries
- XSS protection with proper output encoding
- CSRF protection for state-changing operations
- Rate limiting on API endpoints

## Performance Standards
- **Backend API**: <50ms response time for data retrieval
- **Frontend UI**: <16ms for smooth 60fps interactions
- **Database Queries**: Properly indexed, <10ms execution time
- **Bundle Size**: Frontend JavaScript <1MB compressed

## File Structure
```
/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── services/
│   │   ├── routes/
│   │   └── config/
│   ├── tests/
│   ├── migrations/
│   └── requirements/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── types/
│   │   └── utils/
│   ├── tests/
│   └── public/
├── docker/
├── scripts/
└── docs/
```

## Commit Standards
- **Convention**: Conventional Commits specification
- **Format**: `type(scope): description`
- **Types**: feat, fix, docs, style, refactor, test, chore

## Testing Requirements
- **Coverage**: Minimum 90% code coverage
- **Unit Tests**: All business logic methods
- **Integration Tests**: API endpoints and database interactions
- **E2E Tests**: Critical user workflows
- **Accessibility Tests**: All UI components

This constitution must be followed strictly for all development work.