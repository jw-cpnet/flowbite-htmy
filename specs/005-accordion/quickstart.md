# TDD Quickstart: Accordion Component

**Date**: 2025-11-16
**Feature**: 005-accordion
**Purpose**: Test-driven development workflow guide for implementing the Accordion component following strict TDD principles.

## TDD Principles (NON-NEGOTIABLE)

This project mandates Test-Driven Development. Every line of production code MUST be preceded by a failing test:

1. **Write failing test first** - Test describes desired behavior
2. **Confirm test fails** - Run pytest, verify failure for correct reason
3. **Implement minimal code** - Write only enough to pass the test
4. **Confirm test passes** - Run pytest, verify green
5. **Refactor if needed** - Improve code while keeping tests green
6. **Repeat** - Next test, next feature

**⚠️ CRITICAL**: If you write production code without a test, you have violated the constitution and must delete the code and start over.

## Test Structure

### Test File Location

```
tests/test_components/test_accordion.py
```

### Required Imports

```python
import pytest
from htmy import Component
from flowbite_htmy.components import Accordion, Panel, AccordionMode, AccordionVariant
from flowbite_htmy.types import Color
from flowbite_htmy.icons import Icon, get_icon
```

### Fixtures (from conftest.py)

- `renderer`: AsyncHTMLRenderer for rendering components
- `context`: Default Context instance
- `dark_context`: Context with dark mode enabled
- `snapshot`: Syrupy snapshot fixture for regression testing

## Phase 1: Basic Accordion Structure (P1)

**Goal**: Implement core accordion rendering with proper HTML structure, ARIA attributes, and Flowbite classes.

### Test 1: Default Accordion Renders

**Purpose**: Verify accordion renders with collapse mode and default variant.

```python
@pytest.mark.asyncio
async def test_accordion_default_rendering(renderer):
    """Accordion renders with default mode and variant."""
    accordion = Accordion(
        panels=[
            Panel(title="Panel 1", content="Content 1"),
            Panel(title="Panel 2", content="Content 2"),
        ]
    )
    html = await renderer.render(accordion)

    assert 'data-accordion="collapse"' in html
    assert "Panel 1" in html
    assert "Panel 2" in html
    assert "Content 1" in html
    assert "Content 2" in html
```

**Implementation Steps**:
1. Create `src/flowbite_htmy/components/accordion.py`
2. Define `AccordionMode` and `AccordionVariant` enums
3. Define `Panel` dataclass with `title` and `content` fields
4. Define `Accordion` dataclass with `panels`, `mode`, `variant` fields
5. Implement `Accordion.htmy()` method returning basic `html.div()` with `data-accordion` attribute
6. Iterate through panels, render `<h2>` + `<button>` + `<div>` structure
7. Run test, verify it passes

### Test 2: Unique IDs Generated

**Purpose**: Verify each panel gets unique heading and body IDs.

```python
@pytest.mark.asyncio
async def test_accordion_generates_unique_ids(renderer):
    """Each panel has unique IDs for ARIA relationships."""
    accordion = Accordion(
        panels=[
            Panel(title="P1", content="C1"),
            Panel(title="P2", content="C2"),
            Panel(title="P3", content="C3"),
        ]
    )
    html = await renderer.render(accordion)

    # Verify heading IDs exist and are unique
    assert 'id="accordion-' in html
    assert '-heading-0"' in html
    assert '-heading-1"' in html
    assert '-heading-2"' in html

    # Verify body IDs exist and are unique
    assert '-body-0"' in html
    assert '-body-1"' in html
    assert '-body-2"' in html
```

**Implementation Steps**:
1. In `Accordion.htmy()`, generate `base_id` from `id(self)` or custom `accordion_id`
2. For each panel with index i, create `heading_id = f"{base_id}-heading-{i}"`
3. For each panel with index i, create `body_id = f"{base_id}-body-{i}"`
4. Set `id` attribute on `<h2>` and `<button>` to `heading_id`
5. Set `id` attribute on panel `<div>` to `body_id`
6. Run test, verify it passes

### Test 3: ARIA Attributes Present

**Purpose**: Verify aria-expanded, aria-controls, and aria-labelledby are correctly set.

```python
@pytest.mark.asyncio
async def test_accordion_aria_attributes(renderer):
    """ARIA attributes properly link headers and panels."""
    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", is_open=True),
            Panel(title="Q2", content="A2", is_open=False),
        ]
    )
    html = await renderer.render(accordion)

    # First panel (open)
    assert 'aria-expanded="true"' in html
    assert 'aria-controls="accordion-' in html
    assert '-body-0"' in html

    # Second panel (closed)
    assert 'aria-expanded="false"' in html
    assert 'aria-controls="accordion-' in html
    assert '-body-1"' in html

    # Both panels have aria-labelledby
    assert 'aria-labelledby="accordion-' in html
```

**Implementation Steps**:
1. On `<button>`, add `aria_expanded` attribute with value from `panel.is_open` ("true" or "false")
2. On `<button>`, add `aria_controls` attribute pointing to `body_id`
3. On `<button>`, add `data_accordion_target` attribute with `#{body_id}`
4. On panel `<div>`, add `aria_labelledby` attribute pointing to `heading_id`
5. Run test, verify it passes

### Test 4: Flowbite Classes Applied

**Purpose**: Verify Flowbite CSS classes are applied to container, buttons, and panels.

```python
@pytest.mark.asyncio
async def test_accordion_flowbite_classes(renderer):
    """Flowbite classes applied to accordion elements."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        variant=AccordionVariant.DEFAULT,
    )
    html = await renderer.render(accordion)

    # Button classes
    assert "flex items-center justify-between" in html
    assert "w-full p-5 font-medium" in html
    assert "border border-b-0 border-gray-200" in html
    assert "rounded-t-xl" in html
    assert "focus:ring-4" in html
    assert "hover:bg-gray-100" in html

    # Dark mode classes
    assert "dark:border-gray-700" in html
    assert "dark:text-gray-400" in html
    assert "dark:hover:bg-gray-800" in html
```

**Implementation Steps**:
1. Import `ClassBuilder` from `flowbite_htmy.base`
2. In `Accordion.htmy()`, create `ClassBuilder` for button classes
3. Add base classes: `"flex items-center justify-between w-full p-5 font-medium rtl:text-right gap-3"`
4. Add color classes: `"text-gray-500 dark:text-gray-400"`
5. Add border classes based on variant (DEFAULT: `"border border-b-0 border-gray-200 dark:border-gray-700"`)
6. Add first panel: `"rounded-t-xl"`
7. Add focus classes: `"focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800"`
8. Add hover classes: `"hover:bg-gray-100 dark:hover:bg-gray-800"`
9. Apply similar pattern for panel body wrapper classes
10. Run test, verify it passes

### Test 5: Data-Accordion Attribute

**Purpose**: Verify data-accordion attribute set correctly for both modes.

```python
@pytest.mark.asyncio
async def test_accordion_data_attribute_collapse(renderer):
    """Collapse mode sets data-accordion='collapse'."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        mode=AccordionMode.COLLAPSE,
    )
    html = await renderer.render(accordion)
    assert 'data-accordion="collapse"' in html

@pytest.mark.asyncio
async def test_accordion_data_attribute_always_open(renderer):
    """Always-open mode sets data-accordion='open'."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        mode=AccordionMode.ALWAYS_OPEN,
    )
    html = await renderer.render(accordion)
    assert 'data-accordion="open"' in html
```

**Implementation Steps**:
1. In `Accordion.htmy()`, add `data_accordion` attribute to container `<div>`
2. Set value to `self.mode.value` (enum value: "collapse" or "open")
3. Run tests, verify they pass

## Phase 2: Variants & Customization (P2)

**Goal**: Implement visual variants, color customization, and icon support.

### Test 6: Flush Variant Removes Borders

**Purpose**: Verify flush variant applies correct classes (no side borders, no rounding).

```python
@pytest.mark.asyncio
async def test_accordion_flush_variant(renderer):
    """Flush variant removes side borders and rounding."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        variant=AccordionVariant.FLUSH,
    )
    html = await renderer.render(accordion)

    # Flush button classes (border-b only, no rounding, py-5)
    assert "border-b border-gray-200" in html
    assert "py-5" in html
    assert "rounded-t-xl" not in html  # No rounding
    assert "border border-b-0" not in html  # No side borders

    # Flush body classes (border-b only, py-5)
    assert "border-b border-gray-200" in html
    assert "py-5" in html
```

**Implementation Steps**:
1. In `_build_button_classes()` method, check `self.variant`
2. If `AccordionVariant.FLUSH`, use `"border-b border-gray-200 dark:border-gray-700 py-5"`
3. If `AccordionVariant.DEFAULT`, use `"border border-b-0 border-gray-200 dark:border-gray-700 p-5 rounded-t-xl"`
4. Apply same pattern for body wrapper classes
5. Run test, verify it passes

### Test 7: Color Prop Applies Header Classes

**Purpose**: Verify color prop changes header background and hover colors.

```python
@pytest.mark.asyncio
async def test_accordion_color_customization(renderer):
    """Color prop applies background and hover classes."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        color=Color.BLUE,
    )
    html = await renderer.render(accordion)

    # Blue color classes (hover state)
    assert "hover:bg-blue-100" in html
    assert "dark:hover:bg-blue-800" in html or "dark:hover:bg-gray-800" in html
```

**Implementation Steps**:
1. Define `COLOR_CLASSES` dictionary mapping `Color` enum to hover classes
2. In `_build_button_classes()`, look up `self.color` in dictionary
3. Add color-specific hover classes to button
4. Run test, verify it passes

### Test 8: Dark Mode Classes Always Included

**Purpose**: Verify dark mode classes present regardless of theme context.

```python
@pytest.mark.asyncio
async def test_accordion_dark_mode_classes_always_included(renderer, context):
    """Dark mode classes always present in light mode context."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")]
    )
    html = await renderer.render(accordion, context)  # Light mode context

    # Dark classes must be present even in light mode
    assert "dark:border-gray-700" in html
    assert "dark:text-gray-400" in html
    assert "dark:hover:bg-gray-800" in html
    assert "dark:focus:ring-gray-800" in html
```

**Implementation Steps**:
1. In `_build_button_classes()`, always add dark mode classes
2. Never use `if theme.dark_mode:` conditionals for dark classes
3. Pattern: `builder.add("text-gray-500 dark:text-gray-400")` (both variants together)
4. Run test, verify it passes

### Test 9: Always-Open Mode Data Attribute

**Purpose**: Verify always-open mode sets correct data attribute.

```python
@pytest.mark.asyncio
async def test_accordion_always_open_mode(renderer):
    """Always-open mode allows multiple panels open."""
    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", is_open=True),
            Panel(title="Q2", content="A2", is_open=True),
        ],
        mode=AccordionMode.ALWAYS_OPEN,
    )
    html = await renderer.render(accordion)

    assert 'data-accordion="open"' in html
    # Both panels can be open (no hidden class)
    assert html.count('aria-expanded="true"') == 2
```

**Implementation Steps**:
1. Verify `data_accordion` attribute uses `self.mode.value`
2. Verify `is_open=True` removes `hidden` class from panel body
3. Run test, verify it passes

### Test 10: Custom Icons Replace Default

**Purpose**: Verify custom panel icons render instead of default chevron.

```python
@pytest.mark.asyncio
async def test_accordion_custom_panel_icons(renderer):
    """Custom icons replace default chevron."""
    custom_icon = get_icon(Icon.INFORMATION_CIRCLE, class_="w-5 h-5")

    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", icon=custom_icon),
        ]
    )
    html = await renderer.render(accordion)

    # Custom icon SVG present (information circle has specific path)
    assert "w-5 h-5" in html
    # Default chevron NOT present (or overridden)
```

**Implementation Steps**:
1. In panel rendering loop, check if `panel.icon` is not None
2. If custom icon: render `panel.icon` component
3. If None: render default `get_icon(Icon.CHEVRON_DOWN, class_="w-3 h-3 shrink-0", data_accordion_icon="true")`
4. Run test, verify it passes

## Phase 3: HTMX Integration (P3)

**Goal**: Support HTMX attributes for dynamic content loading.

### Test 11: hx-get Attribute Renders

**Purpose**: Verify hx-get attribute renders on panel body.

```python
@pytest.mark.asyncio
async def test_accordion_htmx_get_attribute(renderer):
    """HTMX hx-get attribute renders on panel body."""
    accordion = Accordion(
        panels=[
            Panel(
                title="Lazy Load",
                content="Loading...",
                hx_get="/api/content/1",
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-get="/api/content/1"' in html
```

**Implementation Steps**:
1. On panel body `<div>`, add `hx_get` attribute if `panel.hx_get` is not None
2. Use htmy's `hx_get` parameter (converts underscore to hyphen)
3. Run test, verify it passes

### Test 12: hx-trigger Attribute Configurable

**Purpose**: Verify hx-trigger attribute can be customized.

```python
@pytest.mark.asyncio
async def test_accordion_htmx_trigger_attribute(renderer):
    """HTMX hx-trigger attribute is configurable."""
    accordion = Accordion(
        panels=[
            Panel(
                title="Custom Trigger",
                content="Content",
                hx_get="/api/data",
                hx_trigger="revealed once",
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-trigger="revealed once"' in html
```

**Implementation Steps**:
1. On panel body `<div>`, add `hx_trigger` attribute if `panel.hx_get` is not None
2. Use `panel.hx_trigger` value (default: "revealed")
3. Run test, verify it passes

### Test 13: Multiple HTMX Attributes Supported

**Purpose**: Verify multiple HTMX attributes can be combined.

```python
@pytest.mark.asyncio
async def test_accordion_multiple_htmx_attributes(renderer):
    """Multiple HTMX attributes can be combined."""
    # Note: Panel dataclass needs hx_swap, hx_target props added
    accordion = Accordion(
        panels=[
            Panel(
                title="Full HTMX",
                content="Content",
                hx_get="/api/data",
                hx_trigger="revealed",
                # Future: hx_swap="innerHTML", hx_target="this"
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-get="/api/data"' in html
    assert 'hx-trigger="revealed"' in html
```

**Implementation Steps**:
1. Add `hx_swap` and `hx_target` props to Panel dataclass (optional, defaults None)
2. On panel body `<div>`, add these attributes if provided
3. Run test, verify it passes

## Phase 4: Edge Cases

**Goal**: Handle boundary conditions and unusual inputs gracefully.

### Test 14: Single Panel Accordion

**Purpose**: Verify single-panel accordion works correctly.

```python
@pytest.mark.asyncio
async def test_accordion_single_panel(renderer):
    """Accordion with single panel renders correctly."""
    accordion = Accordion(
        panels=[Panel(title="Only Panel", content="Only Content")]
    )
    html = await renderer.render(accordion)

    assert "Only Panel" in html
    assert "Only Content" in html
    assert "-heading-0" in html
    assert "-body-0" in html
```

**Implementation Steps**:
1. Verify accordion works with `len(panels) == 1`
2. Verify first panel gets `rounded-t-xl`
3. Verify last panel gets `border-t-0` (same panel if only one)
4. Run test, verify it passes

### Test 15: Empty Content Panels

**Purpose**: Verify panels with empty content string render.

```python
@pytest.mark.asyncio
async def test_accordion_empty_content(renderer):
    """Panels with empty content render empty body."""
    accordion = Accordion(
        panels=[Panel(title="Empty Panel", content="")]
    )
    html = await renderer.render(accordion)

    assert "Empty Panel" in html
    # Panel body exists but is empty
    assert "-body-0" in html
```

**Implementation Steps**:
1. Allow `panel.content = ""` (empty string)
2. Render empty `<div>` wrapper if content is empty
3. Run test, verify it passes

### Test 16: Invalid Default Open Index Ignored

**Purpose**: Verify invalid `is_open` on non-existent panels doesn't crash.

```python
@pytest.mark.asyncio
async def test_accordion_handles_invalid_open_index(renderer):
    """Accordion handles is_open gracefully for all panels."""
    # This test verifies no IndexError when all panels have is_open set
    accordion = Accordion(
        panels=[
            Panel(title="P1", content="C1", is_open=True),
            Panel(title="P2", content="C2", is_open=False),
        ]
    )
    html = await renderer.render(accordion)

    assert 'aria-expanded="true"' in html  # P1
    assert 'aria-expanded="false"' in html  # P2
```

**Implementation Steps**:
1. Verify `panel.is_open` is per-panel, not index-based
2. No special handling needed (each Panel has own `is_open` prop)
3. Run test, verify it passes

### Test 17: Custom class_ Merges

**Purpose**: Verify custom CSS classes merge with component classes.

```python
@pytest.mark.asyncio
async def test_accordion_custom_classes(renderer):
    """Custom classes merge with component classes."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        class_="my-8 max-w-2xl",
    )
    html = await renderer.render(accordion)

    assert "my-8" in html
    assert "max-w-2xl" in html
```

**Implementation Steps**:
1. On container `<div>`, use `ClassBuilder().merge(self.class_)`
2. Verify custom classes appended after component classes
3. Run test, verify it passes

## Test Execution Order

**Strict TDD Sequence**:

1. Write Test 1 → Run (fail) → Implement → Run (pass)
2. Write Test 2 → Run (fail) → Implement → Run (pass)
3. Write Test 3 → Run (fail) → Implement → Run (pass)
4. Continue for all 17 tests in order

**Commands**:

```bash
# Run single test
pytest tests/test_components/test_accordion.py::test_accordion_default_rendering -v

# Run all accordion tests
pytest tests/test_components/test_accordion.py -v

# Run with coverage
pytest tests/test_components/test_accordion.py --cov=src/flowbite_htmy/components/accordion

# Run in watch mode (requires pytest-watch)
ptw tests/test_components/test_accordion.py
```

## Coverage Goals

- **Target**: >90% line coverage (project standard)
- **Expected**: 95-99% coverage with 17 tests
- **Uncovered**: Likely only defensive error handling (e.g., empty panels list validation)

**Coverage Report**:

```bash
pytest tests/test_components/test_accordion.py --cov=src/flowbite_htmy/components/accordion --cov-report=html
# View: htmlcov/index.html
```

## Refactoring Checkpoints

After tests pass, refactor while keeping tests green:

1. **After Test 5**: Extract `_build_button_classes()` method
2. **After Test 7**: Extract `_build_body_classes()` method
3. **After Test 10**: Extract `_render_panel_icon()` method
4. **After Test 13**: Extract `_render_panel()` method for single panel rendering
5. **After Test 17**: Review and consolidate class building logic

**Refactoring Rules**:
- Run tests after each refactoring
- All tests must stay green
- No new tests written during refactoring (red-green-refactor cycle)

## Next Steps

1. Create `tests/test_components/test_accordion.py`
2. Import fixtures from conftest.py
3. Write Test 1, run (fail), implement, run (pass)
4. Continue through all 17 tests in order
5. Achieve >90% coverage
6. Export Accordion from `src/flowbite_htmy/components/__init__.py`
7. Add accordion section to showcase app
8. Update CLAUDE.md with accordion component status

**Ready to implement!** 🚀
