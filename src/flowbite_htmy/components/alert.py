"""Alert component for Flowbite."""

from dataclasses import dataclass

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Color


@dataclass(frozen=True, kw_only=True)
class Alert:
    """Flowbite alert component.

    A component for displaying informational messages, warnings, errors,
    and success notifications to users.

    Example:
        >>> Alert(
        ...     title="Success!",
        ...     message="Your changes have been saved.",
        ...     color=Color.SUCCESS
        ... )
    """

    message: str
    """Alert message content."""

    title: str | None = None
    """Optional alert title (displayed in bold)."""

    color: Color = Color.INFO
    """Alert color variant (default: INFO/blue)."""

    bordered: bool = False
    """Add border accent to the alert."""

    class_: str = ""
    """Additional custom classes."""

    def htmy(self, context: Context) -> Component:
        """Render the alert component.

        Args:
            context: Rendering context.

        Returns:
            Alert HTML component (div element).
        """
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        # Build content
        content: tuple[Component, ...]
        if self.title:
            content = (
                html.span(self.title, class_="font-medium"),
                " ",
                self.message,
            )
        else:
            content = (self.message,)

        return html.div(*content, class_=classes, role="alert")

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the alert.

        Args:
            theme: Theme context for dark mode.

        Returns:
            Complete class string.
        """
        # Base alert classes
        builder = ClassBuilder("p-4 mb-4 text-sm rounded-lg")

        # Color-specific classes
        color_classes = self._get_color_classes()
        builder.add(color_classes)

        # Border if requested
        if self.bordered:
            border_classes = self._get_border_classes()
            builder.add(border_classes)

        # Dark mode classes
        dark_classes = self._get_dark_classes()
        if theme.dark_mode and dark_classes:
            builder.add(dark_classes)

        return builder.merge(self.class_)

    def _get_color_classes(self) -> str:
        """Get light mode color classes.

        Returns:
            Color class string for light mode.
        """
        color_map = {
            Color.PRIMARY: "text-blue-800 bg-blue-50",
            Color.SECONDARY: "text-gray-800 bg-gray-50",
            Color.SUCCESS: "text-green-800 bg-green-50",
            Color.DANGER: "text-red-800 bg-red-50",
            Color.WARNING: "text-yellow-800 bg-yellow-50",
            Color.INFO: "text-blue-800 bg-blue-50",
            Color.DARK: "text-gray-800 bg-gray-50",
            Color.LIGHT: "text-gray-800 bg-gray-50",
            # Direct color names
            Color.BLUE: "text-blue-800 bg-blue-50",
            Color.GREEN: "text-green-800 bg-green-50",
            Color.RED: "text-red-800 bg-red-50",
            Color.YELLOW: "text-yellow-800 bg-yellow-50",
            Color.GRAY: "text-gray-800 bg-gray-50",
        }
        return color_map.get(self.color, color_map[Color.INFO])

    def _get_border_classes(self) -> str:
        """Get border classes based on color.

        Returns:
            Border class string.
        """
        border_map = {
            Color.PRIMARY: "border border-blue-300",
            Color.SECONDARY: "border border-gray-300",
            Color.SUCCESS: "border border-green-300",
            Color.DANGER: "border border-red-300",
            Color.WARNING: "border border-yellow-300",
            Color.INFO: "border border-blue-300",
            Color.DARK: "border border-gray-300",
            Color.LIGHT: "border border-gray-300",
            # Direct color names
            Color.BLUE: "border border-blue-300",
            Color.GREEN: "border border-green-300",
            Color.RED: "border border-red-300",
            Color.YELLOW: "border border-yellow-300",
            Color.GRAY: "border border-gray-300",
        }
        return border_map.get(self.color, border_map[Color.INFO])

    def _get_dark_classes(self) -> str:
        """Get dark mode color classes.

        Returns:
            Color class string for dark mode.
        """
        dark_map = {
            Color.PRIMARY: "dark:bg-gray-800 dark:text-blue-400",
            Color.SECONDARY: "dark:bg-gray-800 dark:text-gray-300",
            Color.SUCCESS: "dark:bg-gray-800 dark:text-green-400",
            Color.DANGER: "dark:bg-gray-800 dark:text-red-400",
            Color.WARNING: "dark:bg-gray-800 dark:text-yellow-300",
            Color.INFO: "dark:bg-gray-800 dark:text-blue-400",
            Color.DARK: "dark:bg-gray-800 dark:text-gray-300",
            Color.LIGHT: "dark:bg-gray-800 dark:text-gray-300",
            # Direct color names
            Color.BLUE: "dark:bg-gray-800 dark:text-blue-400",
            Color.GREEN: "dark:bg-gray-800 dark:text-green-400",
            Color.RED: "dark:bg-gray-800 dark:text-red-400",
            Color.YELLOW: "dark:bg-gray-800 dark:text-yellow-300",
            Color.GRAY: "dark:bg-gray-800 dark:text-gray-300",
        }

        dark_border_suffix = ""
        if self.bordered:
            # Add dark mode border colors
            border_dark_map = {
                Color.PRIMARY: " dark:border-blue-800",
                Color.SUCCESS: " dark:border-green-800",
                Color.DANGER: " dark:border-red-800",
                Color.WARNING: " dark:border-yellow-800",
                Color.INFO: " dark:border-blue-800",
                Color.BLUE: " dark:border-blue-800",
                Color.GREEN: " dark:border-green-800",
                Color.RED: " dark:border-red-800",
                Color.YELLOW: " dark:border-yellow-800",
            }
            dark_border_suffix = border_dark_map.get(self.color, "")

        return dark_map.get(self.color, "") + dark_border_suffix
