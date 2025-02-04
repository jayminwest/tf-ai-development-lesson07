import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.probability import FreqDist
import os

def create_visualizations(freq_dist: FreqDist) -> None:
    """Create and save word frequency visualizations.
    
    Args:
        freq_dist: NLTK frequency distribution of words
    """
    # Ensure the directory exists
    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    # Bar chart
    plt.figure(figsize=(10, 6))
    words, freqs = zip(*freq_dist.most_common(10))
    plt.bar(words, freqs, color='skyblue')
    plt.title('Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/word_frequencies.png')
    plt.close()
    
    # Word cloud
    wordcloud = WordCloud(
        background_color='white',
        max_words=100,
        width=800,
        height=400
    ).generate_from_frequencies(freq_dist)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('static/images/word_cloud.png')
    plt.close()
