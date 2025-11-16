# Research: Accordion Component Implementation

**Date**: 2025-11-16
**Feature**: 005-accordion
**Objective**: Resolve technical unknowns for ARIA patterns, Flowbite integration, HTMX coexistence, ID generation, and icon systems.

## 1. ARIA Accordion Pattern (W3C WAI-ARIA Authoring Practices)

### Decision

Use W3C standard ARIA accordion pattern with proper semantic HTML structure and required accessibility attributes.

###

 Rationale

- **WCAG 2.1 AA Compliance**: Required for accessibility (Success Criterion SC-002 in spec)
- **Screen Reader Support**: Proper ARIA attributes enable assistive technology to understand accordion structure
- **Keyboard Navigation**: Standard pattern ensures consistent keyboard UX across browsers
- **Semantic HTML**: Using `<button>` elements inside `<h2>` provides proper document outline

### Implementation Details

**Required ARIA Attributes**:

1. **On Button (Header)**:
   - `aria-expanded="true|false"` - Indicates current expanded state
   - `aria-controls="{panel-id}"` - References the controlled panel element

2. **On Panel (Body)**:
   - `aria-labelledby="{header-id}"` - References the header button that controls it
   - No `role="region"` needed (Flowbite doesn't use it, panel IDs sufficient)

**HTML Structure** (per W3C + Flowbite):
```html
<div id="accordion-{id}" data-accordion="collapse">
  <h2 id="accordion-{id}-heading-{index}">
    <button
      type="button"
      aria-expanded="true|false"
      aria-controls="accordion-{id}-body-{index}"
      data-accordion-target="#accordion-{id}-body-{index}">
      Panel Title
    </button>
  </h2>
  <div
    id="accordion-{id}-body-{index}"
    aria-labelledby="accordion-{id}-heading-{index}"
    class="hidden">
    Panel Content
  </div>
</div>
```

**Keyboard Navigation** (Flowbite JS handles):
- **Tab**: Focus next/previous button
- **Enter/Space**: Toggle panel expand/collapse
- **Arrow Keys**: NOT implemented by Flowbite (optional per W3C)

### Alternatives Considered

- **role="region"** on panels: W3C recommends but Flowbite omits. DECISION: Follow Flowbite for consistency.
- **Arrow key navigation**: W3C optional. DECISION: Skip for v1, rely on Tab navigation (simpler, Flowbite doesn't implement).

## 2. Flowbite Accordion Implementation

### Decision

Follow Flowbite's exact HTML structure and class patterns for pixel-perfect consistency. Use Flowbite JavaScript `initAccordions()` for collapse behavior.

### Rationale

- **Visual Consistency**: Success Criterion SC-004 requires "pixel-perfect consistency to official Flowbite examples"
- **JavaScript Integration**: Flowbite JS provides battle-tested collapse logic, focus management, and event handling
- **Maintainability**: Following Flowbite patterns ensures updates/fixes in Flowbite CSS/JS work seamlessly

### Implementation Details

**HTML Structure** (from flowbite-llms-full.txt):

```html
<!-- Container with data-accordion attribute -->
<div id="accordion-collapse" data-accordion="collapse">

  <!-- Panel 1 -->
  <h2 id="accordion-collapse-heading-1">
    <button
      type="button"
      class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
      data-accordion-target="#accordion-collapse-body-1"
      aria-expanded="true"
      aria-controls="accordion-collapse-body-1">
      <span>Panel Title</span>
      <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
      </svg>
    </button>
  </h2>
  <div id="accordion-collapse-body-1" class="hidden" aria-labelledby="accordion-collapse-heading-1">
    <div class="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900">
      Panel Content
    </div>
  </div>

  <!-- Subsequent panels... -->
</div>
```

**Data Attributes**:

1. **data-accordion="collapse|open"** (on container):
   - `collapse` - Single panel open at a time (default)
   - `open` - Multiple panels can be open (always-open mode)

2. **data-accordion-target="#id"** (on button):
   - CSS selector pointing to panel body
   - Must include `#` prefix for ID selector

3. **data-accordion-icon** (on SVG):
   - Marks icon for rotation animation
   - Flowbite JS adds/removes `rotate-180` class

4. **data-active-classes** & **data-inactive-classes** (on container, optional):
   - Custom classes for expanded/collapsed button states
   - Default: gray colors; can override for blue, green, etc.

**CSS Classes** (Default Accordion):

**Button (Header)**:
- Base: `flex items-center justify-between w-full p-5 font-medium rtl:text-right gap-3`
- Colors: `text-gray-500 dark:text-gray-400`
- Border: `border border-b-0 border-gray-200 dark:border-gray-700`
- First panel: `rounded-t-xl`
- Last panel: `rounded-b-xl` (when collapsed)
- Focus: `focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800`
- Hover: `hover:bg-gray-100 dark:hover:bg-gray-800`

**Panel Body Wrapper**:
- Always: `hidden` (Flowbite JS toggles)
- Padding: `p-5`
- Border: `border border-b-0 border-gray-200 dark:border-gray-700`
- Background (first panel): `dark:bg-gray-900`
- Last panel: `border-t-0` instead of `border-b-0`

**Icon**:
- Size: `w-3 h-3`
- Rotation: `rotate-180` (added by JS when expanded)
- Utility: `shrink-0` (prevent icon from shrinking)
- Accessibility: `aria-hidden="true"` (decorative)

**CSS Classes** (Flush Accordion):

**Button (Header)**:
- Base: `flex items-center justify-between w-full py-5 font-medium rtl:text-right gap-3`
- Colors: `text-gray-500 dark:text-gray-400`
- Border: `border-b border-gray-200 dark:border-gray-700`
- NO rounded corners, NO side/top borders, NO padding-x (py-5 only)

**Panel Body Wrapper**:
- Padding: `py-5` (no px)
- Border: `border-b border-gray-200 dark:border-gray-700`
- NO background color
- NO side/top borders

**JavaScript Initialization**:
- Flowbite auto-initializes accordions on page load via `data-accordion` attribute
- Manual initialization: `new Accordion(element, panels, options)` (if needed for HTMX)

### Alternatives Considered

- **Pure CSS accordion** (no JavaScript): REJECTED - doesn't support ARIA updates, no smooth animations, breaks accessibility.
- **Custom JavaScript**: REJECTED - reinventing the wheel, maintenance burden, Flowbite JS is 3KB and battle-tested.

## 3. Flowbite + HTMX Integration Pattern

### Decision

Use HTMX attributes on panel body wrapper, NOT on button. Re-initialize Flowbite accordion after HTMX content swap using `htmx:afterSwap` event.

### Rationale

- **Event Coexistence**: Flowbite click handler on button conflicts with HTMX click triggers. Putting HTMX on panel body avoids conflicts.
- **Lazy Loading**: Panel content can be loaded when expanded (trigger: `revealed`) rather than on page load.
- **Dynamic Panels**: HTMX can add/remove panels, and Flowbite can be re-initialized to manage new DOM elements.

### Implementation Details

**HTMX Attributes on Panel Body**:

```html
<div
  id="accordion-{id}-body-{index}"
  class="hidden"
  aria-labelledby="accordion-{id}-heading-{index}"
  hx-get="/api/panel-content/{id}"
  hx-trigger="revealed"
  hx-swap="innerHTML"
  hx-target="this">
  <!-- Initial content or loading indicator -->
</div>
```

**Key Decisions**:

1. **hx-trigger="revealed"** (default):
   - Flowbite fires `revealed` event when panel is expanded
   - Content loads on first expand, cached thereafter
   - Alternative: `hx-trigger="click from:.accordion-button"` (custom selector)

2. **hx-swap="innerHTML"**:
   - Replace panel body content, preserve wrapper
   - Maintains `aria-labelledby` and `hidden` class

3. **hx-target="this"**:
   - Swap content into the panel body itself
   - Simpler than external target

**Re-initialization After HTMX Swap**:

When HTMX adds/removes panels dynamically, Flowbite JavaScript needs to re-bind event handlers:

```html
<script>
  document.body.addEventListener('htmx:afterSwap', function(event) {
    // Re-initialize all accordions after HTMX swaps content
    if (event.target.matches('[data-accordion]') || event.target.closest('[data-accordion]')) {
      // Flowbite 2.x auto-reinitializes, or manually call:
      // initAccordions();
    }
  });
</script>
```

**Event Conflicts - Avoided**:

- **Problem**: Flowbite button has `click` event listener for collapse toggle.
- **Solution**: NEVER put `hx-post` or `hx-get` on the `<button>` element. HTMX triggers on button would conflict with Flowbite collapse logic.
- **Pattern**: HTMX attributes only on panel body (`<div>`), Flowbite manages button entirely.

### Alternatives Considered

- **HTMX on button**: REJECTED - conflicts with Flowbite click handler, breaks collapse behavior.
- **Manual accordion state management**: REJECTED - duplicates Flowbite logic, high maintenance.
- **Disable Flowbite JS, use pure HTMX**: REJECTED - loses smooth animations, ARIA updates, keyboard support.

## 4. Unique ID Generation Strategy

### Decision

Generate IDs using pattern: `accordion-{self_id}-heading-{index}` and `accordion-{self_id}-body-{index}`, where `self_id` is from Python's `id(self)` function, ensuring uniqueness even for nested accordions.

### Rationale

- **Collision Avoidance**: Python's `id()` returns unique memory address, guarantees no ID collisions between component instances.
- **Nested Accordion Support**: Child accordions get different `self_id`, preventing `aria-controls` conflicts.
- **Deterministic per Instance**: Same component instance always generates same IDs (useful for testing snapshots).
- **No Global State**: No need for global counters or registries.

### Implementation Details

**ID Generation Logic**:

```python
@dataclass(frozen=True, kw_only=True)
class Accordion:
    panels: list[Panel]
    accordion_id: str | None = None

    def htmy(self, context: Context) -> Component:
        # Use custom ID or auto-generate from self
        base_id = self.accordion_id or f"accordion-{id(self)}"

        panels_html = []
        for index, panel in enumerate(self.panels):
            heading_id = f"{base_id}-heading-{index}"
            body_id = f"{base_id}-body-{index}"

            # Use heading_id and body_id in ARIA attributes
            panels_html.append(
                html.h2(
                    html.button(
                        ...,
                        aria_controls=body_id,
                        data_accordion_target=f"#{body_id}",
                        id=heading_id
                    ),
                    id=heading_id
                ),
                html.div(
                    ...,
                    id=body_id,
                    aria_labelledby=heading_id
                )
            )
```

**Example Generated IDs**:

- First accordion instance: `accordion-140312345678-heading-0`, `accordion-140312345678-body-0`
- Nested accordion: `accordion-140312999999-heading-0` (different self_id)
- Custom ID: `accordion-faq-heading-0` (user provided `accordion_id="faq"`)

**Custom ID Support**:

- `accordion_id` prop allows user to override auto-generation
- Useful for testing, stable IDs across renders, CSS selectors
- User responsible for uniqueness if custom ID provided

### Alternatives Considered

- **Global counter**: REJECTED - requires global state, not thread-safe, complicates testing.
- **UUID**: REJECTED - too long (36 chars), ugly IDs, overkill for page-scoped uniqueness.
- **Hash of panel titles**: REJECTED - not unique (duplicate titles possible), unstable (titles change).

## 5. Icon System Integration

### Decision

Use existing `Icon.CHEVRON_DOWN` from `flowbite_htmy.icons` as default expand/collapse indicator. Support custom icons via optional `icon: Component | None` prop on Panel dataclass.

### Rationale

- **Consistency**: Flowbite accordion uses chevron-down icon rotated 180° when expanded
- **Existing Infrastructure**: Project already has icon system with `get_icon()` helper
- **Flexibility**: Custom icons allow overriding default (e.g., plus/minus icons, question mark icons)
- **Dark Mode**: Icon system handles dark mode colors via Tailwind classes

### Implementation Details

**Default Icon** (Chevron Down):

```python
from flowbite_htmy.icons import Icon, get_icon

# In Accordion.htmy() method:
icon_component = get_icon(
    Icon.CHEVRON_DOWN,
    class_="w-3 h-3 shrink-0",
    data_accordion_icon="true",
    aria_hidden="true"
)
```

**Custom Icon Support** (Panel dataclass):

```python
@dataclass(frozen=True, kw_only=True)
class Panel:
    title: str
    content: str | Component
    icon: Component | None = None  # Optional custom icon
    ...

# In Accordion.htmy():
if panel.icon:
    icon_html = panel.icon  # Use custom icon
else:
    icon_html = get_icon(Icon.CHEVRON_DOWN, ...)  # Use default
```

**Icon Rotation CSS**:

Flowbite JavaScript automatically adds/removes `rotate-180` class to elements with `data-accordion-icon` attribute:

```html
<!-- Collapsed state -->
<svg data-accordion-icon class="w-3 h-3 shrink-0" ...>

<!-- Expanded state (Flowbite JS adds rotate-180) -->
<svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" ...>
```

**Tailwind Transition**:

Add `transition-transform duration-200` to icon for smooth rotation animation:

```python
icon_component = get_icon(
    Icon.CHEVRON_DOWN,
    class_="w-3 h-3 shrink-0 transition-transform duration-200"
)
```

**Dark Mode Icon Colors**:

Icon inherits text color from button via `currentColor`:

```html
<button class="text-gray-500 dark:text-gray-400 ...">
  <svg fill="currentColor">  <!-- Inherits gray-500/dark:gray-400 -->
</button>
```

No explicit dark mode classes needed on icon itself.

### Alternatives Considered

- **Hardcode SVG strings**: REJECTED - not maintainable, duplicates icon definitions, no dark mode support.
- **Require custom icons always**: REJECTED - too much boilerplate for common case (most accordions use chevron).
- **Plus/minus icons as default**: REJECTED - Flowbite uses chevron, deviating breaks consistency (SC-004).

## Summary of Technical Decisions

| Research Area | Decision | Rationale |
|---------------|----------|-----------|
| **ARIA Pattern** | Use W3C standard with `aria-expanded`, `aria-controls`, `aria-labelledby` on `<h2>`+`<button>` structure | WCAG 2.1 AA compliance, screen reader support, semantic HTML |
| **Flowbite Integration** | Follow exact HTML structure and classes, use `data-accordion` attributes, rely on Flowbite JS for collapse logic | Pixel-perfect consistency (SC-004), battle-tested JS, maintainability |
| **HTMX Integration** | HTMX attributes on panel body (not button), `hx-trigger="revealed"`, re-initialize Flowbite after swaps | Avoid event conflicts, lazy loading, dynamic panel support |
| **ID Generation** | `accordion-{id(self)}-heading/body-{index}` pattern, optional custom ID via `accordion_id` prop | Collision avoidance, nested accordion support, no global state |
| **Icon System** | Default `Icon.CHEVRON_DOWN` with `data-accordion-icon`, optional custom `icon` prop on Panel | Flowbite consistency, existing infrastructure, flexibility |

## Open Questions (Resolved)

None remaining. All technical unknowns have been resolved with concrete implementation decisions.

## Next Phase

Phase 1: Data Model & Contracts - Define Accordion and Panel entities with full type annotations, generate component API contract, create TDD quickstart guide.
