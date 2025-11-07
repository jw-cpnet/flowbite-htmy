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

```python
from fastapi import FastAPI
from fasthx.htmy import HTMY
from flowbite_htmy.components import Button
from flowbite_htmy.types import Color, Size

app = FastAPI()
htmy = HTMY()

@app.get("/")
@htmy.page(lambda _: Button(
    label="Click Me",
    color=Color.PRIMARY,
    size=Size.LG,
    hx_get="/clicked",
))
def index() -> None:
    ...
```

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

### Phase 1 - Core Components (In Progress)

- [ ] Button
- [ ] Badge
- [ ] Alert
- [ ] Card
- [ ] Avatar

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
