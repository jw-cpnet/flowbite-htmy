# Textarea Component API Contract

**Version**: 1.0.0
**Date**: 2025-11-14
**Status**: Draft

## Component Signature

```python
@dataclass(frozen=True, kw_only=True)
class Textarea:
    """Multi-line text input component with Flowbite styling."""

    # Required
    id: str
    label: str

    # Optional - Content
    value: str | None = None
    placeholder: str | None = None
    name: str | None = None

    # Optional - Sizing
    rows: int = 4

    # Optional - States
    required: bool = False
    disabled: bool = False
    readonly: bool = False

    # Optional - Validation
    validation: Literal["success", "error"] | None = None
    helper_text: str | None = None

    # Optional - Styling
    class_: str = ""

    # Optional - Integration
    attrs: dict[str, Any] | None = None
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_patch: str | None = None
    hx_delete: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
```

## Public Methods

### `htmy(context: Context) -> Component`

**Purpose**: Render the textarea component as an htmy Component tree.

**Parameters**:
- `context` (Context): htmy rendering context containing theme information

**Returns**:
- `Component`: htmy component tree representing the textarea with label and optional helper text

**Behavior**:
1. Retrieves theme from context via `ThemeContext.from_context(context)`
2. Builds label with required indicator if `required=True`
3. Builds textarea element with appropriate classes based on validation state and disabled/readonly states
4. Optionally appends helper text paragraph if `helper_text` is provided
5. Wraps all elements in a div with `class_` applied

**Rendering Structure**:
```html
<div class="{class_}">
  <label for="{id}" class="{label_classes}">{label with optional asterisk}</label>
  <textarea id="{id}" rows="{rows}" class="{textarea_classes}" ...>{value}</textarea>
  <!-- Optional helper text -->
  <p id="{id}-helper" class="{helper_classes}">{helper_text}</p>
</div>
```

## Internal Methods (Private)

### `_get_display_label() -> str`

**Purpose**: Get label text with asterisk appended if required.

**Returns**: Label string with " *" suffix if `required=True`, otherwise unchanged label.

---

### `_build_label_classes() -> str`

**Purpose**: Build CSS classes for the label element based on validation state.

**Returns**: Space-separated string of CSS classes for label.

**Classes**:
- Base: `"block mb-2 text-sm font-medium"`
- Success: `"text-green-700 dark:text-green-500"`
- Error: `"text-red-700 dark:text-red-500"`
- Default: `"text-gray-900 dark:text-white"`

---

### `_build_textarea_classes(theme: ThemeContext) -> str`

**Purpose**: Build CSS classes for the textarea element based on state and validation.

**Parameters**:
- `theme` (ThemeContext): Theme context (for pattern consistency, not currently used for conditional logic)

**Returns**: Space-separated string of CSS classes for textarea.

**Class Categories**:
1. **Base**: `"block p-2.5 w-full text-sm rounded-lg border"`
2. **Focus**: `"focus:ring-blue-500 focus:border-blue-500 dark:focus:ring-blue-500 dark:focus:border-blue-500"`
3. **Disabled** (if `disabled=True`): `"cursor-not-allowed bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400"`
4. **Validation** (if not disabled):
   - Success: `"bg-green-50 border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 dark:border-green-500"`
   - Error: `"bg-red-50 border-red-500 text-red-900 placeholder-red-700 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500"`
   - Default: `"bg-gray-50 text-gray-900 border-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"`

---

### `_build_textarea_attrs() -> dict[str, Any]`

**Purpose**: Build HTML attributes dictionary for the textarea element.

**Returns**: Dictionary of HTML attributes.

**Attributes Added**:
- Always: `id`, `rows` (clamped to min 1)
- Conditional:
  - `name` (if provided)
  - `placeholder` (if provided)
  - `required` (if `required=True`)
  - `disabled` (if `disabled=True` - takes precedence over readonly)
  - `readonly` (if `readonly=True` and not disabled)
  - `aria_describedby` (if `helper_text` is provided, set to `{id}-helper`)
  - `hx_*` attributes (if any HTMX props provided)
  - Custom attributes from `attrs` dict (merged last, can override)

**Special Logic**:
- Rows clamping: `effective_rows = max(1, self.rows)`
- Disabled precedence: If `disabled=True`, `readonly` attribute is not added

---

### `_render_helper_text() -> Component`

**Purpose**: Render helper text paragraph with validation-appropriate styling.

**Returns**: htmy Component (html.p element).

**Classes**:
- Base: `"mt-2 text-sm"`
- Success: `"text-green-600 dark:text-green-500"`
- Error: `"text-red-600 dark:text-red-500"`
- Default: `"text-gray-500 dark:text-gray-400"`

**Attributes**:
- `id`: Set to `{component.id}-helper` for ARIA association

## Prop Behaviors

### Required Props

| Prop | Type | Behavior |
|------|------|----------|
| `id` | str | Used for textarea ID and label's `for` attribute. Must be unique on page. |
| `label` | str | Displayed as label text. Asterisk appended if `required=True`. |

### Content Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `value` | str \| None | None | Pre-fills textarea with content. Empty string if None. |
| `placeholder` | str \| None | None | Displays placeholder text when textarea is empty. |
| `name` | str \| None | None | Sets name attribute for form submission. Optional. |

### Sizing Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `rows` | int | 4 | Number of visible text lines. Clamped to minimum of 1. |

### State Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `required` | bool | False | If True, appends " *" to label and adds `required` HTML attribute. |
| `disabled` | bool | False | If True, grays out textarea, prevents interaction, overrides `readonly`. |
| `readonly` | bool | False | If True and `disabled` is False, prevents editing but allows focus/selection. |

### Validation Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `validation` | ValidationState | None | Controls border/text colors. `"success"` = green, `"error"` = red, None = default. |
| `helper_text` | str \| None | None | Displays help text below textarea. Color matches validation state. |

### Styling Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `class_` | str | "" | Additional CSS classes applied to wrapper div. |

### Integration Props

| Prop | Type | Default | Behavior |
|------|------|---------|----------|
| `attrs` | dict[str, Any] \| None | None | Passthrough HTML attributes merged into textarea element. |
| `hx_get` | str \| None | None | HTMX GET request URL. |
| `hx_post` | str \| None | None | HTMX POST request URL. |
| `hx_put` | str \| None | None | HTMX PUT request URL. |
| `hx_patch` | str \| None | None | HTMX PATCH request URL. |
| `hx_delete` | str \| None | None | HTMX DELETE request URL. |
| `hx_target` | str \| None | None | HTMX target element selector. |
| `hx_swap` | str \| None | None | HTMX swap strategy. |
| `hx_trigger` | str \| None | None | HTMX trigger event. |

## Validation Rules

1. **ID Required**: Component cannot be instantiated without an `id` (enforced by dataclass).
2. **Label Required**: Component cannot be instantiated without a `label` (enforced by dataclass).
3. **Rows Minimum**: Rows value is clamped to minimum of 1 regardless of input.
4. **Disabled Precedence**: If both `disabled` and `readonly` are True, only `disabled` attribute is rendered.
5. **Validation State Type**: `validation` must be `"success"`, `"error"`, or `None` (enforced by mypy via Literal type).

## Error Handling

**No Runtime Errors**: The component does not raise exceptions during rendering. All edge cases are handled gracefully:
- Invalid rows (≤0) → Clamped to 1
- Disabled + readonly → Disabled takes precedence
- Empty helper_text → Helper paragraph not rendered
- Empty value → Empty textarea content

**Type Errors**: Invalid prop types will be caught by mypy during development (strict mode enabled).

## Usage Examples

See [quickstart.md](../quickstart.md) for comprehensive usage examples.

---

**API Contract Version**: 1.0.0
**Last Updated**: 2025-11-14
**Status**: Ready for implementation
