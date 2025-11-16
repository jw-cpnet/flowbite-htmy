# Data Model: Dropdown Component

**Feature**: Dropdown Component (007-dropdown)
**Date**: 2025-11-16
**Purpose**: Entity definitions and relationships for dropdown menu component

## Entity Overview

The Dropdown component consists of 9 entity types:

1. **DropdownPlacement** (Enum) - Positioning options
2. **DropdownTriggerType** (Enum) - Trigger element types
3. **DropdownTriggerMode** (Enum) - Activation methods
4. **DropdownDivider** (Class) - Visual separator
5. **DropdownHeader** (Class) - Section header
6. **DropdownItem** (Class) - Clickable menu item
7. **Dropdown** (Class) - Main dropdown component

Additional imported types:
8. **Color** (Enum) - From `flowbite_htmy.types` - Color variants
9. **Size** (Enum) - From `flowbite_htmy.types` - Size variants

---

## 1. DropdownPlacement (Enum)

### Purpose
Defines where the dropdown menu appears relative to the trigger element.

### Values
```python
class DropdownPlacement(str, Enum):
    TOP = "top"           # Menu appears above trigger
    BOTTOM = "bottom"     # Menu appears below trigger (default)
    LEFT = "left"         # Menu appears to the left of trigger
    RIGHT = "right"       # Menu appears to the right of trigger
```

### Validation Rules
- Must be one of the four defined values
- Used in `data-dropdown-placement` attribute for Flowbite JS

### Usage
```python
dropdown = Dropdown(
    placement=DropdownPlacement.TOP,
    # ...
)
```

---

## 2. DropdownTriggerType (Enum)

### Purpose
Defines the visual type of the trigger element that opens the dropdown.

### Values
```python
class DropdownTriggerType(str, Enum):
    BUTTON = "button"     # Standard button trigger (default)
    AVATAR = "avatar"     # Avatar image trigger (for user menus)
    TEXT = "text"         # Text link trigger (minimal styling)
```

### Validation Rules
- Must be one of the three defined values
- Determines which CSS classes are applied to trigger element

### State Transitions
```
BUTTON → Renders as <button> with button styling
AVATAR → Renders as <img> wrapped in clickable container
TEXT → Renders as <button> with text-only styling (no background)
```

### Usage
```python
# Button trigger (default)
dropdown = Dropdown(trigger_type=DropdownTriggerType.BUTTON)

# Avatar trigger for user menu
dropdown = Dropdown(
    trigger_type=DropdownTriggerType.AVATAR,
    avatar_src="/images/user.jpg",
    avatar_alt="User menu"
)

# Text link trigger
dropdown = Dropdown(trigger_type=DropdownTriggerType.TEXT)
```

---

## 3. DropdownTriggerMode (Enum)

### Purpose
Defines how the dropdown is activated (click vs. hover).

### Values
```python
class DropdownTriggerMode(str, Enum):
    CLICK = "click"       # Opens on click (default)
    HOVER = "hover"       # Opens on hover
```

### Validation Rules
- Must be one of the two defined values
- Used in `data-dropdown-trigger` attribute for Flowbite JS

### Behavior
- **CLICK**: User must click trigger to open/close dropdown
- **HOVER**: Dropdown opens when mouse enters trigger, closes when mouse leaves

### Usage
```python
# Click trigger (default)
dropdown = Dropdown(trigger_mode=DropdownTriggerMode.CLICK)

# Hover trigger (for navigation menus)
dropdown = Dropdown(trigger_mode=DropdownTriggerMode.HOVER)
```

---

## 4. DropdownDivider (Class)

### Purpose
Visual separator (horizontal line) between menu items.

### Fields
```python
@dataclass(frozen=True, kw_only=True)
class DropdownDivider:
    class_: str = ""      # Custom CSS classes
```

### Validation Rules
- No required fields
- Always renders as `<hr>` element with Flowbite divider classes

### Rendering
```html
<hr class="h-0 my-1 border-gray-100 dark:border-gray-600 {class_}" />
```

### Usage
```python
items = [
    DropdownItem(label="Profile"),
    DropdownDivider(),  # Separator
    DropdownItem(label="Settings"),
]
```

---

## 5. DropdownHeader (Class)

### Purpose
Non-clickable section header for organizing menu items.

### Fields
```python
@dataclass(frozen=True, kw_only=True)
class DropdownHeader:
    label: str            # Header text (required)
    class_: str = ""      # Custom CSS classes
```

### Validation Rules
- `label` is required and must not be empty
- Not interactive (no href, no click handler)
- Uses `role="presentation"` for ARIA

### Rendering
```html
<div class="px-4 py-3 text-sm text-gray-900 dark:text-white {class_}" role="presentation">
    {label}
</div>
```

### Usage
```python
items = [
    DropdownHeader(label="Account"),
    DropdownItem(label="Profile"),
    DropdownItem(label="Settings"),
]
```

---

## 6. DropdownItem (Class)

### Purpose
Clickable menu item with optional icon and HTMX attributes.

### Fields
```python
@dataclass(frozen=True, kw_only=True)
class DropdownItem:
    # Content
    label: str                    # Item text (required)
    icon: Icon | None = None      # Optional icon from flowbite_htmy.icons

    # Navigation
    href: str = "#"               # Link destination (default: "#")

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
    disabled: bool = False        # Disable item

    # Nested dropdown
    dropdown: Dropdown | None = None  # For multi-level menus

    # Styling
    class_: str = ""              # Custom CSS classes
```

### Validation Rules
- `label` is required and must not be empty
- If `dropdown` is provided, item becomes a parent for nested dropdown
- Cannot have both `href` navigation and `dropdown` (choose one purpose)
- HTMX attributes are optional and mutually compatible

### State Transitions
```
Normal → Hover → Active → Clicked
  ↓
Disabled (cannot transition)
```

### Rendering (Simple Item)
```html
<li>
    <a href="{href}"
       class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 {class_}"
       role="menuitem"
       tabindex="0">
        {icon if provided}
        {label}
    </a>
</li>
```

### Rendering (Nested Dropdown)
```html
<li>
    <button data-dropdown-toggle="nested-{id}" role="menuitem">
        {label}
    </button>
    {nested dropdown component}
</li>
```

### Usage
```python
# Simple link
DropdownItem(label="Profile", href="/profile")

# With icon
DropdownItem(label="Dashboard", icon=Icon.DASHBOARD, href="/dashboard")

# With HTMX
DropdownItem(
    label="Load More",
    hx_get="/api/items",
    hx_target="#items-list",
    hx_swap="beforeend"
)

# Nested dropdown
DropdownItem(
    label="Settings",
    dropdown=Dropdown(
        items=[
            DropdownItem(label="Account", href="/settings/account"),
            DropdownItem(label="Privacy", href="/settings/privacy"),
        ]
    )
)

# Disabled item
DropdownItem(label="Coming Soon", disabled=True)
```

---

## 7. Dropdown (Class)

### Purpose
Main dropdown component that renders trigger and menu container.

### Fields
```python
@dataclass(frozen=True, kw_only=True)
class Dropdown:
    # Items (can be mix of DropdownItem, DropdownHeader, DropdownDivider)
    items: list[DropdownItem | DropdownHeader | DropdownDivider]

    # Trigger configuration
    trigger_label: str                               # Trigger button text
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
    dropdown_id: str | None = None                   # Custom ID (auto-generated if None)

    # State
    disabled: bool = False

    # Styling
    trigger_class: str = ""                          # Custom classes for trigger
    menu_class: str = ""                             # Custom classes for menu
```

### Validation Rules
- `items` must contain at least one element
- `trigger_label` is required
- If `trigger_type=AVATAR`, `avatar_src` must be provided
- If `dropdown_id` is None, generate unique ID using `f"dropdown-{id(self)}"`
- Color and Size only apply when `trigger_type=BUTTON`

### Generated IDs
```python
# Trigger ID: "trigger-{dropdown_id}"
# Menu ID: "{dropdown_id}"
# Relationship: aria-controls="{dropdown_id}"
```

### ARIA Attributes
- Trigger: `aria-expanded="false"` (Flowbite JS updates to "true" when open)
- Trigger: `aria-haspopup="true"`
- Trigger: `aria-controls="{dropdown_id}"`
- Menu: `id="{dropdown_id}"`
- Menu: `role="menu"`
- Menu: `aria-labelledby="trigger-{dropdown_id}"`

### Flowbite Data Attributes
- Trigger: `data-dropdown-toggle="{dropdown_id}"`
- Trigger: `data-dropdown-placement="{placement.value}"`
- Trigger: `data-dropdown-trigger="{trigger_mode.value}"`

### Rendering (Button Trigger)
```html
<div>
    <!-- Trigger Button -->
    <button id="trigger-{dropdown_id}"
            data-dropdown-toggle="{dropdown_id}"
            data-dropdown-placement="{placement.value}"
            data-dropdown-trigger="{trigger_mode.value}"
            aria-expanded="false"
            aria-haspopup="true"
            aria-controls="{dropdown_id}"
            type="button"
            class="{color_classes} {size_classes} {trigger_class}">
        {trigger_label}
        <svg><!-- Dropdown chevron icon --></svg>
    </button>

    <!-- Dropdown Menu -->
    <div id="{dropdown_id}"
         role="menu"
         aria-labelledby="trigger-{dropdown_id}"
         class="z-10 hidden bg-white rounded-lg shadow {menu_class} dark:bg-gray-700">
        <ul class="py-2 text-sm text-gray-700 dark:text-gray-200">
            {rendered items}
        </ul>
    </div>
</div>
```

### Usage
```python
# Basic button dropdown
dropdown = Dropdown(
    trigger_label="Actions",
    items=[
        DropdownItem(label="Edit", href="/edit"),
        DropdownItem(label="Delete", href="/delete"),
    ]
)

# Avatar dropdown (user menu)
dropdown = Dropdown(
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

# Custom color and placement
dropdown = Dropdown(
    trigger_label="Options",
    color=Color.GREEN,
    size=Size.LG,
    placement=DropdownPlacement.TOP,
    items=[
        DropdownItem(label="Option 1"),
        DropdownItem(label="Option 2"),
    ]
)

# Hover trigger
dropdown = Dropdown(
    trigger_label="Hover Me",
    trigger_mode=DropdownTriggerMode.HOVER,
    items=[
        DropdownItem(label="Quick Action 1"),
        DropdownItem(label="Quick Action 2"),
    ]
)
```

---

## Relationships

### Composition Hierarchy
```
Dropdown
├── trigger_type (DropdownTriggerType enum)
├── trigger_mode (DropdownTriggerMode enum)
├── placement (DropdownPlacement enum)
├── color (Color enum)
├── size (Size enum)
└── items (list of:)
    ├── DropdownItem
    │   ├── icon (Icon enum, optional)
    │   └── dropdown (Dropdown, optional, for nesting)
    ├── DropdownHeader
    └── DropdownDivider
```

### Type Dependencies
- `Dropdown` → `DropdownTriggerType`, `DropdownTriggerMode`, `DropdownPlacement`, `Color`, `Size`, `DropdownItem`, `DropdownHeader`, `DropdownDivider`
- `DropdownItem` → `Icon` (from `flowbite_htmy.icons`), `Dropdown` (for nesting)

### State Management
- Visibility state managed by Flowbite JavaScript (not Python component state)
- `aria-expanded` attribute updated dynamically by Flowbite JS
- Component is stateless from htmy perspective (render only)

---

## Invariants

1. **Unique IDs**: Each dropdown instance must have a unique `dropdown_id` for ARIA relationships
2. **Item Consistency**: `items` list must not be empty
3. **Avatar Requirement**: If `trigger_type=AVATAR`, `avatar_src` must be provided
4. **Nesting Limit**: Recommended maximum 3 levels of nesting for UX
5. **Dark Mode**: All components must include `dark:` classes (always, not conditionally)

---

## Performance Considerations

- **ID Generation**: Use `id(self)` for collision-free unique IDs
- **Rendering**: Component is stateless, so rendering is O(n) where n = number of items
- **Nested Dropdowns**: Each level creates a new Dropdown instance (recursive composition)

---

## Next Steps

Proceed to API Contracts generation (component interfaces).
