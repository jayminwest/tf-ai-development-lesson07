import sys
from pathlib import Path

from aider.coders import Coder
from aider.models import Model

MODEL_NAME = "sonnet"
CONTEXT_EDITABLE = [
    "button_config.py",
    "templates/index.html", 
    "static/app.js",
    "app.py",
]
CONTEXT_READ_ONLY = ["prompts/DEVELOPER_GUIDE.md"]

def new_llm_button(button_name: str = "", button_prompt: str = "") -> None:
    """
    Create a new LLM button with the specified name and prompt.

    Args:
        button_name (str): The name of the button.
        button_prompt (str): The prompt for the button.
    """

    prompt = f"""Please add a new analysis button with the following details:
Button Name: {button_name}
Button Prompt: {button_prompt}

Required changes:

1. In button_config.py:
   - Add a new ButtonConfig instance to initialize_default_buttons()
   - Generate a unique button_id (lowercase, underscores for spaces)
   - Set appropriate result_type ('text' or 'html')
   - Include the provided prompt in the config

2. In app.py:
   - If needed, add a new processing case in process_analysis()
   - Follow existing error handling patterns
   - Maintain async/await pattern for LLM operations

3. If custom analysis is needed:
   In article_analysis.py:
   - Add any new analysis functions
   - Include type hints and docstrings
   - Follow existing patterns for text processing

4. If visualizations are needed:
   In article_visualizations.py:
   - Add new visualization functions
   - Follow matplotlib/wordcloud patterns
   - Ensure proper file paths and cleanup

The following will update automatically:
- Button rendering in templates/index.html
- Event handling in static/app.js
- Route registration in app.py

Please maintain:
- Consistent error handling
- Type hints and docstrings
- Async processing for LLM operations
- Project code style guidelines
"""

    model = Model(MODEL_NAME)

    # Initialize AI Coding Assistant
    coder = Coder.create(
        main_model=model,
        fnames=CONTEXT_EDITABLE,
        read_only_fnames=CONTEXT_READ_ONLY,
        auto_commits=False,
        suggest_shell_commands=False,
    )

    # Create the new button
    coder.run(prompt)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python new_prompt_button.py <button_name> <button_prompt>")
        sys.exit(1)

    button_name = sys.argv[1]
    button_prompt = sys.argv[2]

    new_llm_button(button_name, button_prompt)
