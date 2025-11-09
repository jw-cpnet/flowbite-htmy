"""Badge component for Flowbite."""

from dataclasses import dataclass

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Color


@dataclass(frozen=True, kw_only=True)
class Badge:
    """Flowbite badge component.

    A simple badge component for displaying labels, counts,
    and status indicators.

    Example:
        >>> Badge(label="New", color=Color.SUCCESS, rounded=True)
    """

    label: str
    """Badge text content."""

    color: Color = Color.PRIMARY
    """Badge color variant."""

    large: bool = False
    """Use larger text size (text-sm instead of text-xs)."""

    rounded: bool = False
    """Use fully rounded edges (pill style)."""

    border: bool = False
    """Add border with matching color (outlined badge style)."""

    class_: str = ""
    """Additional custom classes."""

    def htmy(self, context: Context) -> Component:
        """Render the badge component.

        Args:
            context: Rendering context.

        Returns:
            Badge HTML component (span element).
        """
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        return html.span(self.label, class_=classes)

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the badge.

        Args:
            theme: Theme context for dark mode.

        Returns:
            Complete class string.
        """
        # Base badge classes
        builder = ClassBuilder("font-medium px-2.5 py-0.5")

        # Size
        if self.large:
            builder.add("text-sm")
        else:
            builder.add("text-xs")

        # Border radius
        if self.rounded:
            builder.add("rounded-full")
        else:
            builder.add("rounded-sm")

        # Border style
        if self.border:
            border_classes = self._get_border_classes()
            builder.add(border_classes)
        else:
            # Color-specific classes (only for non-bordered badges)
            color_classes = self._get_color_classes()
            builder.add(color_classes)

            # Dark mode classes (only for non-bordered badges)
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
            Color.PRIMARY: "bg-blue-100 text-blue-800",
            Color.SECONDARY: "bg-gray-100 text-gray-800",
            Color.SUCCESS: "bg-green-100 text-green-800",
            Color.DANGER: "bg-red-100 text-red-800",
            Color.WARNING: "bg-yellow-100 text-yellow-800",
            Color.INFO: "bg-cyan-100 text-cyan-800",
            Color.DARK: "bg-gray-100 text-gray-800",
            Color.LIGHT: "bg-gray-100 text-gray-800",
            # Direct color names
            Color.BLUE: "bg-blue-100 text-blue-800",
            Color.GREEN: "bg-green-100 text-green-800",
            Color.RED: "bg-red-100 text-red-800",
            Color.YELLOW: "bg-yellow-100 text-yellow-800",
            Color.INDIGO: "bg-indigo-100 text-indigo-800",
            Color.PURPLE: "bg-purple-100 text-purple-800",
            Color.PINK: "bg-pink-100 text-pink-800",
            Color.GRAY: "bg-gray-100 text-gray-800",
        }
        return color_map.get(self.color, color_map[Color.PRIMARY])

    def _get_dark_classes(self) -> str:
        """Get dark mode color classes.

        Returns:
            Color class string for dark mode.
        """
        dark_map = {
            Color.PRIMARY: "dark:bg-blue-900 dark:text-blue-300",
            Color.SECONDARY: "dark:bg-gray-700 dark:text-gray-300",
            Color.SUCCESS: "dark:bg-green-900 dark:text-green-300",
            Color.DANGER: "dark:bg-red-900 dark:text-red-300",
            Color.WARNING: "dark:bg-yellow-900 dark:text-yellow-300",
            Color.INFO: "dark:bg-cyan-900 dark:text-cyan-300",
            Color.DARK: "dark:bg-gray-700 dark:text-gray-300",
            Color.LIGHT: "dark:bg-gray-700 dark:text-gray-300",
            # Direct color names
            Color.BLUE: "dark:bg-blue-900 dark:text-blue-300",
            Color.GREEN: "dark:bg-green-900 dark:text-green-300",
            Color.RED: "dark:bg-red-900 dark:text-red-300",
            Color.YELLOW: "dark:bg-yellow-900 dark:text-yellow-300",
            Color.INDIGO: "dark:bg-indigo-900 dark:text-indigo-300",
            Color.PURPLE: "dark:bg-purple-900 dark:text-purple-300",
            Color.PINK: "dark:bg-pink-900 dark:text-pink-300",
            Color.GRAY: "dark:bg-gray-700 dark:text-gray-300",
        }
        return dark_map.get(self.color, "")

    def _get_border_classes(self) -> str:
        """Get border classes for outlined badge style.

        Returns:
            Border class string with color-specific borders.
        """
        border_map = {
            Color.PRIMARY: "bg-blue-100 text-blue-800 border border-blue-400 dark:bg-gray-700 dark:text-blue-400 dark:border-blue-400",
            Color.SECONDARY: "bg-gray-100 text-gray-800 border border-gray-500 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
            Color.SUCCESS: "bg-green-100 text-green-800 border border-green-400 dark:bg-gray-700 dark:text-green-400 dark:border-green-400",
            Color.DANGER: "bg-red-100 text-red-800 border border-red-400 dark:bg-gray-700 dark:text-red-400 dark:border-red-400",
            Color.WARNING: "bg-yellow-100 text-yellow-800 border border-yellow-300 dark:bg-gray-700 dark:text-yellow-300 dark:border-yellow-300",
            Color.INFO: "bg-cyan-100 text-cyan-800 border border-cyan-400 dark:bg-gray-700 dark:text-cyan-400 dark:border-cyan-400",
            Color.DARK: "bg-gray-100 text-gray-800 border border-gray-500 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
            # Direct color names
            Color.BLUE: "bg-blue-100 text-blue-800 border border-blue-400 dark:bg-gray-700 dark:text-blue-400 dark:border-blue-400",
            Color.GREEN: "bg-green-100 text-green-800 border border-green-400 dark:bg-gray-700 dark:text-green-400 dark:border-green-400",
            Color.RED: "bg-red-100 text-red-800 border border-red-400 dark:bg-gray-700 dark:text-red-400 dark:border-red-400",
            Color.YELLOW: "bg-yellow-100 text-yellow-800 border border-yellow-300 dark:bg-gray-700 dark:text-yellow-300 dark:border-yellow-300",
            Color.INDIGO: "bg-indigo-100 text-indigo-800 border border-indigo-400 dark:bg-gray-700 dark:text-indigo-400 dark:border-indigo-400",
            Color.PURPLE: "bg-purple-100 text-purple-800 border border-purple-400 dark:bg-gray-700 dark:text-purple-400 dark:border-purple-400",
            Color.PINK: "bg-pink-100 text-pink-800 border border-pink-400 dark:bg-gray-700 dark:text-pink-400 dark:border-pink-400",
            Color.GRAY: "bg-gray-100 text-gray-800 border border-gray-500 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
        }
        return border_map.get(self.color, border_map[Color.PRIMARY])
