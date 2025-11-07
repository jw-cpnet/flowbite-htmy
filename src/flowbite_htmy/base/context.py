"""Context providers for theme and configuration."""

from dataclasses import dataclass
from typing import Any

from htmy import Component, ComponentType, Context


@dataclass
class ThemeContext:
    """Theme configuration context provider.

    Provides theme settings (like dark mode) to child components
    through the htmy context system.

    Example:
        >>> from htmy import Renderer
        >>> page = ThemeContext(
        ...     Button(label="Click"),
        ...     dark_mode=True
        ... )
        >>> await Renderer().render(page)
    """

    dark_mode: bool = False
    """Enable dark mode styling."""

    colors: dict[str, str] | None = None
    """Custom color overrides mapping color names to values."""

    def __init__(
        self,
        *children: ComponentType,
        dark_mode: bool = False,
        colors: dict[str, str] | None = None,
    ) -> None:
        """Initialize the ThemeContext.

        Args:
            *children: Child components to wrap in this context.
            dark_mode: Enable dark mode styling.
            colors: Custom color overrides.
        """
        self._children = children
        self.dark_mode = dark_mode
        self.colors = colors

    def htmy_context(self) -> Context:
        """Provide the theme context to child components.

        Returns:
            Context dictionary with this ThemeContext instance.
        """
        return {ThemeContext: self}

    def htmy(self, context: Context) -> Component:
        """Render child components with theme context.

        Context providers must also be components, as they
        wrap children components in their context.

        Args:
            context: Current rendering context.

        Returns:
            The child components.
        """
        return self._children

    @classmethod
    def from_context(cls, context: Context) -> "ThemeContext":
        """Extract ThemeContext from rendering context.

        Args:
            context: Current rendering context.

        Returns:
            ThemeContext instance from context, or default instance.

        Raises:
            TypeError: If context contains invalid ThemeContext.
        """
        theme_context = context.get(cls)
        if theme_context is None:
            # Return default theme if not in context
            return cls()
        if isinstance(theme_context, ThemeContext):
            return theme_context

        raise TypeError(f"Invalid theme context: {type(theme_context)}")

    def get_color(self, color: str, default: str | None = None) -> str | None:
        """Get a color value, checking custom overrides first.

        Args:
            color: Color name to look up.
            default: Default value if color not found.

        Returns:
            Color value or default.
        """
        if self.colors and color in self.colors:
            return self.colors[color]
        return default
