"""Alert component for Flowbite."""

from dataclasses import dataclass

from htmy import Component, Context, SafeStr, html

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

    message: str | Component
    """Alert message content (can be string or htmy Component for complex content)."""

    title: str | None = None
    """Optional alert title (displayed in bold)."""

    color: Color = Color.INFO
    """Alert color variant (default: INFO/blue)."""

    bordered: bool = False
    """Add border accent to the alert."""

    border_accent: bool = False
    """Add top border accent (4px border-t) instead of full border."""

    icon: SafeStr | None = None
    """Optional SVG icon displayed before content."""

    dismissible: bool = False
    """Add close button to dismiss the alert."""

    id: str | None = None
    """Element ID (required for dismissible alerts)."""

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

        # Build content parts
        children: list[Component] = []

        # Add icon if provided
        if self.icon:
            children.append(
                html.div(
                    self.icon,
                    html.span("Info", class_="sr-only"),
                    class_="flex items-center",
                )
            )

        # Build text content
        if self.title:
            text_content: Component = html.div(
                html.span(self.title, class_="font-medium"),
                " ",
                self.message,  # type: ignore[arg-type]
                class_="ms-3 text-sm font-medium" if self.icon else "",
            )
        else:
            text_content = html.div(
                self.message,  # type: ignore[arg-type]
                class_="ms-3 text-sm font-medium" if self.icon else "",
            )

        children.append(text_content)

        # Add close button if dismissible
        if self.dismissible:
            close_button = self._build_close_button()
            children.append(close_button)

        # Build alert attributes
        attrs: dict[str, str] = {"class_": classes, "role": "alert"}
        if self.id:
            attrs["id"] = self.id

        return html.div(*children, **attrs)  # type: ignore[arg-type]

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the alert.

        Args:
            theme: Theme context for dark mode.

        Returns:
            Complete class string.
        """
        # Base alert classes
        builder = ClassBuilder("p-4 mb-4 text-sm rounded-lg")

        # Add flex layout if icon or dismissible
        if self.icon or self.dismissible:
            builder.add("flex items-center")

        # Color-specific classes
        color_classes = self._get_color_classes()
        builder.add(color_classes)

        # Border variants
        if self.border_accent:
            # Top border only (4px)
            border_classes = self._get_border_accent_classes()
            builder.add(border_classes)
        elif self.bordered:
            # Full border
            border_classes = self._get_border_classes()
            builder.add(border_classes)

        # Dark mode classes
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
        if self.bordered or self.border_accent:
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

    def _get_border_accent_classes(self) -> str:
        """Get top border accent classes (4px border-t).

        Returns:
            Border-t class string.
        """
        border_map = {
            Color.PRIMARY: "border-t-4 border-blue-300",
            Color.SECONDARY: "border-t-4 border-gray-300",
            Color.SUCCESS: "border-t-4 border-green-300",
            Color.DANGER: "border-t-4 border-red-300",
            Color.WARNING: "border-t-4 border-yellow-300",
            Color.INFO: "border-t-4 border-blue-300",
            Color.DARK: "border-t-4 border-gray-300",
            Color.LIGHT: "border-t-4 border-gray-300",
            # Direct color names
            Color.BLUE: "border-t-4 border-blue-300",
            Color.GREEN: "border-t-4 border-green-300",
            Color.RED: "border-t-4 border-red-300",
            Color.YELLOW: "border-t-4 border-yellow-300",
            Color.GRAY: "border-t-4 border-gray-300",
        }
        return border_map.get(self.color, border_map[Color.INFO])

    def _build_close_button(self) -> Component:
        """Build the close button for dismissible alerts.

        Returns:
            Close button component.
        """
        # Close icon SVG
        close_icon = SafeStr(
            '<svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>'
            "</svg>"
        )

        # Button color classes based on alert color
        button_color_map = {
            Color.PRIMARY: "bg-blue-50 text-blue-500 hover:bg-blue-200 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700",
            Color.INFO: "bg-blue-50 text-blue-500 hover:bg-blue-200 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700",
            Color.BLUE: "bg-blue-50 text-blue-500 hover:bg-blue-200 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700",
            Color.DANGER: "bg-red-50 text-red-500 hover:bg-red-200 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700",
            Color.RED: "bg-red-50 text-red-500 hover:bg-red-200 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700",
            Color.SUCCESS: "bg-green-50 text-green-500 hover:bg-green-200 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700",
            Color.GREEN: "bg-green-50 text-green-500 hover:bg-green-200 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700",
            Color.WARNING: "bg-yellow-50 text-yellow-500 hover:bg-yellow-200 dark:bg-gray-800 dark:text-yellow-400 dark:hover:bg-gray-700",
            Color.YELLOW: "bg-yellow-50 text-yellow-500 hover:bg-yellow-200 dark:bg-gray-800 dark:text-yellow-400 dark:hover:bg-gray-700",
            Color.DARK: "bg-gray-50 text-gray-500 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700",
            Color.GRAY: "bg-gray-50 text-gray-500 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700",
        }
        button_classes = button_color_map.get(self.color, button_color_map[Color.INFO])

        attrs: dict[str, str] = {
            "type": "button",
            "class_": f"ms-auto -mx-1.5 -my-1.5 rounded-lg focus:ring-2 p-1.5 inline-flex items-center justify-center h-8 w-8 {button_classes}",
            "aria-label": "Close",
        }
        if self.id:
            attrs["data-dismiss-target"] = f"#{self.id}"

        return html.button(
            html.span("Close", class_="sr-only"),
            close_icon,
            **attrs,
        )
