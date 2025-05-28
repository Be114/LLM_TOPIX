"""Data formatting utilities for services.

This module contains formatters for converting database objects
to API response formats, promoting reusability and separation of concerns.
"""

from typing import Dict, Any
import logging

from app.config.constants import SUMMARY_MAX_LENGTH, SUMMARY_TRUNCATE_SUFFIX

logger = logging.getLogger(__name__)


class ArticleFormatter:
    """Formatter class for article data transformations."""
    
    @staticmethod
    def truncate_summary(summary: str, max_length: int = SUMMARY_MAX_LENGTH) -> str:
        """Truncate summary text to specified length with ellipsis.
        
        Args:
            summary: The original summary text
            max_length: Maximum allowed length (default from constants)
            
        Returns:
            Truncated summary with ellipsis if needed
        """
        if len(summary) <= max_length:
            return summary
        
        return summary[:max_length] + SUMMARY_TRUNCATE_SUFFIX
    
    @staticmethod
    def format_article_for_api(article: Any) -> Dict[str, Any]:
        """Format a database article object for API response.
        
        Args:
            article: Database article object/row
            
        Returns:
            Dictionary formatted for API response
        """
        try:
            return {
                'title': article.title,
                'summary_truncated': ArticleFormatter.truncate_summary(article.summary),
                'published_at': article.published_at,
                'source_url': article.source_url
            }
        except AttributeError as e:
            logger.error(f"Error formatting article: missing attribute {e}")
            raise ValueError(f"Invalid article object: {e}")
    
    @staticmethod
    def format_articles_list(articles: list) -> list[Dict[str, Any]]:
        """Format a list of articles for API response.
        
        Args:
            articles: List of database article objects/rows
            
        Returns:
            List of formatted article dictionaries
        """
        return [ArticleFormatter.format_article_for_api(article) for article in articles]