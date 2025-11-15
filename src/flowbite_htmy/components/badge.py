"""Badge component for Flowbite."""

from dataclasses import dataclass
from typing import Any

from htmy import Component, Context, SafeStr, html

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

    href: str | None = None
    """Optional URL to make the badge a clickable link."""

    icon: SafeStr | None = None
    """Optional SVG icon to display before the label."""

    icon_only: bool = False
    """If True, only the icon is displayed and label becomes screen-reader only."""

    dismissible: bool = False
    """If True, adds a close button with data-dismiss-target attribute."""

    id: str | None = None
    """Optional ID for dismissible badges (required when dismissible=True)."""

    class_: str = ""
    """Additional custom classes."""

    def htmy(self, context: Context) -> Component:
        """Render the badge component.

        Args:
            context: Rendering context.

        Returns:
            Badge HTML component (span or anchor element).
        """
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        # Build content with optional icon
        content_parts: list[Any] = []

        if self.icon:
            content_parts.append(self.icon)

        # Add label (screen-reader only if icon_only is True)
        if self.icon_only:
            content_parts.append(html.span(self.label, class_="sr-only"))
        else:
            content_parts.append(self.label)

        # Add dismiss button if dismissible
        if self.dismissible:
            dismiss_button = self._create_dismiss_button()
            content_parts.append(dismiss_button)

        # Use single content if only one part, otherwise use list
        content: Any = content_parts if len(content_parts) > 1 else self.label

        # Render as link if href is provided
        if self.href:
            if isinstance(content, list):
                return html.a(*content, href=self.href, class_=classes)
            return html.a(content, href=self.href, class_=classes)

        # Render as span (with optional id for dismissible)
        span_attrs = {"class": classes}
        if self.id:
            span_attrs["id"] = self.id

        if isinstance(content, list):
            return html.span(*content, **span_attrs)
        return html.span(content, **span_attrs)

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the badge.

        Args:
            theme: Theme context for dark mode.

        Returns:
            Complete class string.
        """
        # Base badge classes
        if self.icon_only:
            # Icon-only badges are circular with fixed dimensions
            base = "inline-flex items-center justify-center w-6 h-6 font-semibold"
        elif self.dismissible:
            # Dismissible badges use slightly different padding
            base = "inline-flex items-center px-2 py-1 font-medium"
        else:
            base = "font-medium px-2.5 py-0.5"

            # Add layout classes for links or icons
            if self.href:
                base += " inline-flex items-center justify-center"
            elif self.icon:
                base += " inline-flex items-center"

        builder = ClassBuilder(base)

        # Size
        if self.large:
            builder.add("text-sm")
        else:
            builder.add("text-xs")

        # Border radius (icon-only badges are always circular)
        if self.icon_only or self.rounded:
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
            # Always include dark: classes - Tailwind handles activation
            dark_classes = self._get_dark_classes()
            if dark_classes:
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
            Border class string with color-specific borders and optional hover states.
        """
        # Add hover classes if this is a link
        hover = "hover:bg-blue-200" if self.href else ""

        border_map = {
            Color.PRIMARY: f"bg-blue-100 text-blue-800 border border-blue-400 {hover} dark:bg-gray-700 dark:text-blue-400 dark:border-blue-400",
            Color.SECONDARY: f"bg-gray-100 text-gray-800 border border-gray-500 {hover} dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
            Color.SUCCESS: f"bg-green-100 text-green-800 border border-green-400 {hover} dark:bg-gray-700 dark:text-green-400 dark:border-green-400",
            Color.DANGER: f"bg-red-100 text-red-800 border border-red-400 {hover} dark:bg-gray-700 dark:text-red-400 dark:border-red-400",
            Color.WARNING: f"bg-yellow-100 text-yellow-800 border border-yellow-300 {hover} dark:bg-gray-700 dark:text-yellow-300 dark:border-yellow-300",
            Color.INFO: f"bg-cyan-100 text-cyan-800 border border-cyan-400 {hover} dark:bg-gray-700 dark:text-cyan-400 dark:border-cyan-400",
            Color.DARK: f"bg-gray-100 text-gray-800 border border-gray-500 {hover} dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
            # Direct color names
            Color.BLUE: f"bg-blue-100 text-blue-800 border border-blue-400 {hover} dark:bg-gray-700 dark:text-blue-400 dark:border-blue-400",
            Color.GREEN: f"bg-green-100 text-green-800 border border-green-400 {hover} dark:bg-gray-700 dark:text-green-400 dark:border-green-400",
            Color.RED: f"bg-red-100 text-red-800 border border-red-400 {hover} dark:bg-gray-700 dark:text-red-400 dark:border-red-400",
            Color.YELLOW: f"bg-yellow-100 text-yellow-800 border border-yellow-300 {hover} dark:bg-gray-700 dark:text-yellow-300 dark:border-yellow-300",
            Color.INDIGO: f"bg-indigo-100 text-indigo-800 border border-indigo-400 {hover} dark:bg-gray-700 dark:text-indigo-400 dark:border-indigo-400",
            Color.PURPLE: f"bg-purple-100 text-purple-800 border border-purple-400 {hover} dark:bg-gray-700 dark:text-purple-400 dark:border-purple-400",
            Color.PINK: f"bg-pink-100 text-pink-800 border border-pink-400 {hover} dark:bg-gray-700 dark:text-pink-400 dark:border-pink-400",
            Color.GRAY: f"bg-gray-100 text-gray-800 border border-gray-500 {hover} dark:bg-gray-700 dark:text-gray-400 dark:border-gray-500",
        }
        return border_map.get(self.color, border_map[Color.PRIMARY])

    def _create_dismiss_button(self) -> Component:
        """Create dismiss button for dismissible badges.

        Returns:
            HTML button component with close icon.
        """
        from flowbite_htmy.icons import Icon, get_icon

        # Map colors to dismiss button styles
        dismiss_color_map = {
            Color.BLUE: "text-blue-400 hover:bg-blue-200 hover:text-blue-900 dark:hover:bg-blue-800 dark:hover:text-blue-300",
            Color.GRAY: "text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-gray-300",
            Color.RED: "text-red-400 hover:bg-red-200 hover:text-red-900 dark:hover:bg-red-800 dark:hover:text-red-300",
            Color.GREEN: "text-green-400 hover:bg-green-200 hover:text-green-900 dark:hover:bg-green-800 dark:hover:text-green-300",
            Color.YELLOW: "text-yellow-400 hover:bg-yellow-200 hover:text-yellow-900 dark:hover:bg-yellow-800 dark:hover:text-yellow-300",
            Color.INDIGO: "text-indigo-400 hover:bg-indigo-200 hover:text-indigo-900 dark:hover:bg-indigo-800 dark:hover:text-indigo-300",
            Color.PURPLE: "text-purple-400 hover:bg-purple-200 hover:text-purple-900 dark:hover:bg-purple-800 dark:hover:text-purple-300",
            Color.PINK: "text-pink-400 hover:bg-pink-200 hover:text-pink-900 dark:hover:bg-pink-800 dark:hover:text-pink-300",
        }

        color_classes = dismiss_color_map.get(self.color, dismiss_color_map[Color.BLUE])
        target = f"#{self.id}" if self.id else "#"

        return html.button(
            get_icon(Icon.CLOSE, class_="w-2 h-2"),
            html.span("Remove badge", class_="sr-only"),
            type="button",
            class_=f"inline-flex items-center p-1 ms-2 text-sm bg-transparent rounded-xs {color_classes}",
            **{"data-dismiss-target": target, "aria-label": "Remove"},
        )
