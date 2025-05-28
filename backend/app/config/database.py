"""Database configuration and connection management.

This module provides database configuration settings and utilities
for connecting to PostgreSQL database with proper Flask session management.
"""

import logging
import os
from typing import Any
from flask import g, current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .constants import (
    build_database_url,
    DATABASE_NAME_DEV,
    DATABASE_NAME_TEST
)

logger = logging.getLogger(__name__)

# Global application-level database objects
_engine = None
_SessionLocal = None


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


def init_db(app: Any) -> None:
    """Initialize database engine and session factory for the application.
    
    This function should be called once during application startup to create
    the global database engine and session factory.
    
    Args:
        app: Flask application instance
    """
    global _engine, _SessionLocal
    
    database_url = app.config.get('DATABASE_URL') or get_database_url()
    
    if _engine is None:
        _engine = create_engine(
            database_url,
            pool_pre_ping=True,  # Verify connections before use
            pool_recycle=3600,   # Recycle connections after 1 hour
            echo=app.config.get('SQLALCHEMY_ECHO', False)
        )
        logger.info("Database engine initialized")
    
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
        logger.info("Database session factory initialized")


def get_db() -> Session:
    """Get database session for the current request.
    
    This function provides a database session that is scoped to the current
    Flask request context. The same session is reused within a single request.
    
    Returns:
        Session: SQLAlchemy database session
    """
    if 'db' not in g:
        if _SessionLocal is None:
            raise RuntimeError("Database not initialized. Call init_db() first.")
        g.db = _SessionLocal()
        logger.debug("Created new database session for request")
    
    return g.db


def close_db(e: Any = None) -> None:
    """Close database session at the end of request.
    
    This function is registered as a teardown handler and automatically
    closes the database session when the request context ends.
    
    Args:
        e: Exception that caused teardown (if any)
    """
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        logger.debug("Closed database session for request")


def get_engine() -> Any:
    """Get the global database engine.
    
    Returns:
        Engine: SQLAlchemy database engine
    """
    if _engine is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    
    return _engine


def dispose_db() -> None:
    """Dispose of database engine on application shutdown.
    
    This function should be called during application shutdown to properly
    dispose of the database engine and close all connections.
    """
    global _engine
    
    if _engine is not None:
        _engine.dispose()
        logger.info("Database engine disposed")
        _engine = None