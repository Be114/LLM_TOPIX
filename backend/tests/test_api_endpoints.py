"""Test suite for API endpoints.

This module contains tests for the Flask API endpoints,
specifically the /api/articles/latest endpoint.
"""

import pytest
import json
from datetime import datetime
from unittest.mock import patch, Mock
from typing import Dict, Any

from app.app import create_app
from app.exceptions import DatabaseError, ApplicationError


class TestArticleAPI:
    """Test cases for article-related API endpoints."""
    
    def setup_method(self) -> None:
        """Set up test fixtures before each test method."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def teardown_method(self) -> None:
        """Clean up after each test method."""
        self.app_context.pop()
    
    def test_get_latest_articles_endpoint_exists(self) -> None:
        """Test that the /api/articles/latest endpoint exists and responds.
        
        This test verifies that the endpoint is properly configured
        and returns a valid HTTP response.
        """
        response = self.client.get('/api/articles/latest')
        
        # Should not return 404 (endpoint should exist)
        assert response.status_code != 404
    
    def test_get_latest_articles_returns_json(self) -> None:
        """Test that the endpoint returns valid JSON response.
        
        This test ensures that the response is properly formatted
        as JSON with correct content type headers.
        """
        response = self.client.get('/api/articles/latest')
        
        assert response.content_type == 'application/json'
        
        # Should be able to parse as JSON
        data = json.loads(response.data)
        assert isinstance(data, list)
    
    def test_get_latest_articles_success_response_format(self) -> None:
        """Test the structure of successful API response.
        
        This test verifies that the API returns articles in the
        expected format with all required fields.
        """
        response = self.client.get('/api/articles/latest')
        
        if response.status_code == 200:
            data = json.loads(response.data)
            assert isinstance(data, list)
            
            for article in data:
                required_keys = {'title', 'summary_truncated', 'published_at', 'source_url'}
                assert set(article.keys()) == required_keys
    
    def test_get_latest_articles_handles_database_error(self) -> None:
        """Test API error handling when database operations fail.
        
        This test verifies that database errors are properly handled
        and return appropriate HTTP status codes.
        """
        with patch('app.services.article_service.ArticleService.get_latest_articles') as mock_service:
            mock_service.side_effect = DatabaseError("Database connection failed")
            
            response = self.client.get('/api/articles/latest')
            
            assert response.status_code == 503
            
            error_data = json.loads(response.data)
            assert 'error' in error_data
    
    def test_get_latest_articles_handles_application_error(self) -> None:
        """Test API error handling for general application errors.
        
        This test verifies that application errors are properly handled
        and return appropriate error responses.
        """
        with patch('app.services.article_service.ArticleService.get_latest_articles') as mock_service:
            mock_service.side_effect = ApplicationError("Internal error", 500)
            
            response = self.client.get('/api/articles/latest')
            
            assert response.status_code == 500
            
            error_data = json.loads(response.data)
            assert 'error' in error_data
    
    def test_get_latest_articles_cors_headers(self) -> None:
        """Test that CORS headers are properly set for cross-origin requests.
        
        This test ensures that the frontend can properly access the API
        from different origins.
        """
        response = self.client.get('/api/articles/latest')
        
        # CORS headers should be present
        assert 'Access-Control-Allow-Origin' in response.headers
    
    def test_get_latest_articles_limits_response_size(self) -> None:
        """Test that API response is limited to maximum 5 articles.
        
        This test verifies that the API enforces the business rule
        of returning only the latest 5 articles.
        """
        response = self.client.get('/api/articles/latest')
        
        if response.status_code == 200:
            data = json.loads(response.data)
            assert len(data) <= 5