/**
 * @fileoverview Client-side handlers for Wikipedia article fetching and analysis.
 *
 * @description
 * Provides functionality for fetching Wikipedia articles and requesting their
 * analysis. Handles user interactions, API communication, and DOM updates.
 *
 * @author Jaymin West <jaymin@tandemflow.com>
 * @copyright 2024 TandemFlow
 * @license MIT
 */

/**
 * Handles click events on the article fetch button.
 * Makes an API request to retrieve Wikipedia article content based on user input.
 *
 * @private
 * @fires {fetch} Sends POST request to /fetch endpoint with article title
 * @throws {Error} If article title is empty or network request fails
 */
document.getElementById('fetch-article').addEventListener('click', async () => {
    const articleTitleInput = document.querySelector('input[name="article_title"]');
    const articleTitle = articleTitleInput.value.trim();
    if (!articleTitle) {
        alert('Please enter a Wikipedia article title.');
        return;
    }

    document.getElementById('loading').style.display = 'block';

    const response = await fetch('/fetch', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({article_title: articleTitle})
    });

    document.getElementById('loading').style.display = 'none';

    if (response.ok) {
        const data = await response.json();
        document.getElementById('article-title').textContent = data.title;
        document.getElementById('raw-text').textContent = data.content;
        document.getElementById('article-content').style.display = 'block';
    } else {
        const errorData = await response.json();
        alert('Error: ' + errorData.error);
    }
});

/**
 * Handles click events on the article analysis button.
 * Sends fetched article content to server for analysis and displays results.
 *
 * @private
 * @fires {fetch} Sends POST request to /analyze endpoint with article content
 * @throws {Error} If no article content exists or network request fails
 */
class ButtonHandler {
    static createHandler(buttonId, endpoint) {
        document.getElementById(buttonId).addEventListener('click', async () => {
            const content = document.getElementById('raw-text').textContent;
            if (!content) {
                alert('No article content to analyze.');
                return;
            }

            document.getElementById('loading').style.display = 'block';

            try {
                const response = await fetch(`/${endpoint}`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({content: content})
                });

                if (response.ok) {
                    const data = await response.json();
                    const resultDiv = document.getElementById('analysis-results');
                    const resultContent = data.result_type === 'html' ? 
                        data.result : 
                        `<p>${data.result}</p>`;
                    
                    resultDiv.innerHTML += `
                        <div class="analysis-result">
                            <h3>${buttonId} Results</h3>
                            ${resultContent}
                        </div>`;
                } else {
                    const errorData = await response.json();
                    alert('Error: ' + errorData.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        });
    }
}

