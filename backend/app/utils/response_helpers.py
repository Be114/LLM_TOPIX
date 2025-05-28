"""Response helper utilities for consistent API responses.

This module provides utility functions for creating standardized
API responses across the application.
"""

from typing import Dict, Tuple, Any
from flask import jsonify


def create_error_response(error_code: str, message: str, status_code: int, details: Dict[str, Any] = None) -> Tuple[Dict[str, str], int]:
    """Create a standardized error response according to CLAUDE.md format.
    
    Args:
        error_code: The error code (e.g., 'DATABASE_UNAVAILABLE')
        message: Human-readable error message
        status_code: HTTP status code
        details: Optional additional error details
        
    Returns:
        Tuple containing JSON response dict and status code
    """
    from datetime import datetime
    
    error_response = {
        "status": "error",
        "error": {
            "code": error_code,
            "message": message,
            "details": details or {
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        }
    }
    
    return jsonify(error_response), status_code


def create_success_response(data: Any, status_code: int = 200, message: str = None) -> Tuple[Dict[str, Any], int]:
    """Create a standardized success response according to CLAUDE.md format.
    
    Args:
        data: The response data
        status_code: HTTP status code (default: 200)
        message: Optional success message
        
    Returns:
        Tuple containing JSON response dict and status code
    """
    response = {
        "status": "success",
        "data": data
    }
    
    if message:
        response["message"] = message
    
    return jsonify(response), status_code


def create_not_found_response(resource: str = "resource") -> Tuple[Dict[str, str], int]:
    """Create a standardized 404 response.
    
    Args:
        resource: The type of resource that was not found
        
    Returns:
        Tuple containing JSON response dict and 404 status code
    """
    return create_error_response(
        'RESOURCE_NOT_FOUND',
        f'The requested {resource} was not found',
        404
    )


def create_internal_error_response() -> Tuple[Dict[str, str], int]:
    """Create a standardized 500 response.
    
    Returns:
        Tuple containing JSON response dict and 500 status code
    """
    return create_error_response(
        'INTERNAL_SERVER_ERROR',
        'An unexpected error occurred',
        500
    )