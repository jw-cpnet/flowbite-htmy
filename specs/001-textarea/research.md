# Research: Textarea Component Patterns

**Date**: 2025-11-14
**Purpose**: Extract proven patterns from existing components and Flowbite CSS for Textarea implementation

## 1. Validation State Pattern

**Source**: `src/flowbite_htmy/components/input.py`

### Type Definition

```python
ValidationState = Literal["success", "error"] | None
```

**Decision**: Use the same `Validation State` type from Input component for consistency.

### Label Classes by Validation State

Pattern extracted from Input component (lines 110-121):

```python
def _build_label_classes(self) -> str:
    """Build label CSS classes based on validation state."""
    builder = ClassBuilder("block mb-2 text-sm font-medium")

    if self.validation == "success":
        builder.add("text-green-700 dark:text-green-500")
    elif self.validation == "error":
        builder.add("text-red-700 dark:text-red-500")
    else:
        builder.add("text-gray-900 dark:text-white")

    return builder.build()
```

**Rationale**: This provides clear visual feedback for validation states that meets WCAG contrast requirements. Dark mode classes are always included (not conditional).

### Textarea Classes by Validation State

Pattern adapted from Input component (lines 123-155):

- **Success state**: Green border, green background tint, green text and placeholder
- **Error state**: Red border, red background tint, red text and placeholder
- **Default state**: Gray border, neutral background, standard text colors

**Classes to use**:
- Success: `bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 dark:border-green-500`
- Error: `bg-red-50 border border-red-500 text-red-900 placeholder-red-700 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500`
- Default: `border border-gray-300 text-gray-900 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white`

### Helper Text Rendering

Pattern extracted from Input component (lines 182-194):

```python
def _render_helper_text(self) -> Component:
    """Render helper text with appropriate styling."""
    text_classes = "mt-2 text-sm"

    if self.validation == "success":
        text_classes += " text-green-600 dark:text-green-500"
    elif self.validation == "error":
        text_classes += " text-red-600 dark:text-red-500"
    else:
        text_classes += " text-gray-500 dark:text-gray-400"

    return html.p(self.helper_text, class_=text_classes)
```

**Rationale**: Helper text color matches validation state for visual consistency. Always includes dark mode variants.

---

## 2. Required Field Indicator Pattern

**Source**: Clarification Q1 from spec.md, Radio/Checkbox component analysis

### Decision

When `required=True`, append asterisk to label text: `"Comment" → "Comment *"`

### Implementation Pattern

```python
def _get_display_label(self) -> str:
    """Get label text with asterisk if required."""
    if self.required:
        return f"{self.label} *"
    return self.label
```

**Rationale**:
- Matches WCAG best practices for visual required indicators
- Consistent with industry-standard form design (Bootstrap, Material UI, Flowbite)
- Simple implementation without additional ARIA complexity
- Clear visual signal for users

**Alternative Considered**: Red asterisk before label with aria-hidden
**Rejected Because**: More complex implementation, asterisk after label is more common pattern

---

## 3. Label and ID Association Pattern

**Source**: `src/flowbite_htmy/components/input.py` (lines 96-101)

### Pattern

```python
html.label(
    self.label,  # or self._get_display_label() for required asterisk
    **{"for": self.id},
    class_=label_classes,
)
```

**Key Points**:
- Use `**{"for": self.id}` syntax (not `for_=` ) to set HTML `for` attribute
- Label text comes first, then `for` attribute, then classes
- ID is required prop - no auto-generation needed based on existing pattern

### ARIA Label Handling

From spec.md FR-019: "System MUST raise ValueError when label is empty and no aria_label is provided"

**Implementation**:
```python
if not self.label and not self.aria_label:
    raise ValueError("Either label or aria_label must be provided for accessibility")
```

**Rationale**: Ensures accessibility - all form inputs need an accessible label for screen readers.

---

## 4. Flowbite CSS Classes for Textarea

**Source**: `flowbite-llms-full.txt` - Textarea section

### Base Textarea Classes

From Flowbite documentation example:

```html
<textarea
    id="message"
    rows="4"
    class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    placeholder="Write your thoughts here...">
</textarea>
```

### Class Breakdown

**Layout**: `block p-2.5 w-full`
- `block`: Display as block element
- `p-2.5`: Padding 2.5 units (Tailwind scale)
- `w-full`: Full width

**Typography**: `text-sm`
- `text-sm`: Small text size (14px)

**Default Colors**:
- Light mode: `text-gray-900 bg-gray-50 border-gray-300`
- Dark mode: `dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white`

**Shape**: `rounded-lg border`
- `rounded-lg`: Large border radius
- `border`: 1px border width

**Focus States**: `focus:ring-blue-500 focus:border-blue-500 dark:focus:ring-blue-500 dark:focus:border-blue-500`
- Blue ring and border on focus (light and dark modes)

### Disabled State Classes

Pattern from Input component:

```python
if self.disabled:
    builder.add("cursor-not-allowed bg-gray-100 dark:bg-gray-700")
```

**Classes**: `cursor-not-allowed bg-gray-100 dark:bg-gray-700`

**Rationale**: Visual feedback (different background) and UX feedback (cursor change) that field is disabled.

---

## 5. Edge Case Handling Patterns

### Rows Clamping (Clarification Q2)

**Decision**: Clamp rows to minimum of 1

**Implementation**:
```python
@property
def effective_rows(self) -> int:
    """Get effective rows value, clamped to minimum of 1."""
    return max(1, self.rows)
```

**Rationale**: Prevents broken UI states where textarea has zero or negative height. Browser-safe and predictable behavior.

**Alternative Considered**: Raise ValueError for invalid rows
**Rejected Because**: Too strict - clamping is more forgiving and prevents runtime errors

### Disabled vs Readonly Precedence (Clarification Q3)

**Decision**: Disabled takes precedence over readonly

**Implementation**:
```python
def _build_textarea_attrs(self) -> dict[str, Any]:
    attrs = {...}

    # Disabled overrides readonly
    if self.disabled:
        attrs["disabled"] = ""
        # Don't add readonly if disabled
    elif self.readonly:
        attrs["readonly"] = ""

    return attrs
```

**Rationale**:
- Matches HTML5 semantics where disabled is more restrictive
- Disabled prevents all interaction (no focus, no selection)
- Readonly allows focus and selection but not editing
- Precedence: disabled > readonly > normal

**Alternative Considered**: Raise ValueError when both set
**Rejected Because**: Too strict - developers may set both accidentally, silent precedence is more forgiving

### Disabled State - No Validation

From Input component pattern (lines 132-137):

```python
if self.disabled:
    builder.add("cursor-not-allowed bg-gray-100 dark:bg-gray-700")
else:
    # Normal background
    builder.add("bg-gray-50 dark:bg-gray-700")
    # ...then validation classes
```

**Pattern**: Disabled state overrides validation styling. Don't show success/error colors on disabled fields.

**Rationale**: Disabled fields aren't being validated, so validation styling is misleading.

---

## 6. HTMX Integration Pattern

**Source**: Existing component patterns (Button, Input, etc.)

### Pattern

Components accept HTMX attributes as optional props:

```python
# Props
hx_get: str | None = None
hx_post: str | None = None
hx_target: str | None = None
hx_swap: str | None = None
hx_trigger: str | None = None
```

### Attribute Building

```python
attrs: dict[str, Any] = {
    "id": self.id,
    # ... other standard attrs
}

# Add HTMX attributes if provided
if self.hx_get:
    attrs["hx_get"] = self.hx_get
if self.hx_post:
    attrs["hx_post"] = self.hx_post
# ... etc for other HTMX attrs
```

**Note**: htmy automatically converts underscores to hyphens in attribute names:
- `hx_get` → `hx-get`
- `hx_target` → `hx-target`

### Passthrough Attributes

Additional pattern for uncommon attributes via `attrs` dict:

```python
# From spec FR-014
attrs: dict[str, Any] | None = None

# In attribute building:
if self.attrs:
    textarea_attrs.update(self.attrs)
```

**Rationale**: Allows users to pass any HTML attribute not explicitly modeled as props (e.g., `autocomplete`, `spellcheck`, `maxlength`, etc.)

---

## Summary of Decisions

### Pattern Adoptions

1. ✅ **ValidationState**: Use `Literal["success", "error"] | None` from Input component
2. ✅ **Label Classes**: Tri-state pattern (success green, error red, default gray) with dark mode
3. ✅ **Helper Text**: Color-matched pattern from Input component
4. ✅ **Required Indicator**: Append asterisk to label text when `required=True`
5. ✅ **Flowbite CSS**: Base classes from official Flowbite textarea documentation
6. ✅ **Disabled State**: Cursor and background changes, overrides validation styling
7. ✅ **Rows Clamping**: Minimum value of 1, prevents UI breakage
8. ✅ **State Precedence**: Disabled overrides readonly
9. ✅ **HTMX Attributes**: Optional props pattern with underscore→hyphen conversion
10. ✅ **Passthrough Attrs**: `attrs` dict for additional HTML attributes

### Implementation Checklist

- [x] ValidationState type definition located (`Literal["success", "error"] | None`)
- [x] Label class building pattern extracted
- [x] Textarea class building pattern defined (adapted from Input)
- [x] Helper text rendering pattern extracted
- [x] Required field indicator pattern defined
- [x] Flowbite CSS classes documented
- [x] Edge case handling decisions documented (rows, disabled+readonly)
- [x] HTMX integration pattern documented
- [x] All NEEDS CLARIFICATION items resolved

### Ready for Phase 1

All research complete. Ready to proceed with:
1. Data model definition (dataclass structure)
2. Component API contract (props and methods)
3. Quickstart documentation (usage examples)
4. Agent context update

---

**Research Complete**: 2025-11-14
**Next Phase**: Phase 1 - Design & Contracts
