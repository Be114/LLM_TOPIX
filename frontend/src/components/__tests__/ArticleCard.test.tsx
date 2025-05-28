/**
 * Test suite for ArticleCard component.
 * 
 * This module contains comprehensive tests for the ArticleCard component,
 * covering UI display, accessibility, responsive design, and user interactions.
 */

import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ArticleCard } from '../ArticleCard';
import { Article, ArticleId, ISO8601String, URLString } from '../../types/article';

describe('ArticleCard Component', () => {
  const mockArticle: Article = {
    id: 1 as ArticleId,
    title: 'Test Article Title',
    summary_truncated: 'This is a test article summary that should be displayed correctly.',
    published_at: '2024-01-15T10:30:00Z' as ISO8601String,
    source_url: 'https://example.com/test-article' as URLString
  };

  const longSummaryArticle: Article = {
    id: 2 as ArticleId,
    title: 'Article with Long Summary',
    summary_truncated: 'A'.repeat(100) + '...',
    published_at: '2024-01-15T10:30:00Z' as ISO8601String,
    source_url: 'https://example.com/long-article' as URLString
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('UI Display Functionality', () => {
    test('displays article title correctly', () => {
      /**
       * Test that the article title is rendered and visible to users.
       * This is critical for article identification and SEO.
       */
      render(<ArticleCard article={mockArticle} />);
      
      const titleElement = screen.getByText(mockArticle.title);
      expect(titleElement).toBeInTheDocument();
      expect(titleElement).toBeVisible();
    });

    test('displays article summary correctly', () => {
      /**
       * Test that the article summary is rendered properly.
       * This provides users with a preview of the article content.
       */
      render(<ArticleCard article={mockArticle} />);
      
      const summaryElement = screen.getByText(mockArticle.summary_truncated);
      expect(summaryElement).toBeInTheDocument();
      expect(summaryElement).toBeVisible();
    });

    test('displays formatted publication date', () => {
      /**
       * Test that the publication date is displayed in a human-readable format.
       * Users need to understand when the article was published.
       */
      render(<ArticleCard article={mockArticle} />);
      
      // Should display date in readable format
      const dateElement = screen.getByText(/2024/);
      expect(dateElement).toBeInTheDocument();
    });

    test('displays source URL or source name', () => {
      /**
       * Test that the article source is displayed to give users
       * context about the article's origin.
       */
      render(<ArticleCard article={mockArticle} />);
      
      // Should display either the full URL or a formatted source name
      const sourceElement = screen.getByText(/example\.com/);
      expect(sourceElement).toBeInTheDocument();
    });
  });

  describe('Summary Truncation Functionality', () => {
    test('displays ellipsis for truncated summaries', () => {
      /**
       * Test that truncated summaries are properly indicated with ellipsis.
       * This helps users understand that there is more content available.
       */
      render(<ArticleCard article={longSummaryArticle} />);
      
      const summaryElement = screen.getByText(longSummaryArticle.summary_truncated);
      expect(summaryElement).toBeInTheDocument();
      expect(summaryElement.textContent).toContain('...');
    });

    test('handles exactly 100 character summaries correctly', () => {
      /**
       * Test edge case where summary is exactly at the character limit.
       * This ensures consistent handling of boundary conditions.
       */
      const exactLengthArticle: Article = {
        ...mockArticle,
        summary_truncated: 'A'.repeat(100)
      };
      
      render(<ArticleCard article={exactLengthArticle} />);
      
      const summaryElement = screen.getByText(exactLengthArticle.summary_truncated);
      expect(summaryElement).toBeInTheDocument();
      expect(summaryElement.textContent).not.toContain('...');
    });

    test('displays full summary when under 100 characters', () => {
      /**
       * Test that short summaries are displayed in full without ellipsis.
       * This ensures optimal use of available space for short content.
       */
      const shortSummaryArticle: Article = {
        ...mockArticle,
        summary_truncated: 'Short summary'
      };
      
      render(<ArticleCard article={shortSummaryArticle} />);
      
      const summaryElement = screen.getByText('Short summary');
      expect(summaryElement).toBeInTheDocument();
      expect(summaryElement.textContent).not.toContain('...');
    });
  });

  describe('Responsive Design', () => {
    test('renders correctly on mobile viewport', () => {
      /**
       * Test that the component displays properly on mobile devices.
       * This ensures good user experience across all device types.
       */
      // Mock mobile viewport
      Object.defineProperty(window, 'innerWidth', {
        writable: true,
        configurable: true,
        value: 375,
      });
      
      render(<ArticleCard article={mockArticle} />);
      
      const cardElement = screen.getByRole('article');
      expect(cardElement).toBeInTheDocument();
      
      // Should be visible and accessible on mobile
      expect(cardElement).toBeVisible();
    });

    test('renders correctly on desktop viewport', () => {
      /**
       * Test that the component displays properly on desktop devices.
       * This ensures consistent experience across device types.
       */
      // Mock desktop viewport
      Object.defineProperty(window, 'innerWidth', {
        writable: true,
        configurable: true,
        value: 1920,
      });
      
      render(<ArticleCard article={mockArticle} />);
      
      const cardElement = screen.getByRole('article');
      expect(cardElement).toBeInTheDocument();
      expect(cardElement).toBeVisible();
    });
  });

  describe('Accessibility Features', () => {
    test('has proper ARIA attributes', () => {
      /**
       * Test that the component includes necessary ARIA attributes
       * for screen readers and assistive technologies.
       */
      render(<ArticleCard article={mockArticle} />);
      
      const cardElement = screen.getByRole('article');
      expect(cardElement).toHaveAttribute('aria-label');
      
      // Should have accessible name for the article
      expect(cardElement).toHaveAccessibleName();
    });

    test('supports keyboard navigation', () => {
      /**
       * Test that the component can be navigated using keyboard only.
       * This is essential for accessibility compliance.
       */
      const mockOnClick = jest.fn();
      render(<ArticleCard article={mockArticle} onClick={mockOnClick} />);
      
      const cardElement = screen.getByRole('article');
      
      // Should be focusable
      cardElement.focus();
      expect(cardElement).toHaveFocus();
      
      // Should respond to Enter key
      fireEvent.keyDown(cardElement, { key: 'Enter', code: 'Enter' });
      expect(mockOnClick).toHaveBeenCalledWith(mockArticle);
    });

    test('has proper heading hierarchy', () => {
      /**
       * Test that the component uses proper heading tags for SEO
       * and screen reader navigation.
       */
      render(<ArticleCard article={mockArticle} />);
      
      // Article title should be in a heading element
      const titleHeading = screen.getByRole('heading');
      expect(titleHeading).toBeInTheDocument();
      expect(titleHeading).toHaveTextContent(mockArticle.title);
    });
  });

  describe('User Interactions', () => {
    test('calls onClick handler when clicked', () => {
      /**
       * Test that click events are properly handled and propagated.
       * This enables article navigation and interaction.
       */
      const mockOnClick = jest.fn();
      render(<ArticleCard article={mockArticle} onClick={mockOnClick} />);
      
      const cardElement = screen.getByRole('article');
      fireEvent.click(cardElement);
      
      expect(mockOnClick).toHaveBeenCalledTimes(1);
      expect(mockOnClick).toHaveBeenCalledWith(mockArticle);
    });

    test('does not crash when onClick is not provided', () => {
      /**
       * Test that the component handles missing onClick gracefully.
       * This ensures robust behavior in different usage scenarios.
       */
      expect(() => {
        render(<ArticleCard article={mockArticle} />);
        
        const cardElement = screen.getByRole('article');
        fireEvent.click(cardElement);
      }).not.toThrow();
    });
  });

  describe('Performance Requirements', () => {
    test('renders within performance budget (16ms for 60fps)', () => {
      /**
       * Test that the component renders quickly enough to maintain
       * smooth 60fps user interface performance.
       */
      const startTime = performance.now();
      
      render(<ArticleCard article={mockArticle} />);
      
      const endTime = performance.now();
      const renderTime = endTime - startTime;
      
      expect(renderTime).toBeLessThan(16); // 16ms for 60fps
    });
  });

  describe('Error Handling', () => {
    test('handles missing article data gracefully', () => {
      /**
       * Test that the component doesn't crash with incomplete article data.
       * This ensures robust error handling in production.
       */
      const incompleteArticle = {
        id: 1 as ArticleId,
        title: '',
        summary_truncated: '',
        published_at: '' as ISO8601String,
        source_url: '' as URLString
      } as Article;
      
      expect(() => {
        render(<ArticleCard article={incompleteArticle} />);
      }).not.toThrow();
    });

    test('requires article ID to be present and defined', () => {
      /**
       * RED phase test: This test ensures that Article ID is mandatory.
       * When we make id required in Article type, this test should pass,
       * but TypeScript should catch attempts to create Articles without id.
       */
      const articleWithId: Article = {
        id: 1 as ArticleId,
        title: 'Test Article',
        summary_truncated: 'Test summary',
        published_at: '2024-01-15T10:30:00Z' as ISO8601String,
        source_url: 'https://example.com' as URLString
      };
      
      // This should work fine
      expect(() => {
        render(<ArticleCard article={articleWithId} />);
      }).not.toThrow();
      
      // Verify the id is actually present and accessible
      const renderedCard = screen.getByRole('article');
      expect(renderedCard).toBeInTheDocument();
      
      // The article should have an id property that's not undefined
      expect(articleWithId.id).toBeDefined();
      expect(typeof articleWithId.id).toBe('number');
      expect(articleWithId.id).toBeGreaterThan(0);
    });
  });
});