# Architect Prompt Template
Process this file working through each step to ensure each objective is met.

## High Level Goals

- Improve the front end webpage for better user experience.
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

