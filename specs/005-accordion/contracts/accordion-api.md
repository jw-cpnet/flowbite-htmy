# Component API Contract: Accordion

**Date**: 2025-11-16
**Feature**: 005-accordion
**Purpose**: Define the public API, rendering contract, and usage examples for the Accordion component.

## Component Signature

### Accordion Class

```python
from dataclasses import dataclass
from htmy import Component, Context
from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Color

@dataclass(frozen=True, kw_only=True)
class Accordion:
    """
    Flowbite accordion component with collapsible panels.

    Renders a collection of collapsible panels with proper ARIA attributes,
    Flowbite styling, and optional HTMX integration for dynamic content loading.

    Example:
        >>> accordion = Accordion(
        ...     panels=[
        ...         Panel(title="Question 1", content="Answer 1"),
        ...         Panel(title="Question 2", content="Answer 2", is_open=True),
        ...     ],
        ...     mode=AccordionMode.COLLAPSE,
        ... )
    """

    panels: list[Panel]
    """Collection of accordion panels (minimum 1 required)."""

    mode: AccordionMode = AccordionMode.COLLAPSE
    """Collapse behavior mode (COLLAPSE: single panel open, ALWAYS_OPEN: multiple panels open)."""

    variant: AccordionVariant = AccordionVariant.DEFAULT
    """Visual style variant (DEFAULT: bordered, FLUSH: borderless)."""

    color: Color = Color.PRIMARY
    """Header background color from Flowbite color palette."""

    class_: str = ""
    """Custom CSS classes to merge with component classes."""

    accordion_id: str | None = None
    """Custom ID for accordion container (auto-generated if None)."""

    def htmy(self, context: Context) -> Component:
        """
        Render accordion component as HTML.

        Args:
            context: htmy rendering context for theme and nested components.

        Returns:
            Component representing the complete accordion HTML structure.
        """
        ...
```

### Panel Data Class

```python
@dataclass(frozen=True, kw_only=True)
class Panel:
    """
    Individual collapsible panel within an accordion.

    Example:
        >>> panel = Panel(
        ...     title="What is Flowbite?",
        ...     content="Flowbite is an open-source library...",
        ...     is_open=True,
        ...     hx_get="/api/faq/1",
        ... )
    """

    title: str
    """Panel header text displayed in the button."""

    content: str | Component
    """Panel body content (plain string or htmy component)."""

    is_open: bool = False
    """Whether panel is expanded by default."""

    icon: Component | None = None
    """Custom expand/collapse icon (uses chevron if None)."""

    hx_get: str | None = None
    """HTMX GET endpoint for lazy content loading."""

    hx_trigger: str = "revealed"
    """HTMX trigger event (default: fires when panel expands)."""

    class_: str = ""
    """Custom CSS classes for panel wrapper."""
```

### AccordionMode Enum

```python
from enum import Enum

class AccordionMode(str, Enum):
    """Accordion collapse behavior modes."""

    COLLAPSE = "collapse"
    """Only one panel can be open at a time (default)."""

    ALWAYS_OPEN = "open"
    """Multiple panels can be open simultaneously."""
```

### AccordionVariant Enum

```python
class AccordionVariant(str, Enum):
    """Accordion visual style variants."""

    DEFAULT = "default"
    """Standard bordered accordion with rounded corners (default)."""

    FLUSH = "flush"
    """Flush accordion with no side borders, minimal padding."""
```

## Rendering Contract

### Input Requirements

**Valid Inputs**:
- `panels`: Non-empty list of Panel instances (minimum 1)
- `mode`: AccordionMode enum value (COLLAPSE or ALWAYS_OPEN)
- `variant`: AccordionVariant enum value (DEFAULT or FLUSH)
- `color`: Color enum value from `flowbite_htmy.types.Color`
- `class_`: Any string (empty string allowed)
- `accordion_id`: Valid HTML ID string or None

**Invalid Inputs** (raises TypeError/ValueError):
- `panels=[]` - Empty list (minimum 1 panel required)
- `mode="invalid"` - String instead of enum
- `accordion_id="invalid id"` - Spaces in ID (invalid HTML ID format)

### Output Guarantees

**HTML Structure**:

```html
<div id="{accordion_id}" data-accordion="{mode}" class="{merged_classes}">
  <!-- For each panel -->
  <h2 id="{accordion_id}-heading-{index}">
    <button
      type="button"
      class="{button_classes}"
      data-accordion-target="#{accordion_id}-body-{index}"
      aria-expanded="{is_open}"
      aria-controls="{accordion_id}-body-{index}">
      <span>{panel.title}</span>
      {icon_component}
    </button>
  </h2>
  <div
    id="{accordion_id}-body-{index}"
    class="{body_classes}"
    aria-labelledby="{accordion_id}-heading-{index}"
    hx-get="{panel.hx_get}"
    hx-trigger="{panel.hx_trigger}">
    <div class="{content_wrapper_classes}">
      {panel.content}
    </div>
  </div>
</div>
```

**Guaranteed Attributes**:

1. **Container `<div>`**:
   - `id`: Unique identifier (custom or auto-generated)
   - `data-accordion`: Mode value ("collapse" or "open")
   - `class`: Merged component + custom classes

2. **Header `<h2>`**:
   - `id`: `{accordion_id}-heading-{index}`
   - Semantic HTML heading for document outline

3. **Button `<button>`**:
   - `type="button"`: Prevents form submission
   - `aria-expanded`: `"true"` or `"false"` based on `is_open`
   - `aria-controls`: References panel body ID
   - `data-accordion-target`: CSS selector for panel body (`#id`)
   - `class`: Flowbite classes + hover + focus + dark mode

4. **Panel Body `<div>`**:
   - `id`: `{accordion_id}-body-{index}`
   - `aria-labelledby`: References header button ID
   - `class`: Includes `hidden` if `is_open=False`
   - `hx-get`, `hx-trigger`: HTMX attributes (if provided)

5. **Icon `<svg>`**:
   - `data-accordion-icon="true"`: Marks for Flowbite JS rotation
   - `aria-hidden="true"`: Decorative, hidden from screen readers
   - `class`: Includes `rotate-180` if `is_open=True`

**CSS Classes Applied**:

**DEFAULT Variant**:
- Button: `flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3`
- Body wrapper: `p-5 border border-b-0 border-gray-200 dark:border-gray-700`
- First panel body: `dark:bg-gray-900`
- Last panel: `border-t-0` instead of `border-b-0`

**FLUSH Variant**:
- Button: `flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3`
- Body wrapper: `py-5 border-b border-gray-200 dark:border-gray-700`

**Dark Mode**: All color and border classes include `dark:` equivalents (always present).

## Usage Examples

### Example 1: Basic FAQ Accordion

```python
from flowbite_htmy.components import Accordion, Panel, AccordionMode

accordion = Accordion(
    panels=[
        Panel(
            title="What is Flowbite?",
            content="Flowbite is an open-source library of components built on Tailwind CSS.",
        ),
        Panel(
            title="Is there a Figma file?",
            content="Yes, Flowbite has a complete Figma design system.",
            is_open=True,  # Expanded by default
        ),
        Panel(
            title="What are the differences?",
            content="Flowbite is open source under MIT license, while Tailwind UI is paid.",
        ),
    ],
    mode=AccordionMode.COLLAPSE,  # Only one panel open at a time
)
```

### Example 2: Always-Open Accordion with Icons

```python
from flowbite_htmy.components import Accordion, Panel, AccordionMode, AccordionVariant
from flowbite_htmy.icons import Icon, get_icon

accordion = Accordion(
    panels=[
        Panel(
            title="Getting Started",
            content="Install via pip install flowbite-htmy",
            icon=get_icon(Icon.INFORMATION_CIRCLE, class_="w-5 h-5 me-2"),
        ),
        Panel(
            title="Components",
            content="Browse 50+ UI components",
            icon=get_icon(Icon.CUBE, class_="w-5 h-5 me-2"),
        ),
    ],
    mode=AccordionMode.ALWAYS_OPEN,  # Multiple panels can be open
    variant=AccordionVariant.DEFAULT,
)
```

### Example 3: Flush Accordion with HTMX Lazy Loading

```python
accordion = Accordion(
    panels=[
        Panel(
            title="User Profile",
            content="Loading...",  # Placeholder
            hx_get="/api/user/profile",
            hx_trigger="revealed once",  # Load once when first expanded
        ),
        Panel(
            title="Account Settings",
            content="Loading...",
            hx_get="/api/user/settings",
            hx_trigger="revealed once",
        ),
    ],
    variant=AccordionVariant.FLUSH,  # No borders
    mode=AccordionMode.COLLAPSE,
)
```

### Example 4: Nested Components in Panel Content

```python
from htmy import html
from flowbite_htmy.components import Alert, AlertType

accordion = Accordion(
    panels=[
        Panel(
            title="Important Notice",
            content=Alert(
                message="This is an important notice inside an accordion panel.",
                type_=AlertType.WARNING,
            ),
        ),
        Panel(
            title="Rich Content",
            content=html.div(
                html.p("Paragraph 1", class_="mb-2"),
                html.p("Paragraph 2", class_="mb-2"),
                html.ul(
                    html.li("Item 1"),
                    html.li("Item 2"),
                    class_="list-disc pl-5",
                ),
            ),
        ),
    ],
)
```

### Example 5: Custom ID and Classes

```python
accordion = Accordion(
    panels=[
        Panel(title="Q1", content="A1"),
        Panel(title="Q2", content="A2"),
    ],
    accordion_id="faq-accordion",  # Custom ID for CSS selectors
    class_="my-8",  # Custom spacing class
)

# Renders: <div id="faq-accordion" class="my-8" data-accordion="collapse">
```

## Integration with FastAPI + fasthx

### Basic Route

```python
from fastapi import FastAPI
from fasthx import Jinja

app = FastAPI()
jinja = Jinja(template_folder="templates")

@app.get("/faq")
@jinja.page("faq.html.jinja")
async def faq_page():
    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1"),
            Panel(title="Q2", content="A2", is_open=True),
        ]
    )
    return {"accordion": accordion}
```

### Jinja Template

```jinja
<!-- templates/faq.html.jinja -->
{% extends "base.html.jinja" %}

{% block content %}
<div class="container mx-auto px-4 py-8">
  <h1 class="text-3xl font-bold mb-6">Frequently Asked Questions</h1>
  {{ accordion }}  {# htmy component renders directly #}
</div>
{% endblock %}
```

### HTMX Endpoint for Lazy Loading

```python
@app.get("/api/faq/{faq_id}")
async def get_faq_content(faq_id: int):
    # Fetch from database
    content = db.get_faq_answer(faq_id)
    return html.div(
        html.p(content, class_="text-gray-500 dark:text-gray-400"),
    )
```

## Error Handling

### Empty Panels List

```python
# ❌ INVALID - Raises ValueError
accordion = Accordion(panels=[])
# ValueError: Accordion requires at least 1 panel
```

### Invalid Mode/Variant Type

```python
# ❌ INVALID - Raises TypeError
accordion = Accordion(
    panels=[...],
    mode="collapse"  # String instead of enum
)
# TypeError: mode must be AccordionMode, not str

# ✅ VALID
accordion = Accordion(
    panels=[...],
    mode=AccordionMode.COLLAPSE  # Enum value
)
```

### Invalid HTML ID

```python
# ❌ INVALID - Raises ValueError
accordion = Accordion(
    panels=[...],
    accordion_id="invalid id"  # Spaces not allowed
)
# ValueError: accordion_id must be valid HTML ID (alphanumeric, hyphens, underscores)

# ✅ VALID
accordion = Accordion(
    panels=[...],
    accordion_id="faq-section"  # Valid ID
)
```

## Performance Characteristics

- **Rendering Time**: O(n) where n = number of panels
- **Memory Usage**: O(n) - one Panel instance per panel
- **ID Generation**: O(1) - Python `id()` function is constant time
- **Class Building**: O(1) per panel - ClassBuilder is fluent API with string concatenation

**Expected Performance**:
- 5-panel accordion: <1ms render time
- 20-panel accordion: <5ms render time
- ID collision probability: 0% (Python `id()` guarantees uniqueness per instance)

## Accessibility Compliance

**WCAG 2.1 Level AA**: ✅ Compliant

- **Keyboard Navigation**: All panels accessible via Tab, Enter, Space
- **Screen Reader Support**: ARIA attributes provide semantic relationships
- **Focus Management**: Flowbite JS manages focus on expand/collapse
- **Color Contrast**: Dark mode colors meet 4.5:1 ratio for normal text

**ARIA Attributes**:
- `aria-expanded`: Indicates panel state to screen readers
- `aria-controls`: Links button to controlled panel
- `aria-labelledby`: Links panel to describing button
- `aria-hidden="true"`: Hides decorative icons from screen readers

## Browser Compatibility

- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Tailwind CSS**: 3.4.0 (project dependency)
- **Flowbite CSS**: 2.5.1 (project dependency)
- **Flowbite JavaScript**: Auto-initializes accordions with `data-accordion` attribute
- **HTMX**: 2.0.2 (optional, for lazy loading)

## Next Steps

Create `quickstart.md` with TDD workflow guide showing test-first implementation sequence for all 17 tests across 4 phases.
