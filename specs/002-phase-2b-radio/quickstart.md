# Quickstart Guide: Radio Component

**Feature**: 002-phase-2b-radio
**Date**: 2025-11-14

## Overview

This guide provides step-by-step instructions for developers to implement and test the Radio component following TDD principles.

## Prerequisites

- Python 3.11+ installed
- Virtual environment activated
- Development dependencies installed (`pip install -e ".[dev]"`)
- Familiarity with existing component patterns (Input, Checkbox)

## Development Workflow

### Phase 1: Setup & Validation (TDD Red Phase)

**Step 1: Create ValidationState enum (if not exists)**

Check if `src/flowbite_htmy/types/validation.py` exists:

```bash
ls src/flowbite_htmy/types/validation.py
```

If not exists, create it:

```python
# src/flowbite_htmy/types/validation.py
"""Validation state enum for form components."""

from enum import Enum


class ValidationState(str, Enum):
    """Validation state for form components."""

    DEFAULT = "default"
    ERROR = "error"
    SUCCESS = "success"
```

Export from `src/flowbite_htmy/types/__init__.py`:

```python
from flowbite_htmy.types.validation import ValidationState

__all__ = [..., "ValidationState"]
```

---

**Step 2: Create test file**

Create `tests/test_components/test_radio.py`:

```python
"""Tests for Radio component."""

import pytest
from htmy import Context

from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState


@pytest.mark.asyncio
async def test_radio_default_rendering(renderer):
    """Test default radio button renders with minimal props."""
    radio = Radio(label="Accept Terms")
    html = await renderer.render(radio)

    assert "Accept Terms" in html
    assert 'type="radio"' in html
    assert 'class="' in html


@pytest.mark.asyncio
async def test_radio_checked_state(renderer):
    """Test radio button renders as checked."""
    radio = Radio(label="Option 1", checked=True)
    html = await renderer.render(radio)

    assert "checked" in html


# Add more tests here following TDD
```

---

**Step 3: Run failing tests**

```bash
pytest tests/test_components/test_radio.py
```

Expected: Tests fail because Radio component doesn't exist yet. ✅ **RED PHASE COMPLETE**

---

### Phase 2: Implement Component (TDD Green Phase)

**Step 4: Create Radio component**

Create `src/flowbite_htmy/components/radio.py`:

```python
"""Radio button component with validation and HTMX support."""

from dataclasses import dataclass
from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import ValidationState


# Module-level counter for auto-generated IDs
_radio_counter = 0


def _generate_radio_id() -> str:
    """Generate unique radio button ID."""
    global _radio_counter
    _radio_counter += 1
    return f"radio-{_radio_counter}"


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
        # Generate ID if not provided
        radio_id = self.id if self.id else _generate_radio_id()

        # Build classes
        input_classes = self._build_input_classes()
        label_classes = self._build_label_classes()
        helper_classes = self._build_helper_classes()

        # Build input element
        input_elem = html.input(
            type="radio",
            id=radio_id,
            name=self.name or None,
            value=self.value or None,
            checked=self.checked or None,
            disabled=self.disabled or None,
            aria_label=self.aria_label or None,
            class_=input_classes,
            hx_get=self.hx_get,
            hx_post=self.hx_post,
            hx_put=self.hx_put,
            hx_delete=self.hx_delete,
            hx_patch=self.hx_patch,
            hx_target=self.hx_target,
            hx_swap=self.hx_swap,
            hx_trigger=self.hx_trigger,
            hx_push_url=self.hx_push_url,
            hx_select=self.hx_select,
        )

        # Build label and helper text
        if self.label:
            label_elem = html.label(
                self.label,
                for_=radio_id,
                class_=label_classes,
            )
        else:
            label_elem = None

        helper_elem = (
            html.p(self.helper_text, class_=helper_classes)
            if self.helper_text
            else None
        )

        # Container structure
        return html.div(
            html.div(
                input_elem,
                class_="flex items-center h-5",
            ),
            html.div(
                label_elem,
                helper_elem,
                class_="ms-2 text-sm",
            ) if (label_elem or helper_elem) else None,
            class_="flex items-start",
        )

    def _build_input_classes(self) -> str:
        """Build CSS classes for input element."""
        builder = ClassBuilder("w-4 h-4 bg-gray-100 border-gray-300")
        builder.add("focus:ring-2 dark:ring-offset-gray-800")
        builder.add("dark:bg-gray-700 dark:border-gray-600")

        # Validation state colors
        if self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 border-red-500 dark:border-red-600")
            builder.add("focus:ring-red-500 dark:focus:ring-red-600")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 border-green-500 dark:border-green-600")
            builder.add("focus:ring-green-500 dark:focus:ring-green-600")
        else:
            builder.add("text-blue-600")
            builder.add("focus:ring-blue-500 dark:focus:ring-blue-600")

        if self.disabled:
            builder.add("disabled:opacity-50 disabled:cursor-not-allowed")

        return builder.merge(self.class_)

    def _build_label_classes(self) -> str:
        """Build CSS classes for label text."""
        builder = ClassBuilder("font-medium")

        # Validation state text colors
        if self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 dark:text-red-500")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 dark:text-green-500")
        elif self.disabled:
            builder.add("text-gray-400 dark:text-gray-500")
        else:
            builder.add("text-gray-900 dark:text-gray-300")

        return builder.build()

    def _build_helper_classes(self) -> str:
        """Build CSS classes for helper text."""
        builder = ClassBuilder()

        # Validation state text colors
        if self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 dark:text-red-500")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 dark:text-green-500")
        else:
            builder.add("text-gray-500 dark:text-gray-400")

        return builder.build()
```

---

**Step 5: Export from components package**

Edit `src/flowbite_htmy/components/__init__.py`:

```python
from flowbite_htmy.components.radio import Radio

__all__ = [..., "Radio"]
```

---

**Step 6: Run tests again**

```bash
pytest tests/test_components/test_radio.py
```

Expected: Initial tests pass. ✅ **GREEN PHASE COMPLETE**

---

### Phase 3: Complete Test Coverage (TDD Cycle)

**Step 7: Add comprehensive tests**

Continue TDD cycle by adding more tests to `test_radio.py`:

```python
@pytest.mark.asyncio
async def test_radio_validation_error_state(renderer):
    """Test radio with error validation state."""
    radio = Radio(
        label="Invalid Option",
        validation_state=ValidationState.ERROR,
        helper_text="This option is not available"
    )
    html = await renderer.render(radio)

    assert "Invalid Option" in html
    assert "text-red-600" in html  # Error color
    assert "This option is not available" in html


@pytest.mark.asyncio
async def test_radio_validation_success_state(renderer):
    """Test radio with success validation state."""
    radio = Radio(
        label="Valid Option",
        validation_state=ValidationState.SUCCESS,
        helper_text="Recommended choice"
    )
    html = await renderer.render(radio)

    assert "text-green-600" in html  # Success color
    assert "Recommended choice" in html


@pytest.mark.asyncio
async def test_radio_disabled_state(renderer):
    """Test disabled radio button."""
    radio = Radio(label="Disabled Option", disabled=True)
    html = await renderer.render(radio)

    assert "disabled" in html
    assert "disabled:opacity-50" in html


@pytest.mark.asyncio
async def test_radio_htmx_attributes(renderer):
    """Test radio with HTMX attributes."""
    radio = Radio(
        label="Dynamic Option",
        hx_get="/endpoint",
        hx_target="#result",
        hx_swap="innerHTML"
    )
    html = await renderer.render(radio)

    assert 'hx-get="/endpoint"' in html
    assert 'hx-target="#result"' in html
    assert 'hx-swap="innerHTML"' in html


@pytest.mark.asyncio
async def test_radio_empty_label_with_aria_label(renderer):
    """Test radio with empty label but aria-label provided."""
    radio = Radio(
        label="",
        aria_label="Select option",
        name="test",
        value="1"
    )
    html = await renderer.render(radio)

    assert 'aria-label="Select option"' in html
    assert 'name="test"' in html


def test_radio_empty_label_without_aria_label_raises_error():
    """Test that empty label without aria-label raises ValueError."""
    with pytest.raises(ValueError, match="Either 'label' or 'aria_label'"):
        Radio(label="", aria_label="")


# Add more tests for edge cases, dark mode classes, custom classes, etc.
```

Run tests after each addition:

```bash
pytest tests/test_components/test_radio.py -v
```

---

**Step 8: Achieve >90% coverage**

Check coverage:

```bash
pytest tests/test_components/test_radio.py --cov=src/flowbite_htmy/components/radio --cov-report=term-missing
```

Target: >90% coverage

---

### Phase 4: Type Checking & Linting

**Step 9: Type check with mypy**

```bash
mypy src/flowbite_htmy/components/radio.py
```

Expected: No type errors (100% type coverage)

---

**Step 10: Lint and format**

```bash
ruff check src/flowbite_htmy/components/radio.py
ruff format src/flowbite_htmy/components/radio.py
```

Fix any issues reported by ruff.

---

### Phase 5: Create Showcase Application

**Step 11: Create standalone showcase**

Create `examples/radios.py`:

```python
"""Radio button component showcase application."""

from fasthx import Jinja
from fastapi import FastAPI
from htmy import html

from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState

app = FastAPI()
jinja = Jinja(app)


def build_radios_showcase():
    """Build comprehensive radio button showcase content."""
    return html.div(
        # Section 1: Basic Radio Groups
        html.h2("Basic Radio Groups", class_="text-2xl font-bold mb-4"),

        # Payment method example
        html.div(
            html.h3("Payment Method", class_="text-lg font-semibold mb-2"),
            Radio(label="Credit Card", name="payment", value="credit", checked=True),
            Radio(label="PayPal", name="payment", value="paypal"),
            Radio(label="Bank Transfer", name="payment", value="bank"),
            class_="mb-8"
        ),

        # More sections...
        class_="container mx-auto px-4 py-8"
    )


@app.get("/")
async def index():
    """Render radio showcase."""
    section = build_radios_showcase()
    return await jinja.render_template(
        "radio-layout.html.jinja",
        {"content": await jinja.render(section)}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Create `examples/templates/radio-layout.html.jinja`:

```jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Component Showcase - Flowbite HTMY</title>
    <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css" rel="stylesheet" />
    <script src="https://unpkg.com/htmx.org@2.0.2"></script>
</head>
<body>
    {{ content | safe }}
    <script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"></script>
</body>
</html>
```

---

**Step 12: Run showcase**

```bash
python examples/radios.py
```

Visit http://localhost:8000 to see the showcase.

---

### Phase 6: Integration with Consolidated Showcase

**Step 13: Extract showcase function and add to consolidated app**

Follow the pattern from other components to integrate into `examples/showcase.py`.

---

## Common Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run all Radio tests
pytest tests/test_components/test_radio.py

# Run tests with coverage
pytest tests/test_components/test_radio.py --cov=src/flowbite_htmy/components/radio

# Type check
mypy src/flowbite_htmy/components/radio.py

# Lint
ruff check src/flowbite_htmy/components/radio.py

# Format
ruff format src/flowbite_htmy/components/radio.py

# Run standalone showcase
python examples/radios.py

# Run all tests (entire project)
pytest

# Run with verbose output
pytest -v tests/test_components/test_radio.py
```

---

## Verification Checklist

- [ ] ValidationState enum created (if not exists) and exported
- [ ] Radio component implemented in `src/flowbite_htmy/components/radio.py`
- [ ] Component exported from `src/flowbite_htmy/components/__init__.py`
- [ ] Tests created in `tests/test_components/test_radio.py`
- [ ] All tests pass (`pytest tests/test_components/test_radio.py`)
- [ ] Coverage >90% (`pytest --cov`)
- [ ] Type checking passes (`mypy`)
- [ ] Linting passes (`ruff check`)
- [ ] Code formatted (`ruff format`)
- [ ] Standalone showcase works (`python examples/radios.py`)
- [ ] Integrated into consolidated showcase (optional)

---

## Troubleshooting

**Issue**: ValidationState import error
**Solution**: Ensure `src/flowbite_htmy/types/validation.py` exists and is exported from `__init__.py`

**Issue**: Tests fail with "Radio not found"
**Solution**: Ensure Radio is exported from `src/flowbite_htmy/components/__init__.py`

**Issue**: Type errors in mypy
**Solution**: Check all type hints are correct, ensure `str | None` syntax (Python 3.11+)

**Issue**: Coverage below 90%
**Solution**: Add tests for edge cases (empty labels, disabled states, all validation states)

---

## Next Steps

After completing Radio component:
1. Merge branch to main
2. Update component viability ranking (mark Radio as complete)
3. Proceed with next Phase 2B component (Textarea)
4. Update consolidated showcase with Radio examples

---

## Reference

- Spec: `specs/002-phase-2b-radio/spec.md`
- Research: `specs/002-phase-2b-radio/research.md`
- Data Model: `specs/002-phase-2b-radio/data-model.md`
- Contract: `specs/002-phase-2b-radio/contracts/radio-component.md`
- Checkbox Component (reference): `src/flowbite_htmy/components/checkbox.py`
- Input Component (reference): `src/flowbite_htmy/components/input.py`
