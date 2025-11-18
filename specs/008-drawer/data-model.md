# Data Model: Drawer Component

**Feature**: 008-drawer
**Date**: 2025-11-18
**Purpose**: Define entities, types, and relationships for Drawer component

## Overview

The Drawer component is a stateless UI component rendered server-side. It has no persistent data model or database entities. This document describes the Python dataclass structure and type definitions used for type-safe component instantiation.

## Entities

### DrawerPlacement (Enum)

Type-safe enumeration for drawer positioning.

**Purpose**: Prevent invalid placement values, provide IDE autocomplete, enable type checking

**Definition**:
```python
class DrawerPlacement(str, Enum):
    """Drawer placement positions for edge positioning."""
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
```

**Attributes**:
| Value | String | Description |
|-------|--------|-------------|
| LEFT | "left" | Drawer slides from left edge (default) |
| RIGHT | "right" | Drawer slides from right edge |
| TOP | "top" | Drawer slides from top edge |
| BOTTOM | "bottom" | Drawer slides from bottom edge |

**Validation**: Enum constraint ensures only valid placement values

**Relationships**: Used by Drawer.placement prop

---

### Drawer (Component)

Main component class representing drawer UI element.

**Purpose**: Encapsulate drawer structure, animations, ARIA attributes, and Flowbite integration

**Definition**:
```python
@dataclass(frozen=True, kw_only=True)
class Drawer:
    """
    Off-canvas panel that slides in from screen edge.

    Supports navigation menus, forms, settings panels with full
    ARIA accessibility and HTMX integration.
    """

    # Required props
    trigger_label: str  # Text for trigger button
    content: Component  # Drawer body content (forms, nav, etc.)

    # Optional configuration
    placement: DrawerPlacement = DrawerPlacement.LEFT  # Edge position
    backdrop: bool = True  # Show dimming overlay
    body_scrolling: bool = False  # Allow background page scroll
    edge: bool = False  # Show visible tab when closed

    # Customization
    trigger_color: Color = Color.PRIMARY  # Trigger button color
    trigger_size: Size = Size.MD  # Trigger button size
    drawer_id: str | None = None  # Unique ID (auto-generated if None)

    # Styling
    width: str = "w-80"  # Width for left/right (Tailwind class)
    height: str = "h-1/2"  # Height for top/bottom (Tailwind class)
    class_: str = ""  # Additional CSS classes
    trigger_class: str = ""  # Trigger button CSS classes

    # HTMX attributes (for dynamic content)
    hx_get: str | None = None
    hx_post: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render drawer with trigger, panel, and optional backdrop."""
        ...
```

**Attributes**:

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `trigger_label` | `str` | Yes | - | Text displayed on trigger button |
| `content` | `Component` | Yes | - | htmy component(s) rendered inside drawer |
| `placement` | `DrawerPlacement` | No | `LEFT` | Edge from which drawer slides |
| `backdrop` | `bool` | No | `True` | Whether to show semi-transparent overlay |
| `body_scrolling` | `bool` | No | `False` | Whether background page can scroll |
| `edge` | `bool` | No | `False` | Show visible tab when drawer closed |
| `trigger_color` | `Color` | No | `PRIMARY` | Color variant for trigger button |
| `trigger_size` | `Size` | No | `MD` | Size variant for trigger button |
| `drawer_id` | `str \| None` | No | `None` | Unique ID (auto-generated UUID if None) |
| `width` | `str` | No | `"w-80"` | Width class for LEFT/RIGHT placements |
| `height` | `str` | No | `"h-1/2"` | Height class for TOP/BOTTOM placements |
| `class_` | `str` | No | `""` | Additional CSS classes for drawer panel |
| `trigger_class` | `str` | No | `""` | Additional CSS classes for trigger button |
| `hx_get` | `str \| None` | No | `None` | HTMX GET URL for dynamic content |
| `hx_post` | `str \| None` | No | `None` | HTMX POST URL for dynamic content |
| `hx_target` | `str \| None` | No | `None` | HTMX target selector |
| `hx_swap` | `str \| None` | No | `None` | HTMX swap strategy |

**Validation Rules**:
- `trigger_label` must be non-empty string
- `content` must be valid htmy Component
- `placement` must be valid DrawerPlacement enum value
- `drawer_id` must be unique across page if specified (developer responsibility)
- Tailwind classes in `width`/`height` must be valid (not validated at runtime)

**State Transitions**:
- Drawer has no internal state (stateless component)
- Visibility state managed by Flowbite JavaScript based on user interactions
- Open/close transitions handled via CSS transform classes

**Relationships**:
- Uses `DrawerPlacement` enum for type-safe positioning
- Uses `Color` enum (existing) for trigger button color
- Uses `Size` enum (existing) for trigger button size
- Uses `ThemeContext` (existing) for dark mode support
- Uses `ClassBuilder` (existing) for CSS class construction
- Uses `get_icon()` (existing) for close button icon

---

## Type Definitions

### Component Props Type Map

| Prop | Python Type | HTML Output | Validation |
|------|-------------|-------------|------------|
| `trigger_label` | `str` | Button text content | Non-empty |
| `content` | `Component` | Drawer body HTML | htmy Component |
| `placement` | `DrawerPlacement` | `data-drawer-placement="left"` | Enum values only |
| `backdrop` | `bool` | Renders/omits backdrop `<div>` | True/False |
| `body_scrolling` | `bool` | JavaScript config (not HTML attr) | True/False |
| `edge` | `bool` | Renders/omits edge tab `<button>` | True/False |
| `trigger_color` | `Color` | Button CSS classes | Color enum values |
| `trigger_size` | `Size` | Button CSS classes | Size enum values |
| `drawer_id` | `str \| None` | `id="{drawer_id}"` attribute | Unique string or None |
| `width` | `str` | CSS class in drawer panel | Tailwind class string |
| `height` | `str` | CSS class in drawer panel | Tailwind class string |
| `class_` | `str` | Merged into drawer panel classes | Any string |
| `trigger_class` | `str` | Merged into trigger button classes | Any string |
| `hx_get` | `str \| None` | `hx-get="{url}"` attribute | URL string or None |
| `hx_post` | `str \| None` | `hx-post="{url}"` attribute | URL string or None |
| `hx_target` | `str \| None` | `hx-target="{selector}"` attribute | CSS selector or None |
| `hx_swap` | `str \| None` | `hx-swap="{strategy}"` attribute | HTMX swap value or None |

---

## HTML Structure

**Rendered Output** (conceptual, not actual HTML):

```html
<!-- Trigger Button -->
<button
  data-drawer-target="drawer-{id}"
  data-drawer-show="drawer-{id}"
  class="... {trigger_color} {trigger_size} {trigger_class}">
  {trigger_label}
</button>

<!-- Optional Edge Tab (if edge=True) -->
<button
  data-drawer-show="drawer-{id}"
  class="fixed ... {placement-specific-positioning}">
  › <!-- Arrow icon -->
</button>

<!-- Backdrop (if backdrop=True) -->
<div
  data-drawer-backdrop="drawer-{id}"
  data-drawer-hide="drawer-{id}"
  aria-hidden="true"
  class="fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80">
</div>

<!-- Drawer Panel -->
<div
  id="drawer-{id}"
  tabindex="-1"
  aria-labelledby="drawer-{id}-label"
  aria-hidden="true"
  data-drawer-placement="{placement}"
  class="fixed z-40 {placement-transform} {width|height}
         max-h-screen transition-transform {class_}"
  hx-get="{hx_get}"
  hx-post="{hx_post}"
  hx-target="{hx_target}"
  hx-swap="{hx_swap}">

  <!-- Header (non-scrolling) -->
  <div class="flex items-center justify-between p-4 border-b
              border-gray-200 dark:border-gray-700">
    <h5 id="drawer-{id}-label" class="...">
      Drawer Title
    </h5>
    <button
      data-drawer-hide="drawer-{id}"
      class="...">
      <svg><!-- Close icon --></svg>
    </button>
  </div>

  <!-- Body (scrollable) -->
  <div class="p-4 overflow-y-auto">
    {content}  <!-- User-provided content here -->
  </div>
</div>
```

---

## Constraints

**Performance**:
- Component rendering must complete in <100ms
- CSS transform animations complete within 300ms (specified in Success Criteria)
- No runtime performance cost (stateless component, no state tracking)

**Accessibility**:
- Must include ARIA attributes: `aria-labelledby`, `aria-hidden`, `tabindex="-1"`
- Focus trap enabled by Flowbite JavaScript (Tab/Shift+Tab cycle through drawer elements)
- Escape key closes drawer and returns focus to trigger
- Screen readers announce drawer state changes

**Browser Compatibility**:
- Tailwind CSS 3.4.0 browser support (modern browsers, no IE11)
- Flowbite JavaScript 2.5.1 browser support
- HTMX 2.0.2 browser support (if using dynamic content features)

**Scope Limits**:
- Maximum one drawer visible at a time (auto-close previous on new open)
- Internal content height constraint: 5000px scroll limit (from SC-008)
- Debouncing: ignores clicks during 300ms animation (Flowbite built-in)

---

## Data Flow

**Component Instantiation → HTML Rendering**:

1. Developer creates Drawer instance in Python:
   ```python
   drawer = Drawer(
       trigger_label="Open Menu",
       content=html.div("Menu content"),
       placement=DrawerPlacement.LEFT,
       backdrop=True,
   )
   ```

2. FastAPI route renders component:
   ```python
   html_output = await renderer.render(drawer)
   ```

3. htmy calls `drawer.htmy(context)` method:
   - Retrieves ThemeContext for dark mode
   - Generates unique `drawer_id` if not provided
   - Builds CSS classes using ClassBuilder
   - Constructs HTML structure with data attributes
   - Returns Component tree

4. HTML sent to browser with Flowbite JS included

5. Flowbite JavaScript initializes drawer:
   - Attaches click handlers to triggers
   - Sets up Escape key listener
   - Configures focus trap
   - Manages transform classes for animations

6. User interactions trigger state changes (open/close)

**HTMX Integration Flow** (optional):

1. Drawer content includes HTMX attributes:
   ```python
   Drawer(
       trigger_label="Filters",
       content=html.div("...", hx_get="/api/filters"),
       hx_target="#main-content",
   )
   ```

2. User interaction triggers HTMX request

3. Server responds with HTML and optional `HX-Trigger: close-drawer-{id}` header

4. HTMX swaps content and triggers custom event

5. Event listener closes drawer if header present

---

## Testing Considerations

**Unit Tests** (pytest):
- Test drawer renders with all placement variants
- Test backdrop rendering (enabled/disabled)
- Test edge tab rendering (enabled/disabled)
- Test ARIA attributes present and correct
- Test data attributes for Flowbite integration
- Test dark mode classes included
- Test custom CSS class merging
- Test HTMX attribute passthrough
- Test unique ID generation

**Snapshot Tests** (syrupy):
- Snapshot HTML output for each placement
- Snapshot with/without backdrop
- Snapshot with/without edge tab
- Snapshot dark mode rendering

**Integration Tests** (showcase app):
- Test focus trap behavior (manual browser testing)
- Test Escape key closes drawer
- Test click-outside closes drawer
- Test auto-close on multiple drawers
- Test debouncing during rapid clicks
- Test internal scrolling with long content
- Test HTMX form submission and closure

No database, API contracts, or external data sources required for this component.
