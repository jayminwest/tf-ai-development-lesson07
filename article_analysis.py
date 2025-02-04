import nltk
import re
import asyncio
from ollama import chat
from typing import Tuple, List, Dict, Any

def process_text(text: str) -> Tuple[List[str], List[str]]:
    """Clean and tokenize input text.
    
    Args:
        text: Raw text string to process
        
    Returns:
        Tuple containing:
            - List of cleaned and filtered tokens
            - List of raw sentences
    """
    # Get raw sentences first
    sentences = nltk.sent_tokenize(text)
    
    # Clean text for word analysis
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join(text.split())
    
    # Tokenize cleaned text
    words = nltk.word_tokenize(text)
    
    # Remove stopwords and short words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in words 
             if word not in stop_words and len(word) > 2]
    
    return tokens, sentences

async def generate_summary(text: str) -> str:
    """Generate a summary of the text using Ollama.

    Args:
        text: The text to summarize.

    Returns:
        str: The summary of the text.
    """
    prompt = f"Summarize the following text concisely:\n\n{text}"
    response = await asyncio.to_thread(
        chat,
        model='deepseek-r1:8b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.message.content.strip()

def analyze_text(tokens: List[str], sentences: List[str]) -> Tuple[Dict, nltk.probability.FreqDist]:
    """Calculate text statistics.
    
    Args:
        tokens: List of processed word tokens
        sentences: List of raw sentences
        
    Returns:
        Tuple containing:
            - Dictionary of text statistics
            - Frequency distribution of words
    """
    # Word frequencies
    freq_dist = nltk.FreqDist(tokens)
    
    # Calculate average words per sentence
    stop_words = set(nltk.corpus.stopwords.words('english'))
    sentence_lengths = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence.lower())
        word_count = len([word for word in words 
                         if word.isalnum() and 
                         word not in stop_words and 
                         len(word) > 2])
        sentence_lengths.append(word_count)
    
    avg_sentence_length = round(sum(sentence_lengths) / len(sentences), 2)
    
    # Basic stats
    stats = {
        'total_words': len(tokens),
        'unique_words': len(set(tokens)),
        'avg_sentence_length': avg_sentence_length,
        'top_words': dict(freq_dist.most_common(10))
    }
    
    return stats, freq_dist
