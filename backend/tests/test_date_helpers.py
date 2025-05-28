"""Test suite for date helper utilities.

This module contains tests for the date formatting and timezone
handling utility functions.
"""

import pytest
from datetime import datetime, timezone
from app.utils.date_helpers import format_datetime_to_utc_iso8601, ensure_utc_datetime


class TestDateHelpers:
    """Test cases for date helper utility functions."""
    
    def test_format_naive_datetime_to_utc_iso8601(self) -> None:
        """Test formatting naive datetime to UTC ISO8601 string."""
        naive_dt = datetime(2024, 5, 29, 12, 0, 0)
        result = format_datetime_to_utc_iso8601(naive_dt)
        
        assert result == "2024-05-29T12:00:00Z"
        assert result.endswith('Z')
    
    def test_format_utc_aware_datetime_to_iso8601(self) -> None:
        """Test formatting UTC-aware datetime to ISO8601 string."""
        utc_dt = datetime(2024, 5, 29, 15, 30, 0, tzinfo=timezone.utc)
        result = format_datetime_to_utc_iso8601(utc_dt)
        
        assert result == "2024-05-29T15:30:00Z"
        assert result.endswith('Z')
    
    def test_format_other_timezone_datetime_to_utc_iso8601(self) -> None:
        """Test formatting non-UTC timezone datetime converts to UTC."""
        from datetime import timedelta
        # Create UTC+3 timezone
        utc_plus_3 = timezone(timedelta(hours=3))
        dt_plus_3 = datetime(2024, 5, 29, 15, 30, 0, tzinfo=utc_plus_3)
        
        result = format_datetime_to_utc_iso8601(dt_plus_3)
        
        # Should be converted to UTC (15:30 UTC+3 = 12:30 UTC)
        assert result == "2024-05-29T12:30:00Z"
        assert result.endswith('Z')
    
    def test_format_none_datetime_returns_none(self) -> None:
        """Test that None input returns None."""
        result = format_datetime_to_utc_iso8601(None)
        assert result is None
    
    def test_ensure_utc_datetime_with_naive(self) -> None:
        """Test ensuring naive datetime gets UTC timezone."""
        naive_dt = datetime(2024, 5, 29, 12, 0, 0)
        result = ensure_utc_datetime(naive_dt)
        
        assert result.tzinfo == timezone.utc
        assert result.hour == 12  # Same time, just with timezone
    
    def test_ensure_utc_datetime_with_utc_aware(self) -> None:
        """Test ensuring UTC-aware datetime stays UTC."""
        utc_dt = datetime(2024, 5, 29, 15, 30, 0, tzinfo=timezone.utc)
        result = ensure_utc_datetime(utc_dt)
        
        assert result.tzinfo == timezone.utc
        assert result == utc_dt  # Should be identical
    
    def test_ensure_utc_datetime_with_other_timezone(self) -> None:
        """Test ensuring non-UTC timezone datetime converts to UTC."""
        from datetime import timedelta
        utc_plus_3 = timezone(timedelta(hours=3))
        dt_plus_3 = datetime(2024, 5, 29, 15, 30, 0, tzinfo=utc_plus_3)
        
        result = ensure_utc_datetime(dt_plus_3)
        
        assert result.tzinfo == timezone.utc
        assert result.hour == 12  # Converted to UTC
        assert result.minute == 30
    
    def test_ensure_utc_datetime_with_none(self) -> None:
        """Test that None input returns None."""
        result = ensure_utc_datetime(None)
        assert result is None