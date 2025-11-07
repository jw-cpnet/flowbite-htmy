"""Button component for Flowbite."""

from dataclasses import dataclass

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Color, Size


@dataclass(frozen=True, kw_only=True)
class Button:
    """Flowbite button component.

    A versatile button component with support for different colors, sizes,
    and HTMX attributes for interactive behavior.

    Example:
        >>> Button(label="Click Me", color=Color.PRIMARY, size=Size.MD)
    """

    label: str
    """Button text label."""

    color: Color = Color.PRIMARY
    """Button color variant."""

    size: Size = Size.MD
    """Button size."""

    disabled: bool = False
    """Whether the button is disabled."""

    type: str = "button"
    """Button type attribute (button, submit, reset)."""

    # HTMX attributes
    hx_get: str | None = None
    """HTMX hx-get attribute."""

    hx_post: str | None = None
    """HTMX hx-post attribute."""

    hx_target: str | None = None
    """HTMX hx-target attribute."""

    hx_swap: str | None = None
    """HTMX hx-swap attribute."""

    hx_trigger: str | None = None
    """HTMX hx-trigger attribute."""

    # Custom styling
    class_: str = ""
    """Additional custom classes."""

    def htmy(self, context: Context) -> Component:
        """Render the button component.

        Args:
            context: Rendering context.

        Returns:
            Button HTML component.
        """
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        return html.button(
            self.label,
            type=self.type,
            disabled=self.disabled or None,  # Only include if True
            class_=classes,
            hx_get=self.hx_get,
            hx_post=self.hx_post,
            hx_target=self.hx_target,
            hx_swap=self.hx_swap,
            hx_trigger=self.hx_trigger,
        )

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the button.

        Args:
            theme: Theme context for dark mode support.

        Returns:
            Complete class string.
        """
        # Base button classes (always applied)
        builder = ClassBuilder(
            "font-medium rounded-lg text-sm px-5 py-2.5 focus:ring-4 focus:outline-none"
        )

        # Color-specific classes
        color_classes = self._get_color_classes()
        builder.add(color_classes)

        # Dark mode color variants
        dark_classes = self._get_dark_color_classes()
        if theme.dark_mode and dark_classes:
            builder.add(dark_classes)

        # Merge with custom classes
        return builder.merge(self.class_)

    def _get_color_classes(self) -> str:
        """Get color-specific classes for light mode.

        Returns:
            Color class string.
        """
        color_map = {
            Color.PRIMARY: "text-white bg-blue-700 hover:bg-blue-800 focus:ring-blue-300",
            Color.SECONDARY: "text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-gray-100",
            Color.SUCCESS: "text-white bg-green-700 hover:bg-green-800 focus:ring-green-300",
            Color.DANGER: "text-white bg-red-700 hover:bg-red-800 focus:ring-red-300",
            Color.WARNING: "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300",
            Color.INFO: "text-white bg-cyan-700 hover:bg-cyan-800 focus:ring-cyan-300",
            Color.DARK: "text-white bg-gray-800 hover:bg-gray-900 focus:ring-gray-300",
            Color.LIGHT: "text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-gray-100",
            # Direct color names
            Color.BLUE: "text-white bg-blue-700 hover:bg-blue-800 focus:ring-blue-300",
            Color.GREEN: "text-white bg-green-700 hover:bg-green-800 focus:ring-green-300",
            Color.RED: "text-white bg-red-700 hover:bg-red-800 focus:ring-red-300",
            Color.YELLOW: "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300",
            Color.PURPLE: "text-white bg-purple-700 hover:bg-purple-800 focus:ring-purple-300",
        }
        return color_map.get(self.color, color_map[Color.PRIMARY])

    def _get_dark_color_classes(self) -> str:
        """Get dark mode color-specific classes.

        Returns:
            Dark mode class string.
        """
        dark_map = {
            Color.PRIMARY: "dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            Color.SECONDARY: "dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700",
            Color.SUCCESS: "dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
            Color.DANGER: "dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900",
            Color.WARNING: "dark:focus:ring-yellow-900",
            Color.INFO: "dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800",
            Color.DARK: "dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700",
            Color.LIGHT: "dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700",
            # Direct color names
            Color.BLUE: "dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            Color.GREEN: "dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
            Color.RED: "dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900",
            Color.PURPLE: "dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-900",
        }
        return dark_map.get(self.color, "")
