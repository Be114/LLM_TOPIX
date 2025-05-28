"""Flask application factory.

This module contains the application factory function for creating
and configuring the Flask application instance.
"""

import os
from flask import Flask
from flask_cors import CORS
from typing import Optional

from app.routes.articles import articles_bp


def create_app(config_name: Optional[str] = None) -> Flask:
    """Create and configure the Flask application.
    
    Args:
        config_name: Configuration name ('development', 'testing', 'production')
        
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'testing':
        app.config['TESTING'] = True
        app.config['DATABASE_URL'] = os.getenv(
            'TEST_DATABASE_URL',
            'postgresql://postgres:password@localhost:5432/llm_topix_test'
        )
    else:
        app.config['DATABASE_URL'] = os.getenv(
            'DATABASE_URL',
            'postgresql://postgres:password@localhost:5432/llm_topix_dev'
        )
    
    # Enable CORS for frontend integration
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Register blueprints
    app.register_blueprint(articles_bp)
    
    # Global error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found', 'message': 'The requested resource was not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error', 'message': 'An unexpected error occurred'}, 500
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'service': 'llm-topix-backend'}, 200
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)