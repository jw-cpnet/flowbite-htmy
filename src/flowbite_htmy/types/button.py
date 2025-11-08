"""Button-specific type definitions."""

from enum import Enum


class ButtonVariant(str, Enum):
    """Button style variants."""

    DEFAULT = "default"
    """Solid filled button (default style)."""

    OUTLINE = "outline"
    """Button with border and no fill."""

    GRADIENT = "gradient"
    """Button with gradient background."""

    GRADIENT_OUTLINE = "gradient_outline"
    """Button with gradient border and transparent fill."""

    def __str__(self) -> str:
        """Return the variant value as a string."""
        return self.value
