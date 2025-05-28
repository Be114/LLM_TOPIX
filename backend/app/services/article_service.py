"""Article service for business logic operations.

This module contains the ArticleService class which handles
article-related business operations including retrieval and formatting.
"""

import logging
from typing import List, Dict, Any
import time

from sqlalchemy import create_engine, desc, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from app.models.article import Article
from app.exceptions import DatabaseError, ApplicationError
from app.config.database import get_database_url
from app.config.constants import PERFORMANCE_THRESHOLD_MS
from app.services.formatters import ArticleFormatter

logger = logging.getLogger(__name__)


class ArticleService:
    """Service class for article-related business operations.
    
    This class provides methods for retrieving and processing articles
    from the database with proper error handling and performance optimization.
    """
    
    def __init__(self) -> None:
        """Initialize the ArticleService with database connection."""
        try:
            self.engine = create_engine(get_database_url())
            self.SessionLocal = sessionmaker(bind=self.engine)
        except Exception as e:
            raise DatabaseError(f"Failed to initialize database connection: {str(e)}")
    
    def get_latest_articles(self) -> List[Dict[str, Any]]:
        """Retrieve the latest 5 articles from the database.
        
        This method fetches the most recently published articles,
        limits the result to 5 items, and formats them for frontend consumption.
        The summary field is truncated based on constants.
        
        Returns:
            List[Dict[str, Any]]: List of formatted article dictionaries
        
        Raises:
            DatabaseError: When database operations fail
            ApplicationError: When unexpected errors occur
        """
        start_time = time.time()
        
        try:
            articles = self._fetch_articles_from_database()
            formatted_articles = ArticleFormatter.format_articles_list(articles)
            self._check_performance(start_time)
            
            return formatted_articles
                
        except SQLAlchemyError as e:
            raise DatabaseError(f"Database query failed: {str(e)}")
        except Exception as e:
            raise ApplicationError(f"Unexpected error in get_latest_articles: {str(e)}")
    
    def _fetch_articles_from_database(self) -> List[Any]:
        """Fetch articles from database with proper query optimization.
        
        Returns:
            List of article database objects
        """
        with self.SessionLocal() as session:
            stmt = (
                select(Article.title, Article.summary, Article.published_at, Article.source_url)
                .order_by(desc(Article.published_at))
                .limit(5)
            )
            
            result = session.execute(stmt)
            return result.fetchall()
    
    def _check_performance(self, start_time: float) -> None:
        """Check if operation completed within performance threshold.
        
        Args:
            start_time: Operation start time from time.time()
        """
        execution_time_ms = (time.time() - start_time) * 1000
        if execution_time_ms > PERFORMANCE_THRESHOLD_MS:
            logger.warning(
                f"get_latest_articles took {execution_time_ms:.2f}ms, "
                f"exceeds {PERFORMANCE_THRESHOLD_MS}ms threshold"
            )