# Research: Toast Component

**Feature**: Toast notification component for temporary messages
**Branch**: 003-toast
**Date**: 2025-11-14

## Overview

This document captures technical research and decisions for implementing the Toast component. Research focuses on Flowbite patterns, component API design, HTMX integration patterns, and best practices from existing components.

## Technical Decisions

### Decision 1: Toast Variant Enum Design

**Context**: Toast component needs 4 color variants (success, danger, warning, info) with associated icons and styling.

**Decision**: Create a dedicated `ToastVariant` enum in `src/flowbite_htmy/types/toast.py`

**Rationale**:
- Follows established pattern (ButtonVariant, ValidationState in existing codebase)
- Provides type safety for variant selection
- Enables IDE autocomplete for available variants
- Makes it impossible to pass invalid variant strings
- Clear naming convention (SUCCESS, DANGER, WARNING, INFO)

**Alternatives Considered**:
- **Reuse Color enum**: Rejected - Color enum has 9+ values (primary, secondary, etc.) but Toast only uses 4 specific variants. ToastVariant is more specific and constrains options appropriately.
- **String literals**: Rejected - No type safety, prone to typos, no IDE support
- **Dataclass with constants**: Rejected - Enum is more idiomatic Python for fixed set of options

**Implementation**:
```python
from enum import Enum

class ToastVariant(str, Enum):
    """Toast notification variants."""
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
```

### Decision 2: Default Icons for Each Variant

**Context**: Each toast variant should have a sensible default icon if not explicitly provided.

**Decision**: Map each ToastVariant to a default Icon enum value

**Rationale**:
- Reduces boilerplate - developers don't need to specify icon for common cases
- Ensures consistency across applications (all success toasts use checkmark)
- Follows Flowbite design patterns (success=check, danger=X, warning=exclamation, info=info)
- Icon can still be overridden for custom use cases

**Icon Mapping**:
- SUCCESS → Icon.CHECK (checkmark in circle)
- DANGER → Icon.CLOSE (X in circle)
- WARNING → Icon.EXCLAMATION (exclamation mark)
- INFO → Icon.INFO (info "i" icon)

**Alternatives Considered**:
- **No default icons**: Rejected - Forces developers to specify icon every time, adds boilerplate
- **Hard-coded SVG per variant**: Rejected - Violates DRY, harder to maintain, breaks icon system abstraction

### Decision 3: Dismissible Button Design

**Context**: Toast needs optional close button integrated with Flowbite JavaScript dismiss functionality.

**Decision**: Use `dismissible: bool` prop with default `True`, generate data-dismiss-target attribute

**Rationale**:
- Boolean is simple and clear (no need for DismissButton nested component)
- Matches Flowbite's data-dismiss-target pattern for JavaScript integration
- Generates unique ID for each toast (for dismiss targeting)
- Allows simple `dismissible=False` to hide close button

**Implementation**:
- Auto-generate toast ID if not provided (using Python's uuid or sequential counter)
- Render close button with `data-dismiss-target="#toast-{id}"`
- Close button uses standard Flowbite classes and icon (X icon)
- Include sr-only "Close" label for accessibility

**Alternatives Considered**:
- **Separate DismissButton component**: Rejected - Over-engineering for simple boolean flag
- **Always include close button**: Rejected - Some toasts shouldn't be dismissible (e.g., critical errors requiring action)

### Decision 4: Interactive Toast with Action Buttons

**Context**: User Story 2 requires action buttons (Reply, Undo, View Details) with HTMX integration.

**Decision**: Support optional `action_button` prop with HTMX attributes

**Rationale**:
- Simple cases: Single action button is most common (Reply, Undo)
- Complex cases: Multiple buttons can use custom children (advanced use case)
- HTMX integration via button props (hx_get, hx_post, hx_target, etc.)
- Leverages existing Button component (don't reinvent styling)

**Implementation**:
```python
@dataclass(frozen=True, kw_only=True)
class ToastActionButton:
    label: str
    hx_get: str | None = None
    hx_post: str | None = None
    hx_target: str | None = None
    # ... other HTMX attrs
```

Then Toast accepts `action_button: ToastActionButton | None = None`

**Alternatives Considered**:
- **List of buttons**: Rejected - Most toasts have 0-1 action buttons, list adds complexity
- **String button HTML**: Rejected - Not type-safe, breaks component abstraction
- **Callback props**: Rejected - Server-side rendering doesn't support Python callbacks, use HTMX instead

### Decision 5: Rich Content Toast (Avatar + Formatted Text)

**Context**: User Story 2 requires rich notifications (chat messages, user actions) with avatars.

**Decision**: Support optional `avatar_src` prop for image URL, render with Avatar component if provided

**Rationale**:
- Simple prop for common case (avatar URL)
- Integrates with existing Avatar component (consistent styling)
- Doesn't complicate simple toast use case (optional prop)
- Follows Flowbite "toast-message-cta" and "toast-notification" examples

**Implementation**:
- If `avatar_src` provided, render Avatar component at start of content
- Avatar uses circular style (default Avatar styling)
- Message content wraps appropriately with avatar present

**Alternatives Considered**:
- **Accept Avatar component directly**: Rejected - Most use cases just need URL, prop simplifies API
- **Separate RichToast component**: Rejected - Same component can handle both simple and rich content conditionally

### Decision 6: Component Structure Pattern

**Context**: Need consistent API with existing components (Button, Badge, Alert, Radio, Textarea).

**Decision**: Use dataclass pattern with htmy() method, ClassBuilder for classes

**Rationale**:
- Established pattern in codebase (12 existing components use this)
- Type-safe with frozen dataclass
- ClassBuilder handles conditional classes cleanly
- ThemeContext integration for dark mode

**Component Signature**:
```python
@dataclass(frozen=True, kw_only=True)
class Toast:
    message: str
    variant: ToastVariant = ToastVariant.INFO
    icon: Icon | None = None  # None = use default for variant
    dismissible: bool = True
    action_button: ToastActionButton | None = None
    avatar_src: str | None = None
    id: str | None = None  # Auto-generated if None
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        ...
```

### Decision 7: Dark Mode Classes

**Context**: All components must support dark mode per constitution.

**Decision**: Always include dark: prefixed Tailwind classes (not conditional)

**Rationale**:
- Constitution requirement: "Always include dark mode classes"
- Tailwind's dark: prefix handles activation automatically
- Avoids conditional logic based on theme.dark_mode
- Consistent with all existing components

**Dark Mode Classes**:
- Container: `dark:bg-gray-800`
- Message text: `dark:text-gray-400`
- Icon container: `dark:bg-{color}-800 dark:text-{color}-200`
- Close button: `dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-gray-500 dark:hover:text-white`

### Decision 8: HTMX Integration Pattern

**Context**: Toast perfect for server-side notification responses (hx-trigger events).

**Decision**: Component generates static HTML, application handles HTMX responses

**Rationale**:
- Component responsibility: Render toast HTML
- Application responsibility: Return toast from HTMX endpoint, handle hx-swap target
- Separation of concerns (component doesn't know about routing)
- Standard HTMX pattern: server returns HTML fragment

**Usage Pattern**:
```python
@app.post("/action")
async def action():
    # ... perform action
    toast = Toast(
        message="Action completed successfully",
        variant=ToastVariant.SUCCESS
    )
    return await renderer.render(toast)
```

### Decision 9: Toast Positioning (Out of Scope)

**Context**: Toasts typically positioned (top-right, bottom-left, etc.) on page.

**Decision**: Positioning is application responsibility, NOT component responsibility

**Rationale**:
- Every application has different positioning needs (fixed, absolute, container constraints)
- Some applications use toast libraries (react-toastify pattern) for stacking
- Component generates toast HTML, parent container controls position
- Avoids over-engineering component with positioning logic

**Application Example**:
```python
# Application provides positioned container
html.div(
    Toast(...),
    class_="fixed top-4 right-4 z-50"
)
```

### Decision 10: Test Structure

**Context**: Need comprehensive test coverage (95%+ per constitution).

**Decision**: Test file structure follows existing component patterns (22+ tests estimated)

**Test Categories**:
1. **Default rendering** (1 test) - Minimal props
2. **Variant rendering** (4 tests) - Each variant with default icon
3. **Custom icons** (2 tests) - Override default icon, no icon
4. **Dismissible** (2 tests) - dismissible=True, dismissible=False
5. **Action buttons** (3 tests) - With button, HTMX attrs, no button
6. **Rich content** (2 tests) - With avatar, without avatar
7. **Dark mode** (1 test) - Verify dark: classes present
8. **Custom classes** (1 test) - class_ parameter merges
9. **ID generation** (2 tests) - Auto-generated ID, custom ID
10. **Accessibility** (2 tests) - role="alert", sr-only labels
11. **Edge cases** (2+ tests) - Long messages, empty messages, etc.

**Total**: ~22 tests (similar to Radio with 22 tests, Textarea with 20 tests)

## Flowbite Pattern Analysis

### Flowbite Toast Structure

Analyzed `flowbite-llms-full.txt` for toast patterns. Key findings:

**Base Structure**:
```html
<div id="toast-{type}" class="flex items-center w-full max-w-xs p-4 text-gray-500 bg-white rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800" role="alert">
    <!-- Icon container -->
    <div class="inline-flex items-center justify-center shrink-0 w-8 h-8 text-{color}-500 bg-{color}-100 rounded-lg dark:bg-{color}-800 dark:text-{color}-200">
        <svg>...</svg>
    </div>

    <!-- Message -->
    <div class="ms-3 text-sm font-normal">{message}</div>

    <!-- Close button (optional) -->
    <button type="button" class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700" data-dismiss-target="#toast-{type}" aria-label="Close">
        <span class="sr-only">Close</span>
        <svg>...</svg>
    </button>
</div>
```

**Variant Color Mapping**:
- SUCCESS: green-500, bg-green-100, dark:bg-green-800, dark:text-green-200
- DANGER: red-500, bg-red-100, dark:bg-red-800, dark:text-red-200
- WARNING: yellow-500, bg-yellow-100, dark:bg-yellow-800, dark:text-yellow-200
- INFO: blue-500, bg-blue-100, dark:bg-blue-800, dark:text-blue-200

**Interactive Toast Pattern** (Message CTA):
```html
<div class="flex">
    <img class="w-8 h-8 rounded-full" src="..." alt="..."/>
    <div class="ms-3 text-sm font-normal">
        <span class="mb-1 text-sm font-semibold text-gray-900 dark:text-white">{sender}</span>
        <div class="mb-2 text-sm font-normal">{message}</div>
        <a href="#" class="inline-flex px-2.5 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800">
            {button_label}
        </a>
    </div>
    <button type="button" class="..." data-dismiss-target="#..." aria-label="Close">...</button>
</div>
```

## Best Practices from Existing Components

### From Button Component
- Use ClassBuilder for variant-based class construction
- Support full HTMX attribute set (hx_get, hx_post, hx_target, etc.)
- Always include dark: classes (not conditional)

### From Badge Component
- Use enum for variants (BadgeColor → ToastVariant)
- Map enum values to color classes in dictionaries

### From Alert Component
- Similar dismissible pattern (but Alert doesn't use Flowbite JS)
- Icon positioning on left side
- role="alert" for accessibility

### From Radio Component
- Auto-generate IDs when not provided (radio-1, radio-2 → toast-{uuid})
- ValidationState enum pattern → ToastVariant enum
- Helper text rendering patterns (optional props)

### From Avatar Component
- Circular avatar styling (will reuse for rich toast)
- Image src handling

## Implementation Checklist

- [ ] Create `src/flowbite_htmy/types/toast.py` with ToastVariant enum
- [ ] Create `src/flowbite_htmy/components/toast.py` with Toast dataclass
- [ ] Implement htmy() method with ClassBuilder
- [ ] Define VARIANT_ICON_CLASSES and VARIANT_TEXT_CLASSES dictionaries
- [ ] Add ID auto-generation logic
- [ ] Support optional icon override
- [ ] Support dismissible close button with data-dismiss-target
- [ ] Support optional ToastActionButton
- [ ] Support optional avatar_src with Avatar component integration
- [ ] Export Toast and ToastVariant from __init__.py files
- [ ] Create comprehensive test suite (22+ tests)
- [ ] Create showcase function in examples/toasts.py
- [ ] Add route to examples/showcase.py
- [ ] Verify 95%+ test coverage
- [ ] Verify mypy strict mode passes
- [ ] Verify ruff checks pass

## Open Questions

**None** - All technical decisions resolved through research.

## References

- Flowbite Toast Documentation: `flowbite-llms-full.txt` (Toast section)
- Existing Components: Button, Badge, Alert, Radio, Avatar (patterns)
- Constitution: `.specify/memory/constitution.md` (requirements)
- Session Guide: Basic Memory `flowbite-htmy-session-guide` (architecture patterns)
