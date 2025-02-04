# Architect Prompt Template

## High Level Goals
- Create a Flask web application that allows users to fetch, display and summarize Wikipedia articles using Ollama for summarization

## Mid Level Goals
- Implement a Flask web server with routing and templates
- Create a form for Wikipedia article name entry
- Add Wikipedia article fetching and display functionality
- Integrate Ollama for article summarization
- Implement the summary display interface

## Implementation Guidelines
- Dependencies:
  - Flask for web framework
  - Wikipedia-API for article fetching
  - Ollama for local LLM summarization
- Coding standards:
  - Use Google-style docstrings as per developer guide
  - Type hints for all functions
- Technical requirements:
  - Local Ollama instance must be running
  - Async handling for API calls
  - Error handling for failed article fetches

## Project Context

### Beginning files
- DEVELOPER_GUIDE.md
- wikipedia_fetcher.py
- article_analysis.py

### Ending files
- app.py (Flask application)
- templates/
  - base.html
  - index.html
  - article.html
- static/
  - styles.css
- wikipedia_fetcher.py (modified)
- article_analysis.py (modified)

## Low Level Goals

1. Set up Flask application structure
```python
# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# templates/base.html - Create Bootstrap base template
# templates/index.html - Extend base.html
# static/styles.css - Add custom styles
```

2. Create Wikipedia article input and fetch interface
```python
# templates/index.html
<form id="article-form">
    <input name="article_name" required>
    <button type="button" id="fetch-article">Fetch Wikipedia Article</button>
</form>
<div id="article-content" style="display:none">
    <h2>Raw Wikipedia Text</h2>
    <div id="raw-text"></div>
    <button type="button" id="analyze-article">Analyze Article</button>
</div>

# app.py
@app.route('/fetch', methods=['POST'])
def fetch():
    try:
        article = wikipedia_fetcher.get_article(request.json['article_name'])
        return jsonify({
            'title': article.title,
            'content': article.content
        })
    except ArticleNotFoundError:
        return jsonify({'error': 'Article not found'}), 404

@app.route('/analyze', methods=['POST'])
async def analyze():
    try:
        text = request.json['content']
        summary = await article_analysis.generate_summary(text)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

3. Implement JavaScript for handling article fetch and analysis
```javascript
// templates/index.html
<script>
document.getElementById('fetch-article').addEventListener('click', async () => {
    const articleName = document.querySelector('input[name="article_name"]').value;
    const response = await fetch('/fetch', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({article_name: articleName})
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById('raw-text').textContent = data.content;
        document.getElementById('article-content').style.display = 'block';
    } else {
        alert(data.error);
    }
});

document.getElementById('analyze-article').addEventListener('click', async () => {
    const content = document.getElementById('raw-text').textContent;
    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({content: content})
    });
    const data = await response.json();
    if (response.ok) {
        const summaryDiv = document.createElement('div');
        summaryDiv.innerHTML = `<h3>Analysis Results</h3><p>${data.summary}</p>`;
        document.getElementById('article-content').appendChild(summaryDiv);
    } else {
        alert(data.error);
    }
});
</script>
```

4. Implement Ollama summarization
```python
# article_analysis.py
from ollama import chat
from ollama import ChatResponse

async def generate_summary(text: str) -> str:
    response: ChatResponse = await chat(
        model='deepseek-r1:1.5b',
        messages=[{
            'role': 'user',
            'content': f'Summarize this text concisely: {text}'
        }]
    )
    return response.message.content

# app.py
@app.route('/summarize/<title>')
async def summarize(title):
    article = wikipedia_fetcher.get_article(title)
    summary = await article_analysis.generate_summary(article.content)
    return jsonify({'summary': summary})
```

5. Add error handling and polish
```python
# app.py
@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error=str(error))

# templates/base.html
<div id="loading" style="display:none">
    Loading...
</div>

# static/styles.css
.error { color: red; }
.loading { display: none; }
```
