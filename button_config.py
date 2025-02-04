from dataclasses import dataclass
from typing import Optional

@dataclass
class ButtonConfig:
    """Configuration for an analysis button."""
    id: str
    display_name: str
    endpoint: str
    prompt: str
    result_type: str = "text"  # Can be "text", "html", etc.

class ButtonRegistry:
    """Registry for all analysis buttons."""
    _buttons: dict[str, ButtonConfig] = {}

    @classmethod
    def register(cls, config: ButtonConfig) -> None:
        cls._buttons[config.id] = config

    @classmethod
    def get_all(cls) -> list[ButtonConfig]:
        return list(cls._buttons.values())

    @classmethod
    def get(cls, button_id: str) -> Optional[ButtonConfig]:
        return cls._buttons.get(button_id)

def initialize_default_buttons():
    """Initialize the default analysis buttons."""
    ButtonRegistry.register(ButtonConfig(
        id="summarize",
        display_name="Generate Summary",
        endpoint="summarize",
        prompt="Summarize the following text concisely:",
        result_type="text"
    ))
    
    ButtonRegistry.register(ButtonConfig(
        id="analyze_stats",
        display_name="Analyze Statistics",
        endpoint="analyze_stats",
        prompt="",  # No prompt needed for statistical analysis
        result_type="html"
    ))
