"""Article-related API routes.

This module contains Flask routes for article operations,
including the endpoint for retrieving latest articles.
"""

from flask import Blueprint, jsonify, current_app
from typing import Dict, Any, Tuple

from app.services.article_service import ArticleService
from app.exceptions import DatabaseError, ApplicationError, NotFoundError


articles_bp = Blueprint('articles', __name__, url_prefix='/api/articles')


@articles_bp.route('/latest', methods=['GET'])
def get_latest_articles() -> Tuple[Dict[str, Any], int]:
    """Get the latest 5 articles endpoint.
    
    This endpoint retrieves the most recently published articles
    and returns them in JSON format for frontend consumption.
    
    Returns:
        Tuple[Dict[str, Any], int]: JSON response and HTTP status code
        
    Response Format:
        [
            {
                "title": "Article Title",
                "summary_truncated": "Article summary...",
                "published_at": "2024-01-15T10:30:00Z",
                "source_url": "https://example.com/article"
            }
        ]
    
    Error Responses:
        503: Database connection/query error
        500: Internal server error
    """
    try:
        article_service = ArticleService()
        articles = article_service.get_latest_articles()
        
        # Convert datetime objects to ISO format strings for JSON serialization
        for article in articles:
            if 'published_at' in article and article['published_at']:
                article['published_at'] = article['published_at'].isoformat()
        
        return jsonify(articles), 200
        
    except DatabaseError as e:
        current_app.logger.error(f"Database error in get_latest_articles: {e.message}")
        return jsonify({
            'error': 'Database service unavailable',
            'message': 'Please try again later'
        }), 503
        
    except ApplicationError as e:
        current_app.logger.error(f"Application error in get_latest_articles: {e.message}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), e.status_code
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error in get_latest_articles: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), 500


@articles_bp.errorhandler(404)
def not_found_error(error: Exception) -> Tuple[Dict[str, str], int]:
    """Handle 404 errors for articles blueprint."""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested article endpoint does not exist'
    }), 404


@articles_bp.errorhandler(405)
def method_not_allowed_error(error: Exception) -> Tuple[Dict[str, str], int]:
    """Handle 405 errors for articles blueprint."""
    return jsonify({
        'error': 'Method not allowed',
        'message': 'This HTTP method is not allowed for this endpoint'
    }), 405