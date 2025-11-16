"""
Flowbite Accordion component with collapsible panels.

Provides a type-safe, accessible accordion component with proper ARIA attributes,
Flowbite styling, and optional HTMX integration for dynamic content loading.

Example:
    >>> accordion = Accordion(
    ...     panels=[
    ...         Panel(title="What is Flowbite?", content="Flowbite is..."),
    ...         Panel(title="How to install?", content="pip install flowbite-htmy"),
    ...     ],
    ...     mode=AccordionMode.COLLAPSE,
    ... )
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.icons import get_accordion_icon
from flowbite_htmy.types import Color

# Color-specific hover classes for accordion buttons
COLOR_CLASSES = {
    Color.BLUE: "hover:bg-blue-100 dark:hover:bg-blue-800",
    Color.GREEN: "hover:bg-green-100 dark:hover:bg-green-800",
    Color.RED: "hover:bg-red-100 dark:hover:bg-red-800",
    Color.YELLOW: "hover:bg-yellow-100 dark:hover:bg-yellow-800",
    Color.PURPLE: "hover:bg-purple-100 dark:hover:bg-purple-800",
    Color.INDIGO: "hover:bg-indigo-100 dark:hover:bg-indigo-800",
    Color.PINK: "hover:bg-pink-100 dark:hover:bg-pink-800",
    Color.PRIMARY: "hover:bg-gray-100 dark:hover:bg-gray-800",  # Gray is default
}


class AccordionMode(str, Enum):
    """Accordion collapse behavior modes."""

    COLLAPSE = "collapse"
    """Only one panel can be open at a time (default)."""

    ALWAYS_OPEN = "open"
    """Multiple panels can be open simultaneously."""


class AccordionVariant(str, Enum):
    """Accordion visual style variants."""

    DEFAULT = "default"
    """Standard bordered accordion with rounded corners (default)."""

    FLUSH = "flush"
    """Flush accordion with no side borders, minimal padding."""


@dataclass(frozen=True, kw_only=True)
class Panel:
    """
    Individual collapsible panel within an accordion.

    Example:
        >>> panel = Panel(
        ...     title="What is Flowbite?",
        ...     content="Flowbite is an open-source library...",
        ...     is_open=True,
        ...     hx_get="/api/faq/1",
        ... )
    """

    title: str
    """Panel header text displayed in the button."""

    content: str | Component
    """Panel body content (plain string or htmy component)."""

    is_open: bool = False
    """Whether panel is expanded by default."""

    icon: Component | None = None
    """Custom expand/collapse icon (uses chevron if None)."""

    hx_get: str | None = None
    """HTMX GET endpoint for lazy content loading."""

    hx_trigger: str = "revealed"
    """HTMX trigger event (default: fires when panel expands)."""

    hx_swap: str | None = None
    """HTMX swap strategy (e.g., 'innerHTML', 'outerHTML')."""

    hx_target: str | None = None
    """HTMX target selector for content swap."""

    class_: str = ""
    """Custom CSS classes for panel wrapper."""


@dataclass(frozen=True, kw_only=True)
class Accordion:
    """
    Flowbite accordion component with collapsible panels.

    Renders a collection of collapsible panels with proper ARIA attributes,
    Flowbite styling, and optional HTMX integration for dynamic content loading.

    Example:
        >>> accordion = Accordion(
        ...     panels=[
        ...         Panel(title="Question 1", content="Answer 1"),
        ...         Panel(title="Question 2", content="Answer 2", is_open=True),
        ...     ],
        ...     mode=AccordionMode.COLLAPSE,
        ... )
    """

    panels: list[Panel]
    """Collection of accordion panels (minimum 1 required)."""

    mode: AccordionMode = AccordionMode.COLLAPSE
    """Collapse behavior mode (COLLAPSE: single panel open, ALWAYS_OPEN: multiple panels open)."""

    variant: AccordionVariant = AccordionVariant.DEFAULT
    """Visual style variant (DEFAULT: bordered, FLUSH: borderless)."""

    color: Color = Color.PRIMARY
    """Header background color from Flowbite color palette."""

    class_: str = ""
    """Custom CSS classes to merge with component classes."""

    accordion_id: str | None = None
    """Custom ID for accordion container (auto-generated if None)."""

    def htmy(self, context: Context) -> Component:
        """
        Render accordion component as HTML.

        Args:
            context: htmy rendering context for theme and nested components.

        Returns:
            Component representing the complete accordion HTML structure.
        """
        theme = ThemeContext.from_context(context)

        # Generate unique base ID for this accordion instance
        base_id = self.accordion_id or f"accordion-{id(self)}"

        # Render all panels
        panel_elements = []
        for index, panel in enumerate(self.panels):
            panel_elements.append(self._render_panel(panel, index, base_id, theme))

        # Build container classes
        container_classes = ClassBuilder()
        if self.class_:
            container_classes.add(self.class_)

        return html.div(
            *panel_elements,
            id=base_id,
            data_accordion=self.mode.value,
            class_=container_classes.build() if self.class_ else None,
        )

    def _render_panel(
        self, panel: Panel, index: int, base_id: str, theme: ThemeContext
    ) -> Component:
        """Render a single accordion panel."""
        heading_id = f"{base_id}-heading-{index}"
        body_id = f"{base_id}-body-{index}"

        # Build button classes
        button_classes = self._build_button_classes(index, theme)

        # Build body classes
        body_classes = self._build_body_classes(index, theme)

        # Get icon (custom or default chevron)
        icon = panel.icon if panel.icon is not None else self._get_default_icon()

        # Build HTMX attributes for panel body
        htmx_attrs = {}
        if panel.hx_get:
            htmx_attrs["hx_get"] = panel.hx_get
            htmx_attrs["hx_trigger"] = panel.hx_trigger
            if panel.hx_swap:
                htmx_attrs["hx_swap"] = panel.hx_swap
            if panel.hx_target:
                htmx_attrs["hx_target"] = panel.hx_target

        return html.div(
            # Header
            html.h2(
                html.button(
                    html.span(panel.title),
                    icon,
                    type="button",
                    class_=button_classes,
                    data_accordion_target=f"#{body_id}",
                    aria_expanded="true" if panel.is_open else "false",
                    aria_controls=body_id,
                ),
                id=heading_id,
            ),
            # Panel body
            html.div(
                html.div(
                    panel.content,
                    class_=body_classes,
                ),
                id=body_id,
                class_="hidden" if not panel.is_open else None,
                aria_labelledby=heading_id,
                **htmx_attrs,
            ),
        )

    def _build_button_classes(self, index: int, theme: ThemeContext) -> str:
        """Build CSS classes for accordion button."""
        builder = ClassBuilder()

        # Base layout classes
        builder.add("flex items-center justify-between w-full font-medium rtl:text-right gap-3")

        # Padding and borders based on variant
        if self.variant == AccordionVariant.DEFAULT:
            builder.add("p-5")
            builder.add("border border-b-0 border-gray-200 dark:border-gray-700")
            # First panel gets rounded top
            if index == 0:
                builder.add("rounded-t-xl")
        else:  # FLUSH
            builder.add("py-5")
            builder.add("border-b border-gray-200 dark:border-gray-700")

        # Text colors (always include dark mode)
        builder.add("text-gray-500 dark:text-gray-400")

        # Focus ring (always include dark mode)
        builder.add("focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800")

        # Hover background (always include dark mode) - color-specific
        color_classes = COLOR_CLASSES.get(self.color, COLOR_CLASSES[Color.PRIMARY])
        builder.add(color_classes)

        return builder.build()

    def _build_body_classes(self, index: int, theme: ThemeContext) -> str:
        """Build CSS classes for accordion panel body."""
        builder = ClassBuilder()

        if self.variant == AccordionVariant.DEFAULT:
            builder.add("p-5")
            builder.add("border border-b-0 border-gray-200 dark:border-gray-700")
        else:  # FLUSH
            builder.add("py-5")
            builder.add("border-b border-gray-200 dark:border-gray-700")

        return builder.build()

    def _get_default_icon(self) -> SafeStr:
        """Get default chevron down icon for accordion."""
        return get_accordion_icon()
