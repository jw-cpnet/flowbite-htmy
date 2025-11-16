# Phase 0 Research: Tabs Component

**Date**: 2025-01-16
**Feature**: Tabs Component ([spec.md](./spec.md))

## Research Questions

1. What are the exact Flowbite CSS classes for all 4 tab variants?
2. What ARIA pattern requirements exist for accessible tabs?
3. What Flowbite JavaScript data attributes are needed?
4. How do HTMX events interact with Flowbite tab switching?
5. What icon positioning patterns exist in current components?
6. How should unique IDs be generated for tab/panel associations?
7. How are disabled tabs handled in Flowbite?

---

## 1. Flowbite Tabs Classes (All Variants)

### Decision: Use Flowbite's 4 Tab Variants with Exact Classes

**Research Source**: flowbite-llms-full.txt, Flowbite tabs documentation

### Variant 1: DEFAULT (Border + Background)

**Active Tab Button**:
```
inline-block p-4 text-blue-600 bg-gray-100 rounded-t-lg active
dark:bg-gray-800 dark:text-blue-500
```

**Inactive Tab Button**:
```
inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50
dark:hover:bg-gray-800 dark:hover:text-gray-300
```

**Container**:
```
flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200
dark:border-gray-700 dark:text-gray-400
```

**Structure**: `<ul>` container with border-bottom, tab items with `me-2` spacing

### Variant 2: UNDERLINE (Minimal with Bottom Border Indicator)

**Active Tab Button**:
```
inline-block p-4 text-blue-600 border-b-2 border-blue-600 rounded-t-lg active
dark:text-blue-500 dark:border-blue-500
```

**Inactive Tab Button**:
```
inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600
hover:border-gray-300 dark:hover:text-gray-300
```

**Container**:
```
text-sm font-medium text-center text-gray-500 border-b border-gray-200
dark:text-gray-400 dark:border-gray-700
```

**Inner Container** (for `-mb-px` trick):
```
flex flex-wrap -mb-px
```

**Structure**: Outer `<div>` with border, inner `<ul>` with negative margin to hide inactive tab borders

### Variant 3: PILLS (Rounded Background Shapes)

**Active Tab Button**:
```
inline-block px-4 py-3 text-white bg-blue-600 rounded-lg active
```

**Inactive Tab Button**:
```
inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100
dark:hover:bg-gray-800 dark:hover:text-white
```

**Container**:
```
flex flex-wrap text-sm font-medium text-center text-gray-500
dark:text-gray-400
```

**Structure**: `<ul>` container, tab items with `me-2` spacing, no border

### Variant 4: FULL_WIDTH (Tabs Stretch to Fill Container)

**Active Tab Button**:
```
inline-block w-full p-4 text-gray-900 bg-gray-100 border-r border-gray-200
dark:border-gray-700 rounded-s-lg focus:ring-4 focus:ring-blue-300 active focus:outline-none
dark:bg-gray-700 dark:text-white
```

**Inactive Tab Button**:
```
inline-block w-full p-4 bg-white border-r border-gray-200
dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-blue-300
focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700
```

**Last Tab Button** (rounded end):
```
... border-s-0 border-gray-200 dark:border-gray-700 rounded-e-lg ...
```

**Container**:
```
text-sm font-medium text-center text-gray-500 rounded-lg shadow-sm flex
dark:divide-gray-700 dark:text-gray-400
```

**List Item**:
```
w-full focus-within:z-10
```

**Structure**: `<ul>` container with flex, list items with `w-full`, buttons with `w-full`, first tab has `rounded-s-lg`, last tab has `rounded-e-lg`

### Color Customization Pattern

Flowbite uses blue (blue-600, blue-500) as default active color. To support Color enum:

- **BLUE**: `text-blue-600 bg-blue-600 border-blue-600 dark:text-blue-500 dark:border-blue-500`
- **GREEN**: `text-green-600 bg-green-600 border-green-600 dark:text-green-500 dark:border-green-500`
- **RED**: `text-red-600 bg-red-600 border-red-600 dark:text-red-500 dark:border-red-500`
- **YELLOW**: `text-yellow-600 bg-yellow-600 border-yellow-600 dark:text-yellow-500 dark:border-yellow-500`
- **PURPLE**: `text-purple-600 bg-purple-600 border-purple-600 dark:text-purple-500 dark:border-purple-500`
- **PINK**: `text-pink-600 bg-pink-600 border-pink-600 dark:text-pink-500 dark:border-pink-500`
- **INDIGO**: `text-indigo-600 bg-indigo-600 border-indigo-600 dark:text-indigo-500 dark:border-indigo-500`
- **GRAY**: `text-gray-600 bg-gray-600 border-gray-600 dark:text-gray-500 dark:border-gray-500`

**Implementation**: Use string replacement or ClassBuilder conditional logic to swap color classes based on Color enum.

### Disabled Tab Classes

**Disabled Tab Button**:
```
inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed
dark:text-gray-500
```

**Note**: Disabled tabs have no hover states, use `cursor-not-allowed`, and have reduced opacity via gray colors.

### Rationale

- **Exact Flowbite Alignment**: Using official Flowbite classes ensures pixel-perfect consistency
- **Dark Mode**: All variants include dark mode classes, aligning with constitution principle
- **Color Flexibility**: Support for 8 colors via enum provides brand customization while maintaining type safety
- **Accessibility**: Disabled state is visually distinct and prevents interaction

---

## 2. ARIA Tabs Pattern Requirements

### Decision: Implement W3C ARIA Authoring Practices for Tabs

**Research Source**: W3C ARIA Authoring Practices Guide, Flowbite tabs implementation

### Required ARIA Roles

**Tablist Container** (`<ul>` or `<div>`):
```html
<ul role="tablist">
```

**Tab Buttons**:
```html
<button role="tab"
        aria-selected="true|false"
        aria-controls="panel-id"
        id="tab-id">
```

**Tab Panels**:
```html
<div role="tabpanel"
     aria-labelledby="tab-id"
     id="panel-id"
     hidden>
```

### ARIA States & Properties

| Attribute | Element | Purpose | Values |
|-----------|---------|---------|--------|
| `role="tablist"` | Container | Identifies tab navigation | N/A |
| `role="presentation"` | List items (`<li>`) | Removes list semantics | N/A (optional) |
| `role="tab"` | Tab buttons | Identifies interactive tab | N/A |
| `role="tabpanel"` | Content panels | Identifies panel associated with tab | N/A |
| `aria-selected` | Tab buttons | Indicates active tab | `"true"` or `"false"` |
| `aria-controls` | Tab buttons | Links tab to its panel | Panel `id` |
| `aria-labelledby` | Tab panels | Links panel to its tab | Tab `id` |
| `id` | Tabs & panels | Unique identifier for associations | String (must be unique) |
| `hidden` | Inactive panels | Hides non-active panels | Boolean attribute |

### Keyboard Interaction (Flowbite JavaScript Handles)

W3C recommends:
- **Tab**: Move focus into tab list, then to next focusable element
- **Arrow Left/Right**: Navigate between tabs
- **Home**: Focus first tab
- **End**: Focus last tab
- **Enter/Space**: Activate focused tab

Flowbite JavaScript implements arrow key navigation automatically when `data-tabs-toggle` is present.

### Rationale

- **Accessibility Compliance**: ARIA roles enable screen readers to announce tab structure correctly
- **Keyboard Navigation**: Flowbite JS handles arrow keys, Home/End for WCAG 2.1 Level AA compliance
- **Semantic HTML**: `role="presentation"` on `<li>` removes list semantics for cleaner screen reader experience
- **Explicit Associations**: `aria-controls` and `aria-labelledby` create bidirectional links between tabs and panels

---

## 3. Flowbite JavaScript Integration

### Decision: Use Flowbite's Data Attributes for Tab Switching

**Research Source**: Flowbite tabs JavaScript documentation (flowbite-llms-full.txt)

### Required Data Attributes

**Tablist Container**:
```html
<ul id="tabs-id"
    data-tabs-toggle="#tab-content-id"
    role="tablist">
```

- `id`: Unique identifier for the tablist
- `data-tabs-toggle`: CSS selector pointing to tab content container

**Tab Buttons**:
```html
<button id="tab-id"
        data-tabs-target="#panel-id"
        type="button"
        role="tab"
        aria-controls="panel-id"
        aria-selected="false">
```

- `id`: Unique identifier for the tab button
- `data-tabs-target`: CSS selector pointing to the specific panel this tab controls
- `type="button"`: Prevents form submission if tabs are in a form
- `aria-selected="false"`: Initially false, Flowbite sets to `"true"` on active tab

**Tab Panels**:
```html
<div id="panel-id"
     role="tabpanel"
     aria-labelledby="tab-id"
     class="hidden">
```

- `id`: Unique identifier matching `data-tabs-target` selector
- `class="hidden"`: Hides inactive panels (Flowbite removes `hidden` class on active panel)

### Optional Customization Attributes

**Active/Inactive Classes** (on tablist container):
```html
<ul data-tabs-toggle="#content"
    data-tabs-active-classes="text-blue-600 border-blue-600"
    data-tabs-inactive-classes="text-gray-500 border-transparent">
```

These allow customizing the classes applied to active vs inactive tabs. We'll use these for color customization.

### Flowbite Initialization

Flowbite auto-initializes when the DOM loads. No manual JavaScript needed in the component.

**Auto-initialization checks**:
- Looks for `[data-tabs-toggle]` elements
- Binds click events to tabs
- Binds keyboard events for arrow navigation
- Updates `aria-selected` and `hidden` class automatically

### Rationale

- **No Manual JS**: Flowbite handles all tab switching logic automatically
- **Declarative**: Data attributes define behavior, not imperative JavaScript
- **Color Customization**: `data-tabs-active-classes` allows dynamic color via Color enum
- **HTMX Compatible**: Data attributes don't conflict with HTMX attributes

---

## 4. HTMX Event Coexistence

### Decision: Place HTMX Attributes on Panel, Not Button

**Research Source**: HTMX documentation, Flowbite event handling patterns, Accordion component implementation (005-accordion)

### Challenge

Flowbite's tab buttons have click event listeners for tab switching. If HTMX attributes like `hx-get` are on the button, two events fire:
1. Flowbite click → switch tabs
2. HTMX click → fetch content

This can cause race conditions or duplicate requests.

### Solution: HTMX on Panel, Not Button

**Pattern** (from Accordion component):
```html
<!-- Tab Button: Only Flowbite attributes, no HTMX -->
<button id="tab-1"
        data-tabs-target="#panel-1"
        role="tab">
    Dashboard
</button>

<!-- Tab Panel: HTMX attributes here -->
<div id="panel-1"
     role="tabpanel"
     hx-get="/api/dashboard"
     hx-trigger="revealed"
     hx-swap="innerHTML">
    Loading...
</div>
```

### HTMX Trigger Strategy

Use `hx-trigger="revealed"` which fires when Flowbite removes the `hidden` class from the panel.

**Alternative triggers**:
- `hx-trigger="revealed once"` - Load only first time panel is revealed
- `hx-trigger="revealed delay:100ms"` - Add delay to avoid race conditions
- `hx-trigger="click from:#tab-1"` - Trigger from specific tab button (more complex)

### HTMX Attributes on Tab vs Panel

| Attribute | Location | Reason |
|-----------|----------|--------|
| `hx-get`, `hx-post` | Panel | Avoids button click conflicts |
| `hx-trigger` | Panel | Controls when request fires (revealed, not click) |
| `hx-target` | Panel | Can override (e.g., `hx-target="#other-div"`) |
| `hx-swap` | Panel | Controls how response replaces content |

**Note**: If user provides `hx-get` on Tab, the component should apply it to the panel `<div>`, not the button.

### Rationale

- **Event Separation**: Flowbite handles button clicks, HTMX handles panel content loading
- **No Conflicts**: `revealed` trigger fires after Flowbite shows panel
- **Proven Pattern**: Accordion component (005-accordion) uses this pattern successfully
- **Flexibility**: Users can override triggers, targets, swap strategies

---

## 5. Icon Positioning Patterns

### Decision: Follow Button Component Icon Pattern with Left/Right Support

**Research Source**: Button component (src/flowbite_htmy/components/button.py), Badge component

### Existing Icon Patterns

**Button Component** (icon left):
```python
if self.icon_left:
    html.span(get_icon(self.icon_left, class_="w-4 h-4"), class_="me-2")
html.span(self.label)
```

**Button Component** (icon right):
```python
html.span(self.label)
if self.icon_right:
    html.span(get_icon(self.icon_right, class_="w-4 h-4"), class_="ms-2")
```

**Spacing**: `me-2` (margin-end) for left icons, `ms-2` (margin-start) for right icons

### Tabs Icon Pattern

Use `icon` + `icon_position` props instead of separate `icon_left`/`icon_right` props for cleaner API:

```python
@dataclass(frozen=True, kw_only=True)
class Tab:
    icon: Icon | None = None
    icon_position: IconPosition = IconPosition.LEFT
```

**Icon Rendering**:
```python
# Left icon (default)
if self.icon and self.icon_position == IconPosition.LEFT:
    html.span(get_icon(self.icon, class_="w-4 h-4"), class_="me-2")
html.span(self.label)

# Right icon
if self.icon and self.icon_position == IconPosition.RIGHT:
    html.span(self.label)
    html.span(get_icon(self.icon, class_="w-4 h-4"), class_="ms-2")
```

**Icon Size**: `w-4 h-4` (consistent with Button, Flowbite docs show same size)

### IconPosition Enum

```python
class IconPosition(str, Enum):
    LEFT = "left"
    RIGHT = "right"
```

### Flowbite Tab Icon Classes (from docs)

**Tab button with icon** (underline variant):
```
inline-flex items-center justify-center p-4 border-b-2 border-transparent ...
```

**Icon classes**:
```
w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500
dark:text-gray-500 dark:group-hover:text-gray-300
```

**Container needs**: `inline-flex items-center justify-center` for vertical alignment

**Note**: Icon colors change on hover via `group` and `group-hover` classes.

### Rationale

- **Consistency**: Matches Button component pattern (w-4 h-4, me-2/ms-2 spacing)
- **Cleaner API**: Single `icon` + `icon_position` vs separate left/right props
- **Flowbite Alignment**: Uses exact icon sizes from Flowbite docs
- **Hover States**: Group classes allow icon color changes on tab hover

---

## 6. Unique ID Generation Strategy

### Decision: Use Python `id(self)` with Custom Override

**Research Source**: Accordion component (005-accordion), Python id() function

### Challenge

Tabs require unique IDs for:
- Tablist container: `<ul id="tabs-123">`
- Tab buttons: `<button id="tab-123-0">`, `<button id="tab-123-1">`
- Tab panels: `<div id="panel-123-0">`, `<div id="panel-123-1">`

IDs must be:
1. **Unique** across multiple Tabs components on the same page
2. **Predictable** for testing and debugging
3. **Server-side safe** (no JavaScript required)

### Solution: Python `id(self)` + Index

**Tabs Component**:
```python
@dataclass(frozen=True, kw_only=True)
class Tabs:
    tabs: list[Tab]
    tabs_id: str | None = None  # Custom override

    def _get_base_id(self) -> str:
        return self.tabs_id or f"tabs-{id(self)}"

    def htmy(self, context: Context) -> Component:
        base_id = self._get_base_id()
        tablist_id = base_id
        content_id = f"{base_id}-content"

        for i, tab in enumerate(self.tabs):
            tab_id = f"tab-{base_id}-{i}"
            panel_id = f"panel-{base_id}-{i}"
```

**Example IDs**:
- Tablist: `tabs-140234567890` (or custom `tabs-profile` if tabs_id="profile")
- Tab button 0: `tab-tabs-140234567890-0`
- Panel 0: `panel-tabs-140234567890-0`
- Tab button 1: `tab-tabs-140234567890-1`
- Panel 1: `panel-tabs-140234567890-1`

### Why `id(self)` Works

Python's `id()` returns the memory address of an object. For `@dataclass(frozen=True)` objects:
- Each instance has a unique memory address
- Two separate `Tabs(...)` calls create different objects with different `id()` values
- IDs are stable during a single render (object lives until render completes)
- IDs change between renders (but tabs are recreated each request anyway)

**Collision Risk**: Extremely low in practice (would require same memory address reuse within single request)

### Custom ID Override

Users can provide `tabs_id="custom"` for:
- **Testing**: Predictable IDs make assertions easier
- **CSS/JS targeting**: Easier to target specific tabs in external scripts
- **SEO**: Human-readable fragment identifiers (#tab-profile-0)

### Rationale

- **Proven Pattern**: Accordion component uses `id(self)` successfully
- **No External Dependencies**: Pure Python, no UUID library needed
- **Debuggable**: IDs are numeric, not random UUIDs (easier to trace)
- **Flexible**: Custom override available when needed

---

## 7. Disabled Tab Behavior

### Decision: Use `aria-disabled` + Styling, Prevent Activation

**Research Source**: W3C ARIA practices, Flowbite disabled tab examples

### Flowbite Disabled Tab Classes

```
inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed
dark:text-gray-500
```

**Key classes**:
- `text-gray-400` / `dark:text-gray-500`: Reduced contrast
- `cursor-not-allowed`: Visual feedback that tab is disabled
- **No hover classes**: Disabled tabs have no hover states

### ARIA Pattern for Disabled Tabs

Two approaches:

**Option 1: `aria-disabled="true"` on button**
```html
<button role="tab" aria-disabled="true" tabindex="-1">
    Disabled Tab
</button>
```

- Screen readers announce "disabled"
- `tabindex="-1"` removes from keyboard navigation
- Button is still clickable (need JavaScript to prevent activation)

**Option 2: Use `<a>` without href**
```html
<a class="... cursor-not-allowed">
    Disabled Tab
</a>
```

- Not focusable (no `href`)
- Not clickable
- Simpler, no JavaScript needed

**Decision**: Use Option 2 (Flowbite's approach) - render disabled tabs as `<a>` without `href`.

### Implementation Pattern

```python
def _render_tab(self, tab: Tab, index: int, base_id: str) -> Component:
    tab_id = f"tab-{base_id}-{index}"
    panel_id = f"panel-{base_id}-{index}"

    classes = self._build_tab_classes(tab)

    if tab.disabled:
        # Disabled tab: render as <a> without href
        return html.a(
            self._render_tab_content(tab),
            class_=classes,
        )
    else:
        # Active tab: render as <button> with Flowbite attributes
        return html.button(
            self._render_tab_content(tab),
            id=tab_id,
            data_tabs_target=f"#{panel_id}",
            type="button",
            role="tab",
            aria_controls=panel_id,
            aria_selected="true" if tab.is_active else "false",
            class_=classes,
        )
```

### Disabled Tab Classes

**Disabled tab** (no variant differences):
```python
if tab.disabled:
    builder = ClassBuilder("inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed")
    builder.add("dark:text-gray-500")
```

**Icon in disabled tab**:
```python
# Icon inherits disabled color automatically via text-gray-400
get_icon(tab.icon, class_="w-4 h-4")
```

### Rationale

- **Flowbite Alignment**: Uses Flowbite's pattern (no href, cursor-not-allowed)
- **Accessibility**: Screen readers won't announce disabled tabs as interactive
- **No JavaScript**: Disabled tabs are inherently non-clickable (no href)
- **Visual Clarity**: Gray colors + cursor-not-allowed clearly indicate disabled state

---

## Research Conclusions

### Key Decisions Summary

1. **Flowbite Classes**: Extracted exact classes for 4 variants (default, underline, pills, full-width) with color customization via Color enum
2. **ARIA Pattern**: Implement full W3C tabs pattern (role="tablist", role="tab", role="tabpanel", aria-selected, aria-controls, aria-labelledby)
3. **Flowbite JS**: Use `data-tabs-toggle`, `data-tabs-target`, `data-tabs-active-classes`, `data-tabs-inactive-classes` for automatic tab switching
4. **HTMX Integration**: Place HTMX attributes on panel `<div>`, not button, with `hx-trigger="revealed"` to avoid conflicts
5. **Icon Positioning**: Use `icon` + `icon_position` props with `w-4 h-4` icons, `me-2`/`ms-2` spacing, matching Button component
6. **Unique IDs**: Use Python `id(self)` + index with custom `tabs_id` override for predictable IDs
7. **Disabled Tabs**: Render as `<a>` without href, use `cursor-not-allowed` and gray colors, exclude from keyboard navigation

### No Unresolved NEEDS CLARIFICATION

All research questions have been answered with concrete decisions. Ready to proceed to Phase 1 design.

### References

- Flowbite Tabs Documentation (flowbite-llms-full.txt)
- W3C ARIA Authoring Practices Guide (Tabs Pattern)
- Accordion Component Implementation (specs/005-accordion/)
- Button Component Implementation (src/flowbite_htmy/components/button.py)
- HTMX Documentation (htmx.org)
