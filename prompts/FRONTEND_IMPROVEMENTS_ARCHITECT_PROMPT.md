# Architect Prompt Template
Process this prompt working through each step to ensure each objective is met.

## High Level Goals

- Improve the front end webpage.
- Ensure the Wikipedia article content can be pasted and edited in a scrollable area.
- Place the "Summarize" button below the editable content on the same page.

## Mid Level Goals

- Modify the HTML structure to include an editable `<div>` or `<textarea>` for the Wikipedia article.
- Add CSS styles to make the editable content scrollable and visually appealing.
- Ensure the "Summarize" button is positioned correctly below the editable content.

## Implementation Guidelines
- **Important technical details**:
  - Use `contenteditable="true"` attribute for an editable `<div>`.
  - Apply CSS properties like `overflow-y: auto;` to make the content area scrollable.
  - Style the button and container for a clean and user-friendly interface.
- **Dependencies and requirements**:
  - Ensure the HTML, CSS, and JavaScript files are correctly linked in the project.
- **Coding standards to follow**:
  - Follow Google-style docstrings and coding conventions as outlined in the DEVELOPER_GUIDE.md.
- **Other technical guidance**:
  - Test the changes to ensure the editable content works as expected and the button is positioned correctly.

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

1. **First task - Add an editable `<div>` or `<textarea>` for Wikipedia article content**
   ```code-example
   - Modify the `templates/index.html` file to include a scrollable, editable `<div>` using the `contenteditable="true"` attribute.
   - Ensure that the `<div>` has a unique ID and class for easy styling with CSS.
   - Follow Google-style docstrings and coding conventions as outlined in `DEVELOPER_GUIDE.md`.
   ```

2. **Second task - Add CSS styles to make the editable content scrollable and visually appealing**
   ```code-example
   - Modify the `static/styles.css` file to add styles for the editable `<div>`, making it scrollable with `overflow-y: auto;`.
   - Ensure that the styles applied to the `<div>` enhance its visual appeal and usability.
   - Follow Google-style docstrings and coding conventions as outlined in `DEVELOPER_GUIDE.md`.
   ```

3. **Third task - Position the "Summarize" button below the editable content**
   ```code-example
   - Modify the `templates/index.html` file to position the "Summarize" button directly below the editable `<div>`.
   - Ensure that the button is styled consistently with other elements on the page.
   - Follow Google-style docstrings and coding conventions as outlined in `DEVELOPER_GUIDE.md`.
   ```

4. **Fourth task - Test the changes to ensure functionality**
   ```code-example
   - Manually test the changes in a web browser to ensure that the editable content works as expected and the button is positioned correctly.
   - Ensure that all changes meet the high-level and mid-level goals outlined in the prompt.
   - Provide visual feedback to the user when the "Summarize" button is clicked, such as a loading spinner or a disabled state for the button.
   - Follow Google-style docstrings and coding conventions as outlined in `DEVELOPER_GUIDE.md`.
   ```
