"""Response helper utilities for consistent API responses.

This module provides utility functions for creating standardized
API responses across the application.
"""

from typing import Dict, Tuple, Any
from flask import jsonify


def create_error_response(error_type: str, message: str, status_code: int) -> Tuple[Dict[str, str], int]:
    """Create a standardized error response.
    
    Args:
        error_type: The type/category of the error
        message: Human-readable error message
        status_code: HTTP status code
        
    Returns:
        Tuple containing JSON response dict and status code
    """
    return jsonify({
        'error': error_type,
        'message': message
    }), status_code


def create_success_response(data: Any, status_code: int = 200) -> Tuple[Dict[str, Any], int]:
    """Create a standardized success response.
    
    Args:
        data: The response data
        status_code: HTTP status code (default: 200)
        
    Returns:
        Tuple containing JSON response dict and status code
    """
    return jsonify(data), status_code


def create_not_found_response(resource: str = "resource") -> Tuple[Dict[str, str], int]:
    """Create a standardized 404 response.
    
    Args:
        resource: The type of resource that was not found
        
    Returns:
        Tuple containing JSON response dict and 404 status code
    """
    return create_error_response(
        'Not found',
        f'The requested {resource} was not found',
        404
    )


def create_internal_error_response() -> Tuple[Dict[str, str], int]:
    """Create a standardized 500 response.
    
    Returns:
        Tuple containing JSON response dict and 500 status code
    """
    return create_error_response(
        'Internal server error',
        'An unexpected error occurred',
        500
    )