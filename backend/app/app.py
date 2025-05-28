"""Flask application factory.

This module contains the application factory function for creating
and configuring the Flask application instance.
"""

from flask import Flask
from flask_cors import CORS
from typing import Optional, Tuple, Dict, Any

from app.routes.articles import articles_bp
from app.config.constants import ALLOWED_ORIGINS, TESTING_ENV
from app.config.database import get_database_url, get_test_database_url, init_db, close_db, dispose_db
from app.utils.response_helpers import create_not_found_response, create_internal_error_response


def create_app(config_name: Optional[str] = None) -> Flask:
    """Create and configure the Flask application.
    
    Args:
        config_name: Configuration name ('development', 'testing', 'production')
        
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    if config_name == TESTING_ENV:
        app.config['TESTING'] = True
        app.config['DATABASE_URL'] = get_test_database_url()
    else:
        app.config['DATABASE_URL'] = get_database_url()
    
    # Initialize database with proper session management
    init_db(app)
    
    # Register database teardown handler
    app.teardown_appcontext(close_db)
    
    # Enable CORS for frontend integration
    CORS(app, resources={
        r"/api/*": {
            "origins": ALLOWED_ORIGINS,
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Register blueprints
    app.register_blueprint(articles_bp)
    
    # Global error handlers
    @app.errorhandler(404)
    def not_found(error: Exception) -> Tuple[Dict[str, str], int]:
        return create_not_found_response()
    
    @app.errorhandler(500)
    def internal_error(error: Exception) -> Tuple[Dict[str, str], int]:
        return create_internal_error_response()
    
    # Health check endpoint
    @app.route('/health')
    def health_check() -> Tuple[Dict[str, str], int]:
        return {'status': 'healthy', 'service': 'llm-topix-backend'}, 200
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)