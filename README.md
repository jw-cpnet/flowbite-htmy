# flowbite-htmy

> Flowbite UI components for htmy - type-safe, composable, HTMX-ready

A Python library that recreates [Flowbite](https://flowbite.com/) UI components using [htmy](https://github.com/volfpeter/htmy) for type-safe, maintainable server-side rendering with FastAPI and HTMX.

## Features

- 🐍 **Python-First**: Pure Python components, no template language needed
- 🔒 **Type-Safe**: Full type hints with IDE autocomplete support
- 🧩 **Composable**: Build complex UIs from simple, reusable components
- ⚡ **HTMX-Native**: First-class HTMX support built-in
- 🎨 **Flowbite Design**: Beautiful Tailwind CSS-based components
- ✅ **Test-Driven**: Comprehensive test coverage with TDD approach
- 🚀 **FastAPI Ready**: Seamless integration with FastAPI + fasthx

## Installation

```bash
pip install flowbite-htmy
```

With FastAPI support:
```bash
pip install flowbite-htmy[fastapi]
```

## Quick Start

### 1. Install the package

```bash
pip install flowbite-htmy[fastapi]
```

### 2. Set up your FastAPI app

```python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer
from flowbite_htmy.router import router as flowbite_router
from flowbite_htmy.helpers import flowbite_css, flowbite_js, flowbite_init_js, htmx_script

app = FastAPI()

# Include flowbite-htmy router (serves initialization JS)
app.include_router(flowbite_router, prefix="/_flowbite_htmy")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Register helpers as Jinja globals
templates.env.globals["flowbite_css"] = flowbite_css
templates.env.globals["flowbite_js"] = flowbite_js
templates.env.globals["htmx_script"] = htmx_script
templates.env.globals["flowbite_init_js"] = flowbite_init_js

jinja = Jinja(templates)
renderer = Renderer()
```

### 3. Create a base template (`templates/base.html.jinja`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    {{ flowbite_css() | safe }}
    {{ htmx_script() | safe }}
</head>
<body>
    {{ content | safe }}

    {{ flowbite_js() | safe }}
    {{ flowbite_init_js() | safe }}
</body>
</html>
```

### 4. Use components in your routes

```python
from flowbite_htmy.components import Button, Alert
from flowbite_htmy.types import Color

@app.get("/")
@jinja.page("base.html.jinja")
async def index():
    content = html.div(
        Alert(
            message="Welcome to flowbite-htmy!",
            color=Color.INFO,
        ),
        Button(label="Click Me", color=Color.PRIMARY),
    )

    return {
        "title": "My App",
        "content": await renderer.render(content)
    }
```

### 5. For production: Set up Tailwind build

```bash
# Get the package path
python -m flowbite_htmy tailwind-config

# Add the output to your tailwind.config.js content array
# Then build: npx tailwindcss -i input.css -o output.css --minify
```

See [Installation Guide](docs/installation.md) for complete setup instructions and [examples/](examples/) for working applications.

## Requirements

- Python 3.11+
- htmy >= 0.1.0
- FastAPI >= 0.104.0 (optional)
- fasthx >= 0.1.0 (optional)

### Peer Dependencies (CDN or npm)

- Tailwind CSS 3.4+
- Flowbite CSS 2.5.1
- HTMX 2.0.2

## Components

### Phase 1 - Core Components ✅ COMPLETE

- ✅ **Button** - Interactive buttons with colors, sizes, HTMX support
- ✅ **Badge** - Labels and indicators with color variants
- ✅ **Alert** - Notification messages with bordered option
- ✅ **Card** - Content containers with images and titles
- ✅ **Avatar** - User profile pictures with placeholders

**Stats**: 36 tests passing, 91% coverage, all type-checked and linted

### Phase 2A - Core Interactive ✅ COMPLETE

- ✅ **Modal** - Dialog boxes with ARIA and Flowbite JS (100% coverage)
- ✅ **Input** - Text input fields with validation states
- ✅ **Select** - Dropdown selection fields (98% coverage)
- ✅ **Pagination** - Page navigation (99% coverage)

### Phase 2B - Form Controls ✅ COMPLETE

- ✅ **Checkbox** - Checkboxes with labels and validation
- ✅ **Radio** - Radio buttons with validation states (99% coverage)
- ✅ **Textarea** - Multi-line text inputs

### Phase 2C - Advanced Interactive (IN PROGRESS)

- ✅ **Toast** - Temporary notifications with actions (92% coverage)
- ✅ **Accordion** - Collapsible panels with ARIA and Flowbite JS (100% coverage, 18 tests)
- ✅ **Dropdown** - Toggleable menus with multi-level nesting
- ✅ **Tabs** - Tabbed navigation with variants and HTMX
- ✅ **Drawer** - Off-canvas panels from any edge with forms and navigation (93% coverage, 23 tests)

**Stats**: 279 tests passing, all type-checked and linted

### Planned Components

See [SPECS.md](SPECS.md) for the complete roadmap.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/flowbite-htmy.git
cd flowbite-htmy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=flowbite_htmy --cov-report=html

# Run specific test file
pytest tests/test_components/test_button.py
```

### Type Checking

```bash
mypy src/flowbite_htmy
```

### Linting

```bash
ruff check src/flowbite_htmy
```

### Running the Example App

```bash
python examples/basic_app.py
# Visit http://localhost:8000
```

## Project Structure

```
flowbite-htmy/
├── src/flowbite_htmy/
│   ├── base/              # Base utilities (ClassBuilder, ThemeContext)
│   ├── components/        # UI components
│   ├── layouts/           # Page layouts
│   ├── utils/             # Helper utilities
│   └── types/             # Type definitions
├── tests/                 # Test suite
├── examples/              # Example applications
└── docs/                  # Documentation
```

## Design Philosophy

1. **Python-Idiomatic**: Components feel natural to Python developers
2. **Composability First**: Build from small, reusable primitives
3. **HTMX-Native**: Replace JavaScript with HTMX patterns where possible
4. **Test-Driven**: Write tests before implementation
5. **Zero JS**: Minimize runtime JavaScript dependencies

## Documentation

- [Specifications](SPECS.md) - Complete project specifications
- [Contributing](CONTRIBUTING.md) - Contributing guidelines (coming soon)
- [API Reference](docs/api-reference.md) - API documentation (coming soon)

## Why flowbite-htmy?

Pure HTMX + Jinja template components are difficult to maintain, reuse, and test. They lack:

- ❌ Type safety
- ❌ IDE support
- ❌ Easy composition
- ❌ Testability

flowbite-htmy solves these problems by bringing Flowbite components to Python with htmy's component-based approach:

- ✅ Full type hints and IDE autocomplete
- ✅ Python-based composition
- ✅ Easy unit testing
- ✅ Seamless FastAPI integration

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Related Projects

- [htmy](https://github.com/volfpeter/htmy) - Python HTML generation
- [fasthx](https://github.com/volfpeter/fasthx) - FastAPI + HTMX integration
- [Flowbite](https://flowbite.com/) - Tailwind CSS component library

## Status

⚠️ **Alpha** - This project is in early development. APIs may change.

Current version: 0.1.0
