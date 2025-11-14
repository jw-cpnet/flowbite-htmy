"""Avatar component for Flowbite."""

from dataclasses import dataclass, field
from typing import Any

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Size


@dataclass(frozen=True, kw_only=True)
class Avatar:
    """Flowbite avatar component.

    A component for displaying user profile pictures or placeholder initials.
    Supports different sizes, bordered style, and both circular and rounded square shapes.

    Supports passthrough attributes for tooltips, dropdowns, and accessibility:
        >>> Avatar(src="...", **{"data-tooltip-target": "tooltip-id"})
        >>> Avatar(src="...", id="avatarButton", **{"data-dropdown-toggle": "menu"})

    Example:
        >>> Avatar(src="/images/user.jpg", alt="User", size=Size.LG)
        >>> Avatar(initials="JD", bordered=True)
        >>> Avatar(initials="JL", class_="w-12 h-12")  # Override size with class_
    """

    src: str | None = None
    """Image source URL. If not provided, initials or placeholder will be shown."""

    alt: str = ""
    """Alt text for the image."""

    initials: str | None = None
    """User initials to display when no image is provided (e.g., 'JD')."""

    size: Size = Size.MD
    """Avatar size (only used if size classes not in class_)."""

    bordered: bool = False
    """Add ring border around avatar."""

    rounded: bool = True
    """Use circular shape (rounded-full). If False, uses rounded-sm."""

    class_: str = ""
    """Additional custom classes (can override size)."""

    attrs: dict[str, Any] = field(default_factory=dict)
    """Passthrough HTML attributes (id, data-*, aria-*, etc.)."""

    def htmy(self, context: Context) -> Component:
        """Render the avatar component.

        Args:
            context: Rendering context.

        Returns:
            Avatar HTML component (img or div element).
        """
        theme = ThemeContext.from_context(context)

        if self.src:
            # Image avatar
            return self._render_image(theme)
        elif self.initials:
            # Initials placeholder
            return self._render_initials(theme)
        else:
            # Default placeholder icon
            return self._render_placeholder(theme)

    def _render_image(self, theme: ThemeContext) -> Component:
        """Render avatar with image.

        Args:
            theme: Theme context.

        Returns:
            Image element.
        """
        classes = self._build_image_classes(theme)
        return html.img(src=self.src, alt=self.alt, class_=classes, **self.attrs)

    def _render_initials(self, theme: ThemeContext) -> Component:
        """Render avatar with initials.

        Args:
            theme: Theme context.

        Returns:
            Div element with initials.
        """
        container_classes = self._build_placeholder_classes(theme)
        # Dark mode classes always included
        text_classes = "font-medium text-gray-600 dark:text-gray-300"

        # initials is guaranteed to be not None here due to the elif check
        initials_text = self.initials if self.initials else ""
        return html.div(
            html.span(initials_text, class_=text_classes),
            class_=container_classes,
            **self.attrs,
        )

    def _render_placeholder(self, theme: ThemeContext) -> Component:
        """Render avatar with default placeholder icon.

        Args:
            theme: Theme context.

        Returns:
            Div element with SVG icon.
        """
        container_classes = self._build_placeholder_classes(theme)

        # Default user icon SVG - using SafeStr for proper SVG path rendering
        from htmy import SafeStr

        svg_content = SafeStr(
            '<svg class="absolute w-12 h-12 text-gray-400 -left-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">'
            '<path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path>'
            "</svg>"
        )

        return html.div(svg_content, class_=container_classes, **self.attrs)

    def _build_image_classes(self, theme: ThemeContext) -> str:
        """Build classes for image avatar.

        Args:
            theme: Theme context.

        Returns:
            Complete class string.
        """
        builder = ClassBuilder()

        # Size classes
        size_classes = self._get_size_classes()
        builder.add(size_classes)

        # Shape
        if self.rounded:
            builder.add("rounded-full")
        else:
            builder.add("rounded-sm")

        # Border (dark mode classes always included)
        if self.bordered:
            builder.add("p-1 ring-2 ring-gray-300 dark:ring-gray-500")

        return builder.merge(self.class_)

    def _build_placeholder_classes(self, theme: ThemeContext) -> str:
        """Build classes for placeholder avatar (initials or icon).

        Args:
            theme: Theme context.

        Returns:
            Complete class string.
        """
        builder = ClassBuilder(
            "relative inline-flex items-center justify-center overflow-hidden bg-gray-100"
        )

        # Size classes
        size_classes = self._get_size_classes()
        builder.add(size_classes)

        # Shape
        if self.rounded:
            builder.add("rounded-full")
        else:
            builder.add("rounded-sm")

        # Dark mode classes (always include - Tailwind activates based on dark mode state)
        builder.add("dark:bg-gray-600")

        return builder.merge(self.class_)

    def _get_size_classes(self) -> str:
        """Get size classes.

        Returns:
            Size class string (width and height).
        """
        size_map = {
            Size.XS: "w-6 h-6",
            Size.SM: "w-8 h-8",
            Size.MD: "w-10 h-10",
            Size.LG: "w-20 h-20",
            Size.XL: "w-24 h-24",
            Size.XXL: "w-32 h-32",
        }
        return size_map.get(self.size, size_map[Size.MD])
