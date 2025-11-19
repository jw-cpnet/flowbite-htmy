# Installation & Setup

This guide shows you how to install and configure flowbite-htmy in your FastAPI application.

## Installation

```bash
pip install flowbite-htmy
```

Or with FastAPI extras:

```bash
pip install flowbite-htmy[fastapi]
```

## Quick Start (5 Minutes)

### 1. Include the Router

Add the flowbite-htmy router to serve initialization JavaScript:

```python
from fastapi import FastAPI
from flowbite_htmy.router import router as flowbite_router

app = FastAPI()
app.include_router(flowbite_router, prefix="/_flowbite_htmy")
```

### 2. Add Scripts to Your Template

Use the helper functions to include required assets in your HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Your styles -->
    {{ flowbite_css() | safe }}
    {{ htmx_script() | safe }}
</head>
<body>
    <!-- Your content -->

    <!-- At the end of body -->
    {{ flowbite_js() | safe }}
    {{ flowbite_init_js() | safe }}
</body>
</html>
```

### 3. Register Helpers (Optional but Recommended)

Make helpers available globally in Jinja2:

```python
from fastapi.templating import Jinja2Templates
from flowbite_htmy.helpers import (
    flowbite_css,
    flowbite_js,
    htmx_script,
    flowbite_init_js,
)

templates = Jinja2Templates(directory="templates")

# Register as globals
templates.env.globals["flowbite_css"] = flowbite_css
templates.env.globals["flowbite_js"] = flowbite_js
templates.env.globals["htmx_script"] = htmx_script
templates.env.globals["flowbite_init_js"] = flowbite_init_js
```

### 4. Use Components

```python
from flowbite_htmy.components import Button
from flowbite_htmy.types import Color, Size, ButtonVariant

button = Button(
    label="Click Me!",
    color=Color.PRIMARY,
    size=Size.LG,
    variant=ButtonVariant.DEFAULT,
)
```

## Production Setup

For production, you should build your own Tailwind CSS bundle instead of using the CDN.

### Setup Tailwind Build Process

1. **Install Tailwind and Flowbite**:

```bash
npm install -D tailwindcss flowbite
```

2. **Get flowbite-htmy package path**:

```bash
python -m flowbite_htmy path
# Output: /path/to/venv/lib/python3.X/site-packages/flowbite_htmy
```

3. **Configure Tailwind** (`tailwind.config.js`):

```javascript
module.exports = {
  content: [
    "./templates/**/*.{html,jinja,jinja2}",
    "/path/to/venv/lib/python3.X/site-packages/flowbite_htmy/**/*.py",  // flowbite-htmy components
    "./node_modules/flowbite/**/*.js",  // Flowbite JS components
  ],
  darkMode: 'class',  // Enable class-based dark mode
  plugins: [
    require('flowbite/plugin'),
  ],
}
```

Or use the CLI helper:

```bash
python -m flowbite_htmy tailwind-config
```

4. **Create CSS input file** (`src/input.css`):

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

5. **Build Tailwind**:

```bash
# Development (watch mode)
npx tailwindcss -i ./src/input.css -o ./static/css/main.css --watch

# Production (minified)
npx tailwindcss -i ./src/input.css -o ./static/css/main.css --minify
```

6. **Use your built CSS**:

```html
<head>
    <!-- Use your built CSS instead of CDN -->
    <link href="/static/css/main.css" rel="stylesheet" />

    <!-- Still use Flowbite CSS/JS from CDN or self-host -->
    {{ flowbite_css() | safe }}
    {{ htmx_script() | safe }}
</head>
```

## Self-Hosting Assets (Advanced)

If you want to self-host Flowbite CSS/JS instead of using CDN:

1. Download Flowbite assets to your `static/` directory
2. Skip the helper functions and add your own tags:

```html
<head>
    <link href="/static/css/tailwind.css" rel="stylesheet" />
    <link href="/static/css/flowbite.min.css" rel="stylesheet" />
    <script src="/static/js/htmx.min.js"></script>
</head>
<body>
    <!-- Your content -->

    <script src="/static/js/flowbite.min.js" defer></script>
    {{ flowbite_init_js() | safe }}  <!-- Still use this! -->
</body>
```

**Important**: Always include `{{ flowbite_init_js() | safe }}` - this is the library's initialization code that's required for components to work properly.

## Helper Functions Reference

### `flowbite_css(version: str = FLOWBITE_VERSION) -> str`

Returns `<link>` tag for Flowbite CSS from CDN.

```python
flowbite_css()           # Uses library default (3.1.2)
flowbite_css("3.1.0")    # Specific version
```

### `flowbite_js(version: str = FLOWBITE_VERSION) -> str`

Returns `<script>` tag for Flowbite JS from CDN.

```python
flowbite_js()            # Uses library default
flowbite_js("3.1.0")     # Specific version
```

### `htmx_script(version: str = HTMX_VERSION) -> str`

Returns `<script>` tag for HTMX from CDN.

```python
htmx_script()            # Uses library default (2.0.2)
htmx_script("1.9.0")     # Specific version
```

### `flowbite_init_js(prefix: str = "/_flowbite_htmy") -> str`

Returns `<script>` tag for flowbite-htmy initialization code.

**Required**: This must be included and must come after `flowbite_js()`.

```python
flowbite_init_js()                        # Default prefix
flowbite_init_js(prefix="/assets/fb")    # Custom prefix
```

### `all_scripts(...) -> str`

Convenience function that returns all scripts in correct order.

```python
from flowbite_htmy.helpers import all_scripts

# In template:
{{ all_scripts() | safe }}
```

## CLI Reference

### Get Installation Path

```bash
python -m flowbite_htmy path
# Output: /path/to/venv/.../flowbite_htmy
```

### Show Version Info

```bash
python -m flowbite_htmy version
```

### Generate Tailwind Config

```bash
python -m flowbite_htmy tailwind-config
```

## Troubleshooting

### Components Not Rendering Correctly

Make sure you have all required dependencies:

```bash
pip install flowbite-htmy[fastapi]
```

### Modals/Toasts Not Working

Ensure you've included the initialization script **after** Flowbite JS:

```html
{{ flowbite_js() | safe }}
{{ flowbite_init_js() | safe }}  <!-- Must come after flowbite_js -->
```

### Tailwind Classes Not Applied

1. Check that your Tailwind config includes the flowbite-htmy package path
2. Verify the path is correct: `python -m flowbite_htmy path`
3. Rebuild Tailwind CSS: `npx tailwindcss -i input.css -o output.css`

### Router Not Found

Make sure you've included the router in your FastAPI app:

```python
from flowbite_htmy.router import router as flowbite_router
app.include_router(flowbite_router, prefix="/_flowbite_htmy")
```

## Next Steps

- Check out the [Component Gallery](components.md) for available components
- See [Examples](../examples/) for complete working applications
- Read the [Component API Reference](api.md) for detailed documentation
