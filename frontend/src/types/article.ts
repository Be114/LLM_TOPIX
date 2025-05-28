/**
 * Type definitions for article-related data structures.
 */

export interface Article {
  /** Unique identifier for the article */
  id: number;
  
  /** Article title */
  title: string;
  
  /** Article summary (may be truncated) */
  summary_truncated: string;
  
  /** Publication date and time */
  published_at: string;
  
  /** Source URL of the original article */
  source_url: string;
}

export interface ArticleCardProps {
  /** Article data to display */
  article: Article;
  
  /** Optional CSS class name for styling */
  className?: string;
  
  /** Optional click handler for article interaction */
  onClick?: (article: Article) => void;
}