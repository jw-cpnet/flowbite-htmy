# Component Quality Standards

**Version**: 1.0.0
**Last Updated**: 2025-11-16
**Applies To**: All htmy components in flowbite-htmy library

## Purpose

This document defines quality standards for flowbite-htmy components based on patterns learned from implementing 14+ components across Phase 1 and Phase 2. Use this as a checklist when creating new components or reviewing existing ones.

**Reference Implementations**: Toast, Modal, Avatar (exemplary quality), Select, Pagination (Phase 2A)

---

## Quality Criteria

### 1. Type Safety (CRITICAL)

**Requirements**:
- [ ] All props have explicit type hints
- [ ] `htmy()` method returns `Component` type
- [ ] `context: Context` parameter properly typed
- [ ] No `Any` types without justification
- [ ] Component passes `mypy --strict`

**Example (Toast - Correct)**:
```python
@dataclass(frozen=True, kw_only=True)
class Toast:
    message: str  # ✅ Explicit type
    variant: ToastVariant = ToastVariant.INFO  # ✅ Enum with default
    icon: Icon | None = None  # ✅ Optional type
    dismissible: bool = True  # ✅ Boolean with default

    def htmy(self, context: Context) -> Component:  # ✅ Return type
        theme = ThemeContext.from_context(context)
        # ...
```

**Validation**:
```bash
mypy src/flowbite_htmy/components/your_component.py --strict
```

---

### 2. HTMX Integration

**Requirements for Interactive Components**:
- [ ] Minimum support: `hx_get`, `hx_post`, `hx_target` (3 attrs)
- [ ] Interactive components: Add `hx_swap`, `hx_trigger` (5 attrs)
- [ ] Advanced components: Full set of 10 attributes
- [ ] All HTMX attrs have `| None` type and `None` default

**Full HTMX Attribute Set** (10 total):
```python
# HTTP Methods
hx_get: str | None = None
hx_post: str | None = None
hx_put: str | None = None
hx_delete: str | None = None
hx_patch: str | None = None

# Behavior Controls
hx_target: str | None = None
hx_swap: str | None = None
hx_trigger: str | None = None
hx_push_url: str | bool | None = None  # Note: can be bool or str
hx_select: str | None = None
```

**When to Include HTMX**:
- **Display-only components** (Badge, Alert, Avatar): Not needed (0 attrs OK)
- **Interactive components** (Button): Full set recommended (10 attrs)
- **Form components** (Input, Select, Textarea): Minimum set (3-5 attrs)
- **Advanced components** (Toast with action button): Full set (10 attrs)

**Example (Button - Correct)**:
```python
# All 10 HTMX attributes supported
@dataclass(frozen=True, kw_only=True)
class Button:
    # ... other props ...
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | bool | None = None
    hx_select: str | None = None

    def htmy(self, context: Context) -> Component:
        button_attrs = {
            "hx-get": self.hx_get,
            "hx-post": self.hx_post,
            # ... all 10 attrs ...
        }
        return html.button(content, **button_attrs)
```

---

### 3. Dark Mode Support (CRITICAL)

**Requirements**:
- [ ] All color classes include `dark:` variants
- [ ] Dark classes **always included** (NOT conditional on theme.dark_mode)
- [ ] Uses `ThemeContext.from_context(context)` if needed
- [ ] Tested in both light and dark modes

**Correct Pattern**:
```python
# ✅ CORRECT - Always include dark: classes
builder = ClassBuilder(
    "bg-white text-gray-900 "
    "dark:bg-gray-800 dark:text-white"  # Always present
)

# OR for dynamic colors:
dark_classes = self._get_dark_classes()
if dark_classes:  # Only check non-empty, NOT theme.dark_mode
    builder.add(dark_classes)
```

**Anti-Pattern** (Fixed in Badge):
```python
# ❌ WRONG - Conditional dark mode
dark_classes = self._get_dark_classes()
if theme.dark_mode and dark_classes:  # ANTI-PATTERN!
    builder.add(dark_classes)
```

**Why This Matters**:
- Tailwind's `dark:` prefix handles activation automatically via `dark` class on `<html>`
- Conditional addition removes dark mode classes entirely from HTML
- Makes debugging harder (classes missing vs. present-but-inactive)
- Violates separation of concerns (component shouldn't know mode state)

**Reference Implementation** (Alert):
```python
def _build_classes(self, theme: ThemeContext) -> str:
    builder = ClassBuilder("p-4 mb-4 text-sm rounded-lg")

    # Color classes
    color_classes = self._get_color_classes()
    builder.add(color_classes)

    # Dark mode classes
    # Always include dark: classes - Tailwind handles activation
    dark_classes = self._get_dark_classes()
    if dark_classes:
        builder.add(dark_classes)

    return builder.merge(self.class_)
```

---

### 4. ClassBuilder Usage

**Requirements**:
- [ ] Uses `ClassBuilder` for class string construction
- [ ] Base classes added first (via constructor or `.add()`)
- [ ] Conditional classes use `.add_if(condition, classes)`
- [ ] Custom classes merged last via `.merge(self.class_)`

**Example (Avatar - Correct)**:
```python
def _build_image_classes(self, theme: ThemeContext) -> str:
    builder = ClassBuilder("rounded-full")  # Base classes in constructor

    # Conditional: size classes
    builder.add(self._get_size_classes())

    # Conditional: border
    builder.add_if(self.bordered, "p-1 ring-2 ring-gray-300 dark:ring-gray-500")

    return builder.merge(self.class_)  # Custom classes merged last
```

**Validation**:
- Constructor or first `.add()` sets base/required classes
- Middle: Variant-specific or conditional classes
- End: `.merge(self.class_)` allows user overrides

---

### 5. Documentation

**Requirements**:
- [ ] Class has comprehensive docstring
- [ ] Docstring includes 1-3 usage examples
- [ ] All public props have docstrings
- [ ] Special patterns or gotchas documented

**Example (Toast - Reference Standard)**:
```python
@dataclass(frozen=True, kw_only=True)
class Toast:
    """Toast notification component for temporary messages.

    Supports four variants (success, danger, warning, info), optional
    action buttons, rich content with avatars, and Flowbite JavaScript
    dismiss functionality.

    Examples:
        Simple success toast:
        >>> Toast(message="Saved successfully", variant=ToastVariant.SUCCESS)

        Interactive toast with action:
        >>> Toast(
        ...     message="New message from Alice",
        ...     variant=ToastVariant.INFO,
        ...     action_button=ToastActionButton(label="Reply", hx_get="/reply")
        ... )

        Rich content toast:
        >>> Toast(
        ...     message="Alice: Thanks for sharing!",
        ...     variant=ToastVariant.INFO,
        ...     avatar_src="/users/alice.jpg"
        ... )
    """

    message: str
    """Toast message content."""

    variant: ToastVariant = ToastVariant.INFO
    """Toast color variant (success, danger, warning, info)."""
```

**Documentation Levels**:
- **Minimum** (90%): Class docstring + basic example + prop docstrings
- **Good** (95%): Multiple examples showing different use cases
- **Excellent** (100%): Examples + edge cases + integration patterns

---

### 6. Prop Conventions

**Requirements**:
- [ ] Reserved words use trailing underscore (`class_`, `type_`, etc.)
- [ ] Boolean props default to `False` (or sensible default)
- [ ] Required props come before optional props
- [ ] Consistent naming with other components

**Reserved Word Handling**:
```python
# ✅ CORRECT
class_: str = ""  # 'class' is reserved keyword
type_: str = "button"  # 'type' is built-in function name
id: str | None = None  # 'id' is built-in but OK in dataclass

# ❌ WRONG (Button before fix)
type: str = "button"  # Should be type_
```

**Prop Ordering**:
```python
@dataclass(frozen=True, kw_only=True)
class Component:
    # 1. Required props (no defaults)
    message: str
    label: str

    # 2. Optional props (with defaults)
    color: Color = Color.PRIMARY
    size: Size = Size.MD
    icon: Icon | None = None

    # 3. Boolean flags
    dismissible: bool = False
    bordered: bool = False

    # 4. HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None

    # 5. Custom classes/attrs (always last)
    class_: str = ""
    attrs: dict[str, Any] | None = None
```

---

### 7. Test Coverage (CRITICAL)

**Requirements**:
- [ ] >90% coverage (enforced by pytest config)
- [ ] Tests for default rendering
- [ ] Tests for all variants (color, size, style)
- [ ] Tests for HTMX attributes (if supported)
- [ ] Tests for dark mode (classes present)
- [ ] Tests for custom classes (`.merge()` works)
- [ ] Edge case tests (None, empty string, etc.)

**Test Structure Example** (Button):
```python
@pytest.mark.asyncio
async def test_button_default(renderer: Renderer) -> None:
    """Test button renders with default props."""
    button = Button(label="Click")
    html = await renderer.render(button)

    assert "Click" in html
    assert "button" in html
    assert "bg-blue-700" in html  # Default color
    assert 'type="button"' in html  # Default type

@pytest.mark.asyncio
async def test_button_htmx_attributes(renderer: Renderer) -> None:
    """Test button with HTMX attributes."""
    button = Button(
        label="Load",
        hx_get="/api/data",
        hx_target="#result"
    )
    html = await renderer.render(button)

    assert 'hx-get="/api/data"' in html
    assert 'hx-target="#result"' in html

@pytest.mark.asyncio
async def test_button_custom_class(renderer: Renderer) -> None:
    """Test button with custom classes."""
    button = Button(label="Custom", class_="my-class")
    html = await renderer.render(button)

    assert "my-class" in html  # Custom class present
    assert "bg-blue-700" in html  # Base classes still present
```

**Coverage Targets**:
- **Minimum**: 90% (enforced)
- **Good**: 95%
- **Excellent**: 98%+ (Avatar standard)

---

### 8. Backward Compatibility (CRITICAL)

**Requirements**:
- [ ] No breaking changes to existing props
- [ ] No changes to component output HTML structure
- [ ] No removal of public props
- [ ] Additions use optional props with defaults

**Safe Changes**:
- Adding new optional props with `None` default
- Adding docstrings or type hints
- Internal refactoring (ClassBuilder usage)
- Adding dark mode classes (always-included pattern)

**Breaking Changes** (Require Major Version):
- Renaming props (e.g., `type` → `type_`)
- Changing prop types
- Changing default values
- Removing props
- Changing HTML output structure

**Example - Safe Addition** (Button):
```python
# v0.1.0
class Button:
    hx_get: str | None = None
    hx_post: str | None = None

# v0.1.1 - SAFE (new optional props)
class Button:
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None  # ✅ New, optional, None default
    hx_delete: str | None = None  # ✅ Safe to add
```

**Example - Breaking Change** (Button):
```python
# v0.1.0
class Button:
    type: str = "button"

# v0.2.0 - BREAKING (prop renamed)
class Button:
    type_: str = "button"  # ❌ Breaks: Button(type="submit")
```

---

## Compliance Scoring

### Critical (Must Pass)
- Type Safety: 100% type coverage, mypy strict
- Dark Mode: Always-included pattern
- Test Coverage: >90%
- Backward Compatibility: No breaking changes (or documented)

### Important (Should Pass)
- ClassBuilder: Consistent usage with `.merge()`
- HTMX Coverage: Appropriate for component type
- Prop Conventions: Reserved words handled correctly

### Nice-to-Have (Can Improve)
- Documentation: Multiple examples (Toast standard)
- Test Coverage: 95%+ (Avatar standard)
- Edge Case Tests: Comprehensive scenarios

### Compliance Levels

- **Full Compliance**: All Critical + Important + Most Nice-to-Have ✅
- **Substantial Compliance**: All Critical + Important ✅
- **Partial Compliance**: All Critical, some Important gaps ⚠️
- **Non-Compliant**: Critical failures ❌

---

## Anti-Patterns to Avoid

### ❌ Conditional Dark Mode

**Wrong**:
```python
if theme.dark_mode:
    builder.add("dark:bg-gray-800")
```

**Why Wrong**: Removes dark mode classes from HTML entirely in light mode

**Correct**:
```python
# Always include dark: classes
builder.add("dark:bg-gray-800")  # Tailwind handles activation
```

**Historical Note**: Badge component (fixed Nov 16, 2025) had this anti-pattern at line 153

---

### ❌ Manual Class String Concatenation

**Wrong**:
```python
classes = "base " + color_classes + " " + size_classes
if custom:
    classes += " " + custom
```

**Why Wrong**: Hard to maintain, error-prone, doesn't handle None values

**Correct**:
```python
builder = ClassBuilder("base")
builder.add(color_classes)
builder.add(size_classes)
return builder.merge(custom)  # Handles None/empty gracefully
```

---

### ❌ Incomplete HTMX Coverage (Interactive Components)

**Wrong** (Button before fix):
```python
class Button:
    hx_get: str | None = None
    hx_post: str | None = None
    # Missing 8 other attrs
```

**Why Wrong**: Limits component flexibility for HTMX-driven applications

**Correct** (Button after fix):
```python
class Button:
    # Full HTMX coverage (10 attributes)
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | bool | None = None
    hx_select: str | None = None
```

**Note**: Full coverage doesn't mean you must USE all attrs - it means the component SUPPORTS them if needed.

---

### ❌ Reserved Word Without Trailing Underscore

**Wrong** (Button before fix):
```python
type: str = "button"  # 'type' is Python built-in
```

**Why Wrong**: Violates PEP 8, inconsistent with `class_` convention

**Correct** (Button after fix):
```python
type_: str = "button"  # Trailing underscore for reserved words
```

---

## Reference Implementations

### Toast Component
**Quality Score**: 100%
**What Makes It Exemplary**:
- ✅ Comprehensive docstring with 3 usage examples
- ✅ Full HTMX coverage (10 attrs in ToastActionButton)
- ✅ Dark mode classes always included
- ✅ ClassBuilder usage consistent
- ✅ 100% type coverage
- ✅ 92% test coverage (23 tests)
- ✅ Proper reserved word handling (type_)

**File**: `src/flowbite_htmy/components/toast.py`

---

### Modal Component
**Quality Score**: 100%
**What Makes It Exemplary**:
- ✅ Phase 2 highest-ranked component
- ✅ Multiple docstring examples
- ✅ Dark mode always included
- ✅ Clean ClassBuilder usage
- ✅ 100% test coverage
- ✅ Proper Flowbite JS integration

**File**: `src/flowbite_htmy/components/modal.py`

---

### Avatar Component
**Quality Score**: 98%
**What Makes It Exemplary**:
- ✅ Excellent test coverage (98%)
- ✅ Multiple rendering modes (image, initials, placeholder)
- ✅ Comprehensive docstrings with examples
- ✅ Dark mode classes always included
- ✅ Passthrough attrs pattern for tooltips/dropdowns
- ✅ Best test:code ratio (165 test lines for 199 code lines)

**File**: `src/flowbite_htmy/components/avatar.py`

**Recommendation**: Use Avatar as the template for high test coverage

---

## Component Review Checklist

Use this checklist when reviewing components (new or existing):

### Pre-Implementation
- [ ] Component provides genuine value (not just a `<div>` wrapper)
- [ ] Component enforces consistent patterns
- [ ] Component handles complex logic internally
- [ ] Showcase will use the component (not bypass it)

### Implementation
- [ ] All props have explicit type hints
- [ ] `htmy()` returns `Component` type
- [ ] Uses `@dataclass(frozen=True, kw_only=True)`
- [ ] ClassBuilder used for class construction
- [ ] Dark mode classes always included (not conditional)
- [ ] HTMX support appropriate for component type
- [ ] Reserved words use trailing underscore
- [ ] Custom classes merged via `.merge(self.class_)`

### Testing
- [ ] Default rendering test
- [ ] All variant tests (color, size, style)
- [ ] HTMX attribute tests (if applicable)
- [ ] Dark mode class presence test
- [ ] Custom class merge test
- [ ] Edge cases (None, empty, unusual combos)
- [ ] Coverage >90%

### Validation
- [ ] `pytest` - All tests pass
- [ ] `pytest --cov` - Coverage >90%
- [ ] `mypy src/flowbite_htmy/components/your_component.py --strict` - No errors
- [ ] `ruff check src/flowbite_htmy/components/your_component.py` - No issues
- [ ] `ruff format src/flowbite_htmy/components/your_component.py` - Formatted
- [ ] Showcase renders component correctly
- [ ] Dark mode toggle works in showcase

### Documentation
- [ ] Class docstring present
- [ ] At least 1 usage example in docstring
- [ ] All props documented
- [ ] Export added to `__init__.py`
- [ ] CLAUDE.md updated if new patterns

---

## Quick Validation Commands

### Type Check
```bash
mypy src/flowbite_htmy/components/your_component.py --strict
```

### Test with Coverage
```bash
pytest tests/test_components/test_your_component.py --cov=src/flowbite_htmy/components/your_component
```

### Lint
```bash
ruff check src/flowbite_htmy/components/your_component.py
```

### Format
```bash
ruff format src/flowbite_htmy/components/your_component.py
```

### Full Validation Suite
```bash
pytest && mypy src/flowbite_htmy && ruff check src/flowbite_htmy
```

---

## Component Quality History

### Improvements Applied (Nov 16, 2025)

**Badge Component**:
- Fixed: Dark mode anti-pattern (conditional → always-included)
- Impact: Coverage 74% → 76%
- Commit: f8a2e5a

**Alert Component**:
- Added: Documentation comment for dark mode pattern
- Impact: Code already correct, comment added for clarity
- Commit: e56d46e

**Button Component**:
- Added: 5 missing HTMX attributes (hx_put, hx_delete, hx_patch, hx_push_url, hx_select)
- Fixed: Naming convention (type → type_) - BREAKING CHANGE
- Impact: Coverage 77% → 78%, full HTMX support
- Commits: 84f2d78 (HTMX), 8c5ede8 (naming)

**Avatar Component**:
- Verified: Already at reference quality (98% coverage)
- No changes needed

### Coverage Trends

| Component | Before Review | After Review | Change |
|-----------|--------------|--------------|--------|
| Badge | 74% | 76% | +2% ✅ |
| Alert | 80% | 80% | → |
| Button | 77% | 78% | +1% ✅ |
| Avatar | 98% | 98% | → (reference) |

---

## Future Component Standards

When implementing new components, use this priority order:

1. **Start with quality checklist** (this document)
2. **Reference implementations**: Toast, Modal, Avatar
3. **TDD workflow**: Write tests first (per CLAUDE.md)
4. **Validate early**: Run pytest + mypy + ruff after each method
5. **Document as you go**: Docstrings with examples immediately
6. **Review before commit**: Self-check against this checklist

**Remember**: Quality is built in, not added later. Following these standards from the start prevents technical debt.

---

**Document Status**: ✅ Complete
**Validation**: Ready for use in component development and reviews
**Maintained By**: Update when new patterns emerge from component implementations
