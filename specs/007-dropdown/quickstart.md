# Quickstart: Dropdown Component TDD Implementation

**Feature**: Dropdown Component (007-dropdown)
**Date**: 2025-11-16
**Purpose**: Step-by-step TDD workflow for implementing dropdown menus

## Prerequisites

- Development environment setup complete
- Virtual environment activated: `source .venv/bin/activate`
- Dependencies installed: `pip install -e ".[dev]"`
- Branch checked out: `007-dropdown`

## TDD Workflow Overview

This guide follows strict Test-Driven Development (Red-Green-Refactor):

1. ✍️ **Write failing test** (RED)
2. ▶️ **Run test** → Confirm it fails
3. 💚 **Write minimal code** to pass test (GREEN)
4. ▶️ **Run test** → Confirm it passes
5. ♻️ **Refactor** if needed (keep tests GREEN)
6. 🔄 **Repeat** for next feature

---

## Phase 1: Setup and Enums

### Step 1.1: Create test file

```bash
touch tests/test_components/test_dropdown.py
```

### Step 1.2: Write enum tests (RED)

**File**: `tests/test_components/test_dropdown.py`

```python
"""Tests for Dropdown component."""
import pytest
from flowbite_htmy.types import (
    DropdownPlacement,
    DropdownTriggerType,
    DropdownTriggerMode,
)


def test_dropdown_placement_enum():
    """Test DropdownPlacement enum values."""
    assert DropdownPlacement.TOP == "top"
    assert DropdownPlacement.BOTTOM == "bottom"
    assert DropdownPlacement.LEFT == "left"
    assert DropdownPlacement.RIGHT == "right"


def test_dropdown_trigger_type_enum():
    """Test DropdownTriggerType enum values."""
    assert DropdownTriggerType.BUTTON == "button"
    assert DropdownTriggerType.AVATAR == "avatar"
    assert DropdownTriggerType.TEXT == "text"


def test_dropdown_trigger_mode_enum():
    """Test DropdownTriggerMode enum values."""
    assert DropdownTriggerMode.CLICK == "click"
    assert DropdownTriggerMode.HOVER == "hover"
```

### Step 1.3: Run tests (should FAIL)

```bash
pytest tests/test_components/test_dropdown.py -v
```

Expected: ImportError (enums don't exist yet)

### Step 1.4: Implement enums (GREEN)

**File**: `src/flowbite_htmy/types/__init__.py`

```python
# Add to existing file
from enum import Enum

class DropdownPlacement(str, Enum):
    """Dropdown menu positioning options."""
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"


class DropdownTriggerType(str, Enum):
    """Dropdown trigger element types."""
    BUTTON = "button"
    AVATAR = "avatar"
    TEXT = "text"


class DropdownTriggerMode(str, Enum):
    """Dropdown activation methods."""
    CLICK = "click"
    HOVER = "hover"


# Update __all__
__all__ = [
    # ... existing exports
    "DropdownPlacement",
    "DropdownTriggerType",
    "DropdownTriggerMode",
]
```

### Step 1.5: Run tests (should PASS)

```bash
pytest tests/test_components/test_dropdown.py -v
```

Expected: 3 tests pass ✅

---

## Phase 2: DropdownDivider

### Step 2.1: Write DropdownDivider test (RED)

**File**: `tests/test_components/test_dropdown.py`

```python
from flowbite_htmy.components import DropdownDivider


@pytest.mark.asyncio
async def test_dropdown_divider_renders(renderer):
    """Test DropdownDivider renders as hr element."""
    divider = DropdownDivider()
    html = await renderer.render(divider)

    assert "<hr" in html
    assert 'class="h-0 my-1 border-gray-100 dark:border-gray-600"' in html


@pytest.mark.asyncio
async def test_dropdown_divider_custom_class(renderer):
    """Test DropdownDivider with custom class."""
    divider = DropdownDivider(class_="my-4")
    html = await renderer.render(divider)

    assert "my-4" in html
```

### Step 2.2: Run tests (should FAIL)

```bash
pytest tests/test_components/test_dropdown.py::test_dropdown_divider_renders -v
```

Expected: ImportError

### Step 2.3: Implement DropdownDivider (GREEN)

**File**: `src/flowbite_htmy/components/dropdown.py` (NEW FILE)

```python
"""Dropdown component with Flowbite styling and JavaScript integration."""
from dataclasses import dataclass
from htmy import Component, Context, html
from flowbite_htmy.base import ClassBuilder


@dataclass(frozen=True, kw_only=True)
class DropdownDivider:
    """Horizontal divider for dropdown menus."""

    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render divider as <hr> element."""
        classes = ClassBuilder("h-0 my-1 border-gray-100 dark:border-gray-600")
        classes.merge(self.class_)

        return html.hr(class_=classes.build())
```

**File**: `src/flowbite_htmy/components/__init__.py`

```python
# Add to existing file
from flowbite_htmy.components.dropdown import DropdownDivider

__all__ = [
    # ... existing exports
    "DropdownDivider",
]
```

### Step 2.4: Run tests (should PASS)

```bash
pytest tests/test_components/test_dropdown.py::test_dropdown_divider_renders -v
pytest tests/test_components/test_dropdown.py::test_dropdown_divider_custom_class -v
```

Expected: 2 tests pass ✅

---

## Phase 3: DropdownHeader

### Step 3.1: Write DropdownHeader tests (RED)

**File**: `tests/test_components/test_dropdown.py`

```python
from flowbite_htmy.components import DropdownHeader


@pytest.mark.asyncio
async def test_dropdown_header_renders(renderer):
    """Test DropdownHeader renders with label."""
    header = DropdownHeader(label="Account Settings")
    html = await renderer.render(header)

    assert "Account Settings" in html
    assert 'role="presentation"' in html
    assert "text-gray-900" in html
    assert "dark:text-white" in html


@pytest.mark.asyncio
async def test_dropdown_header_custom_class(renderer):
    """Test DropdownHeader with custom class."""
    header = DropdownHeader(label="Settings", class_="font-bold")
    html = await renderer.render(header)

    assert "font-bold" in html
```

### Step 3.2: Run tests → FAIL

### Step 3.3: Implement DropdownHeader (GREEN)

**File**: `src/flowbite_htmy/components/dropdown.py`

```python
@dataclass(frozen=True, kw_only=True)
class DropdownHeader:
    """Non-interactive header for dropdown sections."""

    label: str
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render header with role=presentation."""
        classes = ClassBuilder("px-4 py-3 text-sm text-gray-900 dark:text-white")
        classes.merge(self.class_)

        return html.div(
            self.label,
            class_=classes.build(),
            role="presentation",
        )
```

**File**: `src/flowbite_htmy/components/__init__.py`

```python
from flowbite_htmy.components.dropdown import DropdownDivider, DropdownHeader

__all__ = [
    # ... existing exports
    "DropdownDivider",
    "DropdownHeader",
]
```

### Step 3.4: Run tests → PASS

---

## Phase 4: DropdownItem

### Step 4.1: Write DropdownItem tests (RED)

**File**: `tests/test_components/test_dropdown.py`

```python
from flowbite_htmy.components import DropdownItem
from flowbite_htmy.icons import Icon


@pytest.mark.asyncio
async def test_dropdown_item_simple(renderer):
    """Test simple DropdownItem renders."""
    item = DropdownItem(label="Profile", href="/profile")
    html = await renderer.render(item)

    assert "Profile" in html
    assert 'href="/profile"' in html
    assert 'role="menuitem"' in html
    assert "hover:bg-gray-100" in html
    assert "dark:hover:bg-gray-600" in html


@pytest.mark.asyncio
async def test_dropdown_item_with_icon(renderer):
    """Test DropdownItem with icon."""
    item = DropdownItem(label="Dashboard", icon=Icon.DASHBOARD, href="/dashboard")
    html = await renderer.render(item)

    assert "Dashboard" in html
    assert "<svg" in html  # Icon SVG


@pytest.mark.asyncio
async def test_dropdown_item_with_htmx(renderer):
    """Test DropdownItem with HTMX attributes."""
    item = DropdownItem(
        label="Load More",
        hx_get="/api/items",
        hx_target="#list",
        hx_swap="beforeend",
    )
    html = await renderer.render(item)

    assert "Load More" in html
    assert 'hx-get="/api/items"' in html
    assert 'hx-target="#list"' in html
    assert 'hx-swap="beforeend"' in html


@pytest.mark.asyncio
async def test_dropdown_item_disabled(renderer):
    """Test disabled DropdownItem."""
    item = DropdownItem(label="Coming Soon", disabled=True)
    html = await renderer.render(item)

    assert "Coming Soon" in html
    assert "opacity-50" in html or "cursor-not-allowed" in html
```

### Step 4.2: Run tests → FAIL

### Step 4.3: Implement DropdownItem (GREEN)

**File**: `src/flowbite_htmy/components/dropdown.py`

```python
from typing import TYPE_CHECKING
from flowbite_htmy.icons import Icon, get_icon

if TYPE_CHECKING:
    from flowbite_htmy.components.dropdown import Dropdown  # Forward reference


@dataclass(frozen=True, kw_only=True)
class DropdownItem:
    """Interactive menu item for dropdowns."""

    # Content
    label: str
    icon: Icon | None = None

    # Navigation
    href: str = "#"

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

    # State
    disabled: bool = False

    # Nested dropdown
    dropdown: "Dropdown | None" = None

    # Styling
    class_: str = ""

    def htmy(self, context: Context) -> Component:
        """Render menu item."""
        classes = self._build_classes()

        # Build link content
        children = []
        if self.icon:
            children.append(get_icon(self.icon, class_="w-4 h-4 mr-2"))
        children.append(self.label)

        # Build link attributes
        attrs = {
            "href": self.href,
            "class_": classes,
            "role": "menuitem",
            "tabindex": 0 if not self.disabled else -1,
        }

        # Add HTMX attributes if provided
        if self.hx_get:
            attrs["hx_get"] = self.hx_get
        if self.hx_post:
            attrs["hx_post"] = self.hx_post
        # ... (add other HTMX attributes)

        return html.li(
            html.a(*children, **attrs)
        )

    def _build_classes(self) -> str:
        """Build CSS classes for menu item."""
        builder = ClassBuilder("block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white")

        if self.disabled:
            builder.add("opacity-50 cursor-not-allowed")

        return builder.merge(self.class_)
```

### Step 4.4: Run tests → PASS

---

## Phase 5: Dropdown (Main Component)

### Step 5.1: Write Dropdown tests (RED)

**File**: `tests/test_components/test_dropdown.py`

```python
from flowbite_htmy.components import Dropdown
from flowbite_htmy.types import Color, Size, DropdownPlacement


@pytest.mark.asyncio
async def test_dropdown_basic_renders(renderer):
    """Test basic dropdown renders with button trigger."""
    dropdown = Dropdown(
        trigger_label="Actions",
        items=[
            DropdownItem(label="Edit", href="/edit"),
            DropdownItem(label="Delete", href="/delete"),
        ],
    )
    html = await renderer.render(dropdown)

    # Trigger button
    assert "Actions" in html
    assert 'data-dropdown-toggle="dropdown-' in html
    assert 'aria-expanded="false"' in html
    assert 'aria-haspopup="true"' in html

    # Menu
    assert 'role="menu"' in html
    assert "Edit" in html
    assert "Delete" in html


@pytest.mark.asyncio
async def test_dropdown_with_color_and_size(renderer):
    """Test dropdown with custom color and size."""
    dropdown = Dropdown(
        trigger_label="Options",
        color=Color.GREEN,
        size=Size.LG,
        items=[DropdownItem(label="Option 1")],
    )
    html = await renderer.render(dropdown)

    assert "bg-green-700" in html  # Green color
    assert "text-lg" in html or "px-6 py-3" in html  # Large size


@pytest.mark.asyncio
async def test_dropdown_with_placement(renderer):
    """Test dropdown with top placement."""
    dropdown = Dropdown(
        trigger_label="Dropdown",
        placement=DropdownPlacement.TOP,
        items=[DropdownItem(label="Item 1")],
    )
    html = await renderer.render(dropdown)

    assert 'data-dropdown-placement="top"' in html


@pytest.mark.asyncio
async def test_dropdown_with_avatar_trigger(renderer):
    """Test dropdown with avatar trigger."""
    dropdown = Dropdown(
        trigger_label="User Menu",
        trigger_type=DropdownTriggerType.AVATAR,
        avatar_src="/images/user.jpg",
        items=[DropdownItem(label="Profile")],
    )
    html = await renderer.render(dropdown)

    assert 'src="/images/user.jpg"' in html
    assert 'alt="User menu"' in html


@pytest.mark.asyncio
async def test_dropdown_aria_attributes(renderer):
    """Test dropdown ARIA attributes."""
    dropdown = Dropdown(
        trigger_label="Menu",
        dropdown_id="test-dropdown",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert 'id="trigger-test-dropdown"' in html
    assert 'aria-controls="test-dropdown"' in html
    assert 'id="test-dropdown"' in html
    assert 'aria-labelledby="trigger-test-dropdown"' in html


@pytest.mark.asyncio
async def test_dropdown_dark_mode_classes(renderer, dark_context):
    """Test dropdown includes dark mode classes."""
    dropdown = Dropdown(
        trigger_label="Menu",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown, dark_context)

    assert "dark:bg-blue-700" in html or "dark:hover:bg-blue-700" in html
    assert "dark:bg-gray-700" in html  # Menu container
```

### Step 5.2: Run tests → FAIL

### Step 5.3: Implement Dropdown (GREEN)

**File**: `src/flowbite_htmy/components/dropdown.py`

```python
from flowbite_htmy.types import Color, Size, DropdownPlacement, DropdownTriggerType, DropdownTriggerMode
from flowbite_htmy.base import ThemeContext


@dataclass(frozen=True, kw_only=True)
class Dropdown:
    """Toggleable dropdown menu with Flowbite integration."""

    # Items
    items: list[DropdownItem | DropdownHeader | DropdownDivider]

    # Trigger configuration
    trigger_label: str
    trigger_type: DropdownTriggerType = DropdownTriggerType.BUTTON
    trigger_mode: DropdownTriggerMode = DropdownTriggerMode.CLICK

    # Avatar trigger
    avatar_src: str | None = None
    avatar_alt: str = "User menu"

    # Button styling
    color: Color = Color.BLUE
    size: Size = Size.MD

    # Positioning
    placement: DropdownPlacement = DropdownPlacement.BOTTOM

    # Identifiers
    dropdown_id: str | None = None

    # State
    disabled: bool = False

    # Styling
    trigger_class: str = ""
    menu_class: str = ""

    def htmy(self, context: Context) -> Component:
        """Render dropdown with trigger and menu."""
        dropdown_id = self._get_dropdown_id()

        return html.div(
            self._render_trigger(context, dropdown_id),
            self._render_menu(context, dropdown_id),
        )

    def _get_dropdown_id(self) -> str:
        """Get or generate unique dropdown ID."""
        return self.dropdown_id or f"dropdown-{id(self)}"

    def _render_trigger(self, context: Context, dropdown_id: str) -> Component:
        """Render trigger element."""
        trigger_id = f"trigger-{dropdown_id}"
        theme = ThemeContext.from_context(context)

        if self.trigger_type == DropdownTriggerType.AVATAR:
            return self._render_avatar_trigger(trigger_id, dropdown_id)
        elif self.trigger_type == DropdownTriggerType.TEXT:
            return self._render_text_trigger(trigger_id, dropdown_id, theme)
        else:  # BUTTON
            return self._render_button_trigger(trigger_id, dropdown_id, theme)

    def _render_button_trigger(self, trigger_id: str, dropdown_id: str, theme: ThemeContext) -> Component:
        """Render button trigger."""
        classes = self._build_trigger_classes(theme)

        return html.button(
            self.trigger_label,
            # Chevron icon
            html.svg(class_="w-2.5 h-2.5 ms-3", ...),  # TODO: Add chevron SVG
            id=trigger_id,
            data_dropdown_toggle=dropdown_id,
            data_dropdown_placement=self.placement.value,
            data_dropdown_trigger=self.trigger_mode.value,
            aria_expanded="false",
            aria_haspopup="true",
            aria_controls=dropdown_id,
            type_="button",
            class_=classes,
            disabled=self.disabled,
        )

    def _render_menu(self, context: Context, dropdown_id: str) -> Component:
        """Render dropdown menu."""
        theme = ThemeContext.from_context(context)
        classes = self._build_menu_classes(theme)
        trigger_id = f"trigger-{dropdown_id}"

        return html.div(
            html.ul(
                *[item.htmy(context) for item in self.items],
                class_="py-2 text-sm text-gray-700 dark:text-gray-200",
            ),
            id=dropdown_id,
            role="menu",
            aria_labelledby=trigger_id,
            class_=classes,
        )

    def _build_trigger_classes(self, theme: ThemeContext) -> str:
        """Build trigger button classes."""
        # Color variant classes
        COLOR_CLASSES = {
            Color.BLUE: "bg-blue-700 hover:bg-blue-800 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            # ... other colors
        }

        # Size classes
        SIZE_CLASSES = {
            Size.XS: "px-3 py-2 text-xs",
            Size.SM: "px-4 py-2 text-sm",
            Size.MD: "px-5 py-2.5 text-sm",
            # ... other sizes
        }

        builder = ClassBuilder("text-white focus:ring-4 focus:outline-none font-medium rounded-lg inline-flex items-center")
        builder.add(COLOR_CLASSES[self.color])
        builder.add(SIZE_CLASSES[self.size])

        return builder.merge(self.trigger_class)

    def _build_menu_classes(self, theme: ThemeContext) -> str:
        """Build menu container classes."""
        builder = ClassBuilder("z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700")
        return builder.merge(self.menu_class)
```

### Step 5.4: Run tests → PASS

---

## Phase 6: Showcase Application

### Step 6.1: Create showcase file

```bash
touch examples/dropdowns.py
mkdir -p examples/templates
touch examples/templates/dropdowns.html.jinja
```

### Step 6.2: Implement showcase

**File**: `examples/dropdowns.py`

```python
"""Dropdown component showcase."""
from fastapi import FastAPI
from fasthx import Jinja
from flowbite_htmy.components import Dropdown, DropdownItem, DropdownHeader, DropdownDivider
from flowbite_htmy.types import Color, Size, DropdownPlacement, DropdownTriggerType
from flowbite_htmy.icons import Icon

app = FastAPI()
jinja = Jinja(templates_path="examples/templates")


@app.get("/")
@jinja.page("dropdowns.html.jinja")
def index():
    """Render dropdown showcase."""
    # Section 1: Basic dropdown
    basic_dropdown = Dropdown(
        trigger_label="Dropdown button",
        items=[
            DropdownItem(label="Dashboard", href="/dashboard"),
            DropdownItem(label="Settings", href="/settings"),
            DropdownItem(label="Earnings", href="/earnings"),
            DropdownItem(label="Sign out", href="/signout"),
        ],
    )

    # Section 2: Dropdown with header
    header_dropdown = Dropdown(
        trigger_label="User menu",
        items=[
            DropdownHeader(label="Bonnie Green"),
            DropdownHeader(label="name@flowbite.com"),
            DropdownDivider(),
            DropdownItem(label="Dashboard", href="/dashboard"),
            DropdownItem(label="Settings", href="/settings"),
            DropdownDivider(),
            DropdownItem(label="Sign out", href="/signout"),
        ],
    )

    # ... more sections

    return {
        "basic_dropdown": basic_dropdown,
        "header_dropdown": header_dropdown,
        # ...
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
```

**File**: `examples/templates/dropdowns.html.jinja`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dropdown Showcase</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css" rel="stylesheet" />
</head>
<body class="p-8">
    <h1 class="text-3xl font-bold mb-8">Dropdown Component</h1>

    <!-- Section 1: Basic Dropdown -->
    <section class="mb-12">
        <h2 class="text-2xl font-semibold mb-4">Basic Dropdown</h2>
        {{ basic_dropdown }}
    </section>

    <!-- More sections... -->

    <script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"></script>
</body>
</html>
```

### Step 6.3: Test showcase

```bash
python examples/dropdowns.py
# Visit http://localhost:8000
```

---

## Phase 7: Integration and Polish

### Step 7.1: Update consolidated showcase

**File**: `examples/showcase.py`

```python
# Add dropdown import
from flowbite_htmy.components import Dropdown, DropdownItem

# Add dropdown route
@app.get("/dropdowns")
@jinja.page("dropdowns.html.jinja")
def dropdowns():
    # ... dropdown showcase sections
    return {...}
```

### Step 7.2: Run full test suite

```bash
pytest
```

Expected: All tests pass, >90% coverage ✅

### Step 7.3: Type check

```bash
mypy src/flowbite_htmy
```

Expected: No errors ✅

### Step 7.4: Lint and format

```bash
ruff check src/flowbite_htmy
ruff format src/flowbite_htmy
```

Expected: No issues ✅

---

## Testing Checklist

- [ ] Enum tests pass
- [ ] DropdownDivider tests pass
- [ ] DropdownHeader tests pass
- [ ] DropdownItem simple tests pass
- [ ] DropdownItem with icon tests pass
- [ ] DropdownItem with HTMX tests pass
- [ ] DropdownItem disabled tests pass
- [ ] Dropdown basic rendering tests pass
- [ ] Dropdown color/size tests pass
- [ ] Dropdown placement tests pass
- [ ] Dropdown avatar trigger tests pass
- [ ] Dropdown ARIA attributes tests pass
- [ ] Dropdown dark mode tests pass
- [ ] Nested dropdown tests pass
- [ ] Custom class tests pass
- [ ] Edge case tests pass (empty lists, None values, etc.)
- [ ] Test coverage >90%

---

## Deployment Checklist

- [ ] All tests passing
- [ ] Type checking clean (mypy strict)
- [ ] Linting clean (ruff)
- [ ] Formatting applied (ruff format)
- [ ] Showcase application works
- [ ] Consolidated showcase updated
- [ ] CLAUDE.md updated (if needed)
- [ ] README updated (if needed)

---

## Next Steps

After completing this quickstart:

1. Proceed to `/speckit.tasks` to generate task breakdown
2. Use `/speckit.implement` to execute task-by-task implementation
3. Create session note documenting completion

---

## Common Pitfalls

1. **Forgetting dark mode classes**: Always include `dark:` classes, never conditionally
2. **Skipping test failure verification**: Always confirm RED before writing code
3. **Over-implementing**: Write ONLY enough code to pass the current test
4. **Missing ARIA attributes**: Dropdowns require extensive ARIA for accessibility
5. **ID collisions**: Use `id(self)` for unique IDs, not random/sequential numbers

---

## Resources

- [Flowbite Dropdown Docs](https://flowbite.com/docs/components/dropdowns/)
- [WAI-ARIA Menu Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)
- Project CLAUDE.md for development commands
- Constitution for quality standards
