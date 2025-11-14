# Component Contract: Radio

**Feature**: 002-phase-2b-radio
**Date**: 2025-11-14
**Type**: UI Component (htmy)

## Overview

Contract specification for the Radio component API, defining the interface between the component and consuming applications. This document serves as the authoritative reference for component behavior, prop types, and rendered output.

## Component Interface

### Import Path

```python
from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState  # For validation states
```

### Component Signature

```python
@dataclass(frozen=True, kw_only=True)
class Radio:
    # Core form attributes
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

    # HTMX integration
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
```

---

## Props Contract

### Required Props

None - all props have defaults

### Optional Props

| Prop | Type | Default | Constraints | Description |
|------|------|---------|-------------|-------------|
| `label` | `str` | `""` | Empty allowed if `aria_label` provided | Radio button label text |
| `name` | `str` | `""` | - | Form input name for grouping |
| `value` | `str` | `""` | - | Value submitted when checked |
| `checked` | `bool` | `False` | - | Pre-selected state |
| `disabled` | `bool` | `False` | - | Disabled state |
| `validation_state` | `ValidationState` | `DEFAULT` | Must be valid enum value | Visual validation state |
| `helper_text` | `str` | `""` | - | Helper text below radio |
| `aria_label` | `str` | `""` | Required if `label` is empty | ARIA label for accessibility |
| `id` | `str \| None` | `None` | Must be unique if provided | HTML id attribute |
| `class_` | `str` | `""` | - | Additional CSS classes |
| `hx_get` | `str \| None` | `None` | Valid URL | HTMX GET request URL |
| `hx_post` | `str \| None` | `None` | Valid URL | HTMX POST request URL |
| `hx_target` | `str \| None` | `None` | Valid CSS selector | HTMX target element |
| `hx_swap` | `str \| None` | `None` | Valid HTMX swap strategy | HTMX content swap method |
| *...other hx_* | `str \| None` | `None` | Per HTMX spec | Additional HTMX attributes |

### Validation Rules

**At Component Initialization**:
1. If `label == ""` and `aria_label == ""`, raise `ValueError`:
   ```
   ValueError: Either 'label' or 'aria_label' must be provided for accessibility
   ```

2. All props must match declared types (enforced by Python type system + mypy)

---

## Rendered Output Contract

### HTML Structure

**With Label Text**:
```html
<div class="flex items-start">
    <div class="flex items-center h-5">
        <input
            type="radio"
            id="radio-{auto-generated-id}"
            name="{name}"
            value="{value}"
            {checked if checked}
            {disabled if disabled}
            class="{input-classes}"
            {hx-* attributes if provided}
        />
    </div>
    <div class="ms-2 text-sm">
        <label for="radio-{auto-generated-id}" class="{label-classes}">
            {label}
        </label>
        {if helper_text}
        <p class="{helper-classes}">{helper_text}</p>
        {endif}
    </div>
</div>
```

**With Empty Label (aria-label only)**:
```html
<div class="flex items-start">
    <div class="flex items-center h-5">
        <input
            type="radio"
            id="radio-{auto-generated-id}"
            name="{name}"
            value="{value}"
            aria-label="{aria_label}"
            {checked if checked}
            {disabled if disabled}
            class="{input-classes}"
            {hx-* attributes if provided}
        />
    </div>
    {if helper_text}
    <div class="ms-2 text-sm">
        <p class="{helper-classes}">{helper_text}</p>
    </div>
    {endif}
</div>
```

### CSS Classes Contract

**Input Element Classes** (validation state: DEFAULT, not disabled):
```
w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600
```

**Input Element Classes** (validation state: ERROR):
```
w-4 h-4 text-red-600 bg-gray-100 border-red-500 dark:border-red-600 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700
```

**Input Element Classes** (validation state: SUCCESS):
```
w-4 h-4 text-green-600 bg-gray-100 border-green-500 dark:border-green-600 focus:ring-green-500 dark:focus:ring-green-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700
```

**Input Element Classes** (disabled: true):
```
{base classes} disabled:opacity-50 disabled:cursor-not-allowed
```

**Label Element Classes** (validation state: DEFAULT, not disabled):
```
font-medium text-gray-900 dark:text-gray-300
```

**Label Element Classes** (validation state: ERROR):
```
font-medium text-red-600 dark:text-red-500
```

**Label Element Classes** (validation state: SUCCESS):
```
font-medium text-green-600 dark:text-green-500
```

**Label Element Classes** (disabled: true):
```
font-medium text-gray-400 dark:text-gray-500
```

**Helper Text Classes** (validation state: DEFAULT):
```
text-gray-500 dark:text-gray-400
```

**Helper Text Classes** (validation state: ERROR):
```
text-red-600 dark:text-red-500
```

**Helper Text Classes** (validation state: SUCCESS):
```
text-green-600 dark:text-green-500
```

**Custom Classes**: Merged via `class_` prop appended to input element classes

---

## Behavior Contract

### Radio Button Grouping

**Mutual Exclusivity**:
- Radios with the same `name` attribute form a mutually exclusive group
- Only one radio in a group can be checked at a time
- Handled by browser (standard HTML behavior)

**Independent Validation**:
- Each Radio component has its own `validation_state`
- Radios in the same group can have different validation states
- No automatic synchronization of validation states

### HTMX Integration

**Default Trigger**:
- HTMX requests trigger on `change` event when radio is selected
- Implicit in HTMX for form inputs (no need to set `hx-trigger="change"` explicitly)

**Attribute Rendering**:
- All `hx_*` props render as `hx-*` HTML attributes on the `<input>` element
- Underscores convert to hyphens automatically (htmy behavior)
- Example: `hx_get="/endpoint"` → `hx-get="/endpoint"`

### ID Generation

**Auto-Generation**:
- If `id` prop is `None`, component generates unique ID using format: `radio-{counter}`
- Counter is module-level, incremented for each radio creation
- Predictable IDs for testing (not UUID-based)

**Custom ID**:
- If `id` prop provided, use it as-is (no validation of uniqueness)
- Developer responsible for ensuring unique IDs across page

### Accessibility

**Label Association**:
- `<label for="{id}">` associates with `<input id="{id}">`
- Clicking label toggles radio button

**Empty Label**:
- When `label` is empty, `aria-label` MUST be provided
- `aria-label` renders on `<input>` element
- Screen readers announce `aria-label` value

**Keyboard Navigation**:
- Standard HTML radio behavior (browser-controlled):
  - Tab: Focus next/previous radio group
  - Arrow keys: Navigate within radio group
  - Space: Select focused radio

---

## Usage Examples

### Example 1: Basic Radio Group

```python
from flowbite_htmy.components import Radio

# Payment method selection
radios = [
    Radio(label="Credit Card", name="payment", value="credit_card", checked=True),
    Radio(label="PayPal", name="payment", value="paypal"),
    Radio(label="Bank Transfer", name="payment", value="bank_transfer"),
]

# Render in template
for radio in radios:
    await renderer.render(radio)
```

**Expected Output**: 3 radio buttons with "payment" name, only "Credit Card" checked

---

### Example 2: Validation States

```python
from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState

radios = [
    Radio(
        label="Express Shipping",
        name="shipping",
        value="express",
        validation_state=ValidationState.ERROR,
        helper_text="Not available in your region",
        disabled=True
    ),
    Radio(
        label="Standard Shipping",
        name="shipping",
        value="standard",
        validation_state=ValidationState.SUCCESS,
        helper_text="Free shipping on orders over $50",
        checked=True
    ),
]
```

**Expected Output**: Express shipping with red text/disabled, Standard shipping with green text/checked

---

### Example 3: HTMX Dynamic Update

```python
from flowbite_htmy.components import Radio

radio = Radio(
    label="Pickup in Store",
    name="delivery",
    value="pickup",
    hx_get="/update-pickup-locations",
    hx_target="#locations",
    hx_swap="innerHTML"
)
```

**Expected Output**: When selected, triggers GET request to `/update-pickup-locations`, swaps content into `#locations`

---

### Example 4: Empty Label with Accessibility

```python
from flowbite_htmy.components import Radio

# Visual color swatch, no text label
radio = Radio(
    label="",
    aria_label="Select red color",
    name="color",
    value="red",
    class_="w-8 h-8 rounded-full bg-red-500"
)
```

**Expected Output**: Radio with custom styling, no visible label text, screen reader announces "Select red color"

---

## Error Conditions

### Component Creation Errors

**Empty Label and aria-label**:
```python
Radio(label="", aria_label="")  # Raises ValueError
```
Error: `ValueError: Either 'label' or 'aria_label' must be provided for accessibility`

**Invalid ValidationState**:
```python
Radio(validation_state="invalid")  # Type error (mypy catches)
```
Error: Type checking fails - must use `ValidationState` enum

---

## Version Compatibility

- **Flowbite CSS**: 2.5.1 (classes contract matches this version)
- **htmy**: 0.1.0+
- **Python**: 3.11+
- **HTMX**: 2.0.2+ (for HTMX attributes)

---

## Testing Contract

### Test Coverage Requirements

Component implementation MUST pass tests covering:

1. ✅ Default rendering (minimal props)
2. ✅ All validation states (DEFAULT, ERROR, SUCCESS)
3. ✅ Disabled state
4. ✅ Checked state
5. ✅ Helper text rendering
6. ✅ HTMX attribute rendering
7. ✅ Custom classes merging
8. ✅ Empty label with aria-label (valid)
9. ✅ Empty label without aria-label (raises ValueError)
10. ✅ Auto-generated ID vs custom ID
11. ✅ Dark mode classes present in output

### Snapshot Testing

Use syrupy for snapshot testing of rendered HTML output to ensure consistency across changes.

---

## Breaking Changes Policy

**Backwards Compatibility**:
- Adding new optional props: ✅ Allowed (non-breaking)
- Changing default values: ⚠️ Breaking change (requires major version bump)
- Removing props: ❌ Breaking change (requires major version bump)
- Changing CSS classes: ⚠️ May be breaking (document in changelog)
- Changing HTML structure: ❌ Breaking change (requires major version bump)

**Deprecation Process**:
1. Mark deprecated prop with warning in docstring
2. Maintain backwards compatibility for 1 minor version
3. Remove in next major version

---

## Notes

- **No RadioGroup Component**: Each Radio is independent; grouping handled via `name` attribute
- **Stateless**: Component has no internal state; all state passed via props
- **Immutable**: Component is frozen dataclass (cannot modify after creation)
- **Type-Safe**: Full type hints with mypy strict mode compliance
