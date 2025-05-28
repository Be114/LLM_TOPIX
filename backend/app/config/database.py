"""Database configuration and connection management.

This module provides database configuration settings and utilities
for connecting to PostgreSQL database.
"""

import os


def get_database_url() -> str:
    """Get database URL from environment variables.
    
    Returns:
        str: Database connection URL
        
    Raises:
        ValueError: If required environment variables are missing
    """
    # Default to development database if not specified
    database_url = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost:5432/llm_topix_dev'
    )
    
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is required")
    
    return database_url


def get_test_database_url() -> str:
    """Get test database URL.
    
    Returns:
        str: Test database connection URL
    """
    return os.getenv(
        'TEST_DATABASE_URL',
        'postgresql://postgres:password@localhost:5432/llm_topix_test'
    )