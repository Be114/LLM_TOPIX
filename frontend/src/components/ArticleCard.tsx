/**
 * ArticleCard component for displaying individual news articles.
 * 
 * This component renders a single article with title, summary, publication date,
 * and source information. It supports accessibility features, responsive design,
 * and user interactions.
 */

import React from 'react';
import { ArticleCardProps } from '../types/article';

export const ArticleCard: React.FC<ArticleCardProps> = ({ 
  article, 
  className = '', 
  onClick 
}) => {
  /**
   * Format the publication date for display.
   * Converts ISO string to readable format.
   */
  const formatDate = (dateString: string): string => {
    try {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    } catch {
      return dateString; // Fallback to original string if parsing fails
    }
  };

  /**
   * Extract domain name from URL for cleaner source display.
   */
  const formatSourceUrl = (url: string): string => {
    try {
      const domain = new URL(url).hostname;
      return domain.replace('www.', '');
    } catch {
      return url; // Fallback to original URL if parsing fails
    }
  };

  /**
   * Handle click events for keyboard and mouse interactions.
   */
  const handleClick = (): void => {
    if (onClick) {
      onClick(article);
    }
  };

  /**
   * Handle keyboard events for accessibility.
   */
  const handleKeyDown = (event: React.KeyboardEvent): void => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleClick();
    }
  };

  return (
    <article
      className={`article-card ${className}`}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
      tabIndex={onClick ? 0 : -1}
      role="article"
      aria-label={`Article: ${article.title}`}
      style={{
        border: '1px solid #e1e5e9',
        borderRadius: '8px',
        padding: '1rem',
        margin: '0.5rem 0',
        backgroundColor: '#ffffff',
        cursor: onClick ? 'pointer' : 'default',
        transition: 'box-shadow 0.2s ease, transform 0.1s ease',
        ...(onClick && {
          ':hover': {
            boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
            transform: 'translateY(-1px)'
          },
          ':focus': {
            outline: '2px solid #0066cc',
            outlineOffset: '2px'
          }
        })
      }}
    >
      {/* Article Title */}
      <h3 
        style={{
          margin: '0 0 0.5rem 0',
          fontSize: '1.125rem',
          fontWeight: '600',
          lineHeight: '1.4',
          color: '#1a1a1a'
        }}
      >
        {article.title}
      </h3>

      {/* Article Summary */}
      <p 
        style={{
          margin: '0 0 0.75rem 0',
          fontSize: '0.875rem',
          lineHeight: '1.5',
          color: '#4a4a4a'
        }}
      >
        {article.summary_truncated}
      </p>

      {/* Article Metadata */}
      <div 
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          fontSize: '0.75rem',
          color: '#666666',
          marginTop: '0.5rem'
        }}
      >
        {/* Publication Date */}
        <time 
          dateTime={article.published_at}
          style={{ fontWeight: '500' }}
        >
          {formatDate(article.published_at)}
        </time>

        {/* Source */}
        <span 
          style={{
            fontWeight: '500',
            textTransform: 'uppercase',
            letterSpacing: '0.5px'
          }}
        >
          {formatSourceUrl(article.source_url)}
        </span>
      </div>

      {/* Responsive Design Styles */}
      <style jsx>{`
        @media (max-width: 768px) {
          .article-card {
            padding: 0.75rem;
            margin: 0.25rem 0;
          }
          
          .article-card h3 {
            font-size: 1rem;
          }
          
          .article-card p {
            font-size: 0.8125rem;
          }
          
          .article-card > div {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.25rem;
          }
        }
        
        @media (prefers-reduced-motion: reduce) {
          .article-card {
            transition: none;
          }
        }
      `}</style>
    </article>
  );
};