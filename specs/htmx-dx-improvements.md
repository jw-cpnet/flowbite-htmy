# HTMX DX Improvements Spec

## Overview

This spec outlines improvements to the HTMX developer experience in flowbite-htmy, based on friction points discovered during the Nexus migration project.

## Problem Statement

During migration, we encountered these DX issues:

1. **Missing `hx_include`** - Button has many HTMX attrs but is missing `hx_include`, causing TypeError
2. **Event handlers require attrs dict** - `hx-on::after-request` can't be a Python kwarg due to colons
3. **HTMX attrs duplicated** - Button has ~10 HTMX params, but other components (Input, Select) don't

## Changes

### 1. Add Missing HTMX Attributes to Button

**File**: `src/flowbite_htmy/components/button.py`

Add these fields after line 102 (`hx_select`):

```python
hx_include: str | None = None
"""HTMX hx-include attribute for including additional element values."""

hx_confirm: str | None = None
"""HTMX hx-confirm attribute for confirmation dialog."""

hx_vals: str | None = None
"""HTMX hx-vals attribute for adding values to request."""

hx_indicator: str | None = None
"""HTMX hx-indicator attribute for loading indicator element."""

hx_encoding: str | None = None
"""HTMX hx-encoding attribute for request encoding type."""

hx_headers: str | None = None
"""HTMX hx-headers attribute for additional request headers."""

hx_disabled_elt: str | None = None
"""HTMX hx-disabled-elt attribute for elements to disable during request."""
```

Update `button_attrs` dict in `htmy()` method (~line 221-235):

```python
button_attrs: dict[str, Any] = {
    "type": self.type_,
    "disabled": is_disabled or None,
    "class": classes,
    "hx-get": self.hx_get,
    "hx-post": self.hx_post,
    "hx-target": self.hx_target,
    "hx-swap": self.hx_swap,
    "hx-trigger": self.hx_trigger,
    "hx-put": self.hx_put,
    "hx-delete": self.hx_delete,
    "hx-patch": self.hx_patch,
    "hx-push-url": self.hx_push_url,
    "hx-select": self.hx_select,
    # New attributes:
    "hx-include": self.hx_include,
    "hx-confirm": self.hx_confirm,
    "hx-vals": self.hx_vals,
    "hx-indicator": self.hx_indicator,
    "hx-encoding": self.hx_encoding,
    "hx-headers": self.hx_headers,
    "hx-disabled-elt": self.hx_disabled_elt,
}
```

---

### 2. Add `hx_on` Dict Parameter for Event Handlers

**File**: `src/flowbite_htmy/components/button.py`

Add after the other HTMX attributes:

```python
hx_on: dict[str, str] | None = None
"""HTMX event handlers as dict.

Keys are event names (without 'hx-on::' prefix), values are JavaScript code.

Example:
    Button(
        label="Save",
        hx_post="/api/save",
        hx_on={
            "after-request": "if(event.detail.successful) { drawer.hide(); }",
            "before-request": "showLoading()",
        }
    )

Renders as:
    <button hx-post="/api/save"
            hx-on::after-request="if(event.detail.successful) { drawer.hide(); }"
            hx-on::before-request="showLoading()">
        Save
    </button>
"""
```

Update `htmy()` method to process `hx_on` before merging attrs:

```python
# After building button_attrs dict, before merging self.attrs:

# Add hx-on event handlers
if self.hx_on:
    for event, handler in self.hx_on.items():
        button_attrs[f"hx-on::{event}"] = handler

# Merge passthrough attributes
if self.attrs:
    button_attrs.update(self.attrs)
```

---

### 3. Create HtmxMixin for Reusability (Optional Enhancement)

**New File**: `src/flowbite_htmy/base/htmx.py`

```python
"""HTMX attribute mixin for components."""

from dataclasses import dataclass
from typing import Any


@dataclass
class HtmxAttrs:
    """Mixin providing HTMX attributes for interactive components.

    This dataclass can be used as a mixin or standalone to add HTMX
    functionality to any component.

    Example:
        @dataclass(frozen=True, kw_only=True)
        class MyComponent(HtmxAttrs):
            label: str

            def htmy(self, context: Context) -> Component:
                attrs = self.build_htmx_attrs()
                return html.div(self.label, **attrs)
    """

    # Request attributes
    hx_get: str | None = None
    """HTMX hx-get attribute."""

    hx_post: str | None = None
    """HTMX hx-post attribute."""

    hx_put: str | None = None
    """HTMX hx-put attribute."""

    hx_delete: str | None = None
    """HTMX hx-delete attribute."""

    hx_patch: str | None = None
    """HTMX hx-patch attribute."""

    # Target/swap attributes
    hx_target: str | None = None
    """HTMX hx-target attribute."""

    hx_swap: str | None = None
    """HTMX hx-swap attribute."""

    hx_select: str | None = None
    """HTMX hx-select attribute."""

    hx_select_oob: str | None = None
    """HTMX hx-select-oob attribute."""

    hx_swap_oob: str | None = None
    """HTMX hx-swap-oob attribute."""

    # Trigger/timing attributes
    hx_trigger: str | None = None
    """HTMX hx-trigger attribute."""

    hx_push_url: str | bool | None = None
    """HTMX hx-push-url attribute."""

    # Request modification attributes
    hx_include: str | None = None
    """HTMX hx-include attribute."""

    hx_vals: str | None = None
    """HTMX hx-vals attribute."""

    hx_headers: str | None = None
    """HTMX hx-headers attribute."""

    hx_encoding: str | None = None
    """HTMX hx-encoding attribute."""

    # UX attributes
    hx_confirm: str | None = None
    """HTMX hx-confirm attribute."""

    hx_indicator: str | None = None
    """HTMX hx-indicator attribute."""

    hx_disabled_elt: str | None = None
    """HTMX hx-disabled-elt attribute."""

    hx_boost: bool | None = None
    """HTMX hx-boost attribute."""

    # Event handlers
    hx_on: dict[str, str] | None = None
    """HTMX event handlers as dict.

    Keys are event names, values are JavaScript code.
    Example: {"after-request": "drawer.hide()"}
    Renders as: hx-on::after-request="drawer.hide()"
    """

    def build_htmx_attrs(self) -> dict[str, Any]:
        """Build dict of HTMX attributes for HTML rendering.

        Returns:
            Dict with hx-* attribute names as keys.
            None values are excluded.
        """
        attrs: dict[str, Any] = {}

        # Map field names to HTML attribute names
        attr_map = {
            "hx_get": "hx-get",
            "hx_post": "hx-post",
            "hx_put": "hx-put",
            "hx_delete": "hx-delete",
            "hx_patch": "hx-patch",
            "hx_target": "hx-target",
            "hx_swap": "hx-swap",
            "hx_select": "hx-select",
            "hx_select_oob": "hx-select-oob",
            "hx_swap_oob": "hx-swap-oob",
            "hx_trigger": "hx-trigger",
            "hx_push_url": "hx-push-url",
            "hx_include": "hx-include",
            "hx_vals": "hx-vals",
            "hx_headers": "hx-headers",
            "hx_encoding": "hx-encoding",
            "hx_confirm": "hx-confirm",
            "hx_indicator": "hx-indicator",
            "hx_disabled_elt": "hx-disabled-elt",
            "hx_boost": "hx-boost",
        }

        for field_name, attr_name in attr_map.items():
            value = getattr(self, field_name, None)
            if value is not None:
                attrs[attr_name] = value

        # Event handlers: hx-on::event-name
        if self.hx_on:
            for event, handler in self.hx_on.items():
                attrs[f"hx-on::{event}"] = handler

        return attrs
```

**Update**: `src/flowbite_htmy/base/__init__.py`

```python
from flowbite_htmy.base.htmx import HtmxAttrs

__all__ = [
    # ... existing exports
    "HtmxAttrs",
]
```

---

### 4. Add Tests

**File**: `tests/test_button_htmx.py`

```python
"""Tests for Button HTMX functionality."""

import pytest
from htmy import HTMY

from flowbite_htmy.components import Button


@pytest.fixture
def htmy():
    return HTMY()


class TestButtonHtmxInclude:
    """Test hx_include attribute."""

    async def test_hx_include_renders(self, htmy):
        button = Button(
            label="Delete",
            hx_delete="/api/items/1",
            hx_include="[name='page'], [name='size']",
        )
        html = await htmy.render(button)
        assert 'hx-include="[name=\'page\'], [name=\'size\']"' in html


class TestButtonHxOn:
    """Test hx_on event handlers."""

    async def test_single_event_handler(self, htmy):
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={"after-request": "drawer.hide()"},
        )
        html = await htmy.render(button)
        assert 'hx-on::after-request="drawer.hide()"' in html

    async def test_multiple_event_handlers(self, htmy):
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={
                "before-request": "showLoading()",
                "after-request": "hideLoading()",
            },
        )
        html = await htmy.render(button)
        assert 'hx-on::before-request="showLoading()"' in html
        assert 'hx-on::after-request="hideLoading()"' in html

    async def test_complex_handler_with_condition(self, htmy):
        handler = "if(event.detail.successful) { drawer.hide(); }"
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={"after-request": handler},
        )
        html = await htmy.render(button)
        assert f'hx-on::after-request="{handler}"' in html


class TestButtonHtmxConfirm:
    """Test hx_confirm attribute."""

    async def test_hx_confirm_renders(self, htmy):
        button = Button(
            label="Delete",
            hx_delete="/api/items/1",
            hx_confirm="Are you sure?",
        )
        html = await htmy.render(button)
        assert 'hx-confirm="Are you sure?"' in html
```

---

## Usage Examples After Changes

### Before (Current - Awkward)

```python
# Must use attrs dict for hx-include
Button(
    label="Delete",
    attrs={
        "hx-delete": "/api/items/1",
        "hx-include": "[name='page']",
        "hx-on::after-request": "drawer.hide()",
    },
)
```

### After (Clean)

```python
# Native support for all common HTMX attributes
Button(
    label="Delete",
    hx_delete="/api/items/1",
    hx_include="[name='page']",
    hx_on={"after-request": "drawer.hide()"},
)
```

---

## Implementation Order

1. **Add missing attrs to Button** (hx_include, hx_confirm, etc.) - Quick win
2. **Add hx_on dict param** - Major DX improvement
3. **Add tests** - Verify functionality
4. **Create HtmxMixin** (optional) - For future components

## Success Criteria

- [ ] `Button(hx_include="...")` works without TypeError
- [ ] `Button(hx_on={"after-request": "..."})` renders correctly
- [ ] All new attributes have docstrings
- [ ] Tests pass for new functionality
- [ ] Existing tests still pass
