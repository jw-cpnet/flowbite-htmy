# API Contract: Dropdown Component

**Feature**: Dropdown Component (007-dropdown)
**Date**: 2025-11-16
**Purpose**: Component interfaces and usage contracts for dropdown menus

## Overview

This document defines the public API for the Dropdown component and its supporting classes. All classes follow the htmy component pattern with `@dataclass(frozen=True, kw_only=True)` and implement the `htmy()` method.

---

## Enums

### DropdownPlacement

**Module**: `flowbite_htmy.types`

```python
class DropdownPlacement(str, Enum):
    """Dropdown menu positioning options."""
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
```

**Usage**:
```python
from flowbite_htmy.types import DropdownPlacement

placement = DropdownPlacement.TOP
```

---

### DropdownTriggerType

**Module**: `flowbite_htmy.types`

```python
class DropdownTriggerType(str, Enum):
    """Dropdown trigger element types."""
    BUTTON = "button"
    AVATAR = "avatar"
    TEXT = "text"
```

**Usage**:
```python
from flowbite_htmy.types import DropdownTriggerType

trigger_type = DropdownTriggerType.AVATAR
```

---

### DropdownTriggerMode

**Module**: `flowbite_htmy.types`

```python
class DropdownTriggerMode(str, Enum):
    """Dropdown activation methods."""
    CLICK = "click"
    HOVER = "hover"
```

**Usage**:
```python
from flowbite_htmy.types import DropdownTriggerMode

trigger_mode = DropdownTriggerMode.HOVER
```

---

## Component Classes

### DropdownDivider

**Module**: `flowbite_htmy.components`

**Purpose**: Visual separator between menu items.

**Interface**:
```python
@dataclass(frozen=True, kw_only=True)
class DropdownDivider:
    """Horizontal divider for dropdown menus.

    Renders as an <hr> element with Flowbite divider styling.

    Example:
        divider = DropdownDivider()
        divider_with_custom = DropdownDivider(class_="my-custom-class")
    """
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render divider as <hr> element."""
        ...
```

**HTML Output**:
```html
<hr class="h-0 my-1 border-gray-100 dark:border-gray-600" />
```

**Usage Example**:
```python
from flowbite_htmy.components import DropdownDivider

divider = DropdownDivider()
divider_custom = DropdownDivider(class_="my-2")  # Custom margin
```

---

### DropdownHeader

**Module**: `flowbite_htmy.components`

**Purpose**: Non-clickable section header for menu organization.

**Interface**:
```python
@dataclass(frozen=True, kw_only=True)
class DropdownHeader:
    """Non-interactive header for dropdown sections.

    Example:
        header = DropdownHeader(label="Account Settings")
    """
    label: str
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render header with role=presentation."""
        ...
```

**Parameters**:
- `label` (str, required): Header text
- `class_` (str, optional): Custom CSS classes

**HTML Output**:
```html
<div class="px-4 py-3 text-sm text-gray-900 dark:text-white" role="presentation">
    Account Settings
</div>
```

**Usage Example**:
```python
from flowbite_htmy.components import DropdownHeader

header = DropdownHeader(label="User Menu")
header_styled = DropdownHeader(label="Settings", class_="font-bold")
```

---

### DropdownItem

**Module**: `flowbite_htmy.components`

**Purpose**: Clickable menu item with optional icon and HTMX support.

**Interface**:
```python
@dataclass(frozen=True, kw_only=True)
class DropdownItem:
    """Interactive menu item for dropdowns.

    Supports icons, navigation, HTMX attributes, and nested dropdowns.

    Example:
        item = DropdownItem(label="Profile", href="/profile")
        item_with_icon = DropdownItem(
            label="Dashboard",
            icon=Icon.DASHBOARD,
            href="/dashboard"
        )
        item_with_htmx = DropdownItem(
            label="Load More",
            hx_get="/api/items",
            hx_target="#list"
        )
    """
    # Content
    label: str
    icon: Icon | None = None

    # Navigation
    href: str = "#"

    # HTMX attributes
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
    disabled: bool = False

    # Nested dropdown (for multi-level menus)
    dropdown: "Dropdown | None" = None

    # Styling
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render menu item as <li><a> with optional icon and HTMX attributes."""
        ...
```

**Parameters**:
- `label` (str, required): Item text
- `icon` (Icon | None): Optional icon from `flowbite_htmy.icons`
- `href` (str): Link destination (default: "#")
- `hx_get`, `hx_post`, etc.: HTMX attributes for dynamic content
- `disabled` (bool): Disable item (default: False)
- `dropdown` (Dropdown | None): Nested dropdown for multi-level menus
- `class_` (str): Custom CSS classes

**HTML Output (Simple)**:
```html
<li>
    <a href="/profile"
       class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600"
       role="menuitem"
       tabindex="0">
        Profile
    </a>
</li>
```

**HTML Output (With Icon)**:
```html
<li>
    <a href="/dashboard" class="..." role="menuitem" tabindex="0">
        <svg class="w-4 h-4 mr-2"><!-- icon --></svg>
        Dashboard
    </a>
</li>
```

**HTML Output (With HTMX)**:
```html
<li>
    <a href="#"
       hx-get="/api/items"
       hx-target="#list"
       hx-swap="innerHTML"
       class="..."
       role="menuitem">
        Load More
    </a>
</li>
```

**Usage Examples**:
```python
from flowbite_htmy.components import DropdownItem
from flowbite_htmy.icons import Icon

# Simple link
item1 = DropdownItem(label="Profile", href="/profile")

# With icon
item2 = DropdownItem(
    label="Dashboard",
    icon=Icon.DASHBOARD,
    href="/dashboard"
)

# With HTMX
item3 = DropdownItem(
    label="Load More",
    hx_get="/api/items",
    hx_target="#items-list",
    hx_swap="beforeend"
)

# Disabled item
item4 = DropdownItem(label="Coming Soon", disabled=True)

# Nested dropdown (multi-level)
item5 = DropdownItem(
    label="Settings",
    dropdown=Dropdown(
        items=[
            DropdownItem(label="Account", href="/settings/account"),
            DropdownItem(label="Privacy", href="/settings/privacy"),
        ]
    )
)
```

---

### Dropdown

**Module**: `flowbite_htmy.components`

**Purpose**: Main dropdown component with trigger and menu.

**Interface**:
```python
@dataclass(frozen=True, kw_only=True)
class Dropdown:
    """Toggleable dropdown menu with Flowbite integration.

    Supports multiple trigger types (button, avatar, text), positioning,
    HTMX integration, and multi-level nesting.

    Example:
        dropdown = Dropdown(
            trigger_label="Actions",
            items=[
                DropdownItem(label="Edit", href="/edit"),
                DropdownItem(label="Delete", href="/delete"),
            ]
        )
    """
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
    dropdown_id: str | None = None  # Auto-generated if None

    # State
    disabled: bool = False

    # Styling
    trigger_class: str = ""
    menu_class: str = ""

    def htmy(self, context: Context) -> Component:
        """Render dropdown with trigger and menu container."""
        ...

    def _render_trigger(self, context: Context) -> Component:
        """Render trigger element based on trigger_type."""
        ...

    def _render_menu(self, context: Context) -> Component:
        """Render dropdown menu container with items."""
        ...

    def _build_trigger_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for trigger element."""
        ...

    def _build_menu_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for menu container."""
        ...

    def _get_dropdown_id(self) -> str:
        """Get or generate unique dropdown ID."""
        ...
```

**Parameters**:
- `items` (list, required): Menu items (DropdownItem, DropdownHeader, DropdownDivider)
- `trigger_label` (str, required): Trigger button text
- `trigger_type` (DropdownTriggerType): Trigger element type (default: BUTTON)
- `trigger_mode` (DropdownTriggerMode): Activation method (default: CLICK)
- `avatar_src` (str | None): Avatar image URL (required if trigger_type=AVATAR)
- `avatar_alt` (str): Avatar alt text (default: "User menu")
- `color` (Color): Button color variant (default: BLUE, only for BUTTON type)
- `size` (Size): Button size (default: MD, only for BUTTON type)
- `placement` (DropdownPlacement): Menu positioning (default: BOTTOM)
- `dropdown_id` (str | None): Custom ID (auto-generated if None)
- `disabled` (bool): Disable dropdown (default: False)
- `trigger_class` (str): Custom CSS classes for trigger
- `menu_class` (str): Custom CSS classes for menu

**HTML Output** (Button Trigger):
```html
<div>
    <!-- Trigger -->
    <button id="trigger-dropdown-123"
            data-dropdown-toggle="dropdown-123"
            data-dropdown-placement="bottom"
            data-dropdown-trigger="click"
            aria-expanded="false"
            aria-haspopup="true"
            aria-controls="dropdown-123"
            type="button"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Actions
        <svg class="w-2.5 h-2.5 ms-3"><!-- chevron --></svg>
    </button>

    <!-- Menu -->
    <div id="dropdown-123"
         role="menu"
         aria-labelledby="trigger-dropdown-123"
         class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
        <ul class="py-2 text-sm text-gray-700 dark:text-gray-200">
            <li><a href="/edit" role="menuitem">Edit</a></li>
            <li><a href="/delete" role="menuitem">Delete</a></li>
        </ul>
    </div>
</div>
```

**Usage Examples**:
```python
from flowbite_htmy.components import Dropdown, DropdownItem, DropdownHeader, DropdownDivider
from flowbite_htmy.types import Color, Size, DropdownPlacement, DropdownTriggerType

# Basic dropdown
dropdown = Dropdown(
    trigger_label="Actions",
    items=[
        DropdownItem(label="Edit", href="/edit"),
        DropdownItem(label="Delete", href="/delete"),
    ]
)

# Avatar dropdown (user menu)
user_menu = Dropdown(
    trigger_label="User Menu",
    trigger_type=DropdownTriggerType.AVATAR,
    avatar_src="/images/user.jpg",
    items=[
        DropdownHeader(label="John Doe"),
        DropdownHeader(label="john@example.com"),
        DropdownDivider(),
        DropdownItem(label="Dashboard", href="/dashboard"),
        DropdownItem(label="Settings", href="/settings"),
        DropdownDivider(),
        DropdownItem(label="Sign out", href="/logout"),
    ]
)

# Custom color and size
styled_dropdown = Dropdown(
    trigger_label="Options",
    color=Color.GREEN,
    size=Size.LG,
    items=[
        DropdownItem(label="Option 1"),
        DropdownItem(label="Option 2"),
    ]
)

# Top placement
top_dropdown = Dropdown(
    trigger_label="Dropdown",
    placement=DropdownPlacement.TOP,
    items=[
        DropdownItem(label="Item 1"),
        DropdownItem(label="Item 2"),
    ]
)

# Hover trigger
hover_menu = Dropdown(
    trigger_label="Hover Me",
    trigger_mode=DropdownTriggerMode.HOVER,
    items=[
        DropdownItem(label="Quick Action 1"),
        DropdownItem(label="Quick Action 2"),
    ]
)

# Multi-level dropdown
nested_dropdown = Dropdown(
    trigger_label="Main Menu",
    items=[
        DropdownItem(label="Home", href="/"),
        DropdownItem(
            label="Settings",
            dropdown=Dropdown(
                items=[
                    DropdownItem(label="Account", href="/settings/account"),
                    DropdownItem(label="Privacy", href="/settings/privacy"),
                    DropdownItem(label="Security", href="/settings/security"),
                ]
            )
        ),
        DropdownDivider(),
        DropdownItem(label="About", href="/about"),
    ]
)
```

---

## Exports

**From `flowbite_htmy.components`**:
```python
from flowbite_htmy.components import (
    Dropdown,
    DropdownItem,
    DropdownHeader,
    DropdownDivider,
)
```

**From `flowbite_htmy.types`**:
```python
from flowbite_htmy.types import (
    DropdownPlacement,
    DropdownTriggerType,
    DropdownTriggerMode,
    Color,  # Pre-existing
    Size,   # Pre-existing
)
```

**From `flowbite_htmy.icons`**:
```python
from flowbite_htmy.icons import Icon  # For menu item icons
```

---

## Type Signatures

### Component Rendering

All components implement the htmy protocol:

```python
def htmy(self, context: Context) -> Component:
    """Render component to htmy Component."""
    ...
```

### Context Usage

Components retrieve theme context for dark mode support:

```python
from flowbite_htmy.base import ThemeContext

theme = ThemeContext.from_context(context)
if theme.dark_mode:
    # Dark mode classes are ALWAYS included via dark: prefix
    # This check is NOT needed in modern implementation
    pass
```

**Note**: Modern implementation always includes `dark:` classes. Do NOT conditionally add based on `theme.dark_mode`.

---

## Constraints and Invariants

### Required Fields
- `Dropdown.items`: Must contain at least one item
- `Dropdown.trigger_label`: Must not be empty
- `DropdownHeader.label`: Must not be empty
- `DropdownItem.label`: Must not be empty

### Conditional Requirements
- If `trigger_type=AVATAR`, `avatar_src` must be provided
- If `dropdown_id` is None, auto-generate using `f"dropdown-{id(self)}"`

### Type Safety
- All HTMX attributes are `str | None` (nullable)
- Color and Size enums enforce valid values
- Placement, TriggerType, TriggerMode enums prevent invalid states

### ARIA Compliance
- Every dropdown must have unique `id` for ARIA relationships
- Trigger must have `aria-controls` pointing to menu
- Menu must have `aria-labelledby` pointing to trigger
- All items must have `role="menuitem"`

### Flowbite Integration
- Trigger must have `data-dropdown-toggle` attribute
- Trigger must have `type="button"` (for button triggers)
- Menu must have `hidden` class (Flowbite JS removes when opening)

---

## Error Handling

### Validation Errors
- Empty `items` list → ValueError
- Empty `label` → ValueError
- `trigger_type=AVATAR` without `avatar_src` → ValueError

### Type Errors
- Invalid Color/Size/Placement enum → Type error (caught by mypy)
- Wrong type in `items` list → Type error (caught by mypy)

**Note**: Errors should be caught at development time via mypy strict mode, not at runtime.

---

## Versioning

**Initial Release**: v0.2.0 (Phase 2C)

**Compatibility**:
- Flowbite CSS 2.5.1
- Flowbite JavaScript (included with Flowbite CSS)
- HTMX 2.0.2 (optional, for dynamic content)

**Breaking Changes**: None (initial implementation)

---

## Testing Contract

Components must be tested for:

1. **Default Rendering**: Minimal props produce valid HTML
2. **All Variants**: Every enum value tested
3. **HTMX Attributes**: All hx_* props render correctly
4. **Dark Mode**: dark: classes always present
5. **Custom Classes**: class_ prop merges with component classes
6. **ARIA Attributes**: All required ARIA attributes present
7. **Flowbite Data Attributes**: data-dropdown-* attributes correct
8. **Nested Dropdowns**: Multi-level composition works
9. **Edge Cases**: Empty strings, None values, disabled states

**Coverage Target**: >90%

---

## Next Steps

Proceed to Quickstart guide generation (TDD workflow).
