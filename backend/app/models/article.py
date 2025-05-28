"""Article database model for LLM news."""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from app.config.constants import ARTICLE_TITLE_MAX_LENGTH, ARTICLE_URL_MAX_LENGTH

Base = declarative_base()


class Article(Base):
    """Article model representing news articles in the database.
    
    Attributes:
        id: Primary key identifier
        title: Article title (max length defined in constants)
        summary: Article summary/content
        published_at: Publication timestamp
        source_url: Original article URL (max length defined in constants)
        created_at: Record creation timestamp
        updated_at: Record update timestamp
    """
    
    __tablename__ = 'articles'
    
    id: Optional[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(ARTICLE_TITLE_MAX_LENGTH), nullable=False)
    summary: str = Column(Text, nullable=False)
    published_at: datetime = Column(DateTime, nullable=False, index=True)
    source_url: str = Column(String(ARTICLE_URL_MAX_LENGTH), nullable=False, unique=True)
    created_at: datetime = Column(DateTime, default=lambda: datetime.utcnow(), nullable=False)
    updated_at: datetime = Column(
        DateTime, 
        default=lambda: datetime.utcnow(), 
        onupdate=lambda: datetime.utcnow(), 
        nullable=False
    )
    
    def __repr__(self) -> str:
        """String representation of Article."""
        return f'<Article {self.id}: {self.title[:50]}>'