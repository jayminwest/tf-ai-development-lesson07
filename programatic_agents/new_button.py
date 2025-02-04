import sys
from pathlib import Path
from button_config import ButtonConfig, ButtonRegistry

def new_llm_button(button_id: str, display_name: str, endpoint: str, prompt: str) -> None:
    """
    Create a new LLM button with the specified parameters.

    Args:
        button_id (str): Unique identifier for the button
        display_name (str): Display name shown on the button
        endpoint (str): API endpoint for the button's action
        prompt (str): The prompt to use for analysis
    """
    # Create and register the button configuration
    config = ButtonConfig(
        id=button_id,
        display_name=display_name,
        endpoint=endpoint,
        prompt=prompt
    )
    ButtonRegistry.register(config)

    # The actual route registration happens in app.py when the Flask app starts
    print(f"Button '{display_name}' has been registered successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python new_prompt_button.py <button_name> <button_prompt>")
        sys.exit(1)

    button_name = sys.argv[1]
    button_prompt = sys.argv[2]

    new_llm_button(button_name, button_prompt)
