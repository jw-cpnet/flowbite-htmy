# Data Model: Radio Component

**Feature**: 002-phase-2b-radio
**Date**: 2025-11-14

## Overview

The Radio component is a stateless UI component that renders a single radio button with its label, helper text, and associated attributes. This document defines the component's data structure, validation rules, and state management approach.

## Entities

### Radio Component

**Type**: Python dataclass (frozen, keyword-only)

**Purpose**: Represents a single radio button with label, validation state, and accessibility attributes

**Attributes**:

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `label` | `str` | No | `""` | Radio button label text (can be empty if aria_label provided) |
| `name` | `str` | No | `""` | Form input name for grouping (radios with same name are mutually exclusive) |
| `value` | `str` | No | `""` | Value submitted when radio is checked |
| `checked` | `bool` | No | `False` | Whether radio is pre-selected |
| `disabled` | `bool` | No | `False` | Whether radio is disabled (cannot be selected) |
| `validation_state` | `ValidationState` | No | `ValidationState.DEFAULT` | Visual validation state (default/error/success) |
| `helper_text` | `str` | No | `""` | Helper text displayed below radio button |
| `aria_label` | `str` | No | `""` | ARIA label for accessibility (required when label is empty) |
| `id` | `str \| None` | No | `None` | HTML id attribute (auto-generated if not provided) |
| `class_` | `str` | No | `""` | Additional CSS classes to merge with component classes |
| `hx_get` | `str \| None` | No | `None` | HTMX GET request URL |
| `hx_post` | `str \| None` | No | `None` | HTMX POST request URL |
| `hx_put` | `str \| None` | No | `None` | HTMX PUT request URL |
| `hx_delete` | `str \| None` | No | `None` | HTMX DELETE request URL |
| `hx_patch` | `str \| None` | No | `None` | HTMX PATCH request URL |
| `hx_target` | `str \| None` | No | `None` | HTMX target selector |
| `hx_swap` | `str \| None` | No | `None` | HTMX swap strategy |
| `hx_trigger` | `str \| None` | No | `None` | HTMX trigger event (default: "change") |
| `hx_push_url` | `str \| None` | No | `None` | HTMX push URL to browser history |
| `hx_select` | `str \| None` | No | `None` | HTMX select content from response |

**Methods**:

- `htmy(self, context: Context) -> Component`
  - Renders the radio button component as htmy Component
  - Retrieves ThemeContext from context for dark mode awareness
  - Generates unique ID if not provided
  - Builds CSS classes based on validation state, disabled state, and custom classes
  - Returns html.div containing label, input, and optional helper text

- `_build_input_classes(self) -> str`
  - Private method to build CSS classes for `<input>` element
  - Includes base Flowbite radio classes
  - Adds validation state colors (error: red, success: green, default: blue)
  - Adds disabled state classes if applicable
  - Adds dark mode classes (always included)

- `_build_label_classes(self) -> str`
  - Private method to build CSS classes for `<label>` element text
  - Includes base label styling (text-sm, font-medium)
  - Adds validation state text colors
  - Adds disabled state text color if applicable
  - Adds dark mode classes (always included)

- `_build_helper_classes(self) -> str`
  - Private method to build CSS classes for helper text `<p>` element
  - Includes base helper text styling (text-sm)
  - Adds validation state text colors
  - Adds dark mode classes (always included)

- `_validate(self) -> None`
  - Private method called during initialization to validate component state
  - Raises `ValueError` if both `label` and `aria_label` are empty
  - Ensures accessibility requirements are met

**Relationships**:
- Uses `ValidationState` enum for validation state typing
- Uses `ThemeContext` for dark mode awareness (via context)
- Uses `ClassBuilder` utility for CSS class construction

---

### ValidationState Enum

**Type**: String-based Enum

**Purpose**: Type-safe representation of validation states for form components

**Values**:

| Value | String | Description |
|-------|--------|-------------|
| `DEFAULT` | `"default"` | No validation feedback (neutral state) |
| `ERROR` | `"error"` | Error/invalid state (red styling) |
| `SUCCESS` | `"success"` | Success/valid state (green styling) |

**Usage**:
```python
from flowbite_htmy.types import ValidationState

radio = Radio(
    label="Shipping Method",
    validation_state=ValidationState.ERROR
)
```

---

## Validation Rules

### Component-Level Validation

1. **Accessibility Requirement** (enforced in `__post_init__` or `_validate()`):
   - If `label` is empty string, `aria_label` MUST be non-empty
   - Raises `ValueError` if both are empty: "Either 'label' or 'aria_label' must be provided for accessibility"

2. **Frozen Dataclass**:
   - All attributes are immutable after initialization
   - Enforced by `@dataclass(frozen=True)`

3. **Type Safety**:
   - All attributes have explicit type hints
   - `ValidationState` enum ensures only valid states
   - Boolean flags (`checked`, `disabled`) typed as `bool`
   - Optional HTMX attributes typed as `str | None`

### HTML Output Validation

1. **ID Uniqueness**:
   - Auto-generated IDs use module-level counter for uniqueness within session
   - Developer-provided IDs are not validated (trust developer to ensure uniqueness)

2. **Name Grouping**:
   - Radios with same `name` form a mutually exclusive group (HTML behavior)
   - Component does not enforce name presence (valid HTML to omit)

3. **HTMX Trigger**:
   - Default trigger is `change` event (implicit for form inputs in HTMX)
   - Can be overridden via `hx_trigger` attribute

---

## State Management

### Component State

**Stateless**: Radio component has no internal state. All state is passed via props:
- Checked state (`checked` prop) - controlled by parent/form
- Validation state (`validation_state` prop) - controlled by parent
- Disabled state (`disabled` prop) - controlled by parent

**No State Mutations**: Component is immutable (`frozen=True`) - cannot change after creation

### Form State

**Outside Component Scope**: Form state management is handled by:
- Browser (for checked/unchecked state in radio groups)
- Server (for HTMX partial updates)
- Parent application (for validation logic)

Component is a pure presentation layer with no state management responsibilities.

---

## Data Flow

### Rendering Flow

```
1. Application creates Radio instance with props
   ↓
2. Radio.__post_init__ validates props (label/aria_label check)
   ↓
3. Application calls render(Radio(...))
   ↓
4. Radio.htmy(context) method invoked
   ↓
5. ThemeContext retrieved from context
   ↓
6. ID generated if not provided
   ↓
7. CSS classes built based on props + validation state + disabled state
   ↓
8. htmy Component tree constructed:
   - div (container)
     - label (wraps input + label text)
       - input type="radio" (with all attributes)
       - span (label text)
     - p (helper text, if provided)
   ↓
9. HTML rendered and returned
```

### HTMX Interaction Flow

```
1. User clicks radio button
   ↓
2. Browser triggers "change" event
   ↓
3. HTMX intercepts change event (if hx_get/hx_post present)
   ↓
4. HTMX sends HTTP request to specified endpoint
   ↓
5. Server processes request, returns partial HTML
   ↓
6. HTMX swaps content based on hx_target and hx_swap
   ↓
7. Updated Radio components render with new validation states
```

---

## Example Usage

### Basic Radio Group

```python
from flowbite_htmy.components import Radio

# Shipping method selection
radio1 = Radio(
    label="Standard Shipping (5-7 days)",
    name="shipping",
    value="standard",
    checked=True
)

radio2 = Radio(
    label="Express Shipping (2-3 days)",
    name="shipping",
    value="express"
)

radio3 = Radio(
    label="Overnight Shipping (1 day)",
    name="shipping",
    value="overnight"
)
```

### With Validation States

```python
from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState

# Error state - option not available
radio_error = Radio(
    label="Express Shipping (Not available in your region)",
    name="shipping",
    value="express",
    validation_state=ValidationState.ERROR,
    helper_text="This shipping method is not available for your location",
    disabled=True
)

# Success state - recommended option
radio_success = Radio(
    label="Standard Shipping (Recommended)",
    name="shipping",
    value="standard",
    validation_state=ValidationState.SUCCESS,
    helper_text="Free shipping on orders over $50",
    checked=True
)
```

### With HTMX Integration

```python
from flowbite_htmy.components import Radio

# Dynamic price update when shipping method changes
radio_htmx = Radio(
    label="Express Shipping",
    name="shipping",
    value="express",
    hx_get="/calculate-shipping",
    hx_target="#shipping-cost",
    hx_swap="innerHTML"
)
```

### Empty Label with aria-label

```python
from flowbite_htmy.components import Radio

# Icon-only radio (label text empty, aria-label for accessibility)
radio_icon = Radio(
    label="",  # Empty label text
    aria_label="Select blue color",
    name="color",
    value="blue",
    class_="color-swatch color-blue"  # Custom styling for visual indicator
)
```

---

## Type Definitions

```python
from dataclasses import dataclass
from enum import Enum
from htmy import Component, Context


class ValidationState(str, Enum):
    """Validation state for form components."""
    DEFAULT = "default"
    ERROR = "error"
    SUCCESS = "success"


@dataclass(frozen=True, kw_only=True)
class Radio:
    """Radio button component with label, validation, and HTMX support."""

    # Core attributes
    label: str = ""
    name: str = ""
    value: str = ""
    checked: bool = False
    disabled: bool = False

    # Validation & feedback
    validation_state: ValidationState = ValidationState.DEFAULT
    helper_text: str = ""

    # Accessibility
    aria_label: str = ""
    id: str | None = None

    # Styling
    class_: str = ""

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
    hx_select: str | None = None

    def __post_init__(self) -> None:
        """Validate component props."""
        if not self.label and not self.aria_label:
            raise ValueError(
                "Either 'label' or 'aria_label' must be provided for accessibility"
            )

    def htmy(self, context: Context) -> Component:
        """Render radio button component."""
        ...

    def _build_input_classes(self) -> str:
        """Build CSS classes for input element."""
        ...

    def _build_label_classes(self) -> str:
        """Build CSS classes for label text."""
        ...

    def _build_helper_classes(self) -> str:
        """Build CSS classes for helper text."""
        ...
```

---

## Notes

- **No RadioGroup Component**: Each Radio is independent; developers manually group by using the same `name` attribute
- **Mutual Exclusivity**: Handled by browser (standard HTML radio behavior) - radios with same `name` are mutually exclusive
- **ID Generation**: Uses module-level counter for predictable, testable IDs (not UUID for test stability)
- **Dark Mode**: Always include `dark:` prefixed classes; Tailwind handles activation based on dark mode state
- **Type Safety**: Full type hints with mypy strict mode compliance required
