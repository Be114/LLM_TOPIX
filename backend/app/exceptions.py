"""Custom exception classes for the LLM TOPIX application."""


class ApplicationError(Exception):
    """Base exception class for all application errors."""
    
    def __init__(self, message: str, status_code: int = 500) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class DatabaseError(ApplicationError):
    """Exception raised for database-related errors."""
    
    def __init__(self, message: str = "Database operation failed") -> None:
        super().__init__(message, status_code=503)


class ValidationError(ApplicationError):
    """Exception raised for data validation errors."""
    
    def __init__(self, message: str = "Invalid input data") -> None:
        super().__init__(message, status_code=400)


class NotFoundError(ApplicationError):
    """Exception raised when requested resource is not found."""
    
    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, status_code=404)