# Data Model: Accordion Component

**Date**: 2025-11-16
**Feature**: 005-accordion
**Purpose**: Define entities, their attributes, relationships, and validation rules for the Accordion component.

## Entity Diagram

```
Accordion (Component)
  │
  ├─── panels: list[Panel]        (1 to many)
  ├─── mode: AccordionMode         (enum)
  ├─── variant: AccordionVariant   (enum)
  ├─── color: Color                (enum, existing)
  ├─── class_: str                 (custom classes)
  └─── accordion_id: str | None    (optional custom ID)

Panel (Data Class)
  ├─── title: str                  (header text)
  ├─── content: str | Component    (body content)
  ├─── is_open: bool               (default expanded state)
  ├─── icon: Component | None      (optional custom icon)
  ├─── hx_get: str | None          (HTMX GET endpoint)
  ├─── hx_trigger: str             (HTMX trigger event)
  └─── class_: str                 (custom panel classes)

AccordionMode (Enum)
  ├─── COLLAPSE = "collapse"       (single panel open)
  └─── ALWAYS_OPEN = "open"        (multiple panels open)

AccordionVariant (Enum)
  ├─── DEFAULT = "default"         (bordered accordion)
  └─── FLUSH = "flush"             (flush accordion, no borders)
```

## Entities

### 1. Accordion (Component)

**Description**: Main container component that manages a collection of collapsible panels with Flowbite styling and JavaScript integration.

**Attributes**:

| Field | Type | Default | Required | Description |
|-------|------|---------|----------|-------------|
| `panels` | `list[Panel]` | - | Yes | Collection of accordion panels (minimum 1) |
| `mode` | `AccordionMode` | `COLLAPSE` | No | Collapse behavior mode |
| `variant` | `AccordionVariant` | `DEFAULT` | No | Visual style variant |
| `color` | `Color` | `Color.PRIMARY` | No | Header background color (from existing Color enum) |
| `class_` | `str` | `""` | No | Custom CSS classes for container |
| `accordion_id` | `str \| None` | `None` | No | Custom ID (auto-generated if None) |

**Validation Rules**:

1. `panels` must contain at least 1 Panel (FR-001: "generate accordion HTML structure")
2. `accordion_id` if provided must be valid HTML ID (alphanumeric, hyphens, underscores only)
3. `class_` can be empty string (no validation needed)

**Behavior**:

- `htmy(context: Context) -> Component`: Renders complete accordion HTML structure
- Auto-generates unique IDs if `accordion_id` is None: `accordion-{id(self)}`
- Applies dark mode classes unconditionally (Constitution: always include dark classes)
- Integrates with ThemeContext for nested component rendering

**Example**:

```python
accordion = Accordion(
    panels=[
        Panel(title="Question 1", content="Answer 1"),
        Panel(title="Question 2", content="Answer 2", is_open=True),
    ],
    mode=AccordionMode.COLLAPSE,
    variant=AccordionVariant.DEFAULT,
    color=Color.PRIMARY,
)
```

### 2. Panel (Data Class)

**Description**: Individual collapsible section within an accordion, containing header and body content.

**Attributes**:

| Field | Type | Default | Required | Description |
|-------|------|---------|----------|-------------|
| `title` | `str` | - | Yes | Panel header text |
| `content` | `str \| Component` | - | Yes | Panel body content (plain text or htmy component) |
| `is_open` | `bool` | `False` | No | Whether panel is expanded by default |
| `icon` | `Component \| None` | `None` | No | Custom expand/collapse icon (uses default chevron if None) |
| `hx_get` | `str \| None` | `None` | No | HTMX GET endpoint for lazy content loading |
| `hx_trigger` | `str` | `"revealed"` | No | HTMX trigger event (default: revealed when panel expands) |
| `class_` | `str` | `""` | No | Custom CSS classes for panel wrapper |

**Validation Rules**:

1. `title` must not be empty string (header must have text for accessibility)
2. `content` can be empty string (panel can have no body content - edge case)
3. `hx_get` if provided must be valid URL path (basic string validation)
4. `hx_trigger` must be valid HTMX trigger syntax (e.g., "revealed", "click", "click from:selector")

**Behavior**:

- Generates unique `heading-{index}` and `body-{index}` IDs during render
- `is_open=True` sets `aria-expanded="true"` and removes `hidden` class
- `icon=None` uses default `Icon.CHEVRON_DOWN` with rotation animation
- HTMX attributes (`hx_get`, `hx_trigger`) passed through to panel body `<div>`

**Example**:

```python
panel = Panel(
    title="What is Flowbite?",
    content="Flowbite is an open-source library...",
    is_open=True,
    hx_get="/api/faq/1",
    hx_trigger="revealed once",
)
```

### 3. AccordionMode (Enum)

**Description**: Defines accordion collapse behavior mode.

**Values**:

| Value | String Literal | Description |
|-------|----------------|-------------|
| `COLLAPSE` | `"collapse"` | Only one panel can be open at a time (default) |
| `ALWAYS_OPEN` | `"open"` | Multiple panels can be open simultaneously |

**Usage**:

- Maps directly to Flowbite's `data-accordion="{value}"` attribute
- `COLLAPSE` - clicking a panel closes all others (single-panel mode)
- `ALWAYS_OPEN` - clicking a panel doesn't affect others (multi-panel mode)

**Example**:

```python
# Single panel open at a time
accordion = Accordion(panels=[...], mode=AccordionMode.COLLAPSE)
# Renders: <div data-accordion="collapse">

# Multiple panels can be open
accordion = Accordion(panels=[...], mode=AccordionMode.ALWAYS_OPEN)
# Renders: <div data-accordion="open">
```

### 4. AccordionVariant (Enum)

**Description**: Defines accordion visual style variant.

**Values**:

| Value | String Literal | Description |
|-------|----------------|-------------|
| `DEFAULT` | `"default"` | Standard bordered accordion with rounded corners and padding (default) |
| `FLUSH` | `"flush"` | Flush accordion with no side borders, no rounded corners, minimal padding |

**CSS Impact**:

**DEFAULT Variant**:
- Button: `border border-b-0 border-gray-200`, `rounded-t-xl` (first), `p-5`
- Body: `border border-b-0 border-gray-200`, `p-5`

**FLUSH Variant**:
- Button: `border-b border-gray-200` (bottom border only), no rounding, `py-5` (no px)
- Body: `border-b border-gray-200` (bottom border only), `py-5` (no px)

**Example**:

```python
# Default bordered accordion
accordion = Accordion(panels=[...], variant=AccordionVariant.DEFAULT)

# Flush accordion (FAQ style)
accordion = Accordion(panels=[...], variant=AccordionVariant.FLUSH)
```

## Relationships

1. **Accordion → Panel** (1 to many):
   - Accordion contains `list[Panel]`
   - Minimum 1 panel, no maximum (practical limit ~20 for UX)
   - Panels rendered in list order (index-based IDs)

2. **Panel → Component** (0 to 1):
   - Panel's `content` can be `str` or `Component`
   - If `Component`, rendered via htmy's async rendering
   - Enables nested components (e.g., Button, Alert inside panel)

3. **Panel → Icon Component** (0 to 1):
   - Panel's `icon` can be `None` or `Component`
   - If `None`, uses default `Icon.CHEVRON_DOWN`
   - If `Component`, renders custom SVG icon

4. **Accordion → AccordionMode** (1 to 1):
   - Every Accordion has exactly one mode
   - Enum ensures type safety (can't pass invalid mode string)

5. **Accordion → AccordionVariant** (1 to 1):
   - Every Accordion has exactly one variant
   - Enum ensures type safety (can't pass invalid variant string)

6. **Accordion → Color** (1 to 1):
   - Uses existing `Color` enum from `flowbite_htmy.types`
   - Determines header background color and hover state

## State Transitions

**Panel Expand/Collapse State**:

```
[Collapsed]
   ├─ User clicks button
   │  └─> Flowbite JS updates:
   │       - aria-expanded: false → true
   │       - class: adds "hidden" removal
   │       - icon: adds rotate-180
   │
   ├─ HTMX trigger fires (if hx_get set)
   │  └─> Content loads asynchronously
   │       - hx-trigger="revealed" fires on expand
   │       - hx-swap="innerHTML" updates body
   │
   └─> [Expanded]

[Expanded]
   └─ User clicks button
      └─> Flowbite JS updates:
          - aria-expanded: true → false
          - class: adds "hidden"
          - icon: removes rotate-180
      └─> [Collapsed]
```

**Mode-Specific Behavior**:

**COLLAPSE Mode**:
```
[Panel 1: Open, Panel 2: Closed, Panel 3: Closed]
   └─ User clicks Panel 2 button
      └─> Flowbite JS:
          - Panel 1: Open → Closed
          - Panel 2: Closed → Open
          - Panel 3: Unchanged (Closed)
      └─> [Panel 1: Closed, Panel 2: Open, Panel 3: Closed]
```

**ALWAYS_OPEN Mode**:
```
[Panel 1: Open, Panel 2: Closed, Panel 3: Open]
   └─ User clicks Panel 2 button
      └─> Flowbite JS:
          - Panel 1: Unchanged (Open)
          - Panel 2: Closed → Open
          - Panel 3: Unchanged (Open)
      └─> [Panel 1: Open, Panel 2: Open, Panel 3: Open]
```

## Validation Summary

| Entity | Field | Validation Rule |
|--------|-------|----------------|
| Accordion | `panels` | Minimum 1 panel required |
| Accordion | `accordion_id` | Valid HTML ID format (if provided) |
| Panel | `title` | Non-empty string |
| Panel | `hx_get` | Valid URL path (if provided) |
| Panel | `hx_trigger` | Valid HTMX trigger syntax (if provided) |

**Note**: Most validation is enforced by Python type system (dataclass frozen=True, type hints). Runtime validation only needed for empty strings and HTML ID format.

## Type Safety

All entities use full type annotations compatible with mypy strict mode:

```python
from dataclasses import dataclass
from enum import Enum
from htmy import Component, Context

@dataclass(frozen=True, kw_only=True)
class Panel:
    title: str
    content: str | Component
    is_open: bool = False
    icon: Component | None = None
    hx_get: str | None = None
    hx_trigger: str = "revealed"
    class_: str = ""

class AccordionMode(str, Enum):
    COLLAPSE = "collapse"
    ALWAYS_OPEN = "open"

class AccordionVariant(str, Enum):
    DEFAULT = "default"
    FLUSH = "flush"

@dataclass(frozen=True, kw_only=True)
class Accordion:
    panels: list[Panel]
    mode: AccordionMode = AccordionMode.COLLAPSE
    variant: AccordionVariant = AccordionVariant.DEFAULT
    color: Color = Color.PRIMARY
    class_: str = ""
    accordion_id: str | None = None

    def htmy(self, context: Context) -> Component:
        ...
```

**Type Coverage**: 100% (all fields, methods, parameters have explicit types)

## Next Phase

Phase 1 (continued): Generate component API contract in `/contracts/accordion-api.md` and TDD quickstart guide in `quickstart.md`.
