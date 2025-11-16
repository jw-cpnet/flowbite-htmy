# Quickstart Guide: Tabs Component TDD Implementation

**Date**: 2025-01-16
**Feature**: Tabs Component ([spec.md](./spec.md))

## Overview

This guide provides the TDD workflow for implementing the Tabs component following strict Red-Green-Refactor cycles. All tests must be written **before** implementation code.

---

## Prerequisites

1. **Environment activated**: `source .venv/bin/activate`
2. **Dependencies installed**: `pip install -e ".[dev]"`
3. **Baseline tests passing**: `pytest --no-cov -q` (205/205 passing before starting)

---

## Test File Structure

**File**: `tests/test_components/test_tabs.py`

**Estimated**: 20-25 tests covering all 5 user stories

### Test Organization

```python
"""Tests for Tabs component (US1-US5)."""

import pytest
from htmy import html
from flowbite_htmy.components import Tabs, Tab, TabVariant, IconPosition
from flowbite_htmy.types import Color
from flowbite_htmy.icons import Icon

# User Story 1: Basic Tab Navigation (6 tests)
class TestBasicTabNavigation:
    """Tests for US1: Basic tab switching and navigation."""

    @pytest.mark.asyncio
    async def test_tabs_renders_default_first_tab_active(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_renders_custom_active_tab(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_generates_unique_ids(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_includes_aria_attributes(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_includes_flowbite_data_attributes(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_hides_inactive_panels(self, renderer):
        ...


# User Story 2: Tab Variants and Visual Customization (7 tests)
class TestTabVariants:
    """Tests for US2: Visual variants and color customization."""

    @pytest.mark.asyncio
    async def test_tabs_default_variant(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_underline_variant(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_pills_variant(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_full_width_variant(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_color_customization(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_dark_mode_classes(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_custom_classes_merged(self, renderer):
        ...


# User Story 3: HTMX Lazy Loading (3 tests)
class TestHTMXIntegration:
    """Tests for US3: HTMX lazy loading and dynamic content."""

    @pytest.mark.asyncio
    async def test_tabs_htmx_get_attribute(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_htmx_trigger_attribute(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tabs_htmx_multiple_attributes(self, renderer):
        ...


# User Story 4: Icons and Enhanced Tab Labels (4 tests)
class TestTabIcons:
    """Tests for US4: Icon support and positioning."""

    @pytest.mark.asyncio
    async def test_tab_with_icon_left(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tab_with_icon_right(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tab_icon_in_disabled_state(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_tab_icons_across_variants(self, renderer):
        ...


# User Story 5: Disabled Tabs (3 tests)
class TestDisabledTabs:
    """Tests for US5: Disabled tab behavior."""

    @pytest.mark.asyncio
    async def test_disabled_tab_styling(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_disabled_tab_cannot_be_active(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_disabled_tab_dark_mode(self, renderer):
        ...


# Edge Cases (4 tests)
class TestEdgeCases:
    """Tests for edge cases and error handling."""

    @pytest.mark.asyncio
    async def test_single_tab(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_empty_content(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_multiple_active_tabs_first_wins(self, renderer):
        ...

    @pytest.mark.asyncio
    async def test_custom_tabs_id_override(self, renderer):
        ...
```

---

## TDD Workflow (Red-Green-Refactor)

### Phase 1: User Story 1 - Basic Tab Navigation

**Goal**: Implement core tab rendering with ARIA and Flowbite attributes (6 tests)

#### Test 1: Default First Tab Active

**RED** - Write failing test:
```python
@pytest.mark.asyncio
async def test_tabs_renders_default_first_tab_active(self, renderer):
    """Given tabs with no active tab specified, first tab should be active."""
    tabs = Tabs(tabs=[
        Tab(label="Profile", content=html.p("Profile content")),
        Tab(label="Dashboard", content=html.p("Dashboard content")),
    ])
    html_output = await renderer.render(tabs)

    assert "Profile" in html_output
    assert "Dashboard" in html_output
    assert 'aria-selected="true"' in html_output  # First tab is active
    assert html_output.count('aria-selected="true"') == 1  # Only one active
```

Run: `pytest tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_renders_default_first_tab_active -v`

Expected: **FAIL** (Tabs class doesn't exist yet)

**GREEN** - Minimal implementation:
1. Create `src/flowbite_htmy/components/tabs.py`
2. Define Tab dataclass with label, content props
3. Define Tabs dataclass with tabs list
4. Implement htmy() method rendering tablist + panels
5. Set first tab as active by default

Run test again: **PASS**

**REFACTOR** - Extract helper methods if needed

#### Tests 2-6: Repeat Red-Green-Refactor

- Test 2: Custom active tab (via `is_active=True`)
- Test 3: Unique IDs generated (`tabs-{id}`, `tab-{id}-0`, `panel-{id}-0`)
- Test 4: ARIA attributes (`role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls`, `aria-labelledby`)
- Test 5: Flowbite data attributes (`data-tabs-toggle`, `data-tabs-target`)
- Test 6: Inactive panels have `hidden` class

### Phase 2: User Story 2 - Tab Variants

**Goal**: Implement 4 visual variants with color customization (7 tests)

#### Test 7: DEFAULT Variant Classes

**RED** - Write failing test:
```python
@pytest.mark.asyncio
async def test_tabs_default_variant(self, renderer):
    """DEFAULT variant should include border-b and bg-gray-100 on active tab."""
    tabs = Tabs(
        tabs=[Tab(label="Tab1", content=html.p("Content"), is_active=True)],
        variant=TabVariant.DEFAULT,
    )
    html_output = await renderer.render(tabs)

    assert "border-b" in html_output
    assert "border-gray-200" in html_output
    assert "bg-gray-100" in html_output  # Active tab background
    assert "dark:bg-gray-800" in html_output  # Dark mode
```

Run: **FAIL** (TabVariant enum doesn't exist, no variant logic)

**GREEN** - Implementation:
1. Create TabVariant enum in `tabs.py`
2. Add `variant` prop to Tabs dataclass
3. Implement `_build_tablist_classes()` method for variant-specific classes
4. Implement `_build_tab_classes()` method for active/inactive tab classes

Run test: **PASS**

**REFACTOR** - Extract color maps and class dictionaries

#### Tests 8-13: Repeat for Other Variants

- Test 8: UNDERLINE variant (`border-b-2`, `border-blue-600` on active)
- Test 9: PILLS variant (`rounded-lg`, `bg-blue-600 text-white` on active)
- Test 10: FULL_WIDTH variant (`w-full`, `rounded-s-lg`, `rounded-e-lg`, `shadow-sm`)
- Test 11: Color customization (GREEN active tab has `text-green-600`, `bg-green-600`)
- Test 12: Dark mode classes always present (`dark:bg-*`, `dark:text-*`, `dark:border-*`)
- Test 13: Custom classes merged via `class_` prop

### Phase 3: User Story 3 - HTMX Integration

**Goal**: Support HTMX attributes for lazy loading (3 tests)

#### Test 14: HTMX hx-get Attribute

**RED** - Write failing test:
```python
@pytest.mark.asyncio
async def test_tabs_htmx_get_attribute(self, renderer):
    """hx-get attribute should appear on panel, not button."""
    tabs = Tabs(tabs=[
        Tab(label="Data", hx_get="/api/data"),
    ])
    html_output = await renderer.render(tabs)

    assert 'hx-get="/api/data"' in html_output
    # hx-get should be on panel div, not button
    assert '<button' in html_output
    assert 'hx-get' not in html_output.split('</button>')[0]  # Not in button
```

Run: **FAIL** (hx_get prop doesn't exist, not rendered)

**GREEN** - Implementation:
1. Add HTMX props to Tab dataclass (hx_get, hx_post, hx_trigger, hx_target, hx_swap)
2. Apply HTMX attributes to panel `<div>`, not button
3. Use `hx_get=hx_get` syntax in html.div() call

Run test: **PASS**

#### Tests 15-16: Additional HTMX Tests

- Test 15: `hx-trigger` attribute on panel
- Test 16: Multiple HTMX attributes together (hx-get + hx-trigger + hx-swap)

### Phase 4: User Story 4 - Icons

**Goal**: Add icon support with left/right positioning (4 tests)

#### Test 17: Icon Left (Default)

**RED** - Write failing test:
```python
@pytest.mark.asyncio
async def test_tab_with_icon_left(self, renderer):
    """Icon should appear to the left of label with me-2 spacing."""
    tabs = Tabs(tabs=[
        Tab(label="Profile", content=html.p("Content"), icon=Icon.USER),
    ])
    html_output = await renderer.render(tabs)

    assert '<svg' in html_output  # Icon SVG present
    assert 'me-2' in html_output  # Left icon spacing
    # Icon should appear before "Profile" text
    icon_pos = html_output.index('<svg')
    label_pos = html_output.index('Profile')
    assert icon_pos < label_pos
```

Run: **FAIL** (icon prop doesn't exist, no rendering logic)

**GREEN** - Implementation:
1. Add `icon` and `icon_position` props to Tab
2. Create IconPosition enum
3. Import `get_icon()` helper
4. Render icon with `w-4 h-4` classes, `me-2` for left, `ms-2` for right

Run test: **PASS**

#### Tests 18-20: Icon Variations

- Test 18: Icon right positioning
- Test 19: Icon in disabled state (gray color)
- Test 20: Icons across different variants (maintain size and spacing)

### Phase 5: User Story 5 - Disabled Tabs

**Goal**: Implement disabled tab state (3 tests)

#### Test 21: Disabled Tab Styling

**RED** - Write failing test:
```python
@pytest.mark.asyncio
async def test_disabled_tab_styling(self, renderer):
    """Disabled tab should have cursor-not-allowed and gray color."""
    tabs = Tabs(tabs=[
        Tab(label="Premium", disabled=True, content=html.p("Content")),
    ])
    html_output = await renderer.render(tabs)

    assert "text-gray-400" in html_output
    assert "cursor-not-allowed" in html_output
    assert "dark:text-gray-500" in html_output
    # Should be <a> not <button>
    assert '<a' in html_output
    assert 'href' not in html_output  # No href attribute
```

Run: **FAIL** (disabled prop doesn't exist, renders as button)

**GREEN** - Implementation:
1. Add `disabled` prop to Tab dataclass
2. In `_render_tab()`, check if disabled
3. If disabled: render as `html.a()` without href, use disabled classes
4. If enabled: render as `html.button()` with Flowbite attributes

Run test: **PASS**

#### Tests 22-23: Disabled Tab Behavior

- Test 22: Disabled tab cannot be active (ignore `is_active=True` if `disabled=True`)
- Test 23: Disabled tab dark mode classes

### Phase 6: Edge Cases

**Goal**: Handle edge cases and validation (4 tests)

#### Test 24-27: Edge Case Coverage

- Test 24: Single tab (renders full tablist UI)
- Test 25: Empty content (render panel with no content)
- Test 26: Multiple tabs with `is_active=True` (first wins)
- Test 27: Custom `tabs_id` override (use custom ID instead of auto-generated)

---

## Running Tests

### Run all Tabs tests:
```bash
pytest tests/test_components/test_tabs.py -v
```

### Run specific user story tests:
```bash
pytest tests/test_components/test_tabs.py::TestBasicTabNavigation -v
pytest tests/test_components/test_tabs.py::TestTabVariants -v
pytest tests/test_components/test_tabs.py::TestHTMXIntegration -v
pytest tests/test_components/test_tabs.py::TestTabIcons -v
pytest tests/test_components/test_tabs.py::TestDisabledTabs -v
pytest tests/test_components/test_tabs.py::TestEdgeCases -v
```

### Run with coverage:
```bash
pytest tests/test_components/test_tabs.py --cov=src/flowbite_htmy/components/tabs --cov-report=term-missing
```

**Target**: >90% coverage (aim for 95-100%)

---

## Implementation Checklist

### Files to Create/Modify

- [x] **Create**: `src/flowbite_htmy/components/tabs.py`
  - Tab dataclass (11 props)
  - Tabs dataclass (5 props)
  - TabVariant enum (4 values)
  - IconPosition enum (2 values)
  - htmy() method with variant logic
  - Helper methods: `_get_base_id()`, `_render_tab()`, `_build_tablist_classes()`, `_build_tab_classes()`

- [x] **Update**: `src/flowbite_htmy/components/__init__.py`
  - Export Tab, Tabs, TabVariant, IconPosition

- [x] **Create**: `tests/test_components/test_tabs.py`
  - 20-25 tests organized by user story

- [x] **Create**: `examples/tabs.py`
  - Showcase app demonstrating all 4 variants
  - HTMX lazy loading example
  - Icon examples
  - Disabled tab example

- [x] **Update**: `examples/showcase.py`
  - Add tabs route and navigation link

### Implementation Steps

1. **Phase 1: Basic Tabs** (US1 - 6 tests)
   - Create Tab and Tabs dataclasses
   - Implement basic rendering (tablist + panels)
   - Add ARIA attributes
   - Add Flowbite data attributes
   - Implement active tab logic

2. **Phase 2: Variants** (US2 - 7 tests)
   - Create TabVariant enum
   - Implement variant-specific class logic
   - Add color customization
   - Ensure dark mode classes always present

3. **Phase 3: HTMX** (US3 - 3 tests)
   - Add HTMX props to Tab
   - Apply HTMX attributes to panel (not button)

4. **Phase 4: Icons** (US4 - 4 tests)
   - Create IconPosition enum
   - Add icon props to Tab
   - Implement icon rendering with positioning

5. **Phase 5: Disabled** (US5 - 3 tests)
   - Add disabled prop to Tab
   - Render disabled tabs as `<a>` without href
   - Apply disabled styling

6. **Phase 6: Edge Cases** (4 tests)
   - Handle single tab, empty content, multiple active tabs, custom IDs

### Quality Gates

Before considering implementation complete:

- [ ] All 20-25 tests passing
- [ ] Test coverage >90% (target: 95-100%)
- [ ] mypy strict mode passes (no type errors)
- [ ] ruff check passes (no linting errors)
- [ ] ruff format applied (code formatted)
- [ ] Showcase app runs and demonstrates all features
- [ ] All 4 variants render correctly in showcase
- [ ] HTMX lazy loading works in showcase
- [ ] Keyboard navigation works (Flowbite JS)
- [ ] Dark mode toggle works in showcase

---

## Tips for TDD Success

1. **One test at a time**: Write one test, see it fail, make it pass, then move to next test
2. **Smallest step possible**: Don't implement more than needed to pass current test
3. **Run tests frequently**: After every change, run tests to verify behavior
4. **Refactor confidently**: With tests passing, refactor freely knowing tests will catch regressions
5. **Test behavior, not implementation**: Focus on what component renders, not how it does it
6. **Use descriptive test names**: Test name should explain what scenario is tested

---

## Expected Test Output (Final)

```bash
$ pytest tests/test_components/test_tabs.py -v

tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_renders_default_first_tab_active PASSED
tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_renders_custom_active_tab PASSED
tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_generates_unique_ids PASSED
tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_includes_aria_attributes PASSED
tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_includes_flowbite_data_attributes PASSED
tests/test_components/test_tabs.py::TestBasicTabNavigation::test_tabs_hides_inactive_panels PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_default_variant PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_underline_variant PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_pills_variant PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_full_width_variant PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_color_customization PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_dark_mode_classes PASSED
tests/test_components/test_tabs.py::TestTabVariants::test_tabs_custom_classes_merged PASSED
tests/test_components/test_tabs.py::TestHTMXIntegration::test_tabs_htmx_get_attribute PASSED
tests/test_components/test_tabs.py::TestHTMXIntegration::test_tabs_htmx_trigger_attribute PASSED
tests/test_components/test_tabs.py::TestHTMXIntegration::test_tabs_htmx_multiple_attributes PASSED
tests/test_components/test_tabs.py::TestTabIcons::test_tab_with_icon_left PASSED
tests/test_components/test_tabs.py::TestTabIcons::test_tab_with_icon_right PASSED
tests/test_components/test_tabs.py::TestTabIcons::test_tab_icon_in_disabled_state PASSED
tests/test_components/test_tabs.py::TestTabIcons::test_tab_icons_across_variants PASSED
tests/test_components/test_tabs.py::TestDisabledTabs::test_disabled_tab_styling PASSED
tests/test_components/test_tabs.py::TestDisabledTabs::test_disabled_tab_cannot_be_active PASSED
tests/test_components/test_tabs.py::TestDisabledTabs::test_disabled_tab_dark_mode PASSED
tests/test_components/test_tabs.py::TestEdgeCases::test_single_tab PASSED
tests/test_components/test_tabs.py::TestEdgeCases::test_empty_content PASSED
tests/test_components/test_tabs.py::TestEdgeCases::test_multiple_active_tabs_first_wins PASSED
tests/test_components/test_tabs.py::TestEdgeCases::test_custom_tabs_id_override PASSED

======================== 27 passed in 0.35s =========================

Coverage: 98%
```

---

## Next Steps After Implementation

1. **Run full test suite**: `pytest` (ensure 232/232 passing - 205 existing + 27 new)
2. **Check coverage**: `pytest --cov` (should be >90%)
3. **Type check**: `mypy src/flowbite_htmy` (strict mode, 100% coverage)
4. **Lint**: `ruff check src/flowbite_htmy` (should pass cleanly)
5. **Format**: `ruff format src/flowbite_htmy` (apply formatting)
6. **Run showcase**: `python examples/tabs.py` (verify all features work)
7. **Test in browser**: Open http://localhost:8000, test tab switching, keyboard nav, HTMX loading
8. **Update agent context**: `.specify/scripts/bash/update-agent-context.sh claude`
9. **Ready for PR**: All quality gates passed, ready to commit
