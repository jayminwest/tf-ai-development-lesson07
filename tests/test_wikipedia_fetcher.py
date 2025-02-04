import pytest
from unittest.mock import Mock, patch
import os
from wikipedia_fetcher import fetch_wikipedia_article

@pytest.fixture
def mock_wikipedia_page():
    """Fixture to create a mock Wikipedia page"""
    mock_page = Mock()
    mock_page.exists.return_value = True
    mock_page.text = "This is a test article content."
    return mock_page

@pytest.fixture
def mock_freq_dist():
    """Fixture to create a mock frequency distribution"""
    mock_dist = Mock()
    return mock_dist

def test_fetch_wikipedia_article_success(mock_wikipedia_page, mock_freq_dist, tmp_path):
    """Test successful article fetch and processing"""
    with patch('wikipediaapi.Wikipedia') as mock_wiki, \
         patch('wikipedia_fetcher.process_text') as mock_process, \
         patch('wikipedia_fetcher.analyze_text') as mock_analyze, \
         patch('wikipedia_fetcher.create_visualizations') as mock_viz:
        
        # Setup mocks
        mock_wiki.return_value.page.return_value = mock_wikipedia_page
        mock_process.return_value = (["test", "words"], ["Test sentence."])
        mock_analyze.return_value = (
            {
                'total_words': 2,
                'unique_words': 2,
                'avg_sentence_length': 2.0,
                'top_words': {'test': 1, 'words': 1}
            },
            mock_freq_dist
        )
        
        # Run the function
        result = fetch_wikipedia_article("Test Article")
        
        # Assertions
        assert result is True
        mock_wiki.return_value.page.assert_called_once_with("Test Article")
        mock_process.assert_called_once()
        mock_analyze.assert_called_once()
        mock_viz.assert_called_once_with(mock_freq_dist)
        
        # Check if file was created
        assert os.path.exists("Test_Article.md")

def test_fetch_wikipedia_article_nonexistent():
    """Test handling of non-existent Wikipedia article"""
    with patch('wikipediaapi.Wikipedia') as mock_wiki:
        # Setup mock for non-existent page
        mock_page = Mock()
        mock_page.exists.return_value = False
        mock_wiki.return_value.page.return_value = mock_page
        
        # Run the function
        result = fetch_wikipedia_article("NonExistentArticle")
        
        # Assertions
        assert result is False
        mock_wiki.return_value.page.assert_called_once_with("NonExistentArticle")
