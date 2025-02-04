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
