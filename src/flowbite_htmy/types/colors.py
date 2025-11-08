"""Color type definitions for Flowbite components."""

from enum import Enum


class Color(str, Enum):
    """Flowbite color variants."""

    # Main colors
    PRIMARY = "primary"
    SECONDARY = "secondary"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
    LIGHT = "light"
    DARK = "dark"

    # Additional colors
    BLUE = "blue"
    GREEN = "green"
    CYAN = "cyan"
    TEAL = "teal"
    LIME = "lime"
    RED = "red"
    YELLOW = "yellow"
    INDIGO = "indigo"
    PURPLE = "purple"
    PINK = "pink"
    GRAY = "gray"

    # Special
    DEFAULT = "default"
    NONE = "none"

    def __str__(self) -> str:
        """Return the color value as a string."""
        return self.value
