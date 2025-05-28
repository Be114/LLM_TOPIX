"""Date and time utility functions.

This module provides utility functions for consistent date and time
handling across the application, including timezone normalization.
"""

from datetime import datetime, timezone
from typing import Union


def format_datetime_to_utc_iso8601(dt: datetime) -> str:
    """Format a datetime object to UTC ISO8601 string format.
    
    This function ensures that datetime objects are always converted
    to UTC timezone and formatted as ISO8601 strings with timezone info.
    
    Args:
        dt: The datetime object to format (can be naive or timezone-aware)
        
    Returns:
        ISO8601 formatted string with UTC timezone (ending with 'Z')
        
    Examples:
        >>> naive_dt = datetime(2024, 5, 29, 12, 0, 0)
        >>> format_datetime_to_utc_iso8601(naive_dt)
        '2024-05-29T12:00:00Z'
        
        >>> aware_dt = datetime(2024, 5, 29, 15, 30, 0, tzinfo=timezone.utc)
        >>> format_datetime_to_utc_iso8601(aware_dt)
        '2024-05-29T15:30:00Z'
    """
    if dt is None:
        return None
    
    # Check if datetime is naive (no timezone info)
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        # Assume naive datetime is already in UTC and add UTC timezone
        dt_utc = dt.replace(tzinfo=timezone.utc)
    else:
        # Convert timezone-aware datetime to UTC
        dt_utc = dt.astimezone(timezone.utc)
    
    # Format as ISO8601 with 'Z' suffix for UTC
    return dt_utc.isoformat().replace('+00:00', 'Z')


def ensure_utc_datetime(dt: Union[datetime, None]) -> Union[datetime, None]:
    """Ensure a datetime object is timezone-aware and in UTC.
    
    Args:
        dt: The datetime object to normalize (can be naive or timezone-aware)
        
    Returns:
        UTC timezone-aware datetime object, or None if input is None
    """
    if dt is None:
        return None
    
    # Check if datetime is naive (no timezone info)
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        # Assume naive datetime is already in UTC and add UTC timezone
        return dt.replace(tzinfo=timezone.utc)
    else:
        # Convert timezone-aware datetime to UTC
        return dt.astimezone(timezone.utc)