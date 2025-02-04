from flask import Flask, render_template, request, jsonify
import asyncio
import nltk
from wikipedia_fetcher import fetch_wikipedia_article_content
from article_analysis import generate_summary

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    data = request.get_json()
    article_title = data.get('article_title')
    if not article_title:
        return jsonify({'error': 'Article title is required'}), 400

    success, content = fetch_wikipedia_article_content(article_title)
    if success:
        return jsonify({'title': article_title, 'content': content})
    else:
        return jsonify({'error': f"Article '{article_title}' not found"}), 404

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        summary = loop.run_until_complete(generate_summary(content))
        loop.close()
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=str(error)), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Page not found'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
