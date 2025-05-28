/**
 * Type definitions for article-related data structures.
 */

// Branded types for type safety
export type ISO8601String = string & { readonly brand: unique symbol };
export type URLString = string & { readonly brand: unique symbol };
export type ArticleId = number & { readonly brand: unique symbol };

export interface Article {
  /** Unique identifier for the article */
  readonly id: ArticleId;
  
  /** Article title */
  readonly title: string;
  
  /** Article summary (may be truncated) */
  readonly summary_truncated: string;
  
  /** Publication date and time in ISO 8601 format */
  readonly published_at: ISO8601String;
  
  /** Source URL of the original article */
  readonly source_url: URLString;
  
  /** Optional full content of the article */
  content?: string;
  
  /** Optional author information */
  author?: string;
  
  /** Optional tags or categories */
  tags?: string[];
  
  /** Record creation timestamp */
  created_at?: ISO8601String;
}

export interface ArticleCardProps {
  /** Article data to display */
  article: Article;
  
  /** Optional CSS class name for styling */
  className?: string;
  
  /** Optional click handler for article interaction */
  onClick?: (article: Article) => void;
}

export interface ArticleListResponse {
  /** Array of articles */
  articles: Article[];
  
  /** Total count of articles returned */
  count: number;
}

// Type guards for runtime validation
export const isValidURL = (url: string): url is URLString => {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
};

export const isValidISO8601 = (dateString: string): dateString is ISO8601String => {
  try {
    const date = new Date(dateString);
    return date.toISOString() === dateString;
  } catch {
    return false;
  }
};

export const isValidArticleId = (id: number): id is ArticleId => {
  return typeof id === 'number' && id > 0 && Number.isInteger(id);
};

export const validateArticle = (article: any): article is Article => {
  return (
    typeof article.id === 'number' &&
    isValidArticleId(article.id) &&
    typeof article.title === 'string' &&
    typeof article.summary_truncated === 'string' &&
    isValidISO8601(article.published_at) &&
    isValidURL(article.source_url)
  );
};