from aider.coders import Coder
from aider.models import Model

MODEL_NAME = "sonnet"
CONTEXT_EDITABLE = [str(pyproject_path)]
CONTEXT_READ_ONLY = ["README.md"]

def new_llm_button(button_name: str = "", button_prompt: str = "") -> None:
    """
    Create a new LLM button with the specified name and prompt.

    Args:
        button_name (str): The name of the button.
        button_prompt (str): The prompt for the button.
    """

    prompt = f"Button Name: {button_name}\nButton Prompt: {button_prompt}"

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
