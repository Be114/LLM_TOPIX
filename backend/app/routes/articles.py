"""Article-related API routes.

This module contains Flask routes for article operations,
including the endpoint for retrieving latest articles.
"""

from flask import Blueprint, current_app
from typing import Dict, Any, Tuple

from app.services.article_service import ArticleService
from app.exceptions import DatabaseError, ApplicationError
from app.utils.response_helpers import (
    create_error_response,
    create_success_response
)
from app.utils.date_helpers import format_datetime_to_utc_iso8601
from app.config.constants import (
    ERROR_CODE_DATABASE_UNAVAILABLE,
    ERROR_CODE_INTERNAL_SERVER_ERROR,
    ERROR_CODE_RESOURCE_NOT_FOUND,
    ERROR_CODE_METHOD_NOT_ALLOWED
)


articles_bp = Blueprint('articles', __name__, url_prefix='/api/articles')


def _format_articles_for_response(articles: list[Dict[str, Any]]) -> list[Dict[str, Any]]:
    """Format articles for JSON response.
    
    Args:
        articles: List of article dictionaries from service
        
    Returns:
        List of formatted article dictionaries with UTC ISO8601 datetime strings
    """
    formatted_articles = []
    for article in articles:
        formatted_article = article.copy()
        if 'published_at' in formatted_article and formatted_article['published_at']:
            formatted_article['published_at'] = format_datetime_to_utc_iso8601(formatted_article['published_at'])
        formatted_articles.append(formatted_article)
    
    return formatted_articles


@articles_bp.route('/latest', methods=['GET'])
def get_latest_articles() -> Tuple[Dict[str, Any], int]:
    """Get the latest articles endpoint.
    
    This endpoint retrieves the most recently published articles
    and returns them in JSON format for frontend consumption.
    
    Returns:
        Tuple[Dict[str, Any], int]: JSON response and HTTP status code
        
    Response Format:
        {
            "articles": [
                {
                    "title": "Article Title",
                    "summary_truncated": "Article summary...",
                    "published_at": "2024-01-15T10:30:00Z",
                    "source_url": "https://example.com/article"
                }
            ],
            "count": 5
        }
    
    Error Responses:
        503: Database connection/query error
        500: Internal server error
    """
    try:
        from app.config.database import get_db
        db_session = get_db()
        article_service = ArticleService(db_session)
        articles = article_service.get_latest_articles()
        
        formatted_articles = _format_articles_for_response(articles)
        
        return create_success_response({
            'articles': formatted_articles,
            'count': len(formatted_articles)
        })
        
    except DatabaseError as e:
        current_app.logger.error(f"Database error in get_latest_articles: {e.message}")
        return create_error_response(
            ERROR_CODE_DATABASE_UNAVAILABLE,
            'Database service is temporarily unavailable. Please try again later.',
            503
        )
        
    except ApplicationError as e:
        current_app.logger.error(f"Application error in get_latest_articles: {e.message}")
        return create_error_response(
            ERROR_CODE_INTERNAL_SERVER_ERROR,
            'An unexpected error occurred',
            getattr(e, 'status_code', 500)
        )
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error in get_latest_articles: {str(e)}")
        return create_error_response(
            ERROR_CODE_INTERNAL_SERVER_ERROR,
            'An unexpected error occurred',
            500
        )


@articles_bp.errorhandler(404)
def not_found_error(error: Exception) -> Tuple[Dict[str, str], int]:
    """Handle 404 errors for articles blueprint."""
    return create_error_response(
        ERROR_CODE_RESOURCE_NOT_FOUND,
        'The requested article endpoint does not exist',
        404
    )


@articles_bp.errorhandler(405)
def method_not_allowed_error(error: Exception) -> Tuple[Dict[str, str], int]:
    """Handle 405 errors for articles blueprint."""
    return create_error_response(
        ERROR_CODE_METHOD_NOT_ALLOWED,
        'This HTTP method is not allowed for this endpoint',
        405
    )