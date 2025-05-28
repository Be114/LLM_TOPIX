"""Test suite for data formatters.

This module contains tests for the formatting utilities that convert
database objects to API response formats.
"""

import pytest
from unittest.mock import Mock
from app.services.formatters import ArticleFormatter


class TestArticleFormatter:
    """Test cases for ArticleFormatter class."""

    def test_truncate_summary_under_limit(self) -> None:
        """Test truncate_summary with text under the limit."""
        short_text = "This is a short summary."
        result = ArticleFormatter.truncate_summary(short_text, max_length=100)
        
        assert result == short_text
        assert not result.endswith("...")

    def test_truncate_summary_over_limit(self) -> None:
        """Test truncate_summary with text over the limit."""
        long_text = "A" * 150
        result = ArticleFormatter.truncate_summary(long_text, max_length=100)
        
        assert len(result) == 103  # 100 chars + "..."
        assert result.endswith("...")
        assert result.startswith("A" * 100)

    def test_truncate_summary_exactly_at_limit(self) -> None:
        """Test truncate_summary with text exactly at the limit."""
        exact_text = "A" * 100
        result = ArticleFormatter.truncate_summary(exact_text, max_length=100)
        
        assert result == exact_text
        assert not result.endswith("...")

    def test_truncate_summary_handles_none_input(self) -> None:
        """RED phase test: truncate_summary should handle None input gracefully."""
        # This test should initially fail because the current implementation
        # doesn't handle None input - it will raise AttributeError
        result = ArticleFormatter.truncate_summary(None)
        
        assert result == ""  # Should return empty string for None

    def test_format_article_for_api_handles_none_fields(self) -> None:
        """RED phase test: format_article_for_api should handle None fields."""
        # Test for None title
        article_none_title = Mock()
        article_none_title.id = 1
        article_none_title.title = None
        article_none_title.summary = "Valid summary"
        article_none_title.published_at = "2024-01-15T10:30:00Z"
        article_none_title.source_url = "https://example.com"
        
        with pytest.raises(ValueError, match="Article title cannot be None"):
            ArticleFormatter.format_article_for_api(article_none_title)

    def test_format_article_for_api_handles_none_id(self) -> None:
        """RED phase test: format_article_for_api should handle None ID."""
        article_none_id = Mock()
        article_none_id.id = None
        article_none_id.title = "Valid Title"
        article_none_id.summary = "Valid summary"
        article_none_id.published_at = "2024-01-15T10:30:00Z"
        article_none_id.source_url = "https://example.com"
        
        with pytest.raises(ValueError, match="Article ID cannot be None"):
            ArticleFormatter.format_article_for_api(article_none_id)

    def test_format_article_for_api_handles_none_published_at(self) -> None:
        """RED phase test: format_article_for_api should handle None published_at."""
        article_none_published = Mock()
        article_none_published.id = 1
        article_none_published.title = "Valid Title"
        article_none_published.summary = "Valid summary"
        article_none_published.published_at = None
        article_none_published.source_url = "https://example.com"
        
        with pytest.raises(ValueError, match="Article published_at cannot be None"):
            ArticleFormatter.format_article_for_api(article_none_published)

    def test_format_article_for_api_handles_none_source_url(self) -> None:
        """RED phase test: format_article_for_api should handle None source_url."""
        article_none_url = Mock()
        article_none_url.id = 1
        article_none_url.title = "Valid Title"
        article_none_url.summary = "Valid summary"
        article_none_url.published_at = "2024-01-15T10:30:00Z"
        article_none_url.source_url = None
        
        with pytest.raises(ValueError, match="Article source_url cannot be None"):
            ArticleFormatter.format_article_for_api(article_none_url)

    def test_format_article_for_api_handles_none_summary(self) -> None:
        """RED phase test: format_article_for_api should handle None summary gracefully."""
        article_none_summary = Mock()
        article_none_summary.id = 1
        article_none_summary.title = "Valid Title"
        article_none_summary.summary = None
        article_none_summary.published_at = "2024-01-15T10:30:00Z"
        article_none_summary.source_url = "https://example.com"
        
        result = ArticleFormatter.format_article_for_api(article_none_summary)
        
        # Summary should be converted to empty string when None
        assert result['summary_truncated'] == ""
        assert result['id'] == 1
        assert result['title'] == "Valid Title"

    def test_format_article_for_api_with_valid_data(self) -> None:
        """Test format_article_for_api with valid complete data."""
        article = Mock()
        article.id = 1
        article.title = "Test Article Title"
        article.summary = "This is a test article summary that is quite long and should be truncated."
        article.published_at = "2024-01-15T10:30:00Z"
        article.source_url = "https://example.com/article"
        
        result = ArticleFormatter.format_article_for_api(article)
        
        assert result['id'] == 1
        assert result['title'] == "Test Article Title"
        assert 'summary_truncated' in result
        assert result['published_at'] == "2024-01-15T10:30:00Z"
        assert result['source_url'] == "https://example.com/article"