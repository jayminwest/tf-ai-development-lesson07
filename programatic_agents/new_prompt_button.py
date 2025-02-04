from aider.coders import Coder
from aider.models import Model    context_editable = [str(pyproject_path)]

def new_llm_button(button_name="", button_prompt=""):
    context_read_only = ["README.md"]

    prompt = f""

    model = Model("sonnet")

    # Initialize AI Coding Assistant
    coder = Coder.create(
        main_model=model,
        fnames=context_editable,
        read_only_fnames=context_read_only,
        auto_commits=False,
        suggest_shell_commands=False,
    )

    # Run the version bump
    coder.run(prompt)
    
    if __name__ == "__main__":