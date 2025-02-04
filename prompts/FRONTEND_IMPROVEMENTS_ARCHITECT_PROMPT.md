# Architect Prompt Template
Process this file working through each step to ensure each objective is met.

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
> Ordered from first to last

1. **First task - what is the first task?**  
```code-example
What prompt would you run to complete this task?
What file do you want to work on?
What function do you want to work on?
What are details you want to add to ensure consistency?
```

2. **Second task - what is the second task?**  
```code-example
What prompt would you run to complete this task?
What file do you want to work on?
What function do you want to work on?
What are details you want to add to ensure consistency?
```

3. **Third task - what is the third task?**  
```code-example
What prompt would you run to complete this task?
What file do you want to work on?
What function do you want to work on?
What are details you want to add to ensure consistency?
```