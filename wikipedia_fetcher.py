"""Wikipedia article fetcher and analyzer.

This module provides functionality to fetch articles from Wikipedia,
save them locally, and perform text analysis including word frequency
and sentence structure analysis.

Typical usage:
    python wikipedia_fetcher.py "Article Title"

Dependencies:
    - wikipediaapi: For fetching Wikipedia content
    - nltk: For text processing and analysis
"""

import wikipediaapi
import sys
import nltk
import asyncio
from typing import Dict, Any
from article_analysis import process_text, analyze_text
from article_visualizations import create_visualizations

def fetch_wikipedia_article_content(title: str) -> tuple[bool, str]:
    """Fetch a Wikipedia article content.
    
    Args:
        title (str): Title of the Wikipedia article to fetch.
        
    Returns:
        tuple[bool, str]: Tuple containing:
            - bool: True if successful, False if article doesn't exist
            - str: Article content if successful, empty string if failed
    """
    user_agent = "MyWikipediaFetcher/1.0 (https://github.com/yourusername/yourrepo; your.email@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent=user_agent
    )
    page = wiki_wiki.page(title)
    
    if not page.exists():
        return False, ''
        
    content = f"# {title}\n\n{page.text}"
    return True, content

async def main() -> None:
    """Main entry point for the script.
    
    Downloads required NLTK data and processes command line arguments.
    Expects exactly one argument: the Wikipedia article title.
    
    Usage:
        python wikipedia_fetcher.py "Article Title"
        
    Exit codes:
        0: Success
        1: Invalid number of arguments
    """
    # Download required NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')
    
    if len(sys.argv) != 2:
        print("Usage: python wikipedia_fetcher.py <article_title>")
        sys.exit(1)
        
    article_title = sys.argv[1]
    success, content = fetch_wikipedia_article_content(article_title)
    if not success:
        print(f"Error: Article '{article_title}' not found")
        sys.exit(1)
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
