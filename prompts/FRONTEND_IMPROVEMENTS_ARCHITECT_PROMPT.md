# Architect Prompt Template
Process this prompt working through each step to ensure the objective is met.

## High Level Goal

- Ensure that the Wikipedia article content can be pasted, edited, and scrolled within the webpage, without affecting the current functionality of fetching wiki articles.

## Mid Level Goals

- Modify the HTML structure to include an editable element (using `contenteditable="true"`) for the Wikipedia article.
- Add CSS styles to make the editable content scrollable and visually appealing.
- Maintain the existing functionality of fetching Wikipedia articles.

## Implementation Guidelines
- **Technical details**:
  - Use an editable `<div>` with the attribute `contenteditable="true"` to allow in-browser text editing.
  - Apply CSS properties such as `overflow-y: auto;` to ensure the content area is scrollable.
  - Style the editable area to be clean and user-friendly.
  - **Important**: Do not modify any backend or JavaScript code that is responsible for fetching Wikipedia articles. This update is only to change the way the content is displayed.
- **Dependencies and requirements**:
  - Ensure that the HTML and CSS files are properly linked in the project.
- **Coding standards**:
  - Follow Google-style docstrings and coding conventions as outlined in the DEVELOPER_GUIDE.md.
- **Other technical guidance**:
  - Test the editable and scrollable functionality to ensure it works as expected while the article fetching remains unchanged.

## Project Context

### Beginning files
- `templates/index.html`
- `static/styles.css`
- `app.py` (if necessary)
- `static/app.js` (if needed)

### Ending files
- Modified `templates/index.html`
- Modified `static/styles.css`
- Potentially modified or extended `app.py`
- Potentially modified or extended `static/app.js`

## Low Level Goals

1. **Add an editable element for the Wikipedia article content**
   ```html
   <!-- Example snippet in templates/index.html -->
   <div id="wikipedia-article" class="editable-content" contenteditable="true">
       Paste your Wikipedia article here...
   </div>
   ```
   *Note: This should only affect the display and editing of the article content, not the fetching process.*

2. **Style the editable content to be scrollable and visually appealing**
   ```css
   /* Example snippet in static/styles.css */
   .editable-content {
       width: 100%;
       height: 400px; /* Adjust height as needed */
       border: 1px solid #ccc;
       padding: 10px;
       overflow-y: auto; /* Makes the content scrollable */
       font-family: Arial, sans-serif;
       background-color: #fff;
   }
   ```