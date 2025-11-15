# Component Quality Checklist

**Contract Version**: 1.0.0
**Last Updated**: 2025-11-16
**Applies To**: All htmy components in flowbite-htmy library
**Authority**: Derived from constitution (`.specify/memory/constitution.md`) and CLAUDE.md guidance

---

## Purpose

This checklist defines the quality standards that all flowbite-htmy components must meet. It serves as a validation contract for reviewing existing components and implementing new ones.

**Use Cases**:
1. **Component Review** - Validate early components against established patterns
2. **New Component Implementation** - Ensure consistency from the start
3. **Pull Request Review** - Objective quality gate for code review
4. **Refactoring Validation** - Confirm improvements maintain standards

**Reference Implementations**:
- **Toast** (`src/flowbite_htmy/components/toast.py`) - Exemplar for all patterns
- **Modal** (`src/flowbite_htmy/components/modal.py`) - Complex component reference
- **Select** (`src/flowbite_htmy/components/select.py`) - Form component reference

---

## Quality Criteria

### 1. Type Safety ⚡ CRITICAL

Full type coverage with mypy strict mode compliance.

#### Requirements

- [ ] **All props have explicit type hints**
  - No missing types on dataclass fields
  - Use union types for optional values: `str | None`, not bare `Optional`
  - Enums for constrained values (Color, Size, ButtonVariant)

- [ ] **`htmy()` method returns `Component` type**
  - Signature: `def htmy(self, context: Context) -> Component:`
  - Return type explicitly declared, not inferred

- [ ] **`context: Context` parameter typed**
  - All component methods taking context must type it
  - Import from `htmy` package: `from htmy import Context`

- [ ] **No `Any` types without justification**
  - Use specific types or union types instead
  - If `Any` required, document why in comment

- [ ] **Component passes `mypy --strict`**
  - Run: `mypy src/flowbite_htmy/components/{component}.py`
  - Zero errors or warnings
  - Check return types, parameter types, attribute access

#### Example: Correct Type Hints

```python
from dataclasses import dataclass
from htmy import Component, Context
from flowbite_htmy.types import Color, Size

@dataclass(frozen=True, kw_only=True)
class ExampleComponent:
    """Example component with proper type hints."""

    # Required prop - no default
    label: str

    # Optional prop with union type
    icon: str | None = None

    # Enum type for constrained values
    color: Color = Color.PRIMARY
    size: Size = Size.MD

    # HTMX attributes - all optional
    hx_get: str | None = None
    hx_post: str | None = None

    # Custom classes
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render component to htmy Component."""
        # Implementation...
```

#### Validation Command

```bash
mypy --strict src/flowbite_htmy/components/{component}.py
```

**Pass Criteria**: Zero errors, zero warnings.

---

### 2. HTMX Integration 🔌

Support for HTMX attributes appropriate to component type.

#### Requirements by Component Type

**Interactive Components** (Button, Link, Form elements):
- [ ] **Minimum HTMX support**: `hx_get`, `hx_post`, `hx_target`
- [ ] **Standard HTMX support**: Add `hx_swap`, `hx_trigger`
- [ ] **Full HTMX support** (recommended): All 10 attributes

**Notification Components** (Toast, Alert, Banner):
- [ ] **Action buttons** support full HTMX (if component has actions)
- [ ] **Container component** may skip HTMX (passive display)

**Display Components** (Badge, Avatar, Indicator):
- [ ] HTMX support optional (semantic appropriateness)

**Form Components** (Input, Select, Textarea):
- [ ] HTMX optional but recommended for dynamic forms

#### Full HTMX Attribute Set

All HTMX attributes must follow this pattern:

```python
# HTTP Methods
hx_get: str | None = None
hx_post: str | None = None
hx_put: str | None = None
hx_delete: str | None = None
hx_patch: str | None = None

# Request Configuration
hx_target: str | None = None
hx_swap: str | None = None
hx_trigger: str | None = None
hx_select: str | None = None

# URL Behavior
hx_push_url: str | bool | None = None  # Note: bool for true/false values
```

#### Implementation Pattern

```python
def htmy(self, context: Context) -> Component:
    # Build attrs dict for HTMX passthrough
    attrs = {
        "hx-get": self.hx_get,
        "hx-post": self.hx_post,
        "hx-target": self.hx_target,
        "hx-swap": self.hx_swap,
        "hx-trigger": self.hx_trigger,
        # ... remaining HTMX attrs
    }

    return html.button(
        self.label,
        class_=classes,
        **{k: v for k, v in attrs.items() if v is not None}  # Filter None values
    )
```

#### Reference Example

See `toast.py:22-31` (ToastActionButton) for complete HTMX integration pattern.

---

### 3. Dark Mode Support 🌙 CRITICAL

All color classes must include dark mode variants, always included (not conditional).

#### Requirements

- [ ] **All color classes include `dark:` variants**
  - Every `bg-*`, `text-*`, `border-*` class needs dark equivalent
  - Example: `bg-white` → add `dark:bg-gray-800`

- [ ] **Dark classes always included (not conditional)**
  - ❌ WRONG: `if theme.dark_mode: builder.add("dark:bg-gray-800")`
  - ✅ CORRECT: Always include in ClassBuilder: `"bg-white dark:bg-gray-800"`
  - Tailwind's `dark:` prefix handles activation automatically

- [ ] **Uses `ThemeContext.from_context(context)` if needed**
  - Only if component needs theme-specific logic beyond classes
  - Example: Custom dark mode color overrides

- [ ] **Tested in both light and dark modes**
  - Verify dark classes present in HTML output
  - Visual test in showcase app with dark mode toggle

#### Pattern: Always-Included Dark Mode

```python
from flowbite_htmy.base import ClassBuilder

def _build_classes(self, theme: ThemeContext) -> str:
    # ✅ CORRECT - Dark classes always included
    builder = ClassBuilder(
        "flex items-center p-4 "
        "text-gray-500 bg-white "
        "dark:text-gray-400 dark:bg-gray-800"  # Always here!
    )

    # Add variant-specific dark classes
    builder.add_from_dict({
        Color.PRIMARY: "bg-blue-600 dark:bg-blue-700",
        Color.SUCCESS: "bg-green-600 dark:bg-green-700",
        # ...
    }, self.color)

    return builder.merge(self.class_)
```

#### Anti-Pattern: Conditional Dark Mode

```python
# ❌ WRONG - Don't do this!
dark_classes = self._get_dark_classes()
if theme.dark_mode and dark_classes:  # ANTI-PATTERN
    builder.add(dark_classes)
```

**Why It's Wrong**: Tailwind's dark mode is activated by the `dark` class on `<html>`. The `dark:` prefix in classes is inert until activated. Conditional inclusion breaks server-side rendering when theme changes client-side.

#### Validation

1. **Code Review**: Search for `if theme.dark_mode` or `if dark_mode` - should not exist
2. **HTML Output Test**: All components should have `dark:` classes in rendered HTML
3. **Visual Test**: Toggle dark mode in showcase app, verify appearance

**Reference**: CLAUDE.md lines 97-104 (Dark Mode Classes section)

---

### 4. ClassBuilder Usage 🔧

Consistent use of ClassBuilder utility for class string construction.

#### Requirements

- [ ] **Uses `ClassBuilder` for class string construction**
  - Import: `from flowbite_htmy.base import ClassBuilder`
  - All components must use ClassBuilder, not manual string concatenation

- [ ] **Base classes added first via constructor**
  - Pattern: `ClassBuilder("base classes here")`
  - Base classes are always-present structural classes

- [ ] **Conditional classes use `.add_if()`**
  - Pattern: `builder.add_if(condition, "conditional-classes")`
  - Example: `builder.add_if(self.pill, "rounded-full")`

- [ ] **Custom classes merged last via `.merge(self.class_)`**
  - Always the final operation before returning
  - Allows user-provided classes to override defaults

#### Standard Pattern

```python
from flowbite_htmy.base import ClassBuilder

def _build_classes(self, theme: ThemeContext) -> str:
    # Step 1: Base classes (always present)
    builder = ClassBuilder(
        "inline-flex items-center justify-center "
        "font-medium rounded-lg "
        "dark:focus:ring-gray-700"
    )

    # Step 2: Add variant classes from dict
    builder.add_from_dict({
        Color.PRIMARY: "text-white bg-blue-700 hover:bg-blue-800",
        Color.SECONDARY: "text-gray-900 bg-gray-100 hover:bg-gray-200",
    }, self.color)

    # Step 3: Add size classes from dict
    builder.add_from_dict({
        Size.SM: "text-sm px-3 py-2",
        Size.MD: "text-base px-5 py-2.5",
    }, self.size)

    # Step 4: Conditional classes
    builder.add_if(self.pill, "rounded-full")
    builder.add_if(self.disabled, "opacity-50 cursor-not-allowed")

    # Step 5: Merge custom classes (ALWAYS LAST)
    return builder.merge(self.class_)
```

#### ClassBuilder API Reference

| Method | Signature | Purpose |
|--------|-----------|---------|
| `__init__` | `ClassBuilder(base: str)` | Initialize with base classes |
| `.add()` | `add(classes: str) -> Self` | Add classes unconditionally |
| `.add_if()` | `add_if(condition: bool, classes: str) -> Self` | Add classes if condition true |
| `.add_from_dict()` | `add_from_dict(mapping: dict, key: Any) -> Self` | Add classes from dict lookup |
| `.merge()` | `merge(custom: str) -> str` | Merge custom classes, return final string |
| `.build()` | `build() -> str` | Return final string (use `.merge()` instead) |

#### Validation

- [ ] No manual string concatenation: `"class1 " + "class2"` or `f"{base} {variant}"`
- [ ] No list joining: `" ".join([base, variant, custom])`
- [ ] Every component ends with `.merge(self.class_)`

---

### 5. Documentation 📚

Comprehensive docstrings with examples for all public components and props.

#### Requirements

- [ ] **Class has comprehensive docstring**
  - Summary line describing component purpose
  - Optional extended description explaining use cases
  - References to related components or Flowbite docs

- [ ] **Docstring includes usage examples**
  - Minimum: 1 basic example showing default usage
  - Recommended: 2-3 examples covering common variants
  - Advanced: Edge case examples (disabled, loading, etc.)

- [ ] **All public props have docstrings**
  - Every dataclass field needs docstring
  - Format: `"""Prop description."""` immediately after field
  - Include default behavior if non-obvious

- [ ] **Special patterns or gotchas documented**
  - Example: "Use `icon_only=True` to hide label for icon buttons"
  - Example: "HTMX attributes only applied if component is interactive"

#### Example: Comprehensive Documentation

```python
from dataclasses import dataclass
from htmy import Component, Context

@dataclass(frozen=True, kw_only=True)
class Button:
    """Flowbite button component for interactive actions.

    Supports multiple variants (default, outline, gradient), sizes,
    colors, and full HTMX integration for dynamic interactions.

    Examples:
        Basic button:
        >>> Button(label="Click me")

        Button with HTMX:
        >>> Button(
        ...     label="Load more",
        ...     hx_get="/api/items",
        ...     hx_target="#items-list",
        ...     hx_swap="beforeend"
        ... )

        Icon-only button:
        >>> Button(
        ...     label="Delete",
        ...     icon="trash",
        ...     icon_only=True,
        ...     color=Color.DANGER
        ... )
    """

    label: str
    """Button text label (required)."""

    icon: str | None = None
    """Optional icon name (e.g., 'home', 'trash', 'plus').

    Uses icon system from flowbite_htmy.icons. If provided with
    icon_only=True, label is visually hidden but preserved for a11y.
    """

    color: Color = Color.PRIMARY
    """Button color variant (default: PRIMARY).

    Available colors: PRIMARY, SECONDARY, SUCCESS, DANGER, WARNING, INFO.
    Use Color.NONE for custom styling via class_ prop.
    """

    disabled: bool = False
    """Whether button is disabled (default: False).

    Disabled buttons show reduced opacity and cursor-not-allowed.
    HTMX attributes are still rendered but button is non-interactive.
    """

    # ... remaining props ...

    def htmy(self, context: Context) -> Component:
        """Render button to htmy Component."""
        # Implementation...
```

#### Documentation Quality Levels

**Excellent (95-100%)** - Toast, Modal, Select:
- Class docstring with 3+ examples
- All props documented with detailed explanations
- Edge cases and gotchas documented

**Good (90-95%)** - Badge, Alert, Avatar:
- Class docstring with 1-2 examples
- All props documented
- Basic usage clear

**Acceptable (85-90%)** - Early implementations:
- Class docstring with 1 example
- Most props documented
- Minimal but functional

**Needs Improvement (<85%)**:
- Missing examples
- Incomplete prop docstrings
- Unclear usage

#### Validation

```bash
# Check for missing docstrings
python -c "
import ast
with open('src/flowbite_htmy/components/{component}.py') as f:
    tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if not ast.get_docstring(node):
                print(f'Class {node.name} missing docstring')
"
```

---

### 6. Prop Conventions 🏷️

Consistent naming and ordering of component properties.

#### Requirements

- [ ] **Reserved words use trailing underscore**
  - `class_` not `class` (Python reserved word)
  - `type_` not `type` (Python reserved word)
  - `id_` not `id` (Python built-in)
  - Pattern: `{word}_` for any Python keyword or built-in

- [ ] **Boolean props default to `False` (or sensible default)**
  - Example: `disabled: bool = False`
  - Example: `dismissible: bool = False`
  - Exceptions: If "enabled" is more natural than "disabled"

- [ ] **Required props come before optional props**
  - Required: No default value
  - Optional: Has default value
  - Use `kw_only=True` on dataclass to allow any order in calls

- [ ] **Consistent naming with other components**
  - Use established names: `class_`, `attrs`, `color`, `size`
  - Don't invent new names: `custom_class`, `css_class`, `style_class`

#### Example: Correct Prop Ordering

```python
@dataclass(frozen=True, kw_only=True)
class Alert:
    """Alert component."""

    # REQUIRED PROPS (no defaults)
    message: str | Component

    # OPTIONAL PROPS - Semantic/behavior
    title: str | None = None
    color: Color = Color.INFO
    bordered: bool = False
    dismissible: bool = False

    # OPTIONAL PROPS - Content
    icon: str | None = None

    # OPTIONAL PROPS - HTMX (if applicable)
    hx_get: str | None = None
    hx_post: str | None = None

    # OPTIONAL PROPS - Styling (always last)
    id_: str | None = None  # Note trailing underscore
    class_: str = ""        # Note trailing underscore
```

#### Prop Naming Standards

| Purpose | Prop Name | Type | Default |
|---------|-----------|------|---------|
| Custom CSS classes | `class_` | `str` | `""` |
| Component ID | `id_` | `str \| None` | `None` |
| Additional attributes | `attrs` | `dict[str, Any]` | `field(default_factory=dict)` |
| Element type | `type_` | `str` | Component-specific |
| Color variant | `color` | `Color` | `Color.PRIMARY` or appropriate |
| Size variant | `size` | `Size` | `Size.MD` |
| Disabled state | `disabled` | `bool` | `False` |

#### Validation

- [ ] No props named `class`, `type`, `id` without trailing underscore
- [ ] All boolean props default to `False` (or documented exception)
- [ ] Props ordered: required → optional semantic → HTMX → styling

---

### 7. Test Coverage 🧪 CRITICAL

Comprehensive test suite with >90% coverage.

#### Requirements

- [ ] **>90% coverage (enforced by pytest config)**
  - Run: `pytest --cov=src/flowbite_htmy/components/{component}`
  - Must achieve 90%+ or build fails
  - Check untested lines: `--cov-report=term-missing`

- [ ] **Tests for default rendering**
  - Basic test: Component with minimal required props renders
  - Validates HTML structure, base classes, default behavior

- [ ] **Tests for all variants**
  - Color variants: Test each Color enum value
  - Size variants: Test each Size enum value
  - Style variants: Test outline, gradient, pill, etc.

- [ ] **Tests for HTMX attributes**
  - Each supported HTMX attr has test
  - Verify attribute passthrough to HTML
  - Test attribute filtering (None values excluded)

- [ ] **Tests for dark mode**
  - Verify dark classes always present in output
  - Test with `dark_context` fixture (see conftest.py)

- [ ] **Tests for custom classes**
  - Verify `class_` prop merges correctly
  - Test custom classes don't override required structural classes

- [ ] **Edge case tests**
  - None values for optional props
  - Empty strings
  - Conflicting props (e.g., `icon_only=True` without `icon`)
  - Boundary values (very long labels, etc.)

#### Test Structure Pattern

```python
import pytest
from flowbite_htmy.components import ExampleComponent
from flowbite_htmy.types import Color, Size

@pytest.mark.asyncio
class TestExampleComponent:
    """Test suite for ExampleComponent."""

    async def test_default_rendering(self, renderer):
        """Test component renders with default props."""
        component = ExampleComponent(label="Test")
        html = await renderer.render(component)

        assert "Test" in html
        assert "base-class" in html

    async def test_color_variants(self, renderer):
        """Test all color variants render correctly."""
        for color in Color:
            component = ExampleComponent(label="Test", color=color)
            html = await renderer.render(component)
            # Color-specific assertions...

    async def test_htmx_attributes(self, renderer):
        """Test HTMX attribute passthrough."""
        component = ExampleComponent(
            label="Test",
            hx_get="/api/test",
            hx_target="#target"
        )
        html = await renderer.render(component)

        assert 'hx-get="/api/test"' in html
        assert 'hx-target="#target"' in html

    async def test_dark_mode(self, renderer):
        """Test dark mode classes always included."""
        component = ExampleComponent(label="Test")
        html = await renderer.render(component)

        assert "dark:" in html  # Verify dark classes present

    async def test_custom_classes(self, renderer):
        """Test custom class merging."""
        component = ExampleComponent(label="Test", class_="custom-class")
        html = await renderer.render(component)

        assert "custom-class" in html
        assert "base-class" in html  # Base classes preserved

    async def test_edge_cases(self, renderer):
        """Test edge cases and boundary conditions."""
        # None values
        component = ExampleComponent(label="Test", icon=None)
        html = await renderer.render(component)
        assert "icon" not in html.lower()

        # Empty strings
        component = ExampleComponent(label="", class_="")
        html = await renderer.render(component)
        # Assertions for empty state...
```

#### Coverage Validation

```bash
# Run coverage for specific component
pytest --cov=src/flowbite_htmy/components/button tests/test_components/test_button.py

# Generate HTML coverage report
pytest --cov=src/flowbite_htmy/components --cov-report=html
open htmlcov/index.html

# Check for untested lines
pytest --cov=src/flowbite_htmy/components/button --cov-report=term-missing
```

#### Snapshot Testing (Optional but Recommended)

```python
async def test_snapshot_default(self, renderer, snapshot):
    """Test default rendering matches snapshot."""
    component = ExampleComponent(label="Test")
    html = await renderer.render(component)
    assert html == snapshot

# Update snapshots when intentionally changing output
# pytest --snapshot-update
```

**Reference**: Avatar has best test coverage (165 test lines for 199 implementation lines = 83% ratio)

---

### 8. Backward Compatibility 🔒 CRITICAL

No breaking changes to existing component APIs or behavior.

#### Requirements

- [ ] **No breaking changes to existing props**
  - Don't rename public props
  - Don't change prop types (e.g., `str` → `int`)
  - Don't remove public props
  - Don't change default values (behavior change)

- [ ] **No changes to component output HTML structure**
  - Element types must remain the same (`<button>` → `<a>` is breaking)
  - Required attributes must be preserved
  - Class ordering may change but base classes must remain

- [ ] **No removal of public props**
  - If prop is no longer needed, deprecate with warning
  - Keep deprecated prop functional for 1-2 releases
  - Document migration path in CHANGELOG

- [ ] **Additions use optional props with defaults**
  - New props must have default values
  - New props cannot be required
  - New props cannot change existing behavior when not specified

#### Safe Changes (Non-Breaking)

✅ **These changes are SAFE**:
- Add new optional props with defaults
- Add missing HTMX attributes (all optional with `None`)
- Enhance docstrings (add examples, clarify)
- Fix dark mode pattern (remove conditional, always include classes)
- Add type hints (make types more specific)
- Refactor private methods (names starting with `_`)
- Add internal validation/error handling
- Improve test coverage

#### Breaking Changes (Require Major Version)

❌ **These changes are BREAKING**:
- Rename public props (`type` → `type_`)
- Change prop types (`str` → `str | int` if users rely on exact type)
- Change default values (`disabled=False` → `disabled=True`)
- Remove public props (even if "unused")
- Change HTML element types (`<button>` → `<a>`)
- Reorder required vs optional props (if not using `kw_only`)
- Change output class names that users may target with CSS

#### Deprecation Pattern (For Necessary Breaking Changes)

```python
from dataclasses import dataclass
import warnings

@dataclass(frozen=True, kw_only=True)
class Button:
    """Button component."""

    # New prop (correct naming)
    type_: str = "button"
    """Button type attribute."""

    # Deprecated prop (keep for compatibility)
    type: str | None = None  # Deprecated: Use type_ instead
    """(Deprecated) Use type_ instead. Removed in v0.3.0."""

    def __post_init__(self):
        # Handle deprecation
        if self.type is not None:
            warnings.warn(
                "Button.type is deprecated, use Button.type_ instead. "
                "Will be removed in v0.3.0.",
                DeprecationWarning,
                stacklevel=2
            )
            # Use deprecated value if new value not set
            if self.type_ == "button":  # Default value
                object.__setattr__(self, "type_", self.type)
```

#### Validation Process

**Before ANY change**:
1. Run full test suite: `pytest` - All 187 tests must pass
2. Check if change affects HTML output or prop signature
3. If breaking, defer to next major version OR implement deprecation
4. Document change in CHANGELOG with migration guide

**After change**:
1. Run full test suite: `pytest` - All 187 tests must still pass
2. Run showcase app: `python examples/showcase.py` - Verify no errors
3. Manual test: Check affected component in showcase UI
4. Review snapshots: `pytest --snapshot-update` if HTML changed

---

## Scoring System

### Criterion Weights

| Criterion | Weight | Justification |
|-----------|--------|---------------|
| Type Safety | CRITICAL | Constitution requirement, prevents runtime errors |
| Backward Compatibility | CRITICAL | API stability for users, version contract |
| Test Coverage | CRITICAL | Constitution requirement, confidence in changes |
| Dark Mode Support | IMPORTANT | Core feature, user experience |
| ClassBuilder Usage | IMPORTANT | Code consistency, maintainability |
| HTMX Integration | NICE-TO-HAVE | Feature completeness, not always semantic |
| Documentation | NICE-TO-HAVE | User experience, not functionality |
| Prop Conventions | NICE-TO-HAVE | Consistency, minor impact |

### Compliance Levels

#### Full Compliance ✅

**Criteria**: All 8 quality criteria pass.

**Characteristics**:
- Passes mypy strict mode
- >90% test coverage
- All tests pass
- Comprehensive documentation
- Follows all established patterns
- Zero breaking changes

**Components at this level**:
- Toast (reference implementation)
- Modal (reference implementation)
- Select (reference implementation)

---

#### Substantial Compliance ⚠️

**Criteria**: Critical + Important criteria pass, 1-2 Nice-to-Have gaps.

**Characteristics**:
- Type safe and well-tested
- Follows ClassBuilder and dark mode patterns
- May lack full HTMX support (if not semantic)
- May need more documentation examples
- Minor prop naming inconsistencies

**Acceptable gaps**:
- Missing some HTMX attrs (for display-only components)
- Only 1 docstring example (instead of 3)
- Minor prop naming issues (not breaking)

**Components at this level**:
- Avatar (94% coverage, excellent documentation)
- Alert (98% coverage, could use HTMX for actions)
- Badge (98% coverage, needs more doc examples)

---

#### Partial Compliance 🔴

**Criteria**: Critical criteria pass, some Important gaps.

**Characteristics**:
- Type safe (mypy passes)
- Adequate test coverage (>90%)
- All tests pass
- Missing dark mode pattern (conditional instead of always-included)
- Inconsistent ClassBuilder usage
- May have HTMX gaps on interactive components

**Must fix**:
- Dark mode anti-patterns
- Missing ClassBuilder usage
- HTMX gaps on interactive components

**Components at this level**:
- Badge (conditional dark mode - MUST FIX)
- Alert (conditional dark mode - MUST FIX)
- Button (missing 5 HTMX attrs - should add)

---

#### Non-Compliant ❌

**Criteria**: One or more Critical failures.

**Characteristics**:
- Fails mypy strict mode
- OR <90% test coverage
- OR breaks existing tests
- OR breaking changes without deprecation

**Blocker**: Cannot merge until Critical issues resolved.

**No current components at this level** (all pass Critical criteria).

---

## Usage Guidelines

### For Component Review (Current Task)

1. **Open component file** (e.g., `src/flowbite_htmy/components/button.py`)
2. **Open test file** (e.g., `tests/test_components/test_button.py`)
3. **Check each criterion** systematically
4. **Record findings** in ComponentReview data model (see `data-model.md`)
5. **Assign compliance level** based on scoring system
6. **Prioritize fixes** based on criterion weights

### For New Component Implementation

1. **Before writing code**: Review this checklist
2. **During implementation**: Validate each criterion as you build
3. **TDD approach**: Write tests first, then implement
4. **Before PR**: Run validation commands for all criteria
5. **In PR description**: Link to checklist, confirm compliance level

### For Pull Request Review

**Reviewer checklist**:
1. Run `pytest` - All tests pass?
2. Run `mypy --strict src/flowbite_htmy` - Zero errors?
3. Check component code against criteria 3-6 (Dark Mode, ClassBuilder, Docs, Props)
4. Verify backward compatibility (criterion 8)
5. Request changes if Partial Compliance or worse
6. Approve if Substantial Compliance or better

---

## Validation Commands

Quick reference for automated checks:

```bash
# Type checking (Criterion 1)
mypy --strict src/flowbite_htmy/components/{component}.py

# Test coverage (Criterion 7)
pytest --cov=src/flowbite_htmy/components/{component} tests/test_components/test_{component}.py
pytest --cov-report=term-missing  # Show untested lines

# All tests (Criterion 8)
pytest

# Linting (code quality)
ruff check src/flowbite_htmy/components/{component}.py
ruff format --check src/flowbite_htmy/components/{component}.py

# Showcase validation (Criterion 8)
python examples/showcase.py
# Open http://localhost:8000 and test component
```

---

## Exceptions and Waivers

### When to Request Exception

Some criteria may not apply to specific components:

**HTMX Integration** - Not semantic for:
- Display-only components (Badge, Avatar, Indicator)
- Static layout components
- Components that never trigger actions

**Request exception**: Document in component docstring why HTMX support is not included.

### Waiver Process

1. Document exception in PR description
2. Reference this checklist with criterion number
3. Explain why exception is appropriate
4. Get approval from project maintainer

**Example waiver request**:
> "Badge component does not implement HTMX integration (Criterion 2) because badges are display-only elements. Adding HTMX attributes would violate semantic HTML. See component-quality-checklist.md for exception guidelines."

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-16 | Initial checklist based on research findings and constitution |

---

## References

- **Constitution**: `.specify/memory/constitution.md` - Project principles
- **CLAUDE.md**: Development guide with patterns
- **Research Findings**: `specs/004-component-review/research.md` - Pattern analysis
- **Data Model**: `specs/004-component-review/data-model.md` - Review data structures

---

**Contract Status**: ✅ Active - Applies to all component reviews and implementations
