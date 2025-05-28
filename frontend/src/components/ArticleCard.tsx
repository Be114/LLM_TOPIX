/**
 * ArticleCard component for displaying individual news articles.
 * 
 * This component renders a single article with title, summary, publication date,
 * and source information. It supports accessibility features, responsive design,
 * and user interactions.
 */

import React, { useMemo } from 'react';
import { ArticleCardProps } from '../types/article';
import styles from './ArticleCard.module.css';

// Extract utility functions outside component to prevent recreation on every render
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

const formatSourceUrl = (url: string): string => {
  try {
    const domain = new URL(url).hostname;
    return domain.replace('www.', '');
  } catch {
    return url; // Fallback to original URL if parsing fails
  }
};

export const ArticleCard: React.FC<ArticleCardProps> = React.memo(({ 
  article, 
  className = '', 
  onClick 
}) => {
  // Memoize expensive computations
  const formattedDate = useMemo(() => formatDate(article.published_at), [article.published_at]);
  const formattedSource = useMemo(() => formatSourceUrl(article.source_url), [article.source_url]);

  const handleClick = (): void => {
    if (onClick) {
      onClick(article);
    }
  };

  const handleKeyDown = (event: React.KeyboardEvent): void => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleClick();
    }
  };

  const cardClasses = `${styles.articleCard} ${className}`;

  return (
    <article
      className={cardClasses}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
      tabIndex={onClick ? 0 : -1}
      role="article"
      aria-label={`Article: ${article.title}`}
    >
      <header className={styles.cardHeader}>
        <h3 className={styles.title}>
          {article.title}
        </h3>

        <div className={styles.sourceInfo}>
          <a 
            href={article.source_url}
            className={styles.source}
            target="_blank"
            rel="noopener noreferrer"
            onClick={(e) => e.stopPropagation()} // Prevent card click when clicking source link
            aria-label={`Read original article at ${formattedSource}`}
          >
            {formattedSource}
          </a>
          <time 
            dateTime={article.published_at}
            className={styles.date}
          >
            {formattedDate}
          </time>
        </div>
      </header>

      <p className={styles.summary}>
        {article.summary_truncated}
      </p>
    </article>
  );
});