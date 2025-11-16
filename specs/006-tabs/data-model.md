# Data Model: Tabs Component

**Date**: 2025-01-16
**Feature**: Tabs Component ([spec.md](./spec.md))

## Overview

The Tabs component consists of two primary entities: **Tab** (individual tab with label and content) and **Tabs** (container managing multiple tabs). Additional supporting enums provide type-safe configuration options.

---

## Entities

### Tab (Individual Tab)

Represents a single tab with its button label, optional content panel, icon, state, and HTMX attributes.

**Properties**:

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `label` | `str` | Yes | - | Tab button text (e.g., "Profile", "Dashboard") |
| `content` | `Component \| None` | No | `None` | Tab panel content (htmy Component or None for HTMX lazy loading) |
| `icon` | `Icon \| None` | No | `None` | Optional icon from Icon enum (e.g., Icon.USER, Icon.DASHBOARD) |
| `icon_position` | `IconPosition` | No | `IconPosition.LEFT` | Icon placement relative to label (LEFT or RIGHT) |
| `disabled` | `bool` | No | `False` | Whether tab is disabled (non-interactive) |
| `is_active` | `bool` | No | `False` | Whether tab is initially active (only one should be True) |
| `hx_get` | `str \| None` | No | `None` | HTMX GET request URL for lazy loading |
| `hx_post` | `str \| None` | No | `None` | HTMX POST request URL |
| `hx_trigger` | `str \| None` | No | `None` | HTMX trigger event (e.g., "revealed", "click") |
| `hx_target` | `str \| None` | No | `None` | HTMX target selector (default: self) |
| `hx_swap` | `str \| None` | No | `None` | HTMX swap strategy (e.g., "innerHTML", "outerHTML") |
| `class_` | `str` | No | `""` | Custom CSS classes merged with variant classes |

**Relationships**:
- **Belongs to**: One Tabs container
- **Has**: Zero or one content Component
- **Uses**: Zero or one Icon

**State Transitions**:
- **Active ↔ Inactive**: User clicks tab button → Flowbite JS updates `aria-selected` and shows/hides panel
- **Enabled → Disabled**: Set `disabled=True` → Renders as non-interactive `<a>` element
- **Static → Lazy-Loaded**: Provide `hx_get` → Panel content fetched on first activation

**Validation Rules**:
- `label` must not be empty string
- If `disabled=True`, `is_active` should be `False` (disabled tabs can't be active)
- If `hx_get` is provided, `content` is typically `None` (HTMX replaces it)
- `icon_position` only applies when `icon` is not None

**Examples**:

```python
# Basic static tab
Tab(label="Profile", content=html.p("Profile content"))

# Tab with left icon (default)
Tab(label="Dashboard", content=html.p("Dashboard"), icon=Icon.DASHBOARD)

# Tab with right icon
Tab(label="Settings", content=html.p("Settings"), icon=Icon.SETTINGS, icon_position=IconPosition.RIGHT)

# Disabled tab
Tab(label="Premium", disabled=True, content=html.p("Requires subscription"))

# HTMX lazy-loaded tab
Tab(label="Data", hx_get="/api/data", hx_trigger="revealed once")
```

---

### Tabs (Container)

Manages a collection of Tab objects and renders them with tablist navigation UI.

**Properties**:

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `tabs` | `list[Tab]` | Yes | - | List of Tab objects (minimum 1) |
| `variant` | `TabVariant` | No | `TabVariant.DEFAULT` | Visual style (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH) |
| `color` | `Color` | No | `Color.BLUE` | Active tab indicator color |
| `tabs_id` | `str \| None` | No | `None` | Custom ID override (default: auto-generated from id(self)) |
| `class_` | `str` | No | `""` | Custom CSS classes for tablist container |

**Derived Properties** (calculated during rendering):
- `base_id`: `tabs_id` if provided, else `f"tabs-{id(self)}"`
- `active_tab_index`: Index of first tab with `is_active=True`, or 0 if none

**Relationships**:
- **Contains**: Multiple Tab objects (1 to N)
- **Uses**: TabVariant enum for styling
- **Uses**: Color enum for active indicator

**Behavior**:
- Generates unique IDs for tablist, tabs, and panels using `base_id`
- Activates first tab by default if no tab has `is_active=True`
- Renders tablist container (`<ul role="tablist">`) with tab buttons
- Renders content container (`<div id="{base_id}-content">`) with tab panels
- Applies variant-specific classes to tablist and tab buttons
- Applies color-specific classes to active tab indicator

**Validation Rules**:
- `tabs` list must not be empty
- At most one tab should have `is_active=True` (if multiple, first wins)
- `tabs_id`, if provided, should be a valid HTML ID (alphanumeric, hyphens, underscores)

**Examples**:

```python
# Basic tabs with default variant
Tabs(tabs=[
    Tab(label="Profile", content=html.p("Profile")),
    Tab(label="Settings", content=html.p("Settings")),
])

# Underline variant with green color
Tabs(
    tabs=[...],
    variant=TabVariant.UNDERLINE,
    color=Color.GREEN,
)

# Pills variant with custom ID
Tabs(
    tabs=[...],
    variant=TabVariant.PILLS,
    tabs_id="user-tabs",
)

# Full-width variant with HTMX tabs
Tabs(
    tabs=[
        Tab(label="Overview", content=html.p("Overview")),
        Tab(label="Data", hx_get="/api/data", hx_trigger="revealed once"),
        Tab(label="Reports", hx_get="/api/reports", hx_trigger="revealed once"),
    ],
    variant=TabVariant.FULL_WIDTH,
)
```

---

## Supporting Enums

### TabVariant

Enumeration of visual styles for tabs.

**Values**:

| Value | Description | Visual Characteristics |
|-------|-------------|------------------------|
| `DEFAULT` | Border + background styling | Active tab has bg-gray-100, border-b on container |
| `UNDERLINE` | Minimal with bottom border indicator | Active tab has border-b-2, no background |
| `PILLS` | Rounded background shapes | Active tab has bg-blue-600, rounded-lg |
| `FULL_WIDTH` | Tabs stretch to fill container | Tabs have w-full, equal distribution, shadow-sm |

**Implementation**:

```python
class TabVariant(str, Enum):
    DEFAULT = "default"
    UNDERLINE = "underline"
    PILLS = "pills"
    FULL_WIDTH = "full-width"
```

---

### IconPosition

Enumeration of icon placement options relative to tab label.

**Values**:

| Value | Description | Spacing |
|-------|-------------|---------|
| `LEFT` | Icon appears to the left of label | Icon has `me-2` (margin-end) |
| `RIGHT` | Icon appears to the right of label | Icon has `ms-2` (margin-start) |

**Implementation**:

```python
class IconPosition(str, Enum):
    LEFT = "left"
    RIGHT = "right"
```

---

## Rendering Structure

### HTML Structure

```html
<!-- Tablist Container -->
<ul id="tabs-{base_id}"
    data-tabs-toggle="#tabs-{base_id}-content"
    role="tablist"
    class="[variant-specific classes] [custom classes]">

    <!-- Tab Button (enabled) -->
    <li class="me-2" role="presentation">
        <button id="tab-{base_id}-0"
                data-tabs-target="#panel-{base_id}-0"
                type="button"
                role="tab"
                aria-controls="panel-{base_id}-0"
                aria-selected="true"
                class="[variant-specific] [active/inactive] [color-specific]">
            <span class="me-2">[Icon SVG]</span>
            <span>Label</span>
        </button>
    </li>

    <!-- Tab Button (disabled) -->
    <li role="presentation">
        <a class="[variant-specific] [disabled classes]">
            Disabled Label
        </a>
    </li>
</ul>

<!-- Content Container -->
<div id="tabs-{base_id}-content">
    <!-- Tab Panel (active) -->
    <div id="panel-{base_id}-0"
         role="tabpanel"
         aria-labelledby="tab-{base_id}-0"
         class="[panel classes]">
        [Content Component]
    </div>

    <!-- Tab Panel (inactive, HTMX lazy-loaded) -->
    <div id="panel-{base_id}-1"
         role="tabpanel"
         aria-labelledby="tab-{base_id}-1"
         class="hidden"
         hx-get="/api/dashboard"
         hx-trigger="revealed once">
        Loading...
    </div>
</div>
```

### ID Generation Pattern

**Base ID**: `tabs_id` or `f"tabs-{id(self)}"`

**Derived IDs**:
- Tablist: `{base_id}` (e.g., `tabs-140234567890`)
- Content container: `{base_id}-content` (e.g., `tabs-140234567890-content`)
- Tab button i: `tab-{base_id}-{i}` (e.g., `tab-tabs-140234567890-0`)
- Panel i: `panel-{base_id}-{i}` (e.g., `panel-tabs-140234567890-0`)

### ARIA Associations

| Association | Attribute | Target |
|-------------|-----------|--------|
| Tab → Panel | `aria-controls="panel-{base_id}-{i}"` | Panel ID |
| Panel → Tab | `aria-labelledby="tab-{base_id}-{i}"` | Tab ID |
| Tablist → Content | `data-tabs-toggle="#tabs-{base_id}-content"` | Content container ID |
| Tab → Panel | `data-tabs-target="#panel-{base_id}-{i}"` | Panel ID (Flowbite) |

---

## Class Construction Logic

### Variant-Specific Classes

**DEFAULT Variant**:
- **Tablist**: `flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400`
- **Active tab**: `inline-block p-4 text-{color}-600 bg-gray-100 rounded-t-lg active dark:bg-gray-800 dark:text-{color}-500`
- **Inactive tab**: `inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300`

**UNDERLINE Variant**:
- **Outer container**: `text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700`
- **Tablist**: `flex flex-wrap -mb-px`
- **Active tab**: `inline-block p-4 text-{color}-600 border-b-2 border-{color}-600 rounded-t-lg active dark:text-{color}-500 dark:border-{color}-500`
- **Inactive tab**: `inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300`

**PILLS Variant**:
- **Tablist**: `flex flex-wrap text-sm font-medium text-center text-gray-500 dark:text-gray-400`
- **Active tab**: `inline-block px-4 py-3 text-white bg-{color}-600 rounded-lg active`
- **Inactive tab**: `inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white`

**FULL_WIDTH Variant**:
- **Tablist**: `text-sm font-medium text-center text-gray-500 rounded-lg shadow-sm flex dark:divide-gray-700 dark:text-gray-400`
- **List item**: `w-full focus-within:z-10`
- **Active tab**: `inline-block w-full p-4 text-gray-900 bg-gray-100 border-r border-gray-200 dark:border-gray-700 focus:ring-4 focus:ring-{color}-300 active focus:outline-none dark:bg-gray-700 dark:text-white`
- **Inactive tab**: `inline-block w-full p-4 bg-white border-r border-gray-200 dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-{color}-300 focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700`
- **First tab**: Add `rounded-s-lg`
- **Last tab**: Replace `border-r` with `border-s-0`, add `rounded-e-lg`

**Disabled Tab** (all variants):
- `inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500`

### Color Replacement Pattern

Use ClassBuilder or string replacement to inject color:

```python
def _get_color_classes(self, color: Color) -> dict[str, str]:
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
    c600, c500, c300 = color_map[color]
    return {
        "text": f"text-{c600} dark:text-{c500}",
        "bg": f"bg-{c600}",
        "border": f"border-{c600} dark:border-{c500}",
        "focus-ring": f"focus:ring-{c300}",
    }
```

---

## Edge Case Handling

### Empty Tabs List

**Validation**: Raise `ValueError` if `tabs` list is empty in `__post_init__` or during rendering.

```python
if not self.tabs:
    raise ValueError("Tabs component requires at least one Tab")
```

### Multiple Active Tabs

**Behavior**: If multiple tabs have `is_active=True`, activate only the first one.

```python
active_indices = [i for i, tab in enumerate(self.tabs) if tab.is_active]
active_index = active_indices[0] if active_indices else 0
```

### No Active Tabs

**Behavior**: Activate first tab by default (set `aria-selected="true"` on first tab, remove `hidden` from first panel).

### Single Tab

**Behavior**: Render full tablist UI (not just content). Users can choose tabs for semantic structure even with one tab.

### Icon Without Label

**Validation**: `label` is required (non-empty). Icon-only tabs are not supported for accessibility.

### Disabled + Active

**Validation**: If `tab.disabled=True`, ignore `is_active=True` (disabled tabs cannot be active).

```python
if tab.disabled and tab.is_active:
    # Log warning or raise error
    pass  # Treat as inactive
```

---

## Summary

- **Tab**: 11 properties (label, content, icon, icon_position, disabled, is_active, 5 HTMX attrs, class_)
- **Tabs**: 5 properties (tabs, variant, color, tabs_id, class_)
- **TabVariant**: 4 values (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH)
- **IconPosition**: 2 values (LEFT, RIGHT)
- **ID Generation**: `id(self)` + index with custom override
- **Validation**: Non-empty tabs, single active tab, non-empty labels
- **Rendering**: Tablist + content container, variant-specific classes, color customization
