"""
Application constants for LLM TOPIX backend.

This module contains all magic numbers, hardcoded values, and configuration
constants to improve maintainability and security.
"""
import os
from typing import Final

# Database Configuration
DATABASE_HOST: Final[str] = os.getenv('DB_HOST', 'localhost')
DATABASE_PORT: Final[str] = os.getenv('DB_PORT', '5432')
DATABASE_USER: Final[str] = os.getenv('DB_USER', 'postgres')
DATABASE_PASS: Final[str] = os.getenv('DB_PASS', 'password')

# Environment-specific database names
DATABASE_NAME_DEV: Final[str] = os.getenv('DB_NAME_DEV', 'llm_topix_dev')
DATABASE_NAME_TEST: Final[str] = os.getenv('DB_NAME_TEST', 'llm_topix_test')

# Performance thresholds
PERFORMANCE_THRESHOLD_MS: Final[int] = 50
SUMMARY_MAX_LENGTH: Final[int] = 100
SUMMARY_TRUNCATE_SUFFIX: Final[str] = "..."

# Database field constraints
ARTICLE_TITLE_MAX_LENGTH: Final[int] = 255
ARTICLE_URL_MAX_LENGTH: Final[int] = 512

# CORS configuration
ALLOWED_ORIGINS: Final[list[str]] = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

# Environment configurations
TESTING_ENV: Final[str] = 'testing'
DEVELOPMENT_ENV: Final[str] = 'development'
PRODUCTION_ENV: Final[str] = 'production'

# Error codes according to CLAUDE.md taxonomy
ERROR_CODE_VALIDATION_ERROR: Final[str] = 'VALIDATION_ERROR'
ERROR_CODE_AUTHENTICATION_REQUIRED: Final[str] = 'AUTHENTICATION_REQUIRED'
ERROR_CODE_AUTHORIZATION_DENIED: Final[str] = 'AUTHORIZATION_DENIED'
ERROR_CODE_RESOURCE_NOT_FOUND: Final[str] = 'RESOURCE_NOT_FOUND'
ERROR_CODE_METHOD_NOT_ALLOWED: Final[str] = 'METHOD_NOT_ALLOWED'
ERROR_CODE_RATE_LIMIT_EXCEEDED: Final[str] = 'RATE_LIMIT_EXCEEDED'
ERROR_CODE_DATABASE_UNAVAILABLE: Final[str] = 'DATABASE_UNAVAILABLE'
ERROR_CODE_INTERNAL_SERVER_ERROR: Final[str] = 'INTERNAL_SERVER_ERROR'


def build_database_url(database_name: str) -> str:
    """
    Build a PostgreSQL database URL from configuration constants.
    
    Args:
        database_name: The name of the database to connect to
        
    Returns:
        A PostgreSQL connection URL string
    """
    return f'postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}'