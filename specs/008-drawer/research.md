# Research: Drawer Component

**Feature**: 008-drawer
**Date**: 2025-11-18
**Purpose**: Resolve technical unknowns and establish implementation patterns for Drawer component

## Research Tasks

### 1. Flowbite Drawer Implementation Pattern

**Question**: How does Flowbite implement drawer positioning, animations, and state management?

**Decision**: Use Flowbite's data attribute pattern with JavaScript initialization

**Rationale**:
- Flowbite uses `data-drawer-*` attributes for declarative configuration
- Drawer positioning controlled via `data-drawer-placement` (top, right, bottom, left)
- Visibility toggled via `data-drawer-target`, `data-drawer-show`, `data-drawer-hide`, `data-drawer-toggle`
- JavaScript manages transitions, backdrop click handling, and Escape key behavior
- CSS transforms handle slide animations (translateX for left/right, translateY for top/bottom)

**Alternatives Considered**:
- Pure CSS approach (rejected: no state management for multiple drawers, complex focus trap)
- Custom JavaScript (rejected: reinventing Flowbite's tested patterns, breaks consistency with other components)

**Implementation Pattern**:
```python
# Drawer trigger button
html.button(
    "Open Drawer",
    data_drawer_target=drawer_id,
    data_drawer_show=drawer_id,
)

# Drawer panel
html.div(
    # ... content ...,
    id=drawer_id,
    class_="fixed z-40 transition-transform",
    data_drawer_placement="left",  # or right, top, bottom
    aria_labelledby=f"{drawer_id}-label",
)
```

---

### 2. Focus Trap Implementation Strategy

**Question**: How to implement focus trap (Tab/Shift+Tab cycling) for drawer accessibility?

**Decision**: Rely on Flowbite JavaScript focus management with ARIA attributes

**Rationale**:
- Flowbite's drawer JavaScript includes built-in focus trap functionality
- Uses `aria-hidden="true"` on drawer when closed to hide from screen readers
- Automatically manages focus on open/close (focuses first interactive element on open, returns focus to trigger on close)
- Prevents Tab/Shift+Tab from reaching background elements when drawer is open
- Aligns with WAI-ARIA authoring practices for modal dialogs

**Alternatives Considered**:
- Custom JavaScript focus trap (rejected: duplicates Flowbite functionality, adds maintenance burden)
- No focus trap (rejected: violates accessibility best practices and clarification decision)
- Python-side focus management (rejected: focus is runtime browser behavior, not server-side concern)

**Implementation Pattern**:
```python
# Drawer panel with ARIA attributes for focus management
html.div(
    content,
    id=drawer_id,
    tabindex="-1",  # Makes drawer programmatically focusable
    aria_hidden="true",  # Hidden by default, Flowbite JS toggles
    aria_labelledby=f"{drawer_id}-label",
    class_="...",
)
```

---

### 3. Viewport Constraint and Internal Scrolling

**Question**: How to constrain drawer height to viewport with internal scrolling?

**Decision**: Use `max-h-screen` Tailwind class with `overflow-y-auto` on drawer body

**Rationale**:
- Tailwind's `max-h-screen` constrains to 100vh (viewport height)
- `overflow-y-auto` enables scrolling only when content exceeds height
- Drawer structure: fixed header (close button) + scrollable body + optional footer
- Keeps close button always visible (critical for accessibility and UX)
- Flowbite's default drawer CSS already supports this pattern

**Alternatives Considered**:
- Fixed height drawers (rejected: doesn't adapt to different viewport sizes)
- JavaScript viewport calculation (rejected: unnecessary complexity, CSS handles this natively)
- Full-height scrolling drawer (rejected: close button scrolls out of view, poor UX)

**Implementation Pattern**:
```python
html.div(
    # Drawer container - fixed positioning
    html.div(
        # Header with close button (non-scrolling)
        html.div(..., class_="flex items-center justify-between p-4"),
        # Body content (scrollable)
        html.div(drawer_content, class_="p-4 overflow-y-auto"),
        # Optional footer (non-scrolling)
    ),
    class_="fixed ... max-h-screen",  # Constrain to viewport
)
```

---

### 4. Placement-Specific Transform Classes

**Question**: What CSS transform classes are needed for each drawer placement?

**Decision**: Use Flowbite's placement-specific transform patterns

**Rationale**:
- **LEFT** placement: `left-0 top-0 -translate-x-full` (closed) → `translate-x-0` (open)
- **RIGHT** placement: `right-0 top-0 translate-x-full` (closed) → `translate-x-0` (open)
- **TOP** placement: `top-0 left-0 -translate-y-full` (closed) → `translate-y-0` (open)
- **BOTTOM** placement: `bottom-0 left-0 translate-y-full` (closed) → `translate-y-0` (open)
- Flowbite JavaScript adds/removes transform classes to trigger CSS transitions
- Consistent with Flowbite design system and existing animation patterns

**Alternatives Considered**:
- Custom animation keyframes (rejected: Flowbite uses transforms, consistency important)
- Opacity-only animations (rejected: doesn't provide spatial context of drawer origin)
- JavaScript-based animations (rejected: CSS transitions are more performant and declarative)

**Implementation Pattern**:
```python
PLACEMENT_CLASSES = {
    DrawerPlacement.LEFT: "left-0 top-0 h-screen -translate-x-full",
    DrawerPlacement.RIGHT: "right-0 top-0 h-screen translate-x-full",
    DrawerPlacement.TOP: "top-0 left-0 w-full -translate-y-full",
    DrawerPlacement.BOTTOM: "bottom-0 left-0 w-full translate-y-full",
}
```

---

### 5. HTMX Drawer Closure Integration

**Question**: How to support server-controlled drawer closure via HTMX responses?

**Decision**: Use HTMX's HX-Trigger response header with custom event listener

**Rationale**:
- Server sends `HX-Trigger: close-drawer-{drawer_id}` header on successful form submission
- HTMX triggers custom JavaScript event on client
- Event listener calls Flowbite's drawer hide method
- Provides flexibility: developers choose per-endpoint whether to close drawer
- Aligns with HTMX philosophy of server-driven UI updates

**Alternatives Considered**:
- Always auto-close on any HTMX response (rejected: violates clarification decision, inflexible)
- Client-side only control (rejected: server can't influence UI state)
- Return HTML with JavaScript to close drawer (rejected: mixes concerns, less declarative)

**Implementation Pattern**:
```python
# Client-side (in Jinja template):
# <script>
#   document.body.addEventListener('close-drawer-example', () => {
#     const drawer = FlowbiteInstances.getInstance('Drawer', 'drawer-example');
#     drawer.hide();
#   });
# </script>

# Server-side (FastAPI endpoint):
from fastapi import Response
response = Response(content="<div>Success!</div>")
response.headers["HX-Trigger"] = "close-drawer-example"
return response
```

---

### 6. Multiple Drawer Auto-Close Behavior

**Question**: How to automatically close previous drawer when opening a new one?

**Decision**: Rely on Flowbite JavaScript's built-in singleton behavior per drawer instance

**Rationale**:
- Each drawer is a separate Flowbite instance with unique ID
- Flowbite JavaScript manages visibility state per instance
- When drawer opens, previous drawer must be explicitly closed
- Component doesn't need special logic - Flowbite's `data-drawer-show` handles this
- Alternative: add custom JavaScript to listen for drawer show events and close others

**Alternatives Considered**:
- Track open drawer globally in Python (rejected: state is runtime browser concern)
- Custom JavaScript coordinator (selected: needed to meet clarification requirement)
- Allow multiple drawers simultaneously (rejected: violates clarification decision)

**Implementation Pattern**:
```javascript
// In showcase Jinja template - custom auto-close behavior
document.addEventListener('DOMContentLoaded', () => {
  let currentDrawer = null;

  document.querySelectorAll('[data-drawer-show]').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const targetId = trigger.getAttribute('data-drawer-show');
      if (currentDrawer && currentDrawer !== targetId) {
        const prevDrawer = FlowbiteInstances.getInstance('Drawer', currentDrawer);
        if (prevDrawer) prevDrawer.hide();
      }
      currentDrawer = targetId;
    });
  });
});
```

---

### 7. Animation Debouncing Implementation

**Question**: How to debounce trigger clicks during 300ms animation?

**Decision**: Use Flowbite's built-in animation state tracking (no custom debouncing needed)

**Rationale**:
- Flowbite JavaScript already prevents multiple transitions during animation
- When drawer is animating (opening or closing), additional trigger clicks are ignored
- Animation state managed via CSS classes: `transform`, `transition-transform`
- Flowbite adds `translate-x-0` (open) or `translate-x-full` (closed) after checking current state
- No custom debouncing logic required - Flowbite handles this internally

**Alternatives Considered**:
- Custom JavaScript debounce wrapper (rejected: duplicates Flowbite functionality)
- CSS pointer-events: none during animation (rejected: prevents legitimate user interactions)
- Python-side debouncing (rejected: debouncing is client-side runtime behavior)

**Implementation Pattern**:
No additional implementation needed - Flowbite JavaScript handles debouncing automatically.

---

### 8. Backdrop Implementation Pattern

**Question**: How to implement optional backdrop overlay?

**Decision**: Use Flowbite's backdrop pattern with conditional rendering

**Rationale**:
- Backdrop is separate element with `fixed inset-0` positioning
- Z-index: `z-30` (below drawer's `z-40`)
- Background: `bg-gray-900/50` (semi-transparent dark overlay)
- Click handler: `data-drawer-hide={drawer_id}` closes drawer on backdrop click
- Conditional rendering: only create backdrop element when `backdrop=True`
- Dark mode: `dark:bg-gray-900/80` for stronger contrast

**Alternatives Considered**:
- Always render backdrop with `hidden` class (rejected: unnecessary DOM nodes, complexity)
- JavaScript-generated backdrop (rejected: Flowbite expects HTML structure, not dynamic generation)
- CSS-only backdrop via `::before` pseudo-element (rejected: can't attach click handlers to pseudo-elements)

**Implementation Pattern**:
```python
if self.backdrop:
    backdrop = html.div(
        data_drawer_backdrop=drawer_id,
        data_drawer_hide=drawer_id,
        aria_hidden="true",
        class_="fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80",
    )
```

---

### 9. DrawerPlacement Enum Definition

**Question**: How to define DrawerPlacement enum for type safety?

**Decision**: Use Python's `str` and `Enum` with string values matching Flowbite's placement names

**Rationale**:
- Matches existing Color and Size enum patterns in flowbite-htmy
- String values ("left", "right", "top", "bottom") match Flowbite's `data-drawer-placement` attribute
- Inheriting from `str` allows direct use in HTML attributes without `.value`
- IDE autocomplete and type checking prevent invalid placement values
- Aligns with constitution principle II (Type Safety First)

**Alternatives Considered**:
- Plain strings (rejected: no type safety, no IDE autocomplete)
- Integer enum (rejected: doesn't match Flowbite's string-based API)
- Separate enum without `str` inheritance (rejected: requires `.value` everywhere, verbose)

**Implementation Pattern**:
```python
from enum import Enum

class DrawerPlacement(str, Enum):
    """Drawer placement positions."""
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
```

---

### 10. Edge Variant Implementation

**Question**: How to implement edge/swipeable variant with visible tab when closed?

**Decision**: Use separate button element positioned at drawer edge with `data-drawer-show` attribute

**Rationale**:
- Edge tab is visually distinct trigger that remains visible when drawer is closed
- Positioned at drawer edge using absolute/fixed positioning
- For LEFT placement: small vertical button on left edge of viewport
- Clicking tab opens drawer (uses same `data-drawer-show` pattern as main trigger)
- Flowbite handles show/hide of tab based on drawer state
- Edge variant is opt-in via prop (default: no edge tab)

**Alternatives Considered**:
- CSS-only tab using drawer's border (rejected: can't attach click handler)
- JavaScript-managed tab visibility (rejected: Flowbite's declarative pattern is simpler)
- Always show edge tab (rejected: not all use cases need it, adds visual clutter)

**Implementation Pattern**:
```python
if self.edge:
    edge_tab = html.button(
        html.span("›", class_="text-2xl"),  # Arrow icon
        data_drawer_show=drawer_id,
        class_="fixed left-0 top-1/2 -translate-y-1/2 z-30 "
              "bg-gray-50 dark:bg-gray-700 p-2 rounded-r-lg shadow-lg",
    )
```

---

## Summary of Key Decisions

| Decision Area | Choice | Rationale |
|--------------|--------|-----------|
| **State Management** | Flowbite JavaScript with data attributes | Tested, accessible, consistent with project |
| **Focus Trap** | Flowbite's built-in focus management | WAI-ARIA compliant, no custom code needed |
| **Viewport Constraint** | `max-h-screen` + `overflow-y-auto` | Native CSS, keeps header visible |
| **Transforms** | Flowbite placement patterns | Consistent animations for each direction |
| **HTMX Closure** | HX-Trigger header with event listener | Server-controlled, flexible per endpoint |
| **Multi-Drawer** | Custom JavaScript coordinator | Meets auto-close requirement |
| **Debouncing** | Flowbite's internal handling | Already implemented, no extra code |
| **Backdrop** | Conditional rendering with data attributes | Simple, declarative, follows Flowbite pattern |
| **Type Safety** | DrawerPlacement enum (str + Enum) | IDE support, type checking, consistency |
| **Edge Variant** | Optional button with positioning | Opt-in, reuses Flowbite's show mechanism |

All decisions align with project constitution (TDD, type safety, component value, hybrid architecture, quality gates).
