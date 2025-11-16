"""Dropdown component with Flowbite styling and JavaScript integration."""

from dataclasses import dataclass

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import (
    Color,
    DropdownPlacement,
    DropdownTriggerMode,
    DropdownTriggerType,
    Size,
)

# TYPE_CHECKING block removed - no forward references needed in US1


# T020: DropdownDivider class
@dataclass(frozen=True, kw_only=True)
class DropdownDivider:
    """Horizontal divider for dropdown menus."""

    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render divider as <hr> element."""
        classes = ClassBuilder("h-0 my-1 border-gray-100 dark:border-gray-600")
        return html.hr(class_=classes.merge(self.class_))


# T021: DropdownHeader class
@dataclass(frozen=True, kw_only=True)
class DropdownHeader:
    """Non-interactive header for dropdown sections."""

    label: str
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render header with role=presentation."""
        classes = ClassBuilder("px-4 py-3 text-sm text-gray-900 dark:text-white")
        return html.div(
            self.label,
            class_=classes.merge(self.class_),
            role="presentation",
        )


# T022: DropdownItem class (enhanced in US2 with icon and disabled, US3 with HTMX and nesting)
@dataclass(frozen=True, kw_only=True)
class DropdownItem:
    """Interactive menu item for dropdowns."""

    # Content
    label: str
    icon: Icon | None = None  # T039: Add icon support

    # Navigation
    href: str = "#"

    # T060: HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | None = None

    # State
    disabled: bool = False  # T041: Add disabled state

    # T061: Nested dropdown (for multi-level menus)
    dropdown: "Dropdown | None" = None

    # Styling
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render menu item."""
        classes = self._build_classes()

        # T040: Build link content with icon if provided
        children: list[Component | str] = []
        if self.icon:
            children.append(get_icon(self.icon, class_="w-4 h-4 me-2 flex-shrink-0"))
        children.append(self.label)

        # T061: If nested dropdown, render differently
        if self.dropdown:
            # Render nested dropdown structure
            nested_parts: list[Component] = [
                html.a(
                    *children,  # type: ignore[arg-type]
                    href=self.href,
                    class_=classes,
                    role="menuitem",
                    tabindex="0" if not self.disabled else "-1",
                ),
                self.dropdown.htmy(context),
            ]
            return html.li(*nested_parts)  # type: ignore[arg-type]

        # T060: Build attributes dict with HTMX support
        attrs = {
            "href": self.href,
            "class_": classes,
            "role": "menuitem",
            "tabindex": "0" if not self.disabled else "-1",
        }

        # Add HTMX attributes if provided
        if self.hx_get:
            attrs["hx_get"] = self.hx_get
        if self.hx_post:
            attrs["hx_post"] = self.hx_post
        if self.hx_put:
            attrs["hx_put"] = self.hx_put
        if self.hx_delete:
            attrs["hx_delete"] = self.hx_delete
        if self.hx_patch:
            attrs["hx_patch"] = self.hx_patch
        if self.hx_target:
            attrs["hx_target"] = self.hx_target
        if self.hx_swap:
            attrs["hx_swap"] = self.hx_swap
        if self.hx_trigger:
            attrs["hx_trigger"] = self.hx_trigger
        if self.hx_push_url:
            attrs["hx_push_url"] = self.hx_push_url

        return html.li(
            html.a(*children, **attrs)  # type: ignore[arg-type]
        )

    def _build_classes(self) -> str:
        """Build CSS classes for menu item."""
        builder = ClassBuilder(
            "flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
        )

        # T041: Add disabled state styling
        if self.disabled:
            builder.add("opacity-50 cursor-not-allowed pointer-events-none")

        return builder.merge(self.class_)


# T023: Dropdown class with button trigger rendering
@dataclass(frozen=True, kw_only=True)
class Dropdown:
    """Toggleable dropdown menu with Flowbite integration."""

    # Items (required)
    items: list[DropdownItem | DropdownHeader | DropdownDivider]

    # Trigger configuration
    trigger_label: str
    trigger_type: DropdownTriggerType = DropdownTriggerType.BUTTON
    trigger_mode: DropdownTriggerMode = DropdownTriggerMode.CLICK

    # Avatar trigger (only used if trigger_type=AVATAR)
    avatar_src: str | None = None
    avatar_alt: str = "User menu"

    # Button styling (only used if trigger_type=BUTTON)
    color: Color = Color.BLUE
    size: Size = Size.MD

    # Positioning
    placement: DropdownPlacement = DropdownPlacement.BOTTOM

    # Identifiers
    dropdown_id: str | None = None

    # State
    disabled: bool = False

    # Styling
    trigger_class: str = ""
    menu_class: str = ""

    def htmy(self, context: Context) -> Component:
        """Render dropdown with trigger and menu."""
        dropdown_id = self._get_dropdown_id()

        # T057: Dispatch to appropriate trigger renderer based on trigger_type
        if self.trigger_type == DropdownTriggerType.AVATAR:
            trigger = self._render_avatar_trigger(context, dropdown_id)
        elif self.trigger_type == DropdownTriggerType.TEXT:
            trigger = self._render_text_trigger(context, dropdown_id)
        else:  # BUTTON (default)
            trigger = self._render_button_trigger(context, dropdown_id)

        menu = self._render_menu(context, dropdown_id)

        return html.div(trigger, menu)  # type: ignore[arg-type]

    # T024: _render_button_trigger method
    def _render_button_trigger(self, context: Context, dropdown_id: str) -> Component:
        """Render button trigger."""
        trigger_id = f"trigger-{dropdown_id}"
        theme = ThemeContext.from_context(context)
        classes = self._build_trigger_classes(theme)

        # T062: Add chevron icon SVG (using SafeStr since htmy doesn't support SVG children)
        chevron_svg = SafeStr(
            '<svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" '
            'fill="none" viewBox="0 0 10 6">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-width="2" d="m1 1 4 4 4-4"/>'
            "</svg>"
        )

        return html.button(
            self.trigger_label,
            chevron_svg,
            id=trigger_id,
            data_dropdown_toggle=dropdown_id,
            data_dropdown_placement=self.placement.value,
            data_dropdown_trigger=self.trigger_mode.value,
            aria_expanded="false",
            aria_haspopup="true",
            aria_controls=dropdown_id,
            type_="button",
            class_=classes,
            disabled=self.disabled,
        )

    # T055: _render_avatar_trigger method
    def _render_avatar_trigger(self, context: Context, dropdown_id: str) -> Component:
        """Render avatar image trigger."""
        trigger_id = f"trigger-{dropdown_id}"

        return html.button(
            html.img(
                class_="w-10 h-10 rounded-full",
                src=self.avatar_src or "",
                alt=self.avatar_alt,
            ),
            type_="button",
            id=trigger_id,
            data_dropdown_toggle=dropdown_id,
            data_dropdown_placement=self.placement.value,
            data_dropdown_trigger=self.trigger_mode.value,
            aria_expanded="false",
            aria_haspopup="true",
            aria_controls=dropdown_id,
            class_="flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600",
        )

    # T056: _render_text_trigger method
    def _render_text_trigger(self, context: Context, dropdown_id: str) -> Component:
        """Render text link trigger."""
        trigger_id = f"trigger-{dropdown_id}"

        return html.button(
            self.trigger_label,
            type_="button",
            id=trigger_id,
            data_dropdown_toggle=dropdown_id,
            data_dropdown_placement=self.placement.value,
            data_dropdown_trigger=self.trigger_mode.value,
            aria_expanded="false",
            aria_haspopup="true",
            aria_controls=dropdown_id,
            class_="text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 inline-flex items-center dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700",
        )

    # T025: _render_menu method
    def _render_menu(self, context: Context, dropdown_id: str) -> Component:
        """Render dropdown menu."""
        theme = ThemeContext.from_context(context)
        classes = self._build_menu_classes(theme)
        trigger_id = f"trigger-{dropdown_id}"

        # Render items as a list
        rendered_items = [item.htmy(context) for item in self.items]
        ul_element = html.ul(
            *rendered_items,  # type: ignore[arg-type]
            class_="py-2 text-sm text-gray-700 dark:text-gray-200",
        )

        return html.div(
            ul_element,
            id=dropdown_id,
            role="menu",
            aria_labelledby=trigger_id,
            class_=classes,
        )

    # T026: _build_trigger_classes method with Color/Size mapping
    def _build_trigger_classes(self, theme: ThemeContext) -> str:
        """Build trigger button classes."""
        # T042: Complete COLOR_CLASSES mapping for all 8 colors
        COLOR_CLASSES = {
            Color.BLUE: "bg-blue-700 hover:bg-blue-800 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            Color.GREEN: "bg-green-700 hover:bg-green-800 focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
            Color.RED: "bg-red-700 hover:bg-red-800 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800",
            Color.YELLOW: "bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300 dark:focus:ring-yellow-900",
            Color.PURPLE: "bg-purple-700 hover:bg-purple-800 focus:ring-purple-300 dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-900",
            Color.PINK: "bg-pink-700 hover:bg-pink-800 focus:ring-pink-300 dark:bg-pink-600 dark:hover:bg-pink-700 dark:focus:ring-pink-900",
            Color.INDIGO: "bg-indigo-700 hover:bg-indigo-800 focus:ring-indigo-300 dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-900",
            Color.GRAY: "bg-gray-700 hover:bg-gray-800 focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800",
        }

        # T043: Complete SIZE_CLASSES mapping for all 5 sizes (already complete)
        SIZE_CLASSES = {
            Size.XS: "px-3 py-2 text-xs",
            Size.SM: "px-4 py-2 text-sm",
            Size.MD: "px-5 py-2.5 text-sm",
            Size.LG: "px-5 py-3 text-base",
            Size.XL: "px-6 py-3.5 text-base",
        }

        builder = ClassBuilder(
            "text-white focus:ring-4 focus:outline-none font-medium rounded-lg inline-flex items-center"
        )
        builder.add(COLOR_CLASSES.get(self.color, COLOR_CLASSES[Color.BLUE]))
        builder.add(SIZE_CLASSES.get(self.size, SIZE_CLASSES[Size.MD]))

        return builder.merge(self.trigger_class)

    # T027: _build_menu_classes method
    def _build_menu_classes(self, theme: ThemeContext) -> str:
        """Build menu container classes."""
        builder = ClassBuilder(
            "z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700"
        )
        return builder.merge(self.menu_class)

    # T028: _get_dropdown_id method with id(self) generation
    def _get_dropdown_id(self) -> str:
        """Get or generate unique dropdown ID."""
        return self.dropdown_id or f"dropdown-{id(self)}"
