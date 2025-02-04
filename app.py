from flask import Flask, render_template, request, jsonify
import asyncio
import nltk
from wikipedia_fetcher import fetch_wikipedia_article_content
from article_analysis import generate_summary, process_text, analyze_text
from button_config import ButtonRegistry, ButtonConfig, initialize_default_buttons

# Initialize the default buttons
initialize_default_buttons()

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', ButtonRegistry=ButtonRegistry)

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

async def process_analysis(content: str, config: ButtonConfig) -> str:
    """Generic handler for processing text analysis with a configuration."""
    if config.id == "analyze_stats":
        # Use the existing analyze_text function
        tokens, sentences = process_text(content)
        stats, freq_dist = analyze_text(tokens, sentences)
        
        # Format the results as HTML
        html_result = f"""
            <div class='stats-result'>
                <p>Total Words: {stats['total_words']}</p>
                <p>Unique Words: {stats['unique_words']}</p>
                <p>Average Sentence Length: {stats['avg_sentence_length']}</p>
                <h4>Top 10 Words:</h4>
                <ul>
                    {"".join(f"<li>{word}: {count}</li>" for word, count in stats['top_words'].items())}
                </ul>
            </div>
        """
        return html_result
    else:
        # Use the existing generate_summary function
        return await generate_summary(f"{config.prompt}\n\n{content}")


def register_analysis_route(config: ButtonConfig):
    """Dynamically register a new analysis route."""
    endpoint_name = f'handle_{config.id}'
    
    async def route_handler():
        data = request.get_json()
        content = data.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400

        try:
            result = await process_analysis(content, config)
            return jsonify({
                'result': result,
                'result_type': config.result_type
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # Set the endpoint name before registration
    route_handler.__name__ = endpoint_name
    
    # Register the route with the unique endpoint name
    app.add_url_rule(
        f'/{config.endpoint}',
        endpoint=endpoint_name,
        view_func=route_handler,
        methods=['POST']
    )

def register_all_buttons():
    """Register all buttons from the registry."""
    for button in ButtonRegistry.get_all():
        register_analysis_route(button)

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=str(error)), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Page not found'), 404

if __name__ == '__main__':
    register_all_buttons()
    app.run(host='0.0.0.0', port=5001, debug=True)
