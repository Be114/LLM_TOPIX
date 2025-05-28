"""Database configuration and connection management.

This module provides database configuration settings and utilities
for connecting to PostgreSQL database.
"""

import logging
import os
from .constants import (
    build_database_url,
    DATABASE_NAME_DEV,
    DATABASE_NAME_TEST
)

logger = logging.getLogger(__name__)


def get_database_url() -> str:
    """Get database URL from environment variables.
    
    Returns:
        str: Database connection URL
    """
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        database_url = build_database_url(DATABASE_NAME_DEV)
        logger.info(f"Using default database configuration: {database_url}")
    
    return database_url


def get_test_database_url() -> str:
    """Get test database URL.
    
    Returns:
        str: Test database connection URL
    """
    test_database_url = os.getenv('TEST_DATABASE_URL')
    if not test_database_url:
        test_database_url = build_database_url(DATABASE_NAME_TEST)
        logger.info(f"Using default test database configuration: {test_database_url}")
    
    return test_database_url