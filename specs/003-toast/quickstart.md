# Quickstart: Toast Component Implementation

**Feature**: Toast notification component
**Branch**: 003-toast
**Date**: 2025-11-14

## Overview

This guide provides step-by-step instructions for implementing the Toast component using Test-Driven Development (TDD). Follow this workflow to ensure quality, maintainability, and compliance with project constitution.

## Prerequisites

Before starting implementation:

- [x] Feature specification complete (`spec.md`)
- [x] Implementation plan complete (`plan.md`)
- [x] Research complete (`research.md`)
- [x] Data model defined (`data-model.md`)
- [x] API contract documented (`contracts/toast-component.md`)
- [x] Branch created and checked out (`003-toast`)
- [ ] Development environment ready (Python 3.11+, dependencies installed)

## Development Setup

### 1. Activate Virtual Environment

```bash
cd /home/jian/Work/personal/flowbite-htmy
source .venv/bin/activate
```

### 2. Verify Dependencies

```bash
# Check all dependencies installed
pip list | grep -E "htmy|pytest|mypy|ruff"

# If missing, install in editable mode
pip install -e ".[dev]"
```

### 3. Run Existing Tests (Sanity Check)

```bash
# All existing tests should pass
pytest --no-cov -q

# Expected: 164 tests passing (from last session)
```

## TDD Workflow (Red-Green-Refactor)

### Phase 1: User Story 1 - Simple Toast Notifications (P1 - MVP)

**Goal**: Basic toast with message, variant, icon, dismiss button

#### Step 1.1: Create Test File

```bash
touch tests/test_components/test_toast.py
```

#### Step 1.2: Write First Failing Test (RED)

**File**: `tests/test_components/test_toast.py`

```python
import pytest
from htmy import Context
from flowbite_htmy.components import Toast
from flowbite_htmy.types import ToastVariant


@pytest.mark.asyncio
async def test_toast_renders_default(renderer):
    """Test default toast renders with minimal props."""
    toast = Toast(message="Test message")
    html = await renderer.render(toast)

    assert "Test message" in html
    assert "role=\"alert\"" in html
    assert "toast-" in html  # Auto-generated ID
```

#### Step 1.3: Run Test - Verify FAILURE

```bash
pytest tests/test_components/test_toast.py::test_toast_renders_default -v

# Expected: ImportError (Toast doesn't exist yet)
```

#### Step 1.4: Create Enum - ToastVariant (GREEN)

**File**: `src/flowbite_htmy/types/toast.py` (NEW)

```python
"""Toast component types."""

from enum import Enum


class ToastVariant(str, Enum):
    """Toast notification variants."""

    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
```

**File**: `src/flowbite_htmy/types/__init__.py` (MODIFY)

```python
# Add to existing exports
from flowbite_htmy.types.toast import ToastVariant

__all__ = [
    # ... existing exports
    "ToastVariant",
]
```

#### Step 1.5: Create Component Stub - Toast (GREEN)

**File**: `src/flowbite_htmy/components/toast.py` (NEW)

```python
"""Toast notification component."""

from dataclasses import dataclass
from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import ToastVariant


@dataclass(frozen=True, kw_only=True)
class Toast:
    """Toast notification component.

    Temporary notification message with icon, optional action buttons,
    and dismissible close button.
    """

    # Required
    message: str

    # Optional - Styling
    variant: ToastVariant = ToastVariant.INFO
    icon: Icon | None = None
    class_: str = ""

    # Optional - Functionality
    dismissible: bool = True
    id: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render toast notification."""
        theme = ThemeContext.from_context(context)
        toast_id = self.id or f"toast-{id(self)}"

        # Minimal implementation to pass first test
        return html.div(
            self.message,
            id=toast_id,
            role="alert"
        )
```

**File**: `src/flowbite_htmy/components/__init__.py` (MODIFY)

```python
# Add to existing exports
from flowbite_htmy.components.toast import Toast

__all__ = [
    # ... existing exports
    "Toast",
]
```

#### Step 1.6: Run Test - Verify PASS

```bash
pytest tests/test_components/test_toast.py::test_toast_renders_default -v

# Expected: PASSED
```

#### Step 1.7: Add More Tests for Variants (RED)

```python
@pytest.mark.asyncio
async def test_toast_variant_success(renderer):
    """Test success variant renders with green colors."""
    toast = Toast(message="Success", variant=ToastVariant.SUCCESS)
    html = await renderer.render(toast)

    assert "Success" in html
    assert "text-green-500" in html
    assert "bg-green-100" in html


@pytest.mark.asyncio
async def test_toast_variant_danger(renderer):
    """Test danger variant renders with red colors."""
    toast = Toast(message="Error", variant=ToastVariant.DANGER)
    html = await renderer.render(toast)

    assert "Error" in html
    assert "text-red-500" in html
    assert "bg-red-100" in html
```

#### Step 1.8: Run Tests - Verify FAILURE

```bash
pytest tests/test_components/test_toast.py -v

# Expected: 2 failures (color classes not in HTML)
```

#### Step 1.9: Implement Full Rendering (GREEN)

```python
# Update Toast.htmy() method with full implementation
def htmy(self, context: Context) -> Component:
    """Render toast notification."""
    theme = ThemeContext.from_context(context)
    toast_id = self.id or f"toast-{id(self)}"
    icon = self._get_icon()
    classes = self._build_classes(theme)

    return html.div(
        self._render_icon_container(icon),
        html.div(self.message, class_="ms-3 text-sm font-normal"),
        self._render_close_button(toast_id) if self.dismissible else None,
        id=toast_id,
        class_=classes,
        role="alert",
    )


def _build_classes(self, theme: ThemeContext) -> str:
    """Build container classes."""
    builder = ClassBuilder(
        "flex items-center w-full max-w-xs p-4",
        "text-gray-500 bg-white rounded-lg shadow-sm",
        "dark:text-gray-400 dark:bg-gray-800",
    )
    return builder.merge(self.class_)


def _get_icon(self) -> Icon:
    """Get icon for toast (custom or default)."""
    if self.icon is not None:
        return self.icon

    # Default icons per variant
    return {
        ToastVariant.SUCCESS: Icon.CHECK,
        ToastVariant.DANGER: Icon.CLOSE,
        ToastVariant.WARNING: Icon.EXCLAMATION,
        ToastVariant.INFO: Icon.INFO,
    }[self.variant]


def _render_icon_container(self, icon: Icon) -> Component:
    """Render icon container with variant colors."""
    icon_classes = {
        ToastVariant.SUCCESS: (
            "inline-flex items-center justify-center shrink-0 w-8 h-8 "
            "text-green-500 bg-green-100 rounded-lg "
            "dark:bg-green-800 dark:text-green-200"
        ),
        ToastVariant.DANGER: (
            "inline-flex items-center justify-center shrink-0 w-8 h-8 "
            "text-red-500 bg-red-100 rounded-lg "
            "dark:bg-red-800 dark:text-red-200"
        ),
        ToastVariant.WARNING: (
            "inline-flex items-center justify-center shrink-0 w-8 h-8 "
            "text-yellow-500 bg-yellow-100 rounded-lg "
            "dark:bg-yellow-800 dark:text-yellow-200"
        ),
        ToastVariant.INFO: (
            "inline-flex items-center justify-center shrink-0 w-8 h-8 "
            "text-blue-500 bg-blue-100 rounded-lg "
            "dark:bg-blue-800 dark:text-blue-200"
        ),
    }[self.variant]

    icon_component = get_icon(icon, class_="w-4 h-4", aria_hidden="true")

    return html.div(icon_component, class_=icon_classes)


def _render_close_button(self, toast_id: str) -> Component:
    """Render dismissible close button."""
    return html.button(
        html.span("Close", class_="sr-only"),
        get_icon(Icon.CLOSE, class_="w-3 h-3"),
        type="button",
        class_=(
            "ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 "
            "rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 "
            "inline-flex items-center justify-center h-8 w-8 "
            "dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
        ),
        data_dismiss_target=f"#{toast_id}",
        aria_label="Close",
    )
```

#### Step 1.10: Run All Tests - Verify PASS

```bash
pytest tests/test_components/test_toast.py -v

# Expected: All tests passing
```

#### Step 1.11: Run Type Checker (REFACTOR)

```bash
mypy src/flowbite_htmy/components/toast.py
mypy src/flowbite_htmy/types/toast.py

# Expected: Success (no type errors)
```

#### Step 1.12: Run Linter (REFACTOR)

```bash
ruff check src/flowbite_htmy/components/toast.py
ruff format src/flowbite_htmy/components/toast.py

# Expected: All checks pass, code formatted
```

#### Step 1.13: Check Coverage

```bash
pytest tests/test_components/test_toast.py --cov=src/flowbite_htmy/components/toast --cov-report=term

# Expected: >90% coverage
# If <90%, add more tests
```

### Phase 2: User Story 2 - Interactive Toast (P2)

**Goal**: Action buttons with HTMX integration

#### Step 2.1: Add ToastActionButton Tests (RED)

```python
from flowbite_htmy.components import ToastActionButton


@pytest.mark.asyncio
async def test_toast_with_action_button(renderer):
    """Test toast with action button renders correctly."""
    action = ToastActionButton(label="Reply", hx_get="/reply")
    toast = Toast(message="New message", action_button=action)
    html = await renderer.render(toast)

    assert "Reply" in html
    assert 'hx-get="/reply"' in html
```

#### Step 2.2: Run Test - Verify FAILURE

```bash
pytest tests/test_components/test_toast.py::test_toast_with_action_button -v

# Expected: ImportError (ToastActionButton doesn't exist)
```

#### Step 2.3: Implement ToastActionButton (GREEN)

```python
# Add to toast.py BEFORE Toast class

@dataclass(frozen=True, kw_only=True)
class ToastActionButton:
    """Action button for interactive toasts."""

    label: str

    # HTMX attributes
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

    type_: str = "button"
    class_: str = ""


# Update Toast dataclass - add field:
action_button: ToastActionButton | None = None


# Update Toast.htmy() to render action button
# Update Toast._render_content() to include action button rendering
```

#### Step 2.4: Run Test - Verify PASS

```bash
pytest tests/test_components/test_toast.py::test_toast_with_action_button -v

# Expected: PASSED
```

### Phase 3: User Story 3 - Accessibility (P3)

**Goal**: Dark mode, ARIA attributes, custom styling

#### Step 3.1: Add Accessibility Tests (RED)

```python
@pytest.mark.asyncio
async def test_toast_accessibility_attributes(renderer):
    """Test toast includes proper ARIA attributes."""
    toast = Toast(message="Accessible toast")
    html = await renderer.render(toast)

    assert 'role="alert"' in html
    assert 'aria-hidden="true"' in html  # On icon
    assert 'aria-label="Close"' in html  # On close button
    assert 'class="sr-only"' in html  # Screen reader text


@pytest.mark.asyncio
async def test_toast_dark_mode_classes(renderer):
    """Test toast includes dark mode classes."""
    toast = Toast(message="Dark mode toast")
    html = await renderer.render(toast)

    assert "dark:bg-gray-800" in html
    assert "dark:text-gray-400" in html
```

#### Step 3.2: Run Tests - Verify FAILURE (or PASS if already implemented)

```bash
pytest tests/test_components/test_toast.py -k accessibility -v
pytest tests/test_components/test_toast.py -k dark_mode -v
```

#### Step 3.3: Ensure Implementation Complete (GREEN)

(Most accessibility features already implemented in Phase 1)

### Phase 4: Showcase Application

#### Step 4.1: Create Showcase Function

**File**: `examples/toasts.py` (NEW)

```python
"""Toast component showcase."""

from htmy import html

from flowbite_htmy.components import Toast, ToastActionButton
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import ToastVariant


def build_toasts_showcase():
    """Build comprehensive toast showcase content."""
    return html.div(
        # Section 1: Basic Variants
        _section_basic_variants(),

        # Section 2: Custom Icons
        _section_custom_icons(),

        # Section 3: Dismissible Control
        _section_dismissible(),

        # Section 4: Interactive Toasts
        _section_interactive(),

        # Section 5: Rich Content
        _section_rich_content(),

        # Section 6: Custom Styling
        _section_custom_styling(),

        class_="space-y-8",
    )


def _section_basic_variants():
    """Showcase basic toast variants."""
    return html.div(
        html.h2("Basic Variants", class_="text-2xl font-bold mb-4"),
        html.div(
            Toast(message="Operation successful", variant=ToastVariant.SUCCESS),
            Toast(message="Connection failed", variant=ToastVariant.DANGER),
            Toast(message="Please review your settings", variant=ToastVariant.WARNING),
            Toast(message="New updates available", variant=ToastVariant.INFO),
            class_="space-y-4",
        ),
    )


# ... implement other sections
```

#### Step 4.2: Integrate into Consolidated Showcase

**File**: `examples/showcase.py` (MODIFY)

```python
# Add import
from examples.toasts import build_toasts_showcase

# Add route
@app.get("/toasts")
async def toasts_route() -> dict:
    """Toast notifications showcase."""
    section = build_toasts_showcase()
    return {
        "content": await renderer.render(section),
        "active_page": "toasts",
        "routes": ROUTES,
    }

# Add to ROUTES list
ROUTES = [
    # ... existing routes
    {"path": "/toasts", "name": "Toasts"},
]
```

#### Step 4.3: Test Showcase Locally

```bash
python examples/showcase.py
# Visit http://localhost:8000/toasts
# Verify all examples render correctly
```

## Quality Gates

### Gate 1: Test Coverage

```bash
pytest tests/test_components/test_toast.py --cov=src/flowbite_htmy/components/toast --cov-report=term

# Required: >95% coverage
```

### Gate 2: Type Checking

```bash
mypy src/flowbite_htmy/components/toast.py src/flowbite_htmy/types/toast.py

# Required: No errors
```

### Gate 3: Linting

```bash
ruff check src/flowbite_htmy
ruff format --check src/flowbite_htmy

# Required: All checks pass
```

### Gate 4: Full Test Suite

```bash
pytest

# Required: All tests pass (164 + new tests)
```

## Commit Guidelines

### Commit 1: Component Implementation

```bash
git add src/flowbite_htmy/components/toast.py
git add src/flowbite_htmy/types/toast.py
git add src/flowbite_htmy/components/__init__.py
git add src/flowbite_htmy/types/__init__.py
git add tests/test_components/test_toast.py

git commit -m "Implement Toast component with full TDD (Phase 2C)

- Created ToastVariant enum (SUCCESS, DANGER, WARNING, INFO)
- Implemented Toast dataclass with all user stories
- Implemented ToastActionButton for interactive toasts
- 22 comprehensive tests (all passing)
- 99% test coverage
- Full HTMX integration support
- Accessibility compliant (ARIA attributes)
- Dark mode support (always include dark: classes)

User Stories Complete:
- P1: Simple Toast Notifications (MVP)
- P2: Interactive Toast (action buttons)
- P3: Accessibility (dark mode, ARIA, custom styling)

Quality Metrics:
- Test coverage: 99%
- Type checking: 100% (mypy strict mode)
- All ruff checks pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Commit 2: Showcase Integration

```bash
git add examples/toasts.py
git add examples/showcase.py

git commit -m "Add Toast component showcase with 6 sections

- Created build_toasts_showcase() function
- 6 showcase sections: variants, icons, dismissible, interactive, rich, custom
- Integrated into consolidated showcase app
- Added /toasts route and navigation entry

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

## Troubleshooting

### Issue: Tests fail with ImportError

**Solution**: Ensure exports added to `__init__.py` files

### Issue: Type errors in mypy

**Solution**: Add explicit return type hints, use union types (`str | None`)

### Issue: Coverage below 95%

**Solution**: Add tests for edge cases (empty messages, None values, etc.)

### Issue: Icons not rendering

**Solution**: Verify Icon enum values exist in `icons.py`, check get_icon() usage

## Next Steps

After completing Toast component:

1. Run full test suite: `pytest`
2. Update Basic Memory session notes
3. Update component viability ranking (mark Toast as complete)
4. Consider next component (Accordion, Tabs, or Dropdown per Phase 2C)

## Success Criteria Checklist

- [ ] All 3 user stories implemented
- [ ] 22+ tests written and passing
- [ ] >95% test coverage achieved
- [ ] Mypy strict mode passes (100% type coverage)
- [ ] Ruff checks pass (no warnings)
- [ ] Showcase with 6+ examples complete
- [ ] Component exports added to __init__.py
- [ ] Documentation complete (docstrings)
- [ ] Dark mode classes always included
- [ ] ARIA attributes correct (role="alert", aria-hidden, aria-label)
- [ ] HTMX integration working
- [ ] Flowbite dismiss functionality working (data-dismiss-target)

## Reference

- Spec: `specs/003-toast/spec.md`
- Plan: `specs/003-toast/plan.md`
- Research: `specs/003-toast/research.md`
- Data Model: `specs/003-toast/data-model.md`
- Contract: `specs/003-toast/contracts/toast-component.md`
- Constitution: `.specify/memory/constitution.md`
