-- Database initialization script for LLM TOPIX
-- This script creates the articles table with proper indexes and constraints

-- Create articles table
CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    summary TEXT NOT NULL,
    published_at TIMESTAMP NOT NULL,
    source_url VARCHAR(512) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_articles_published_at ON articles(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_articles_created_at ON articles(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_articles_source_url ON articles(source_url);

-- Create full-text search index for future search functionality
CREATE INDEX IF NOT EXISTS idx_articles_title_search ON articles USING gin(to_tsvector('english', title));
CREATE INDEX IF NOT EXISTS idx_articles_summary_search ON articles USING gin(to_tsvector('english', summary));

-- Create trigger to automatically update the updated_at column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_articles_updated_at 
    BEFORE UPDATE ON articles 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- Insert sample data for testing
INSERT INTO articles (title, summary, published_at, source_url) VALUES
(
    'GPT-4 Breakthrough: New Multimodal Capabilities Announced',
    'OpenAI has announced significant improvements to GPT-4, including enhanced multimodal capabilities that allow the model to process and understand images alongside text. This breakthrough represents a major leap forward in AI technology, enabling more sophisticated human-computer interactions across various domains including education, healthcare, and creative industries.',
    '2024-01-15 10:30:00',
    'https://openai.com/blog/gpt-4-multimodal-breakthrough'
),
(
    'Claude AI Introduces Constitutional AI Framework',
    'Anthropic has released details about their Constitutional AI approach used in Claude, which aims to make AI systems more helpful, harmless, and honest. The framework represents a novel approach to AI safety that could influence the entire industry. This methodology focuses on training AI systems to follow a set of principles that guide their behavior and decision-making processes.',
    '2024-01-15 09:15:00',
    'https://anthropic.com/blog/constitutional-ai-framework'
),
(
    'Google Gemini Ultra Achieves New Benchmarks in Reasoning',
    'Google has announced that Gemini Ultra has achieved unprecedented performance on complex reasoning tasks, surpassing previous state-of-the-art results on multiple academic benchmarks. The model demonstrates remarkable capabilities in mathematical problem-solving, code generation, and logical reasoning that could transform how we approach artificial intelligence applications.',
    '2024-01-15 08:45:00',
    'https://deepmind.google/blog/gemini-ultra-reasoning-benchmarks'
),
(
    'LLM Efficiency Revolution: New Compression Techniques Reduce Model Size by 90%',
    'Researchers at MIT have developed revolutionary compression techniques that can reduce large language model sizes by up to 90% while maintaining 95% of their original performance. This breakthrough could democratize access to powerful AI models and enable deployment on edge devices with limited computational resources.',
    '2024-01-15 07:20:00',
    'https://mit.edu/news/llm-compression-breakthrough'
),
(
    'AI Safety Summit: Industry Leaders Propose New Governance Framework',
    'Leading AI companies including OpenAI, Anthropic, and Google have jointly proposed a comprehensive governance framework for AI development and deployment. The framework addresses key concerns around AI safety, transparency, and accountability while promoting continued innovation in the field. This collaborative effort represents an unprecedented level of industry cooperation on AI safety issues.',
    '2024-01-15 06:00:00',
    'https://aisafetysummit.org/governance-framework-proposal'
),
(
    'Breakthrough in AI Interpretability: New Method Reveals How LLMs Think',
    'Scientists have developed a groundbreaking technique to peer inside the "black box" of large language models, revealing how these systems process information and make decisions. This advancement in AI interpretability could lead to more trustworthy and reliable AI systems across all applications.',
    '2024-01-14 22:30:00',
    'https://research.ai/interpretability-breakthrough'
);