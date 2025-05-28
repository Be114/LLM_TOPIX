"""Article database model for LLM news."""

from datetime import datetime
from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    """Article model representing news articles in the database.
    
    Attributes:
        id: Primary key identifier
        title: Article title (max 255 characters)
        summary: Article summary/content
        published_at: Publication timestamp
        source_url: Original article URL
        created_at: Record creation timestamp
        updated_at: Record update timestamp
    """
    
    __tablename__ = 'articles'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(255), nullable=False)
    summary: str = Column(Text, nullable=False)
    published_at: datetime = Column(DateTime, nullable=False, index=True)
    source_url: str = Column(String(512), nullable=False, unique=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow, 
        nullable=False
    )
    
    def __repr__(self) -> str:
        """String representation of Article."""
        return f'<Article {self.id}: {self.title[:50]}>'