# API Contract: Tabs Component

**Date**: 2025-01-16
**Feature**: Tabs Component ([spec.md](../spec.md))

## Overview

This document defines the public API contract for the Tab and Tabs components, including all props, rendering behavior, and usage examples.

---

## Tab Component API

### Signature

```python
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
```

### Props Reference

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `label` | `str` | ✅ Yes | - | Tab button text displayed to users |
| `content` | `Component \| None` | No | `None` | Tab panel content (htmy Component). Use `None` for HTMX lazy-loaded tabs |
| `icon` | `Icon \| None` | No | `None` | Optional icon from Icon enum (e.g., `Icon.USER`, `Icon.DASHBOARD`) |
| `icon_position` | `IconPosition` | No | `IconPosition.LEFT` | Icon placement: `IconPosition.LEFT` or `IconPosition.RIGHT` |
| `disabled` | `bool` | No | `False` | If `True`, tab is non-interactive and grayed out |
| `is_active` | `bool` | No | `False` | If `True`, tab is initially active (only one tab should be active) |
| `hx_get` | `str \| None` | No | `None` | HTMX GET URL for lazy loading content |
| `hx_post` | `str \| None` | No | `None` | HTMX POST URL for sending data |
| `hx_trigger` | `str \| None` | No | `None` | HTMX trigger event (e.g., `"revealed"`, `"click"`) |
| `hx_target` | `str \| None` | No | `None` | HTMX target selector (overrides default self-targeting) |
| `hx_swap` | `str \| None` | No | `None` | HTMX swap strategy (e.g., `"innerHTML"`, `"outerHTML"`) |
| `class_` | `str` | No | `""` | Custom CSS classes merged with component classes |

### Usage Examples

**Basic static tab**:
```python
Tab(label="Profile", content=html.p("User profile content"))
```

**Tab with icon (left, default)**:
```python
Tab(
    label="Dashboard",
    content=html.div(html.h2("Dashboard"), html.p("Analytics")),
    icon=Icon.DASHBOARD,
)
```

**Tab with icon (right)**:
```python
Tab(
    label="Settings",
    content=html.p("Settings content"),
    icon=Icon.SETTINGS,
    icon_position=IconPosition.RIGHT,
)
```

**Disabled tab**:
```python
Tab(label="Premium Features", disabled=True, content=html.p("Requires subscription"))
```

**HTMX lazy-loaded tab**:
```python
Tab(
    label="Reports",
    hx_get="/api/reports",
    hx_trigger="revealed once",  # Load only on first reveal
)
```

**HTMX tab with custom target**:
```python
Tab(
    label="External Data",
    hx_get="/api/external",
    hx_target="#data-container",  # Load into different element
    hx_swap="innerHTML",
)
```

---

## Tabs Component API

### Signature

```python
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

    def htmy(self, context: Context) -> Component:
        """Render tabs with tablist navigation and content panels."""
        ...
```

### Props Reference

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `tabs` | `list[Tab]` | ✅ Yes | - | List of Tab objects (minimum 1 tab required) |
| `variant` | `TabVariant` | No | `TabVariant.DEFAULT` | Visual style: `DEFAULT`, `UNDERLINE`, `PILLS`, `FULL_WIDTH` |
| `color` | `Color` | No | `Color.BLUE` | Active tab indicator color (8 options) |
| `tabs_id` | `str \| None` | No | `None` | Custom ID for tablist (default: auto-generated `tabs-{id(self)}`) |
| `class_` | `str` | No | `""` | Custom CSS classes for tablist container |

### Usage Examples

**Basic tabs (default variant)**:
```python
Tabs(tabs=[
    Tab(label="Profile", content=html.p("Profile content")),
    Tab(label="Dashboard", content=html.p("Dashboard content")),
    Tab(label="Settings", content=html.p("Settings content")),
])
```

**Underline variant with green color**:
```python
Tabs(
    tabs=[
        Tab(label="Overview", content=html.p("Overview"), is_active=True),
        Tab(label="Details", content=html.p("Details")),
    ],
    variant=TabVariant.UNDERLINE,
    color=Color.GREEN,
)
```

**Pills variant**:
```python
Tabs(
    tabs=[
        Tab(label="Tab 1", content=html.p("Content 1")),
        Tab(label="Tab 2", content=html.p("Content 2")),
        Tab(label="Tab 3", content=html.p("Content 3")),
    ],
    variant=TabVariant.PILLS,
)
```

**Full-width variant**:
```python
Tabs(
    tabs=[
        Tab(label="Profile", content=html.p("Profile")),
        Tab(label="Dashboard", content=html.p("Dashboard")),
        Tab(label="Settings", content=html.p("Settings")),
        Tab(label="Invoice", content=html.p("Invoice")),
    ],
    variant=TabVariant.FULL_WIDTH,
)
```

**Tabs with icons**:
```python
Tabs(
    tabs=[
        Tab(label="Profile", icon=Icon.USER, content=html.p("User profile")),
        Tab(label="Dashboard", icon=Icon.DASHBOARD, content=html.p("Dashboard")),
        Tab(label="Settings", icon=Icon.SETTINGS, content=html.p("Settings")),
    ],
    variant=TabVariant.UNDERLINE,
)
```

**Tabs with disabled tab**:
```python
Tabs(tabs=[
    Tab(label="Free Features", content=html.p("Available features")),
    Tab(label="Premium Features", disabled=True, content=html.p("Requires upgrade")),
])
```

**HTMX lazy-loaded tabs**:
```python
Tabs(
    tabs=[
        Tab(label="Overview", content=html.p("Static overview content")),
        Tab(label="Live Data", hx_get="/api/live-data", hx_trigger="revealed once"),
        Tab(label="Reports", hx_get="/api/reports", hx_trigger="revealed"),
    ],
    tabs_id="analytics-tabs",  # Custom ID for easier targeting
)
```

**Full example with all features**:
```python
Tabs(
    tabs=[
        Tab(
            label="Profile",
            content=html.div(
                html.h3("User Profile"),
                html.p("Manage your profile settings"),
            ),
            icon=Icon.USER,
            is_active=True,
        ),
        Tab(
            label="Dashboard",
            hx_get="/api/dashboard",
            hx_trigger="revealed once",
            icon=Icon.DASHBOARD,
            icon_position=IconPosition.RIGHT,
        ),
        Tab(
            label="Settings",
            content=html.p("Settings content"),
            icon=Icon.SETTINGS,
        ),
        Tab(
            label="Premium",
            disabled=True,
            content=html.p("Upgrade required"),
        ),
    ],
    variant=TabVariant.UNDERLINE,
    color=Color.PURPLE,
    tabs_id="user-tabs",
    class_="mt-4",
)
```

---

## Rendering Behavior

### Active Tab Selection

**Rule**: If no tab has `is_active=True`, the first tab is activated by default.

**Examples**:

```python
# No active tab specified → first tab active
Tabs(tabs=[
    Tab(label="A", content=html.p("A")),  # This will be active
    Tab(label="B", content=html.p("B")),
])

# Explicit active tab → second tab active
Tabs(tabs=[
    Tab(label="A", content=html.p("A")),
    Tab(label="B", content=html.p("B"), is_active=True),  # This is active
])

# Multiple active tabs → first active tab wins
Tabs(tabs=[
    Tab(label="A", content=html.p("A")),
    Tab(label="B", content=html.p("B"), is_active=True),  # This wins
    Tab(label="C", content=html.p("C"), is_active=True),  # Ignored
])
```

### ID Generation

**Auto-generated ID** (default):
```python
Tabs(tabs=[...])
# Generates: tabs-{id(self)} (e.g., tabs-140234567890)
# Tab IDs: tab-tabs-140234567890-0, tab-tabs-140234567890-1, ...
# Panel IDs: panel-tabs-140234567890-0, panel-tabs-140234567890-1, ...
```

**Custom ID**:
```python
Tabs(tabs=[...], tabs_id="user-tabs")
# Tablist ID: user-tabs
# Tab IDs: tab-user-tabs-0, tab-user-tabs-1, ...
# Panel IDs: panel-user-tabs-0, panel-user-tabs-1, ...
```

### HTMX Attribute Placement

HTMX attributes from Tab are applied to the panel `<div>`, **not** the tab button.

**Example**:
```python
Tab(label="Data", hx_get="/api/data", hx_trigger="revealed")
```

**Renders as**:
```html
<!-- Button: No HTMX attributes -->
<button id="tab-user-tabs-1"
        data-tabs-target="#panel-user-tabs-1"
        type="button"
        role="tab">
    Data
</button>

<!-- Panel: HTMX attributes here -->
<div id="panel-user-tabs-1"
     role="tabpanel"
     hx-get="/api/data"
     hx-trigger="revealed"
     class="hidden">
    Loading...
</div>
```

### Disabled Tab Rendering

Disabled tabs render as `<a>` elements (not `<button>`) without `href`, making them non-interactive.

**Example**:
```python
Tab(label="Premium", disabled=True)
```

**Renders as**:
```html
<li role="presentation">
    <a class="inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500">
        Premium
    </a>
</li>
```

---

## Variant-Specific Examples

### DEFAULT Variant

```python
Tabs(
    tabs=[
        Tab(label="Profile", content=html.p("Profile"), is_active=True),
        Tab(label="Dashboard", content=html.p("Dashboard")),
        Tab(label="Settings", content=html.p("Settings")),
    ],
    variant=TabVariant.DEFAULT,  # This is default, can be omitted
)
```

**Visual**: Border on bottom of tablist, active tab has gray background.

### UNDERLINE Variant

```python
Tabs(
    tabs=[
        Tab(label="Overview", content=html.p("Overview")),
        Tab(label="Analytics", content=html.p("Analytics"), is_active=True),
    ],
    variant=TabVariant.UNDERLINE,
)
```

**Visual**: No background, active tab has 2px bottom border in blue (or custom color).

### PILLS Variant

```python
Tabs(
    tabs=[
        Tab(label="Tab 1", content=html.p("Content 1")),
        Tab(label="Tab 2", content=html.p("Content 2")),
        Tab(label="Tab 3", content=html.p("Content 3")),
    ],
    variant=TabVariant.PILLS,
    color=Color.GREEN,
)
```

**Visual**: Rounded pill buttons, active tab has solid green background with white text.

### FULL_WIDTH Variant

```python
Tabs(
    tabs=[
        Tab(label="Profile", content=html.p("Profile")),
        Tab(label="Dashboard", content=html.p("Dashboard")),
        Tab(label="Settings", content=html.p("Settings")),
        Tab(label="Invoice", content=html.p("Invoice")),
    ],
    variant=TabVariant.FULL_WIDTH,
)
```

**Visual**: Tabs stretch to fill container width equally, rounded corners on ends, shadow effect.

---

## Color Options

All 8 Color enum values are supported:

```python
# Blue (default)
Tabs(tabs=[...], color=Color.BLUE)

# Green
Tabs(tabs=[...], color=Color.GREEN)

# Red
Tabs(tabs=[...], color=Color.RED)

# Yellow
Tabs(tabs=[...], color=Color.YELLOW)

# Purple
Tabs(tabs=[...], color=Color.PURPLE)

# Pink
Tabs(tabs=[...], color=Color.PINK)

# Indigo
Tabs(tabs=[...], color=Color.INDIGO)

# Gray
Tabs(tabs=[...], color=Color.GRAY)
```

**Effect**: Color applies to active tab indicator (text, background, or border depending on variant).

---

## HTMX Integration Patterns

### Lazy Loading on First Reveal

```python
Tab(
    label="Reports",
    hx_get="/api/reports",
    hx_trigger="revealed once",  # Only loads first time
)
```

**Behavior**: Content loads when tab is first activated, then cached.

### Reload on Every Reveal

```python
Tab(
    label="Live Data",
    hx_get="/api/live-data",
    hx_trigger="revealed",  # Reloads every time
)
```

**Behavior**: Content reloads every time tab is activated (fresh data).

### Custom Trigger

```python
Tab(
    label="Search Results",
    hx_get="/api/search",
    hx_trigger="click from:#search-btn",  # Load when external button clicked
)
```

**Behavior**: Content loads when specified element is clicked.

### Custom Target

```python
Tab(
    label="Sidebar Content",
    hx_get="/api/sidebar",
    hx_target="#sidebar",  # Load into different element
    hx_swap="innerHTML",
)
```

**Behavior**: Content loads into specified target element instead of tab panel.

---

## Accessibility (ARIA)

### Generated ARIA Structure

```html
<!-- Tablist -->
<ul id="tabs-123"
    data-tabs-toggle="#tabs-123-content"
    role="tablist">

    <!-- Tab Button -->
    <li role="presentation">
        <button id="tab-tabs-123-0"
                data-tabs-target="#panel-tabs-123-0"
                type="button"
                role="tab"
                aria-controls="panel-tabs-123-0"
                aria-selected="true">
            Profile
        </button>
    </li>
</ul>

<!-- Content Container -->
<div id="tabs-123-content">
    <!-- Tab Panel -->
    <div id="panel-tabs-123-0"
         role="tabpanel"
         aria-labelledby="tab-tabs-123-0">
        Content here
    </div>
</div>
```

### Screen Reader Announcements

- **Tablist**: "Tab list with 3 tabs"
- **Active tab**: "Profile, tab, selected, 1 of 3"
- **Inactive tab**: "Dashboard, tab, 2 of 3"
- **Disabled tab**: "Premium, unavailable"
- **Tab panel**: "Profile, tab panel"

### Keyboard Navigation

- **Tab**: Move focus to tablist, then to next focusable element outside tabs
- **Arrow Left/Right**: Navigate between tabs (Flowbite JS)
- **Home**: Focus first tab (Flowbite JS)
- **End**: Focus last tab (Flowbite JS)
- **Enter/Space**: Activate focused tab (Flowbite JS)

---

## Custom Classes

### Adding Custom Classes to Tablist

```python
Tabs(
    tabs=[...],
    class_="mt-8 mb-4 shadow-lg",  # Added to tablist container
)
```

**Result**: Classes merged with variant classes via `ClassBuilder.merge()`.

### Adding Custom Classes to Individual Tabs

```python
Tab(
    label="Important",
    content=html.p("Important content"),
    class_="font-bold",  # Added to this tab button
)
```

**Result**: `font-bold` merged with tab button classes.

---

## Edge Cases

### Empty Tabs List

```python
Tabs(tabs=[])  # ❌ Raises ValueError
```

**Error**: `ValueError: Tabs component requires at least one Tab`

### Single Tab

```python
Tabs(tabs=[Tab(label="Only Tab", content=html.p("Content"))])  # ✅ Valid
```

**Behavior**: Renders full tablist UI (not just content). User may want semantic tabs structure.

### All Tabs Disabled

```python
Tabs(tabs=[
    Tab(label="A", disabled=True),
    Tab(label="B", disabled=True),
])  # ✅ Valid but unusual
```

**Behavior**: No active tab (all tabs are non-interactive). First panel is still shown.

### Empty Label

```python
Tab(label="", content=html.p("Content"))  # ❌ Should raise ValueError
```

**Error**: `ValueError: Tab label must not be empty`

---

## Complete FastAPI Example

```python
from fastapi import FastAPI
from fasthx import Jinja
from flowbite_htmy.components import Tabs, Tab, TabVariant, IconPosition
from flowbite_htmy.types import Color
from flowbite_htmy.icons import Icon
from htmy import html

app = FastAPI()
jinja = Jinja(app)

@jinja.page("/")
async def index():
    tabs = Tabs(
        tabs=[
            Tab(
                label="Profile",
                content=html.div(
                    html.h3("User Profile", class_="text-xl font-bold mb-2"),
                    html.p("Manage your account settings"),
                ),
                icon=Icon.USER,
                is_active=True,
            ),
            Tab(
                label="Dashboard",
                hx_get="/api/dashboard",
                hx_trigger="revealed once",
                icon=Icon.DASHBOARD,
            ),
            Tab(
                label="Settings",
                content=html.p("Settings panel"),
                icon=Icon.SETTINGS,
                icon_position=IconPosition.RIGHT,
            ),
            Tab(
                label="Premium",
                disabled=True,
                content=html.p("Upgrade to access premium features"),
            ),
        ],
        variant=TabVariant.UNDERLINE,
        color=Color.PURPLE,
        tabs_id="user-tabs",
    )

    return {"title": "Tabs Demo", "tabs": tabs}

@app.get("/api/dashboard")
async def dashboard_content():
    return html.div(
        html.h3("Dashboard", class_="text-xl font-bold mb-2"),
        html.p("Analytics and metrics loaded dynamically via HTMX"),
    )
```

---

## Summary

- **Tab Component**: 11 props (label, content, icon, icon_position, disabled, is_active, 5 HTMX attrs, class_)
- **Tabs Component**: 5 props (tabs, variant, color, tabs_id, class_)
- **4 Variants**: DEFAULT, UNDERLINE, PILLS, FULL_WIDTH
- **8 Colors**: BLUE (default), GREEN, RED, YELLOW, PURPLE, PINK, INDIGO, GRAY
- **HTMX Support**: Full support for lazy loading with revealed trigger
- **Accessibility**: Complete ARIA implementation with keyboard navigation
- **ID Generation**: Auto-generated or custom override
- **Disabled Tabs**: Non-interactive, visually distinct, excluded from keyboard nav
