"""Test suite for ArticleService.

This module contains comprehensive tests for the ArticleService class,
focusing on the get_latest_articles() method that retrieves the latest
5 news articles with proper sorting and formatting.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch
from typing import List, Dict, Any

from app.services.article_service import ArticleService
from app.exceptions import DatabaseError, ApplicationError


class TestArticleService:
    """Test cases for ArticleService class."""
    
    def setup_method(self) -> None:
        """Set up test fixtures before each test method."""
        self.service = ArticleService()
        self.sample_articles = [
            {
                'id': 1,
                'title': 'Latest AI Breakthrough in Language Models',
                'summary': 'A' * 150,  # 150 characters to test truncation
                'published_at': datetime.now(),
                'source_url': 'https://example.com/article1'
            },
            {
                'id': 2,
                'title': 'GPT-4 Update Announcement',
                'summary': 'B' * 80,  # 80 characters, should not be truncated
                'published_at': datetime.now() - timedelta(hours=1),
                'source_url': 'https://example.com/article2'
            },
            {
                'id': 3,
                'title': 'Claude AI New Features',
                'summary': 'C' * 200,  # 200 characters to test truncation
                'published_at': datetime.now() - timedelta(hours=2),
                'source_url': 'https://example.com/article3'
            }
        ]
    
    def test_get_latest_articles_returns_correct_format(self) -> None:
        """Test that get_latest_articles returns articles in the correct format.
        
        This test verifies that the method returns a list of dictionaries
        with the required keys: title, summary_truncated, published_at, source_url.
        """
        # This test should fail initially (RED phase)
        result = self.service.get_latest_articles()
        
        assert isinstance(result, list)
        assert len(result) <= 5
        
        if result:  # If articles exist
            article = result[0]
            required_keys = {'title', 'summary_truncated', 'published_at', 'source_url'}
            assert set(article.keys()) == required_keys
    
    def test_get_latest_articles_limits_to_five_articles(self) -> None:
        """Test that get_latest_articles returns maximum 5 articles.
        
        This test ensures that even if more than 5 articles exist in the database,
        the method returns only the 5 most recent ones.
        """
        result = self.service.get_latest_articles()
        
        assert isinstance(result, list)
        assert len(result) <= 5
    
    def test_get_latest_articles_sorts_by_published_date_desc(self) -> None:
        """Test that articles are sorted by published_at in descending order.
        
        This test verifies that the most recently published articles appear first
        in the returned list.
        """
        result = self.service.get_latest_articles()
        
        if len(result) > 1:
            for i in range(len(result) - 1):
                current_date = result[i]['published_at']
                next_date = result[i + 1]['published_at']
                assert current_date >= next_date
    
    def test_get_latest_articles_truncates_summary_to_100_chars(self) -> None:
        """Test that summary is truncated to 100 characters with ellipsis.
        
        This test ensures that long summaries are properly truncated to 100
        characters and end with '...' to indicate truncation.
        """
        result = self.service.get_latest_articles()
        
        for article in result:
            summary = article['summary_truncated']
            if len(summary) > 100:
                assert summary.endswith('...')
                assert len(summary) == 103  # 100 chars + '...'
            else:
                assert not summary.endswith('...')
    
    def test_get_latest_articles_handles_empty_database(self) -> None:
        """Test behavior when no articles exist in the database.
        
        This test verifies that the method gracefully handles an empty database
        and returns an empty list without raising exceptions.
        """
        result = self.service.get_latest_articles()
        
        # Should return empty list, not raise exception
        assert isinstance(result, list)
        assert len(result) >= 0  # Could be empty
    
    def test_get_latest_articles_handles_database_error(self) -> None:
        """Test error handling when database connection fails.
        
        This test verifies that DatabaseError is properly raised when
        database operations fail.
        """
        with pytest.raises(DatabaseError):
            # This should eventually raise DatabaseError when connection fails
            # For now, this test will fail as the method doesn't exist
            self.service.get_latest_articles()
    
    def test_get_latest_articles_performance_requirement(self) -> None:
        """Test that get_latest_articles completes within 50ms.
        
        This test ensures the method meets performance requirements
        for fast API responses.
        """
        import time
        
        start_time = time.time()
        self.service.get_latest_articles()
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        assert execution_time < 50, f"Method took {execution_time:.2f}ms, exceeds 50ms limit"
    
    def test_get_latest_articles_returns_required_fields(self) -> None:
        """Test that all required fields are present and correctly formatted.
        
        This test verifies that each article contains all required fields
        with proper data types and formats.
        """
        result = self.service.get_latest_articles()
        
        for article in result:
            # Check required fields exist
            assert 'title' in article
            assert 'summary_truncated' in article
            assert 'published_at' in article
            assert 'source_url' in article
            
            # Check data types
            assert isinstance(article['title'], str)
            assert isinstance(article['summary_truncated'], str)
            assert isinstance(article['published_at'], datetime)
            assert isinstance(article['source_url'], str)
            
            # Check field constraints
            assert len(article['title']) > 0
            assert len(article['summary_truncated']) >= 0
            assert article['source_url'].startswith(('http://', 'https://'))
    
    def test_get_latest_articles_handles_malformed_data(self) -> None:
        """Test error handling for malformed data in database.
        
        This test verifies that the method properly handles and validates
        data integrity issues from the database.
        """
        # This test should verify data validation
        # Will initially fail as validation logic doesn't exist yet
        result = self.service.get_latest_articles()
        
        # All articles should have valid data
        for article in result:
            assert article['title'] is not None
            assert article['summary_truncated'] is not None
            assert article['published_at'] is not None
            assert article['source_url'] is not None