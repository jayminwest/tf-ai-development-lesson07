from flask import Flask, render_template, request, jsonify
import asyncio
import nltk
from wikipedia_fetcher import fetch_wikipedia_article_content
from article_analysis import generate_summary
from button_config import ButtonRegistry, ButtonConfig

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

async def process_analysis(content: str, prompt: str) -> str:
    """Generic handler for processing text analysis with a prompt."""
    return await generate_summary(f"{prompt}\n\n{content}")

@app.route('/analyze', methods=['POST'])
async def analyze():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    try:
        summary = await process_analysis(content, "Summarize the following text:")
        return jsonify({'result': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def register_analysis_route(config: ButtonConfig):
    """Dynamically register a new analysis route."""
    @app.route(f'/{config.endpoint}', methods=['POST'])
    async def handler():
        data = request.get_json()
        content = data.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400

        try:
            result = await process_analysis(content, config.prompt)
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # Rename the function to avoid naming conflicts
    handler.__name__ = f'handle_{config.id}'

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=str(error)), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Page not found'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
