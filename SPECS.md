# Flowbite-HTMY Project Specifications

## Project Overview

**Name**: flowbite-htmy
**Purpose**: A Python library that recreates Flowbite UI components using htmy for type-safe, maintainable server-side rendering with FastAPI + fasthx + HTMX.

**Problem Statement**: Pure HTMX + Jinja template components are difficult to maintain, reuse, and test in Python backends. They lack type safety, composability, and IDE support.

**Solution**: Leverage htmy's Python-first component approach to create reusable, testable Flowbite components that integrate seamlessly with FastAPI and HTMX patterns.

## Technology Stack

- **htmy**: Component-based HTML rendering in pure Python
- **FastAPI + fasthx**: ASGI web framework with HTMX decorator support
- **Flowbite**: Tailwind CSS-based UI component library (free/open-source components only)
- **pytest**: Testing framework with TDD approach
- **Tailwind CSS**: Utility-first CSS framework (peer dependency)

## Design Principles

### 1. Python-Idiomatic Over Exact Replicas
- Components should feel natural to Python developers
- Use dataclasses/Pydantic for component props
- Leverage type hints for IDE support and validation
- Follow PEP 8 and Python naming conventions

### 2. Composability First
- Build small, reusable primitives
- Compose complex components from simpler ones
- Support both class-based and function-based components
- Allow component customization through props and context

### 3. HTMX-Native by Default
- Replace Flowbite's JavaScript with HTMX patterns where possible
- Provide HTMX-ready attributes (hx-get, hx-post, etc.)
- Support progressive enhancement
- Maintain fallback behavior for non-HTMX requests

### 4. Test-Driven Development
- Write tests before implementation
- Test HTML output structure and attributes
- Test component composition and props
- Use snapshot testing for complex components

### 5. Zero Runtime JavaScript When Possible
- Prefer HTMX over custom JavaScript
- For unavoidable JS (dropdowns, modals), provide opt-in Flowbite JS integration
- Document JavaScript dependencies clearly

## Architecture

### Component Organization

```
flowbite_htmy/
├── __init__.py
├── base/
│   ├── __init__.py
│   ├── component.py          # Base component classes and utilities
│   ├── props.py               # Common prop types and validators
│   └── context.py             # Context providers (theme, config)
├── components/
│   ├── __init__.py
│   ├── alert.py               # Alert component
│   ├── badge.py               # Badge component
│   ├── button.py              # Button component
│   ├── card.py                # Card component
│   ├── dropdown.py            # Dropdown component
│   ├── modal.py               # Modal component
│   ├── navbar.py              # Navbar component
│   ├── table.py               # Table component
│   └── ...                    # Additional components
├── layouts/
│   ├── __init__.py
│   ├── page.py                # Page layout wrapper
│   └── grid.py                # Grid/flex layouts
├── utils/
│   ├── __init__.py
│   ├── classes.py             # Tailwind class utilities
│   ├── icons.py               # Icon integration helpers
│   └── htmx.py                # HTMX helper utilities
└── types/
    ├── __init__.py
    ├── colors.py              # Color enums (primary, secondary, etc.)
    ├── sizes.py               # Size enums (sm, md, lg, etc.)
    └── common.py              # Common type definitions
```

### Component Structure Pattern

**Class-Based Components** (for stateful/complex components):
```python
from dataclasses import dataclass
from htmy import Component, Context, html
from flowbite_htmy.types import Color, Size

@dataclass(frozen=True, kw_only=True)
class Button:
    """Flowbite button component."""

    label: str
    color: Color = Color.PRIMARY
    size: Size = Size.MD
    disabled: bool = False
    href: str | None = None
    # HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None
    hx_target: str | None = None
    # Additional props
    class_: str = ""
    **kwargs: Any

    def htmy(self, context: Context) -> Component:
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        tag = html.a if self.href else html.button

        return tag(
            self.label,
            href=self.href,
            disabled=self.disabled if not self.href else None,
            class_=classes,
            hx_get=self.hx_get,
            hx_post=self.hx_post,
            hx_target=self.hx_target,
            **self.kwargs
        )

    def _build_classes(self, theme: ThemeContext) -> str:
        # Class building logic
        pass
```

**Function-Based Components** (for simple/stateless components):
```python
from htmy import component, Component, Context, html
from flowbite_htmy.types import Color

@component
def badge(
    label: str,
    color: Color = Color.INFO,
    rounded: bool = False,
    context: Context = None
) -> Component:
    """Flowbite badge component."""
    classes = f"badge badge-{color.value}"
    if rounded:
        classes += " rounded-full"

    return html.span(label, class_=classes)
```

### Styling Integration

**Tailwind CSS Classes**:
- Use string concatenation for simple cases
- Build a `ClassBuilder` utility for complex conditional classes
- Store Flowbite class mappings in constants
- Allow class override through `class_` prop
- Support dark mode through theme context

```python
# utils/classes.py
class ClassBuilder:
    """Utility for building Tailwind CSS class strings."""

    def __init__(self, base: str = ""):
        self.classes: list[str] = [base] if base else []

    def add(self, *classes: str) -> "ClassBuilder":
        """Add classes unconditionally."""
        self.classes.extend(classes)
        return self

    def add_if(self, condition: bool, *classes: str) -> "ClassBuilder":
        """Add classes conditionally."""
        if condition:
            self.classes.extend(classes)
        return self

    def merge(self, custom: str = "") -> str:
        """Merge with custom classes and return final string."""
        if custom:
            self.classes.append(custom)
        return " ".join(self.classes)
```

### JavaScript Dependency Handling

**Approach**: Three-tier strategy
1. **HTMX-first** (preferred): Use HTMX for interactivity
2. **CSS-only**: Use Tailwind + CSS for simple interactions (hover, focus)
3. **Flowbite JS** (opt-in): For complex components requiring JavaScript

**Implementation**:
```python
# layouts/page.py
@component
def page_head(
    title: str,
    include_flowbite_js: bool = False,
    context: Context = None
) -> Component:
    """Page head with CSS/JS dependencies."""
    return html.head(
        html.title(title),
        html.meta.charset(),
        html.meta.viewport(),
        # Tailwind CSS
        html.script(src="https://cdn.tailwindcss.com"),
        # Flowbite CSS (always included)
        html.link.css("https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css"),
        # HTMX
        html.script(src="https://unpkg.com/htmx.org@2.0.2"),
        # Optional Flowbite JS
        html.script(
            src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"
        ) if include_flowbite_js else None,
    )
```

### Theme and Context

**ThemeContext** for dark mode and customization:
```python
# base/context.py
from dataclasses import dataclass
from htmy import Context

@dataclass
class ThemeContext:
    """Theme configuration context provider."""

    dark_mode: bool = False
    colors: dict[str, str] | None = None

    def htmy_context(self) -> Context:
        return {ThemeContext: self}

    @classmethod
    def from_context(cls, context: Context) -> "ThemeContext":
        theme = context.get(cls)
        return theme if isinstance(theme, cls) else cls()
```

## Testing Strategy

### Test Structure
```
tests/
├── __init__.py
├── conftest.py                # Pytest fixtures
├── test_components/
│   ├── test_alert.py
│   ├── test_badge.py
│   ├── test_button.py
│   └── ...
├── test_layouts/
│   ├── test_page.py
│   └── test_grid.py
├── test_utils/
│   ├── test_classes.py
│   └── test_htmx.py
└── snapshots/                 # HTML snapshots
    ├── test_button_default.html
    └── ...
```

### Testing Approach

**1. Unit Tests** - Test individual components:
```python
# tests/test_components/test_button.py
import asyncio
import pytest
from htmy import Renderer
from flowbite_htmy.components import Button
from flowbite_htmy.types import Color, Size

@pytest.mark.asyncio
async def test_button_renders_default():
    """Test button renders with default props."""
    button = Button(label="Click Me")
    renderer = Renderer()
    html = await renderer.render(button)

    assert "Click Me" in html
    assert "btn" in html
    assert "btn-primary" in html

@pytest.mark.asyncio
async def test_button_with_htmx():
    """Test button renders with HTMX attributes."""
    button = Button(
        label="Load More",
        hx_get="/api/items",
        hx_target="#items"
    )
    renderer = Renderer()
    html = await renderer.render(button)

    assert 'hx-get="/api/items"' in html
    assert 'hx-target="#items"' in html
```

**2. Integration Tests** - Test component composition:
```python
@pytest.mark.asyncio
async def test_card_with_button():
    """Test card containing a button."""
    from flowbite_htmy.components import Card, Button

    card = Card(
        title="User Profile",
        content=(
            html.p("User details here"),
            Button(label="Edit", color=Color.PRIMARY)
        )
    )

    renderer = Renderer()
    html = await renderer.render(card)

    assert "User Profile" in html
    assert "Edit" in html
    assert "btn-primary" in html
```

**3. Snapshot Tests** - Test HTML structure:
```python
@pytest.mark.asyncio
async def test_button_snapshot(snapshot):
    """Test button HTML structure matches snapshot."""
    button = Button(label="Submit", color=Color.SUCCESS, size=Size.LG)
    renderer = Renderer()
    html = await renderer.render(button)

    snapshot.assert_match(html, "button_success_lg.html")
```

**4. Type Tests** - Test type hints (using mypy/pyright):
```python
# tests/test_types.py
from flowbite_htmy.components import Button
from flowbite_htmy.types import Color

def test_button_types():
    """Test button accepts correct types."""
    # Should pass type checking
    button = Button(label="Test", color=Color.PRIMARY)

    # Should fail type checking (caught by mypy/pyright)
    # button = Button(label=123)  # Error: Expected str
    # button = Button(label="Test", color="invalid")  # Error: Expected Color
```

### TDD Workflow

1. **Write failing test** - Define expected behavior
2. **Implement minimal code** - Make test pass
3. **Refactor** - Improve code quality
4. **Repeat** - Next feature/component

Example TDD cycle for Badge component:
```python
# Step 1: Write test (FAILS)
@pytest.mark.asyncio
async def test_badge_default():
    badge = Badge(label="New")
    html = await Renderer().render(badge)
    assert "New" in html
    assert "badge" in html

# Step 2: Implement Badge (PASSES)
@component
def Badge(label: str, context: Context) -> Component:
    return html.span(label, class_="badge")

# Step 3: Add color support - write test first (FAILS)
@pytest.mark.asyncio
async def test_badge_with_color():
    badge = Badge(label="New", color=Color.INFO)
    html = await Renderer().render(badge)
    assert "badge-info" in html

# Step 4: Implement color support (PASSES)
@component
def Badge(label: str, color: Color = Color.DEFAULT, context: Context = None) -> Component:
    return html.span(label, class_=f"badge badge-{color.value}")
```

## MVP Components

### Phase 1 - Core Components (Start Here)
Focus on the most commonly used, JavaScript-free components:

1. **Button** - Primary interactive element
2. **Badge** - Simple indicator component
3. **Alert** - Notification/message component
4. **Card** - Content container
5. **Avatar** - User image/placeholder

**Rationale**: These are purely CSS-based, don't require Flowbite JS, and demonstrate the component patterns.

### Phase 2 - Layout Components
6. **Navbar** - Navigation header
7. **Footer** - Page footer
8. **Sidebar** - Side navigation
9. **Grid** - Layout system

### Phase 3 - Form Components
10. **Input** - Text input field
11. **Textarea** - Multi-line text input
12. **Select** - Dropdown select
13. **Checkbox** - Checkbox input
14. **Radio** - Radio button input

### Phase 4 - Interactive Components (Requires HTMX/JS)
15. **Modal** - Dialog overlay
16. **Dropdown** - Dropdown menu
17. **Tabs** - Tabbed interface
18. **Accordion** - Collapsible panels
19. **Toast** - Notification popup

### Phase 5 - Data Display
20. **Table** - Data table
21. **List** - Styled lists
22. **Timeline** - Event timeline
23. **Pagination** - Page navigation

## Versioning and Dependencies

### Flowbite Version Locking
- Lock to specific Flowbite CSS/JS versions in code
- Document breaking changes between Flowbite versions
- Provide migration guides when updating Flowbite

```python
# flowbite_htmy/__init__.py
__version__ = "0.1.0"
FLOWBITE_VERSION = "2.5.1"
HTMX_VERSION = "2.0.2"
```

### Peer Dependencies
- Flowbite CSS (CDN or npm)
- Tailwind CSS (CDN or npm)
- HTMX (CDN or npm)
- htmy >= 0.1.0
- fasthx >= 0.1.0 (optional, for FastAPI integration)

## Package Structure

```
flowbite-htmy/
├── pyproject.toml
├── README.md
├── SPECS.md
├── LICENSE
├── .gitignore
├── src/
│   └── flowbite_htmy/
│       ├── __init__.py
│       ├── base/
│       ├── components/
│       ├── layouts/
│       ├── utils/
│       └── types/
├── tests/
│   ├── conftest.py
│   ├── test_components/
│   ├── test_layouts/
│   └── test_utils/
├── examples/
│   ├── basic_app.py
│   ├── htmx_integration.py
│   └── templates/
└── docs/
    ├── getting-started.md
    ├── components/
    ├── api-reference.md
    └── migration-from-jinja.md
```

## Development Workflow

### Initial Setup
1. Create project structure
2. Set up pyproject.toml with dependencies
3. Configure pytest and mypy
4. Create base component classes and utilities

### Component Development (TDD)
1. Choose component from MVP list
2. Write test for basic rendering
3. Implement minimal component
4. Write test for props/variants
5. Implement props/variants
6. Write test for HTMX integration
7. Implement HTMX support
8. Write test for composition
9. Refactor and optimize
10. Document component usage

### Quality Checks
- Run pytest with coverage (target: >90%)
- Run mypy for type checking
- Run ruff for linting
- Test in example FastAPI app
- Update documentation

## Documentation Strategy

### 1. API Reference
Auto-generated from docstrings using mkdocs-material or sphinx

### 2. Component Guides
Each component gets:
- Usage examples
- Props reference
- HTMX integration examples
- Composition examples
- Migration notes from Jinja

### 3. Tutorials
- Getting Started
- Building Your First Page
- HTMX Patterns with Flowbite Components
- Testing Your Components
- Migrating from Jinja Templates

### 4. Examples
Working FastAPI applications demonstrating:
- Basic static pages
- HTMX-enhanced interactivity
- Form handling
- Authentication UI
- Dashboard layouts

## Success Metrics

### Technical
- Test coverage > 90%
- Type coverage 100%
- Zero runtime dependencies (except htmy)
- Fast render times (< 1ms per component)

### Usability
- Clear, documented API for each component
- Working examples for common use cases
- Migration path from Jinja documented
- Active maintenance and bug fixes

### Adoption
- Usage in production applications
- Community contributions
- Positive feedback from users
- Integration with other Python frameworks

## Future Considerations

### Post-MVP Features
- Component variants (outlined, ghost, etc.)
- Animation support
- Custom theme builder
- Icon library integration
- Form validation helpers
- A11y improvements
- RTL support

### Advanced Features
- Server-side component caching
- Streaming components
- Suspense-like patterns
- Component testing utilities
- Storybook-like component viewer
- CLI for scaffolding

## Conclusion

This specification provides a comprehensive roadmap for building flowbite-htmy. The focus is on:
- **Developer Experience**: Type-safe, testable, composable components
- **Maintainability**: TDD, clear architecture, good documentation
- **Pragmatism**: Start with simple components, grow incrementally
- **Integration**: Seamless FastAPI + HTMX + htmy experience

By following these specs, we'll create a library that solves the real problem of maintaining UI components in Python backends while staying focused on the end goal.
