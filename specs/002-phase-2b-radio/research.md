# Research: Radio Component

**Feature**: 002-phase-2b-radio
**Date**: 2025-11-14

## Overview

Research findings for implementing the Radio component following TDD approach, examining existing component patterns (Input, Checkbox), Flowbite radio button documentation, and clarifications from the specification session.

## Key Decisions

### 1. Validation State Management

**Decision**: Individual radio buttons each have independent validation states (not group-level)

**Rationale**:
- Provides maximum flexibility for complex forms where individual options may have conditional validation
- Example use case: "Express shipping not available in your region" - specific radio option shows error
- Aligns with independent Radio component design (no RadioGroup wrapper)
- Matches pattern used by Checkbox component

**Alternatives Considered**:
- **Group-level validation**: All radios with same `name` share validation state
  - Rejected: Less flexible, doesn't support conditional option availability
  - Trade-off: Simpler API but can't show per-option feedback
- **Hybrid approach**: Support both individual and group-level
  - Rejected: Adds complexity, unclear which takes precedence
  - Trade-off: Maximum flexibility but confusing API surface

**Implementation Notes**:
- Each Radio instance accepts `validation_state` parameter
- Developers manually apply validation state to each radio as needed
- No automatic synchronization of validation states across name groups

---

### 2. HTMX Trigger Behavior

**Decision**: HTMX requests trigger on `change` event when radio is selected

**Rationale**:
- Most common and expected behavior for radio buttons in interactive forms
- Matches standard UX patterns where selecting a radio option updates UI dynamically
- Examples: loading dependent fields, updating prices, filtering options
- Consistent with Flowbite's HTMX integration examples
- Aligns with how other form components (Input, Checkbox) handle HTMX

**Alternatives Considered**:
- **Manual trigger only**: Developer controls via hx-trigger attribute
  - Rejected: Requires boilerplate for common case
  - Trade-off: More control but less convenient
- **Both approaches**: Default to `change`, allow override via hx-trigger
  - Rejected: Adds complexity, unclear precedence rules
  - Trade-off: Most flexible but harder to document/test

**Implementation Notes**:
- HTMX attributes (hx_get, hx_post, etc.) render on `<input type="radio">` element
- Default trigger is `change` event (implicit in HTMX for form inputs)
- No need to explicitly set `hx-trigger="change"` - HTMX does this automatically for inputs

---

### 3. Empty Label Handling

**Decision**: Allow empty label text when `aria-label` attribute is provided

**Rationale**:
- Supports advanced use cases: icon-only radios, graphical options, custom layouts
- Maintains accessibility: `aria-label` provides screen reader context
- Follows HTML best practices: labels can be visually hidden but accessibility must exist
- Provides flexibility without sacrificing WCAG 2.1 Level AA compliance

**Alternatives Considered**:
- **Require label text**: Raise error if empty
  - Rejected: Too restrictive, prevents valid advanced use cases
  - Trade-off: Simpler but less flexible
- **Allow empty without restriction**: No aria-label requirement
  - Rejected: Violates accessibility standards
  - Trade-off: Maximum flexibility but fails WCAG compliance

**Implementation Notes**:
- `label` parameter is optional (can be empty string or omitted)
- When `label` is empty, `aria_label` parameter MUST be provided
- Component should raise ValueError if both `label` and `aria_label` are empty
- Label text renders inside `<label>` element; aria-label renders on `<input>` element

---

## Best Practices Research

### Flowbite Radio Button Patterns

**Examined**: Flowbite CSS 2.5.1 radio button documentation and examples

**Key Findings**:
1. **Base Classes**: `w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600`
2. **Label Classes**: `ms-2 text-sm font-medium text-gray-900 dark:text-gray-300`
3. **Helper Text Classes**: `text-sm text-gray-500 dark:text-gray-400` (default), `text-sm text-red-600 dark:text-red-500` (error), `text-sm text-green-600 dark:text-green-500` (success)
4. **Disabled Classes**: Add `disabled:opacity-50 disabled:cursor-not-allowed` to input, `text-gray-400 dark:text-gray-500` to label
5. **Container Structure**: Each radio button is wrapped in a flex container for proper alignment

**Validation State Colors**:
- **Default**: No special coloring (base classes)
- **Error**: `text-red-600 dark:text-red-500` for label, `border-red-500 dark:border-red-600` for input
- **Success**: `text-green-600 dark:text-green-500` for label, `border-green-500 dark:border-green-600` for input

---

### Component Pattern Analysis (Input & Checkbox)

**Examined**: `src/flowbite_htmy/components/input.py` and `src/flowbite_htmy/components/checkbox.py`

**Key Patterns Identified**:

1. **Class Structure**:
   ```python
   @dataclass(frozen=True, kw_only=True)
   class Radio:
       label: str = ""
       name: str = ""
       value: str = ""
       checked: bool = False
       disabled: bool = False
       validation_state: ValidationState = ValidationState.DEFAULT
       helper_text: str = ""
       aria_label: str = ""
       class_: str = ""
       # HTMX attributes
       hx_get: str | None = None
       hx_post: str | None = None
       # ... other hx attributes

       def htmy(self, context: Context) -> Component:
           ...
   ```

2. **ID Generation Pattern** (from Checkbox):
   - Use `id` prop if provided
   - Otherwise generate unique ID using counter or UUID
   - Pattern: `f"radio-{uuid.uuid4().hex[:8]}"` or module-level counter

3. **Class Building Pattern**:
   ```python
   def _build_input_classes(self) -> str:
       builder = ClassBuilder("w-4 h-4 bg-gray-100 border-gray-300")
       builder.add("focus:ring-blue-500 focus:ring-2")
       builder.add("dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600")

       # Validation state colors
       if self.validation_state == ValidationState.ERROR:
           builder.add("text-red-600 border-red-500 dark:border-red-600")
       elif self.validation_state == ValidationState.SUCCESS:
           builder.add("text-green-600 border-green-500 dark:border-green-600")
       else:
           builder.add("text-blue-600")

       if self.disabled:
           builder.add("disabled:opacity-50 disabled:cursor-not-allowed")

       return builder.build()
   ```

4. **HTMX Attribute Handling** (from Input):
   - Pass HTMX props directly to input element
   - Convert underscores to hyphens automatically (htmy does this)
   - Example: `hx_get="/endpoint"` → `hx-get="/endpoint"`

5. **Validation State Enum** (likely in `src/flowbite_htmy/types/validation.py`):
   ```python
   from enum import Enum

   class ValidationState(str, Enum):
       DEFAULT = "default"
       ERROR = "error"
       SUCCESS = "success"
   ```

---

## Technical Decisions

### Auto-ID Generation Strategy

**Decision**: Use module-level counter for predictable, testable IDs

**Rationale**:
- Predictable IDs in tests (easier snapshot testing)
- Deterministic behavior (no UUID randomness)
- Matches Checkbox component pattern

**Implementation**:
```python
_radio_counter = 0

def _generate_radio_id() -> str:
    global _radio_counter
    _radio_counter += 1
    return f"radio-{_radio_counter}"
```

---

### Validation State Application

**Decision**: Validation state affects both label and input element classes

**Rationale**:
- Visual feedback on both label text color and input border color
- Matches Flowbite design patterns
- Consistent with Input and Checkbox components

**Implementation**:
- Input classes: Border color changes based on validation state
- Label classes: Text color changes based on validation state
- Helper text classes: Text color matches validation state

---

### Helper Text Positioning

**Decision**: Helper text appears below the radio button within the same container

**Rationale**:
- Follows Flowbite layout patterns
- Keeps helper text associated with individual radio button
- Allows different helper text for each radio in a group

**Implementation**:
- Container div wraps label + input + helper text
- Helper text is a separate `<p>` element with appropriate margin/padding
- Helper text color matches validation state

---

## Integration Points

### ClassBuilder Utility

**Location**: `src/flowbite_htmy/base/classes.py`

**Usage**:
- `.add(classes: str)` - Add classes unconditionally
- `.add_if(condition: bool, classes: str)` - Add classes conditionally
- `.merge(custom_classes: str)` - Merge with custom classes from `class_` prop
- `.build() -> str` - Build final class string

---

### ThemeContext

**Location**: `src/flowbite_htmy/base/context.py`

**Usage**:
```python
theme = ThemeContext.from_context(context)
# Note: Dark mode classes are ALWAYS included in class strings
# ThemeContext is mainly for reference; dark: prefix handles activation
```

---

### ValidationState Enum

**Location**: `src/flowbite_htmy/types/validation.py` (may need to be created)

**Definition**:
```python
from enum import Enum

class ValidationState(str, Enum):
    """Validation state for form components."""
    DEFAULT = "default"
    ERROR = "error"
    SUCCESS = "success"
```

**Export**: Add to `src/flowbite_htmy/types/__init__.py`

---

## Testing Strategy

### Test Coverage Requirements

Following TDD principle, tests MUST cover:

1. **Basic Rendering** (User Story 1 - P1):
   - Default radio button with label
   - Radio with name and value attributes
   - Checked radio button
   - Multiple radios with same name (mutual exclusivity tested in showcase, not unit tests)
   - Auto-generated ID when not provided
   - Custom ID when provided

2. **Validation States** (User Story 2 - P2):
   - Default validation state (no special styling)
   - Error validation state (red colors)
   - Success validation state (green colors)
   - Helper text rendering
   - Helper text color matches validation state

3. **Disabled & Dark Mode** (User Story 3 - P3):
   - Disabled radio button (opacity, cursor)
   - Disabled + checked state
   - Dark mode classes present in output (always included)
   - Custom classes merge correctly

4. **HTMX Integration**:
   - HTMX attributes render on input element
   - Multiple HTMX attributes combine correctly

5. **Edge Cases**:
   - Empty label with aria-label (valid)
   - Empty label without aria-label (should raise ValueError)
   - Very long label text (wraps gracefully)
   - No name attribute (valid but warning in docs)

---

## Open Questions / Deferred

None - all clarifications resolved in specification session.

---

## References

- Flowbite Radio Documentation: https://flowbite.com/docs/forms/radio/
- Existing Input Component: `src/flowbite_htmy/components/input.py`
- Existing Checkbox Component: `src/flowbite_htmy/components/checkbox.py`
- ClassBuilder Utility: `src/flowbite_htmy/base/classes.py`
- WCAG 2.1 Radio Button Guidelines: https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html
