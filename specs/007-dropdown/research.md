# Research: Dropdown Component

**Feature**: Dropdown Component (007-dropdown)
**Date**: 2025-11-16
**Purpose**: Technical research for implementing Flowbite dropdown menus with htmy

## Research Questions

1. How does Flowbite JavaScript handle dropdown positioning and animations?
2. What ARIA patterns are required for accessible dropdown menus?
3. How should multi-level dropdowns be structured in the htmy component tree?
4. What Flowbite CSS classes are used for dropdown styling?
5. How can HTMX and Flowbite JavaScript coexist without event conflicts?
6. What are best practices for keyboard navigation in dropdown menus?

---

## 1. Flowbite JavaScript Dropdown Integration

### Decision
Use Flowbite JavaScript's Dropdown class with data attributes for initialization and positioning. The Dropdown class automatically handles:
- Click-outside behavior
- Positioning logic (with Popper.js)
- Animation transitions
- Keyboard event handling (Escape key)

### Implementation Pattern
```html
<!-- Trigger button with data attributes -->
<button data-dropdown-toggle="menu-id"
        data-dropdown-placement="bottom"
        data-dropdown-trigger="click"
        type="button">
  Dropdown button
</button>

<!-- Menu container -->
<div id="menu-id" class="hidden">
  <!-- Menu items -->
</div>
```

### Data Attributes Required
- `data-dropdown-toggle="<menu-id>"` - On trigger, references menu ID
- `data-dropdown-placement="top|bottom|left|right"` - Optional positioning hint
- `data-dropdown-trigger="click|hover"` - Optional trigger mode (default: click)

### Rationale
Flowbite JavaScript provides battle-tested positioning logic using Popper.js, handling edge detection and auto-repositioning. Reinventing this would add significant complexity. The data attribute pattern integrates cleanly with htmy components.

### Alternatives Considered
- **Pure CSS dropdowns**: Rejected - Cannot handle complex positioning near viewport edges
- **Custom JavaScript**: Rejected - Would duplicate Flowbite functionality and break visual consistency
- **HTMX-only**: Rejected - HTMX is for server communication, not UI positioning logic

---

## 2. ARIA Accessibility Patterns

### Decision
Implement WAI-ARIA Menu Button pattern with required attributes:
- Trigger: `aria-expanded`, `aria-haspopup="true"`, `aria-controls`
- Menu container: `role="menu"`, `id`, `aria-labelledby`
- Menu items: `role="menuitem"`, `tabindex="-1"` (except first item: `tabindex="0"`)
- Headers: `role="presentation"` (non-interactive)
- Dividers: `role="separator"` (non-interactive)

### ARIA State Management
Flowbite JavaScript automatically updates `aria-expanded` when dropdown opens/closes:
- Closed: `aria-expanded="false"`
- Open: `aria-expanded="true"`

### Keyboard Navigation
Required keyboard interactions (handled by Flowbite JS + browser defaults):
- **Escape**: Close dropdown, return focus to trigger
- **Tab**: Close dropdown, move focus to next focusable element
- **Shift+Tab**: Close dropdown, move focus to previous element
- **Enter/Space** (on trigger): Toggle dropdown
- **Enter** (on menu item): Activate item, close dropdown

Arrow key navigation (Up/Down to move between items) is nice-to-have but not required for basic compliance.

### Rationale
WAI-ARIA Menu Button pattern is the standard for dropdown menus. Flowbite already implements keyboard handling, so we leverage it rather than reimplementing.

### Reference
- [WAI-ARIA Authoring Practices - Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)
- [Flowbite Dropdown ARIA Documentation](https://flowbite.com/docs/components/dropdowns/#accessibility)

---

## 3. Multi-Level Dropdown Structure

### Decision
Use nested `Dropdown` components where parent menu items contain child `Dropdown` instances. Each level has its own trigger and menu with independent positioning.

### Pattern
```python
# Parent dropdown
parent_items = [
    DropdownItem(label="Profile", href="/profile"),
    DropdownItem(label="Settings", dropdown=Dropdown(
        trigger="Settings",
        items=[
            DropdownItem(label="Account", href="/settings/account"),
            DropdownItem(label="Privacy", href="/settings/privacy"),
        ]
    )),
]
```

### Rationale
Nested component composition is natural for htmy and aligns with how Flowbite handles multi-level menus. Each submenu is an independent dropdown with its own Flowbite JS instance.

### Positioning
- Level 1: Opens below/above trigger (bottom/top placement)
- Level 2+: Opens to the right of parent item (right placement, or left if near edge)

### Alternatives Considered
- **Flat structure with parent-child relationships**: Rejected - More complex state management, unclear ownership
- **Single Dropdown with nested items**: Rejected - Makes independent positioning logic difficult

---

## 4. Flowbite CSS Classes

### Decision
Use Flowbite's documented CSS classes for dropdown styling:

**Trigger Button** (when trigger_type="button"):
```python
# Base classes
"text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300"
"font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
"dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
```

**Menu Container**:
```python
# Base classes
"z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44"
"dark:bg-gray-700"
```

**Menu Item**:
```python
# Base classes
"block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600"
"dark:hover:text-white"
```

**Dropdown Header**:
```python
"px-4 py-3 text-sm text-gray-900 dark:text-white"
```

**Dropdown Divider**:
```python
"h-0 my-1 border-gray-100 dark:border-gray-600"
```

### Color Variants
Map Color enum to Flowbite color classes:
- BLUE: `bg-blue-700 hover:bg-blue-800 focus:ring-blue-300`
- GREEN: `bg-green-700 hover:bg-green-800 focus:ring-green-300`
- RED: `bg-red-700 hover:bg-red-800 focus:ring-red-300`
- (similar for yellow, purple, pink, indigo, gray)

### Rationale
Using Flowbite's exact CSS classes ensures visual consistency with Flowbite documentation examples and design system.

### Reference
Extracted from `flowbite-llms-full.txt` section on Dropdowns.

---

## 5. HTMX and Flowbite JavaScript Coexistence

### Decision
Place HTMX attributes (`hx-get`, `hx-post`, etc.) on menu items `<a>` tags, not on the trigger button. This prevents event conflicts between Flowbite's click handler and HTMX.

### Pattern
```python
DropdownItem(
    label="Load Content",
    hx_get="/api/content",
    hx_target="#content-area",
    hx_swap="innerHTML"
)

# Renders as:
# <a href="#"
#    hx-get="/api/content"
#    hx-target="#content-area"
#    hx-swap="innerHTML"
#    role="menuitem">
#   Load Content
# </a>
```

### Event Flow
1. User clicks trigger button → Flowbite opens dropdown
2. User clicks menu item with `hx-get` → HTMX makes request
3. HTMX completes → Menu item navigation occurs (or content swaps)
4. Flowbite automatically closes dropdown on item click

### Rationale
Separating Flowbite dropdown control (trigger button) from HTMX actions (menu items) prevents event listener conflicts. Both libraries can coexist cleanly.

### Alternative Considered
- **HTMX on trigger button**: Rejected - Conflicts with Flowbite's `data-dropdown-toggle` click handler

---

## 6. Keyboard Navigation Best Practices

### Decision
Implement basic keyboard navigation following WCAG 2.1 Level AA requirements:
- **Tab order**: Trigger button is focusable, menu items receive focus when menu opens
- **Escape**: Close menu (handled by Flowbite JS)
- **Focus management**: When menu closes, return focus to trigger (Flowbite JS handles this)

### Enhanced Navigation (Nice-to-Have)
For advanced accessibility, consider:
- **Arrow Up/Down**: Navigate between menu items
- **Home/End**: Jump to first/last item
- **Type-ahead**: Jump to item matching typed characters

These are not required for WCAG 2.1 AA compliance but improve UX.

### Implementation
Flowbite JavaScript handles Escape and focus return. Browser defaults handle Tab navigation. Arrow key navigation would require custom JavaScript (deferred to future enhancement).

### Rationale
Focus on WCAG 2.1 AA compliance first (required). Enhanced keyboard navigation can be added later without breaking changes.

### Reference
- [WCAG 2.1 Keyboard Accessible (Guideline 2.1)](https://www.w3.org/WAI/WCAG21/Understanding/keyboard)
- [WAI-ARIA Menu Pattern Keyboard Interaction](https://www.w3.org/WAI/ARIA/apg/patterns/menu/#keyboardinteraction)

---

## Technology Stack Summary

### Core Dependencies
- **htmy 0.1.0+**: Component rendering
- **Flowbite CSS 2.5.1**: Styling classes
- **Flowbite JavaScript**: Dropdown positioning and behavior
- **HTMX 2.0.2**: Optional dynamic content loading
- **ClassBuilder**: Tailwind class construction utility
- **ThemeContext**: Dark mode awareness
- **Icon system**: Menu item icons (`get_icon()`)

### Browser Compatibility
Flowbite supports modern browsers (last 2 versions):
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

### Performance Considerations
- Dropdown rendering: <10ms (htmy is fast)
- Flowbite JS initialization: <50ms (happens once on page load)
- Click response: <100ms (Flowbite animation duration)
- HTMX requests: Variable (depends on server response time)

---

## Implementation Checklist

- [ ] Define DropdownPlacement enum (TOP, BOTTOM, LEFT, RIGHT)
- [ ] Define DropdownTriggerType enum (BUTTON, AVATAR, TEXT)
- [ ] Define DropdownTriggerMode enum (CLICK, HOVER)
- [ ] Implement DropdownItem dataclass with icon, href, HTMX attributes
- [ ] Implement DropdownHeader dataclass (non-interactive label)
- [ ] Implement DropdownDivider dataclass (separator)
- [ ] Implement Dropdown dataclass with trigger, items, placement, mode
- [ ] Add ARIA attributes: aria-expanded, aria-haspopup, aria-controls, aria-labelledby
- [ ] Add Flowbite data attributes: data-dropdown-toggle, data-dropdown-placement, data-dropdown-trigger
- [ ] Generate unique IDs for ARIA relationships (use Python `id(self)`)
- [ ] Support Color enum for trigger button styling
- [ ] Support Size enum for trigger button sizing
- [ ] Support dark mode classes (always include dark: prefix)
- [ ] Support custom classes via class_ prop
- [ ] Support disabled state for trigger and menu items
- [ ] Handle nested dropdowns (recursive Dropdown composition)
- [ ] Write comprehensive tests (>90% coverage target)
- [ ] Create showcase application (examples/dropdowns.py)
- [ ] Integrate with consolidated showcase app

---

## Open Questions

None - All research questions resolved.

---

## Next Steps

Proceed to Phase 1: Data Model and API Contracts.
