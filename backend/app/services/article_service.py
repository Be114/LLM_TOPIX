"""Article service for business logic operations.

This module contains the ArticleService class which handles
article-related business operations including retrieval and formatting.
"""

from datetime import datetime
from typing import List, Dict, Any
import time

from sqlalchemy import create_engine, desc, select
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.article import Article
from app.exceptions import DatabaseError, ApplicationError
from app.config.database import get_database_url


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
        The summary field is truncated to 100 characters with ellipsis if needed.
        
        Returns:
            List[Dict[str, Any]]: List of article dictionaries with keys:
                - title: Article title
                - summary_truncated: Summary limited to 100 chars + "..."
                - published_at: Publication datetime
                - source_url: Original article URL
        
        Raises:
            DatabaseError: When database operations fail
            ApplicationError: When unexpected errors occur
        """
        start_time = time.time()
        
        try:
            with self.SessionLocal() as session:
                # Query for latest 5 articles, ordered by published_at descending
                stmt = (
                    select(Article.title, Article.summary, Article.published_at, Article.source_url)
                    .order_by(desc(Article.published_at))
                    .limit(5)
                )
                
                result = session.execute(stmt)
                articles = result.fetchall()
                
                # Format articles for frontend
                formatted_articles = []
                for article in articles:
                    # Truncate summary to 100 characters with ellipsis
                    summary = article.summary
                    if len(summary) > 100:
                        summary_truncated = summary[:100] + "..."
                    else:
                        summary_truncated = summary
                    
                    formatted_articles.append({
                        'title': article.title,
                        'summary_truncated': summary_truncated,
                        'published_at': article.published_at,
                        'source_url': article.source_url
                    })
                
                # Performance check - should complete within 50ms
                execution_time = (time.time() - start_time) * 1000
                if execution_time > 50:
                    # Log warning but don't fail (could add logging here)
                    pass
                
                return formatted_articles
                
        except SQLAlchemyError as e:
            raise DatabaseError(f"Database query failed: {str(e)}")
        except Exception as e:
            raise ApplicationError(f"Unexpected error in get_latest_articles: {str(e)}")