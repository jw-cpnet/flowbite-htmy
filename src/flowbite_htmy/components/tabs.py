"""Tabs component for flowbite-htmy.

Provides tabbed navigation with multiple visual variants (default, underline, pills, full-width),
full ARIA accessibility support, Flowbite JavaScript integration for keyboard navigation,
HTMX lazy loading capabilities, and comprehensive icon positioning.
"""

from dataclasses import dataclass
from enum import Enum

from htmy import Component, Context, html

from flowbite_htmy.base.classes import ClassBuilder
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color


class TabVariant(str, Enum):
    """Visual styles for tabs component."""

    DEFAULT = "default"  # Border + background styling
    UNDERLINE = "underline"  # Minimal with bottom border indicator
    PILLS = "pills"  # Rounded background shapes
    FULL_WIDTH = "full-width"  # Tabs stretch to fill container


class IconPosition(str, Enum):
    """Icon placement options relative to tab label."""

    LEFT = "left"  # Icon appears to the left of label
    RIGHT = "right"  # Icon appears to the right of label


@dataclass(frozen=True, kw_only=True)
class Tab:
    """Individual tab with label, optional content, icon, and HTMX support."""

    # Required
    label: str

    # Optional content & display
    content: Component | None = None
    icon: Icon | None = None
    icon_position: IconPosition = IconPosition.LEFT

    # State
    disabled: bool = False
    is_active: bool = False

    # HTMX lazy loading
    hx_get: str | None = None
    hx_post: str | None = None
    hx_trigger: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None

    # Customization
    class_: str = ""


@dataclass(frozen=True, kw_only=True)
class Tabs:
    """Container for multiple tabs with navigation and content panels."""

    # Required
    tabs: list[Tab]

    # Optional styling
    variant: TabVariant = TabVariant.DEFAULT
    color: Color = Color.BLUE

    # Optional ID override
    tabs_id: str | None = None

    # Customization
    class_: str = ""

    def _get_base_id(self) -> str:
        """Generate unique base ID for tabs component."""
        return self.tabs_id or f"tabs-{id(self)}"

    def _get_color_classes(self) -> dict[str, str]:
        """Map color enum to Tailwind classes."""
        color_map = {
            Color.BLUE: ("blue-600", "blue-500", "blue-300"),
            Color.GREEN: ("green-600", "green-500", "green-300"),
            Color.RED: ("red-600", "red-500", "red-300"),
            Color.YELLOW: ("yellow-600", "yellow-500", "yellow-300"),
            Color.PURPLE: ("purple-600", "purple-500", "purple-300"),
            Color.PINK: ("pink-600", "pink-500", "pink-300"),
            Color.INDIGO: ("indigo-600", "indigo-500", "indigo-300"),
            Color.GRAY: ("gray-600", "gray-500", "gray-300"),
        }
        c600, c500, c300 = color_map[self.color]
        return {
            "text": f"text-{c600}",
            "text_dark": f"dark:text-{c500}",
            "bg": f"bg-{c600}",
            "border": f"border-{c600}",
            "border_dark": f"dark:border-{c500}",
            "focus_ring": f"focus:ring-{c300}",
        }

    def _get_flowbite_tab_classes(self) -> tuple[str, str]:
        """Get Flowbite data-tabs-active-classes and data-tabs-inactive-classes.

        These attributes tell Flowbite JavaScript which classes to add/remove
        when tabs are activated/deactivated, preventing SSR class retention issues.
        """
        color_classes = self._get_color_classes()

        if self.variant == TabVariant.DEFAULT:
            active = f"active {color_classes['text']} bg-gray-100 dark:bg-gray-800 {color_classes['text_dark']}"
            inactive = "hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300"

        elif self.variant == TabVariant.UNDERLINE:
            # border-b-2 is a base class, not swapped by Flowbite
            active = f"active {color_classes['text']} {color_classes['border']} {color_classes['text_dark']} {color_classes['border_dark']}"
            inactive = "border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"

        elif self.variant == TabVariant.PILLS:
            active = f"active text-white {color_classes['bg']}"
            inactive = "hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"

        elif self.variant == TabVariant.FULL_WIDTH:
            active = f"active text-gray-900 bg-gray-100 dark:bg-gray-700 dark:text-white {color_classes['focus_ring']}"
            inactive = f"bg-white hover:text-gray-700 hover:bg-gray-50 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700 {color_classes['focus_ring']}"

        else:
            active = ""
            inactive = ""

        return (active, inactive)

    def _build_tablist_classes(self) -> str:
        """Build Tailwind classes for tablist container based on variant."""
        if self.variant == TabVariant.DEFAULT:
            builder = ClassBuilder(
                "flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200"
            )
            builder.add("dark:border-gray-700 dark:text-gray-400")
        elif self.variant == TabVariant.UNDERLINE:
            # Underline needs wrapper div classes - we'll handle this in htmy()
            builder = ClassBuilder("flex flex-wrap -mb-px")
        elif self.variant == TabVariant.PILLS:
            builder = ClassBuilder("flex flex-wrap text-sm font-medium text-center text-gray-500")
            builder.add("dark:text-gray-400")
        elif self.variant == TabVariant.FULL_WIDTH:
            builder = ClassBuilder(
                "text-sm font-medium text-center text-gray-500 rounded-lg shadow-sm flex"
            )
            builder.add("dark:divide-gray-700 dark:text-gray-400")
        else:
            builder = ClassBuilder("")

        return builder.merge(self.class_)

    def _build_tab_classes(self, tab: Tab, is_active: bool, tab_index: int) -> str:
        """Build Tailwind classes for tab button based on variant."""
        color_classes = self._get_color_classes()

        if self.variant == TabVariant.DEFAULT:
            if is_active:
                builder = ClassBuilder(
                    f"inline-block p-4 {color_classes['text']} bg-gray-100 rounded-t-lg active"
                )
                builder.add(f"dark:bg-gray-800 {color_classes['text_dark']}")
            else:
                builder = ClassBuilder("inline-block p-4 rounded-t-lg")
                builder.add("hover:text-gray-600 hover:bg-gray-50")
                builder.add("dark:hover:bg-gray-800 dark:hover:text-gray-300")

        elif self.variant == TabVariant.UNDERLINE:
            if is_active:
                builder = ClassBuilder(
                    f"inline-block p-4 {color_classes['text']} border-b-2 {color_classes['border']} rounded-t-lg active"
                )
                builder.add(f"{color_classes['text_dark']} {color_classes['border_dark']}")
            else:
                builder = ClassBuilder(
                    "inline-block p-4 border-b-2 border-transparent rounded-t-lg"
                )
                builder.add("hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300")

        elif self.variant == TabVariant.PILLS:
            if is_active:
                builder = ClassBuilder(
                    f"inline-block px-4 py-3 text-white {color_classes['bg']} rounded-lg active"
                )
            else:
                builder = ClassBuilder("inline-block px-4 py-3 rounded-lg")
                builder.add("hover:text-gray-900 hover:bg-gray-100")
                builder.add("dark:hover:bg-gray-800 dark:hover:text-white")

        elif self.variant == TabVariant.FULL_WIDTH:
            # Base classes for full-width
            builder = ClassBuilder("inline-block w-full p-4")
            if is_active:
                builder.add("text-gray-900 bg-gray-100")
                builder.add("dark:bg-gray-700 dark:text-white")
                builder.add(f"{color_classes['focus_ring']} focus:ring-4 focus:outline-none active")
            else:
                builder.add("bg-white hover:text-gray-700 hover:bg-gray-50")
                builder.add("dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700")
                builder.add(f"{color_classes['focus_ring']} focus:ring-4 focus:outline-none")

            # Add border-r for all but last tab
            if tab_index < len(self.tabs) - 1:
                builder.add("border-r border-gray-200 dark:border-gray-700")
            else:
                # Last tab has border-s-0
                builder.add("border-s-0 border-gray-200 dark:border-gray-700")

            # Add rounded corners for first and last tabs
            if tab_index == 0:
                builder.add("rounded-s-lg")
            if tab_index == len(self.tabs) - 1:
                builder.add("rounded-e-lg")
        else:
            builder = ClassBuilder("inline-block p-4")

        return builder.merge(tab.class_)

    def _render_tab_content(self, tab: Tab, is_disabled: bool = False) -> Component:
        """Render tab button content (icon + label)."""
        # Icon left (default)
        if tab.icon and tab.icon_position == IconPosition.LEFT:
            icon_class = "w-4 h-4 me-2"
            return html.span(get_icon(tab.icon, class_=icon_class), tab.label)

        # Icon right
        if tab.icon and tab.icon_position == IconPosition.RIGHT:
            icon_class = "w-4 h-4 ms-2"
            return html.span(tab.label, get_icon(tab.icon, class_=icon_class))

        # No icon - just label
        return html.span(tab.label)

    def _build_disabled_tab_classes(self, tab: Tab) -> str:
        """Build classes for disabled tab."""
        builder = ClassBuilder("inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed")
        builder.add("dark:text-gray-500")
        return builder.merge(tab.class_)

    def _render_tab(self, tab: Tab, index: int, base_id: str, is_active: bool) -> Component:
        """Render individual tab button."""
        tab_id = f"tab-{base_id}-{index}"
        panel_id = f"panel-{base_id}-{index}"

        # Full-width variant uses w-full on list items
        li_class = (
            "w-full focus-within:z-10" if self.variant == TabVariant.FULL_WIDTH else "me-2"
        )

        # Render tab content (label + optional icon)
        tab_content = self._render_tab_content(tab, is_disabled=tab.disabled)

        # Handle disabled tabs - render as <a> without href
        if tab.disabled:
            classes = self._build_disabled_tab_classes(tab)
            # For icons, use inline-flex
            if tab.icon:
                classes = f"{classes} inline-flex items-center justify-center"

            return html.li(
                html.a(tab_content, class_=classes),  # type: ignore[arg-type]
                role="presentation",
            )

        # Regular tab button
        classes = self._build_tab_classes(tab, is_active, index)

        # For icons, use inline-flex for alignment
        if tab.icon:
            button_extra_class = "inline-flex items-center justify-center"
            # Merge with existing classes
            classes = f"{classes} {button_extra_class}"

        return html.li(
            html.button(
                tab_content,  # type: ignore[arg-type]
                id=tab_id,
                data_tabs_target=f"#{panel_id}",
                type="button",
                role="tab",
                aria_controls=panel_id,
                aria_selected="true" if is_active else "false",
                class_=classes,
            ),
            class_=li_class,
            role="presentation",
        )

    def _render_panel(self, tab: Tab, index: int, base_id: str, is_active: bool) -> Component:
        """Render individual tab panel."""
        tab_id = f"tab-{base_id}-{index}"
        panel_id = f"panel-{base_id}-{index}"

        # Panel classes (hidden if not active)
        panel_classes = "" if is_active else "hidden"

        # Build HTMX attributes dict (only include if not None)
        htmx_attrs: dict[str, str] = {}
        if tab.hx_get is not None:
            htmx_attrs["hx_get"] = tab.hx_get
        if tab.hx_post is not None:
            htmx_attrs["hx_post"] = tab.hx_post
        if tab.hx_trigger is not None:
            htmx_attrs["hx_trigger"] = tab.hx_trigger
        if tab.hx_target is not None:
            htmx_attrs["hx_target"] = tab.hx_target
        if tab.hx_swap is not None:
            htmx_attrs["hx_swap"] = tab.hx_swap

        # Build panel content (handle None case)
        panel_content: Component | str = tab.content if tab.content is not None else ""

        return html.div(
            panel_content,  # type: ignore[arg-type]
            id=panel_id,
            role="tabpanel",
            aria_labelledby=tab_id,
            class_=panel_classes,
            **htmx_attrs,  # Apply HTMX attributes to panel
        )

    def htmy(self, context: Context) -> Component:
        """Render tabs with tablist navigation and content panels."""
        base_id = self._get_base_id()
        content_id = f"{base_id}-content"

        # Determine active tab index (ignore disabled tabs)
        active_indices = [
            i for i, tab in enumerate(self.tabs) if tab.is_active and not tab.disabled
        ]
        # If no active tab or all active tabs disabled, activate first non-disabled tab
        if not active_indices:
            active_index = next((i for i, tab in enumerate(self.tabs) if not tab.disabled), 0)
        else:
            active_index = active_indices[0]

        # Build tablist classes
        tablist_classes = self._build_tablist_classes()

        # Get Flowbite active/inactive classes for JS class swapping
        active_classes, inactive_classes = self._get_flowbite_tab_classes()

        # Render tab buttons as list
        tab_buttons = [
            self._render_tab(tab, i, base_id, i == active_index) for i, tab in enumerate(self.tabs)
        ]

        # Render tablist with Flowbite data attributes
        tablist_ul = html.ul(
            *tab_buttons,  # type: ignore[arg-type]
            id=base_id,
            data_tabs_toggle=f"#{content_id}",
            data_tabs_active_classes=active_classes,
            data_tabs_inactive_classes=inactive_classes,
            role="tablist",
            class_=tablist_classes,
        )

        # UNDERLINE variant needs wrapper div with border
        tablist_component: Component
        if self.variant == TabVariant.UNDERLINE:
            tablist_component = html.div(
                tablist_ul,
                class_="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700",
            )
        else:
            tablist_component = tablist_ul

        # Render content panels as list
        panels = [
            self._render_panel(tab, i, base_id, i == active_index) for i, tab in enumerate(self.tabs)
        ]

        # Render content panels
        content_container = html.div(
            *panels,  # type: ignore[arg-type]
            id=content_id,
        )

        # Return tablist + content container
        return html.div(tablist_component, content_container)
