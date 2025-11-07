# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

flowbite-htmy is a Python library that recreates Flowbite UI components using htmy for type-safe, maintainable server-side rendering with FastAPI and HTMX. The project follows a strict Test-Driven Development (TDD) approach.

**Status**: Alpha (v0.1.0) - Initial scaffolding complete, Phase 1 components in progress

## Core Architecture

### Component Philosophy

This library implements Flowbite components in two styles:

1. **Class-Based Components** (for complex/stateful components):
   - Use `@dataclass(frozen=True, kw_only=True)`
   - Implement `htmy(self, context: Context) -> Component` method
   - Store props as dataclass fields
   - Used for components with complex state or multiple variants (e.g., Button, Card)

2. **Function-Based Components** (for simple/stateless components):
   - Use `@component` decorator from htmy
   - Take props as function parameters with `context: Context` as last param
   - Return Component directly
   - Used for simple display components (e.g., Badge, Icon)

### Key Utilities

**ClassBuilder** (`base/classes.py`):
- Fluent API for building Tailwind CSS class strings
- Methods: `.add()`, `.add_if()`, `.add_from_dict()`, `.merge()`, `.build()`
- Used extensively in component class building logic

**ThemeContext** (`base/context.py`):
- Context provider for theme settings (dark mode, color overrides)
- Components retrieve via `ThemeContext.from_context(context)`
- Wraps child components to provide theme to entire subtree

**Type Definitions** (`types/`):
- `Color` enum: Flowbite color variants (primary, secondary, success, etc.)
- `Size` enum: Size variants (xs, sm, md, lg, xl, 2xl)
- Use these for component props instead of strings

## Development Commands

### Environment Setup
```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# With all optional dependencies
pip install -e ".[all]"
```

### Testing
```bash
# Run all tests with coverage (default pytest config includes coverage)
pytest

# Run specific test file
pytest tests/test_components/test_button.py

# Run specific test function
pytest tests/test_components/test_button.py::test_button_renders_default

# Run tests without coverage for faster execution
pytest --no-cov

# Generate HTML coverage report
pytest --cov-report=html
# View at htmlcov/index.html
```

### Type Checking
```bash
# Type check entire package (strict mode enabled)
mypy src/flowbite_htmy

# Type check specific module
mypy src/flowbite_htmy/components/button.py
```

### Linting & Formatting
```bash
# Check with ruff
ruff check src/flowbite_htmy

# Auto-fix issues
ruff check --fix src/flowbite_htmy

# Format code
ruff format src/flowbite_htmy
```

### Running Examples
```bash
# Run basic FastAPI example
python examples/basic_app.py
# Server runs on http://localhost:8000
```

## TDD Workflow

**This project strictly follows TDD**. When implementing a new component:

1. **Write failing test first** in `tests/test_components/test_{component}.py`
2. **Run test** to confirm it fails: `pytest tests/test_components/test_{component}.py`
3. **Implement minimal code** to pass the test
4. **Run test** to confirm it passes
5. **Refactor** if needed
6. **Repeat** for next feature

### Test Structure
- `tests/conftest.py` provides fixtures: `renderer`, `context`, `dark_context`
- Use `@pytest.mark.asyncio` for async tests (htmy rendering is async)
- Test HTML output using string assertions and `snapshot` fixture (syrupy)

Example test pattern:
```python
@pytest.mark.asyncio
async def test_button_default(renderer):
    button = Button(label="Click")
    html = await renderer.render(button)

    assert "Click" in html
    assert "btn" in html  # Base class
```

## Component Implementation Pattern

When creating a new component in `src/flowbite_htmy/components/{name}.py`:

1. **Import required modules**:
   ```python
   from dataclasses import dataclass
   from typing import Any
   from htmy import Component, Context, html
   from flowbite_htmy.base import ClassBuilder, ThemeContext
   from flowbite_htmy.types import Color, Size
   ```

2. **Define component class**:
   ```python
   @dataclass(frozen=True, kw_only=True)
   class ComponentName:
       """Component docstring."""

       # Required props
       label: str

       # Optional props with defaults
       color: Color = Color.PRIMARY
       size: Size = Size.MD

       # HTMX attributes
       hx_get: str | None = None
       hx_post: str | None = None
       hx_target: str | None = None

       # Custom classes and kwargs
       class_: str = ""

       def htmy(self, context: Context) -> Component:
           theme = ThemeContext.from_context(context)
           classes = self._build_classes(theme)

           return html.tag(
               self.label,
               class_=classes,
               hx_get=self.hx_get,
               # ... other attributes
           )

       def _build_classes(self, theme: ThemeContext) -> str:
           builder = ClassBuilder("base-class")
           builder.add_if(theme.dark_mode, "dark:...")
           # ... conditional classes
           return builder.merge(self.class_)
   ```

3. **Export from** `src/flowbite_htmy/components/__init__.py`:
   ```python
   from flowbite_htmy.components.component_name import ComponentName
   __all__ = [..., "ComponentName"]
   ```

## HTMX Integration

Components support HTMX attributes directly as props:
- `hx_get`, `hx_post`, `hx_put`, `hx_delete`, `hx_patch`
- `hx_target`, `hx_swap`, `hx_trigger`
- `hx_push_url`, `hx_select`, etc.

Underscores in prop names convert to hyphens in HTML (handled by htmy).

## JavaScript Strategy

Three-tier approach:
1. **HTMX-first** (preferred): Use HTMX for interactivity
2. **CSS-only**: Use Tailwind + CSS for simple interactions
3. **Flowbite JS** (opt-in): For complex components requiring JavaScript

Most Phase 1 components are CSS-only (no JS required).

## Flowbite Reference

The file `flowbite-llms-full.txt` (2.7MB) contains complete Flowbite documentation. Use it as reference for:
- Tailwind classes used by Flowbite components
- Component structure and variants
- Accessibility attributes
- JavaScript initialization (if needed)

Access sections with: `grep -A 20 "component-name" flowbite-llms-full.txt`

## Version Locking

Library tracks specific versions:
- Flowbite CSS: 2.5.1 (`FLOWBITE_VERSION` in `__init__.py`)
- HTMX: 2.0.2 (`HTMX_VERSION`)
- Tailwind CSS: 3.4.0 (`TAILWIND_VERSION`)

When updating, check for breaking changes and update all components.

## Phase 1 Components (Current Focus)

Implement in this order:
1. **Button** - Primary interactive element
2. **Badge** - Simple indicator
3. **Alert** - Notification/message
4. **Card** - Content container
5. **Avatar** - User image/placeholder

These are CSS-only components demonstrating core patterns.

## Common Patterns

### Conditional Dark Mode Classes
```python
builder = ClassBuilder("base")
builder.add_if(theme.dark_mode, "dark:bg-gray-800", "dark:text-white")
```

### Color Variants
```python
COLOR_CLASSES = {
    Color.PRIMARY: "bg-blue-600 text-white",
    Color.SECONDARY: "bg-gray-600 text-white",
    # ...
}
classes = COLOR_CLASSES[self.color]
```

### Size Variants
```python
SIZE_CLASSES = {
    Size.SM: "text-sm px-3 py-1.5",
    Size.MD: "text-base px-4 py-2",
    # ...
}
```

## Quality Requirements

- **Test Coverage**: >90% (enforced by pytest config)
- **Type Coverage**: 100% (mypy strict mode)
- **Line Length**: 100 chars (ruff config)
- **Python Version**: 3.11+ (uses modern type hints)

## Project Memory

Development progress is tracked in Basic Memory at:
`/home/jian/Documents/basic-memory/projects/flowbite-htmy`

Use Basic Memory MCP tools to:
- Record completed components
- Track design decisions
- Document breaking changes
- Note implementation patterns

## Workflow for AI Assistants

**Session Start:**
0. **First action** → Read AI Assistant Guide: `read_note(identifier="ai_assistant_guide", project="flowbite-htmy")`

**During Session:**
1. **User asks a question** → Search Basic Memory knowledge base first
2. **Need details** → Read specific note from knowledge base
3. **Need context** → Build context from related notes
4. **Execute commands** → Use information from knowledge base
5. **Update knowledge** → Before write_note/edit_note/delete_note, verify you've read the AI Assistant Guide this session

**Before Writing/Editing Notes:**
- ✅ Read AI Assistant Guide (if not done this session)
- ✅ Use proper observation categories: [spec], [command], [issue], [solution], etc.
- ✅ Include 3-5 observations per note
- ✅ Add 2-3 relations using [[WikiLinks]]
- ✅ Use meaningful tags (#hardware, #troubleshooting, etc.)

**Remember:** Basic Memory contains observations (categorized facts) and relations (connections between topics). This provides richer context than flat markdown files.

---

*This file provides quick context for AI assistants. All detailed documentation is in Basic Memory knowledge base.*
