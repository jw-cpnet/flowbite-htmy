"""Drawer component for Flowbite."""

import uuid
from dataclasses import dataclass
from typing import Literal

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import ButtonVariant, Color, DrawerPlacement, DrawerWidth, Size


@dataclass(frozen=True, kw_only=True)
class Drawer:
    """Flowbite drawer component.

    An off-canvas panel that slides in from any edge of the screen for navigation menus,
    forms, settings panels, and filtering interfaces. Supports ARIA accessibility,
    dark mode, and HTMX integration.

    Example:
        >>> Drawer(
        ...     trigger_label="Open Menu",
        ...     content=html.div("Menu content"),
        ...     placement=DrawerPlacement.LEFT,
        ... )
    """

    # Required props
    trigger_label: str
    """Text label for the trigger button that opens the drawer."""

    content: Component
    """Content to display inside the drawer body (forms, navigation, etc.)."""

    # Optional configuration
    placement: DrawerPlacement = DrawerPlacement.LEFT
    """Edge position from which the drawer slides (LEFT, RIGHT, TOP, BOTTOM). Default is LEFT."""

    backdrop: bool = True
    """Whether to show a dimming backdrop overlay behind the drawer. Default is True."""

    body_scrolling: bool = False
    """Whether to allow scrolling of the background page when drawer is open. Default is False."""

    edge: bool = False
    """Whether to show a visible tab at the edge when drawer is closed. Default is False."""

    # Customization
    trigger_color: Color = Color.PRIMARY
    """Color variant for the trigger button. Default is PRIMARY."""

    trigger_variant: ButtonVariant = ButtonVariant.DEFAULT
    """Visual variant for the trigger button (DEFAULT, OUTLINE, GRADIENT). Default is DEFAULT."""

    trigger_size: Size = Size.MD
    """Size variant for the trigger button. Default is MD."""

    drawer_id: str | None = None
    """Unique ID for the drawer. Auto-generated UUID if not provided."""

    # Styling
    width: str = "w-80"
    """Width class for LEFT/RIGHT placements (Tailwind class). Default is w-80 (320px)."""

    height: str = "h-1/2"
    """Height class for TOP/BOTTOM placements (Tailwind class). Default is h-1/2 (50vh)."""

    class_: str = ""
    """Additional CSS classes for the drawer panel."""

    trigger_class: str = ""
    """Additional CSS classes for the trigger button."""

    # HTMX attributes
    hx_get: str | None = None
    """HTMX hx-get attribute for dynamic content loading."""

    hx_post: str | None = None
    """HTMX hx-post attribute for form submission."""

    hx_target: str | None = None
    """HTMX hx-target attribute specifying where to load content."""

    hx_swap: str | None = None
    """HTMX hx-swap attribute specifying how to swap content."""

    def _get_placement_classes(self) -> str:
        """Get placement-specific transform classes.

        Returns fresh string each time to avoid any potential class leakage.
        """
        placement_map = {
            DrawerPlacement.LEFT: "left-0 top-0 h-screen -translate-x-full",
            DrawerPlacement.RIGHT: "right-0 top-0 h-screen translate-x-full",
            DrawerPlacement.TOP: "top-0 left-0 w-full -translate-y-full",
            DrawerPlacement.BOTTOM: "bottom-0 left-0 w-full translate-y-full",
        }
        return placement_map[self.placement]

    def htmy(self, context: Context) -> Component:
        """Render the Drawer component.

        Args:
            context: htmy rendering context

        Returns:
            Component tree with trigger button, drawer panel, backdrop, and close button
        """
        # T022: Generate unique drawer_id if not provided
        drawer_id = self.drawer_id or f"drawer-{uuid.uuid4().hex[:8]}"

        # Get theme context for dark mode support
        theme = ThemeContext.from_context(context)

        # T023: Build trigger button
        trigger = self._build_trigger(drawer_id)

        # T026: Build optional backdrop
        backdrop = self._build_backdrop(drawer_id) if self.backdrop else None

        # T025: Build drawer panel
        panel = self._build_panel(drawer_id, theme)

        # Build edge tab if enabled
        edge_tab = self._build_edge_tab(drawer_id) if self.edge else None

        # Return complete drawer structure
        components: list[Component] = [trigger]
        if edge_tab:
            components.append(edge_tab)
        if backdrop:
            components.append(backdrop)
        components.append(panel)

        return html.div(*components)  # type: ignore[arg-type]

    def _build_trigger(self, drawer_id: str) -> Component:
        """Build the trigger button with Flowbite data attributes.

        Args:
            drawer_id: Unique drawer identifier

        Returns:
            Button element that triggers drawer open
        """
        from flowbite_htmy.components.button import Button

        return Button(
            label=self.trigger_label,
            color=self.trigger_color,
            variant=self.trigger_variant,
            size=self.trigger_size,
            class_=self.trigger_class,
            attrs={
                "data-drawer-target": drawer_id,
                "data-drawer-show": drawer_id,
                "data-drawer-placement": self.placement.value,
                "aria-controls": drawer_id,
            },
        )

    def _build_backdrop(self, drawer_id: str) -> Component:
        """Build the backdrop overlay.

        Args:
            drawer_id: Unique drawer identifier

        Returns:
            Backdrop div element
        """
        # T026: Backdrop with dark overlay and data attributes
        # CRITICAL: Must have 'hidden' class to be invisible on page load
        backdrop_classes = ClassBuilder("hidden fixed inset-0 z-30")
        backdrop_classes.add("bg-gray-900/50 dark:bg-gray-900/80")

        return html.div(
            class_=backdrop_classes.build(),
            **{
                "data-drawer-backdrop": drawer_id,
                "data-drawer-hide": drawer_id,
                "aria-hidden": "true",
            },
        )

    def _build_edge_tab(self, drawer_id: str) -> Component:
        """Build the edge tab for swipeable variant.

        Args:
            drawer_id: Unique drawer identifier

        Returns:
            Button element positioned at drawer edge
        """
        # Position tab based on placement
        if self.placement == DrawerPlacement.LEFT:
            tab_classes = "fixed left-0 top-1/2 -translate-y-1/2 z-30"
            tab_icon = "›"
        elif self.placement == DrawerPlacement.RIGHT:
            tab_classes = "fixed right-0 top-1/2 -translate-y-1/2 z-30"
            tab_icon = "‹"
        elif self.placement == DrawerPlacement.TOP:
            tab_classes = "fixed top-0 left-1/2 -translate-x-1/2 z-30"
            tab_icon = "⌄"
        else:  # BOTTOM
            tab_classes = "fixed bottom-0 left-1/2 -translate-x-1/2 z-30"
            tab_icon = "⌃"

        tab_classes += " bg-gray-50 dark:bg-gray-700 p-2 rounded shadow-lg"
        tab_classes += " text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-600"

        return html.button(
            html.span(tab_icon, class_="text-2xl"),
            class_=tab_classes,
            **{
                "data-drawer-show": drawer_id,
                "aria-controls": drawer_id,
            },
        )

    def _build_panel(self, drawer_id: str, theme: ThemeContext) -> Component:
        """Build the main drawer panel.

        Args:
            drawer_id: Unique drawer identifier
            theme: Theme context for dark mode

        Returns:
            Drawer panel div with header and body
        """
        # T024: Get placement-specific transform classes
        placement_classes = self._get_placement_classes()

        # Build drawer panel classes
        panel_builder = ClassBuilder("fixed z-40 max-h-screen")
        panel_builder.add(placement_classes)
        panel_builder.add("transition-transform")

        # T028: Add dark mode classes
        panel_builder.add("bg-white dark:bg-gray-800")

        # Add placement-specific border
        if self.placement == DrawerPlacement.LEFT:
            panel_builder.add("border-r border-gray-200 dark:border-gray-700")
        elif self.placement == DrawerPlacement.RIGHT:
            panel_builder.add("border-l border-gray-200 dark:border-gray-700")
        elif self.placement == DrawerPlacement.TOP:
            panel_builder.add("border-b border-gray-200 dark:border-gray-700")
        else:  # BOTTOM
            panel_builder.add("border-t border-gray-200 dark:border-gray-700")

        # Add width/height based on placement
        if self.placement in (DrawerPlacement.LEFT, DrawerPlacement.RIGHT):
            panel_builder.add(self.width)
        else:  # TOP or BOTTOM
            panel_builder.add(self.height)

        # T027: ARIA attributes and data attributes
        panel_attrs = {
            "id": drawer_id,
            "aria-labelledby": f"{drawer_id}-label",
            "aria-hidden": "true",
            "tabindex": "-1",
            "data-drawer-placement": self.placement.value,
        }

        # Add HTMX attributes if provided
        if self.hx_get:
            panel_attrs["hx-get"] = self.hx_get
        if self.hx_post:
            panel_attrs["hx-post"] = self.hx_post
        if self.hx_target:
            panel_attrs["hx-target"] = self.hx_target
        if self.hx_swap:
            panel_attrs["hx-swap"] = self.hx_swap

        # T025: Build header with close button
        header = self._build_header(drawer_id, theme)

        # T025: Build body with content (scrollable)
        body = html.div(
            self.content,  # type: ignore[arg-type]
            class_="p-4 overflow-y-auto",
        )

        # Merge custom classes
        final_classes = panel_builder.merge(self.class_)

        return html.div(
            header,  # type: ignore[arg-type]
            body,
            class_=final_classes,
            **panel_attrs,
        )

    def _build_header(self, drawer_id: str, theme: ThemeContext) -> Component:
        """Build the drawer header with close button.

        Args:
            drawer_id: Unique drawer identifier
            theme: Theme context

        Returns:
            Header div with title and close button
        """
        # Header classes
        header_builder = ClassBuilder("flex items-center justify-between p-4")
        header_builder.add("border-b border-gray-200 dark:border-gray-700")

        # Close button
        close_button = html.button(
            get_icon(Icon.CLOSE, class_="w-3 h-3"),
            type="button",
            class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
            **{
                "data-drawer-hide": drawer_id,
            },
        )

        # Header title (for aria-labelledby)
        title = html.h5(
            self.trigger_label,  # Use trigger label as drawer title
            id=f"{drawer_id}-label",
            class_="text-base font-semibold text-gray-500 uppercase dark:text-gray-400",
        )

        return html.div(
            title,
            close_button,
            class_=header_builder.build(),
        )


@dataclass(frozen=True, kw_only=True)
class DrawerShell:
    """Drawer shell for HTMX dynamic content loading.

    An empty drawer container placed once on the page. Content is loaded
    dynamically via HTMX into the content div identified by ``content_id``.
    Trigger buttons are separate elements with ``hx-get`` / ``hx-target``
    attributes pointing to the content div.

    A hidden trigger button is rendered so Flowbite JS discovers and registers
    the drawer automatically.

    Example:
        >>> DrawerShell(
        ...     id="drawer-update",
        ...     title="Update Item",
        ...     content_id="drawer-update-content",
        ...     width=DrawerWidth.XXL,
        ... )

    Trigger button (separate element):
        >>> Button(
        ...     label="Edit",
        ...     hx_get="/api/items/1",
        ...     hx_target="#drawer-update-content",
        ...     attrs={
        ...         "hx-on::after-request": (
        ...             "initDrawers(); showDrawer('drawer-update');"
        ...         ),
        ...     },
        ... )
    """

    # Required props
    id: str
    """Unique drawer ID (used for Flowbite data attributes and ARIA)."""

    title: str
    """Drawer header title."""

    content_id: str
    """ID for the content div where HTMX will load dynamic content."""

    # Optional configuration
    width: DrawerWidth | str = DrawerWidth.XXL
    """Width of the drawer. Use DrawerWidth enum or custom Tailwind class."""

    position: str = "right"
    """Side the drawer slides in from: ``'left'`` or ``'right'``."""

    show_header: bool = True
    """Whether to show the header with title and close button."""

    header_icon: Component | None = None
    """Optional icon component to display before the title."""

    dismiss_type: Literal["dismiss", "hide"] = "dismiss"
    """Close button action: ``'dismiss'`` uses ``data-drawer-dismiss``,
    ``'hide'`` uses ``data-drawer-hide``."""

    loading_spinner: bool = True
    """Whether to show a loading spinner as default placeholder content."""

    class_: str = ""
    """Additional CSS classes for the drawer container."""

    content_class: str = ""
    """Additional CSS classes for the content div."""

    def htmy(self, context: Context) -> Component:
        """Render the drawer shell."""
        width_class = self.width.value if isinstance(self.width, DrawerWidth) else self.width

        position_classes = (
            "top-0 right-0 translate-x-full"
            if self.position == "right"
            else "top-0 left-0 -translate-x-full"
        )

        container_builder = ClassBuilder(
            f"fixed {position_classes} z-40 w-full h-screen {width_class} p-4 "
            "overflow-y-auto transition-transform bg-white dark:bg-gray-800"
        )

        # Hidden trigger for Flowbite auto-initialisation
        hidden_trigger = html.button(
            type="button",
            class_="hidden",
            **{
                "data-drawer-target": self.id,
                "data-drawer-placement": self.position,
            },
        )

        children: list[Component] = [hidden_trigger]

        if self.show_header:
            children.append(self._render_header())

        children.append(self._render_content())

        return html.div(
            *children,
            id=self.id,
            class_=container_builder.merge(self.class_),
            tabindex="-1",
            **{
                "aria-labelledby": f"{self.id}-label",
                "aria-hidden": "true",
            },
        )

    def _render_header(self) -> Component:
        """Render header with title and close button."""
        title_children: list[Component | str] = []
        if self.header_icon:
            title_children.append(self.header_icon)
        title_children.append(self.title)

        title = html.h5(
            *title_children,
            id=f"{self.id}-label",
            class_=(
                "inline-flex items-center mb-6 text-sm font-semibold "
                "text-gray-500 uppercase dark:text-gray-400"
            ),
        )

        dismiss_attr = (
            {"data-drawer-dismiss": self.id}
            if self.dismiss_type == "dismiss"
            else {"data-drawer-hide": self.id}
        )

        close_button = html.button(
            get_icon(Icon.CLOSE, class_="w-5 h-5"),
            html.span("Close menu", class_="sr-only"),
            type="button",
            class_=(
                "text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 "
                "rounded-lg text-sm p-1.5 absolute top-2.5 right-2.5 inline-flex "
                "items-center dark:hover:bg-gray-600 dark:hover:text-white"
            ),
            **dismiss_attr,
            **{"aria-controls": self.id},
        )

        return html.div(title, close_button)

    def _render_content(self) -> Component:
        """Render the content target div."""
        default_content: list[Component] = []
        if self.loading_spinner:
            default_content.append(
                html.div(
                    html.div(
                        class_=("animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"),
                    ),
                    class_="flex justify-center items-center h-32",
                )
            )

        return html.div(
            *default_content,
            id=self.content_id,
            class_=self.content_class or None,
        )
