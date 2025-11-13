# Data Model: Consolidated Component Showcase Application

**Date**: 2025-11-13
**Feature**: Consolidated Component Showcase
**Purpose**: Define data structures for routes, navigation, and showcase organization

---

## Overview

The consolidated showcase application uses simple data structures to organize component routes, navigation state, and showcase content. Since this is a read-only showcase (no persistence), all data structures are runtime dictionaries and type-annotated for clarity.

---

## 1. ComponentRoute

**Purpose**: Define metadata for each component showcase page route.

**Structure**:
```python
ComponentRoute = TypedDict("ComponentRoute", {
    "name": str,          # URL-safe component name (e.g., "buttons")
    "path": str,          # Full URL path (e.g., "/buttons")
    "title": str,         # Display name (e.g., "Buttons")
    "description": str,   # Short description for homepage
    "order": int,         # Display order in navigation (1-10)
})
```

**Example**:
```python
{
    "name": "buttons",
    "path": "/buttons",
    "title": "Buttons",
    "description": "Interactive buttons with colors, sizes, and icons",
    "order": 1
}
```

**Usage**:
- Define all 10 component routes in a global constant
- Used to generate navigation menu and homepage component gallery
- Provides single source of truth for all route metadata

**Full Definition**:
```python
COMPONENT_ROUTES: list[ComponentRoute] = [
    {
        "name": "buttons",
        "path": "/buttons",
        "title": "Buttons",
        "description": "Interactive buttons with colors, sizes, variants, and icons",
        "order": 1,
    },
    {
        "name": "badges",
        "path": "/badges",
        "title": "Badges",
        "description": "Labels and indicators with color variants",
        "order": 2,
    },
    {
        "name": "alerts",
        "path": "/alerts",
        "title": "Alerts",
        "description": "Notification messages with dismissible option",
        "order": 3,
    },
    {
        "name": "avatars",
        "path": "/avatars",
        "title": "Avatars",
        "description": "User profile pictures with placeholders",
        "order": 4,
    },
    {
        "name": "cards",
        "path": "/cards",
        "title": "Cards",
        "description": "Content containers with images and titles",
        "order": 5,
    },
    {
        "name": "checkboxes",
        "path": "/checkboxes",
        "title": "Checkboxes",
        "description": "Checkboxes with labels and validation states",
        "order": 6,
    },
    {
        "name": "inputs",
        "path": "/inputs",
        "title": "Inputs",
        "description": "Text input fields with validation",
        "order": 7,
    },
    {
        "name": "modals",
        "path": "/modals",
        "title": "Modals",
        "description": "Dialog boxes and popups",
        "order": 8,
    },
    {
        "name": "paginations",
        "path": "/paginations",
        "title": "Paginations",
        "description": "Page navigation with info text",
        "order": 9,
    },
    {
        "name": "selects",
        "path": "/selects",
        "title": "Selects",
        "description": "Dropdown selection fields",
        "order": 10,
    },
]
```

---

## 2. NavigationItem

**Purpose**: Represent a single navigation menu item with active state.

**Structure**:
```python
NavigationItem = TypedDict("NavigationItem", {
    "label": str,          # Display text (e.g., "Buttons")
    "url": str,            # Target URL (e.g., "/buttons")
    "is_active": bool,     # Whether this is the current page
})
```

**Example** (on `/buttons` page):
```python
{
    "label": "Buttons",
    "url": "/buttons",
    "is_active": True
}
```

**Usage**:
- Generated dynamically for each page request
- Used to render navigation menu with active state highlighting
- Transformed into Button components with conditional styling

**Generation Logic**:
```python
def build_navigation_items(current_page: str) -> list[NavigationItem]:
    """Generate navigation items with active state for current page."""
    return [
        {
            "label": route["title"],
            "url": route["path"],
            "is_active": route["name"] == current_page
        }
        for route in COMPONENT_ROUTES
    ]
```

---

## 3. PageContext

**Purpose**: Template context data passed to Jinja for rendering each page.

**Structure**:
```python
PageContext = TypedDict("PageContext", {
    "current_page": str,        # Current page name (e.g., "buttons")
    "title": str,               # Page title for <title> tag
    "navigation": str,          # Rendered navigation HTML (from htmy)
    "content": str,             # Rendered showcase content HTML (from htmy)
})
```

**Example**:
```python
{
    "current_page": "buttons",
    "title": "Buttons - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",  # Rendered htmy navigation
    "content": "<div>...</div>"       # Rendered htmy showcase content
}
```

**Usage**:
- Returned from each route handler
- Passed to `showcase-layout.html.jinja` template
- Provides all data needed for page rendering

---

## 4. ShowcaseSection (Optional - Not Used in MVP)

**Purpose**: Logical grouping of examples within a component page.

**Note**: This structure is **not required for MVP** since existing showcase functions already organize content internally. Included here for completeness and potential future refactoring.

**Structure**:
```python
ShowcaseSection = TypedDict("ShowcaseSection", {
    "title": str,              # Section title (e.g., "Default Buttons")
    "description": str,        # Section description
    "content": Component,      # htmy component with examples
    "order": int,              # Display order within page
})
```

**Example**:
```python
{
    "title": "Default Buttons",
    "description": "Basic button styles with multiple colors",
    "content": html.div(...),  # htmy component
    "order": 1
}
```

---

## Data Flow Diagram

```
User Request → FastAPI Route Handler
                   ↓
            1. Determine current page
                   ↓
            2. Build navigation items (list[NavigationItem])
                   ↓
            3. Render navigation with htmy (→ HTML string)
                   ↓
            4. Call showcase function (e.g., build_buttons_showcase())
                   ↓
            5. Render showcase content with htmy (→ HTML string)
                   ↓
            6. Assemble PageContext dict
                   ↓
            7. Return to fasthx/Jinja
                   ↓
            8. Render showcase-layout.html.jinja
                   ↓
            Final HTML Response → User
```

---

## Type Definitions File

Create `examples/showcase_types.py`:

```python
"""Type definitions for consolidated showcase application."""

from typing import TypedDict


class ComponentRoute(TypedDict):
    """Metadata for a component showcase page route."""
    name: str
    path: str
    title: str
    description: str
    order: int


class NavigationItem(TypedDict):
    """Navigation menu item with active state."""
    label: str
    url: str
    is_active: bool


class PageContext(TypedDict):
    """Template context data for page rendering."""
    current_page: str
    title: str
    navigation: str
    content: str
```

---

## Validation Rules

### ComponentRoute Validation
- **name**: Must be URL-safe (lowercase, hyphens allowed, no spaces)
- **path**: Must start with `/`, match pattern `/[a-z-]+`
- **title**: User-facing string, can contain spaces and capitals
- **description**: Short text (~50-100 chars), no line breaks
- **order**: Positive integer, unique across all routes

### NavigationItem Validation
- **label**: Non-empty string
- **url**: Must be valid path (matches one of COMPONENT_ROUTES)
- **is_active**: Boolean, exactly one item per page should be True

### PageContext Validation
- **current_page**: Must match one of COMPONENT_ROUTES names
- **title**: Non-empty string for browser tab
- **navigation**: Valid HTML string (rendered from htmy)
- **content**: Valid HTML string (rendered from htmy)

---

## State Management

**No Server-Side State Required**:
- All data is computed per-request from COMPONENT_ROUTES constant
- Navigation active state derived from current request path
- No database, no caching, no session management
- Dark mode state managed client-side via localStorage (inherited from base.html.jinja)

**Stateless Benefits**:
- Simple to understand and maintain
- No state synchronization issues
- Easy to test (pure functions)
- Fast response times (no DB queries)
- Horizontally scalable (if needed)

---

## Future Enhancements (Out of Scope for MVP)

If the showcase grows in complexity, consider:

1. **Component Metadata Model**: Add tags, categories, complexity rating to ComponentRoute
2. **Search Index**: Build search data structure for component filtering
3. **Showcase Sections**: Formalize ShowcaseSection structure for consistent rendering
4. **Analytics Events**: Track which components are most viewed (client-side tracking)
5. **Code Examples**: Add code snippet data structure for copy-paste examples

For MVP, the simple structures above are sufficient.
