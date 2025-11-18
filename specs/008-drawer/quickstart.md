# Quickstart: Drawer Component

**Feature**: 008-drawer
**Date**: 2025-11-18
**Audience**: Developers using flowbite-htmy

## What You'll Build

A working drawer component that slides in from any edge of the screen, supporting forms, navigation menus, and dynamic content. You'll learn to use all key features including placement variants, backdrop overlay, HTMX integration, and focus management.

**Time to Complete**: 15 minutes

**Prerequisites**:
- Python 3.11+ installed
- Basic familiarity with FastAPI and htmy
- flowbite-htmy library installed

---

## Step 1: Basic Installation (2 minutes)

If you haven't already installed flowbite-htmy:

```bash
pip install flowbite-htmy
```

Or install from source for development:

```bash
git clone https://github.com/yourusername/flowbite-htmy.git
cd flowbite-htmy
pip install -e ".[dev]"
```

---

## Step 2: Include Required Dependencies (3 minutes)

Create a Jinja template for your page layout that includes Flowbite and HTMX:

**File**: `templates/base.html.jinja`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Flowbite CSS -->
    <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css" rel="stylesheet" />
</head>
<body class="bg-gray-50 dark:bg-gray-900">
    <!-- Page content -->
    {{ content|safe }}

    <!-- Flowbite JavaScript (required for drawer) -->
    <script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"></script>

    <!-- HTMX (optional, for dynamic content) -->
    <script src="https://unpkg.com/htmx.org@2.0.2"></script>
</body>
</html>
```

---

## Step 3: Create Your First Drawer (5 minutes)

Create a FastAPI app with a basic drawer:

**File**: `app.py`

```python
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html
from flowbite_htmy.components import Drawer

app = FastAPI()
templates = Jinja2Templates(directory="templates")
jinja = Jinja(templates)
renderer = Renderer()

@app.get("/")
@jinja.page("base.html.jinja")
async def index():
    # Create a simple drawer with navigation menu
    drawer = Drawer(
        trigger_label="Open Menu",
        content=html.div(
            html.h3("Navigation", class_="text-xl font-bold mb-4 text-gray-900 dark:text-white"),
            html.nav(
                html.a("Home", href="/", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                html.a("About", href="/about", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                html.a("Contact", href="/contact", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                class_="space-y-2",
            ),
        ),
    )

    # Render drawer component
    drawer_html = await renderer.render(drawer)

    return {
        "title": "Drawer Demo",
        "content": f"""
            <div class="container mx-auto p-8">
                <h1 class="text-3xl font-bold mb-8 text-gray-900 dark:text-white">Drawer Component Demo</h1>
                {drawer_html}
            </div>
        """
    }
```

**Run the app**:

```bash
uvicorn app:app --reload
```

Visit `http://localhost:8000` and click "Open Menu" to see your drawer!

---

## Step 4: Try Different Placements (3 minutes)

Add drawers from all four edges:

```python
from flowbite_htmy.types import DrawerPlacement

# Left drawer (default)
left_drawer = Drawer(
    trigger_label="Left Menu",
    content=html.div("Left side content"),
)

# Right drawer
right_drawer = Drawer(
    trigger_label="Right Panel",
    content=html.div("Right side content"),
    placement=DrawerPlacement.RIGHT,
)

# Top drawer
top_drawer = Drawer(
    trigger_label="Top Bar",
    content=html.div("Top content"),
    placement=DrawerPlacement.TOP,
    height="h-1/3",  # Custom height for top/bottom
)

# Bottom drawer
bottom_drawer = Drawer(
    trigger_label="Bottom Sheet",
    content=html.div("Bottom content"),
    placement=DrawerPlacement.BOTTOM,
)
```

---

## Step 5: Add a Form with HTMX (5 minutes)

Create a drawer with a contact form that submits via HTMX:

```python
from flowbite_htmy.components import Drawer, Input, Textarea, Button
from fastapi import Response

# Contact form drawer
contact_form = html.form(
    Input(label="Name", name="name", required=True),
    Input(label="Email", name="email", type="email", required=True),
    Textarea(label="Message", name="message", rows=4),
    Button(label="Send Message", type="submit"),
    hx_post="/api/contact",
    hx_target="#contact-result",
    class_="space-y-4",
)

contact_drawer = Drawer(
    trigger_label="Contact Us",
    content=html.div(
        html.h3("Get in Touch", class_="text-xl font-bold mb-4"),
        contact_form,
        html.div(id="contact-result", class_="mt-4"),
    ),
)

# API endpoint to handle form submission
@app.post("/api/contact")
async def contact(name: str, email: str, message: str):
    # Process form data...
    print(f"Contact from {name} ({email}): {message}")

    # Return success message and close drawer
    response = Response(
        content='<p class="text-green-600">Thank you! We\'ll be in touch soon.</p>'
    )
    # Trigger drawer closure (assuming drawer_id is "drawer-contact")
    response.headers["HX-Trigger"] = "close-drawer-contact"
    return response
```

**Add event listener in template**:

```html
<!-- In base.html.jinja, before closing </body> -->
<script>
    // Listen for HTMX close trigger
    document.body.addEventListener('close-drawer-contact', () => {
        const drawer = FlowbiteInstances.getInstance('Drawer', 'drawer-contact');
        if (drawer) drawer.hide();
    });
</script>
```

---

## Common Use Cases

### Use Case 1: Navigation Menu

```python
nav_drawer = Drawer(
    trigger_label="☰ Menu",
    content=html.nav(
        html.a("Dashboard", href="/dashboard", class_="..."),
        html.a("Analytics", href="/analytics", class_="..."),
        html.a("Settings", href="/settings", class_="..."),
    ),
    placement=DrawerPlacement.LEFT,
    width="w-64",
)
```

### Use Case 2: Filter Panel

```python
filter_drawer = Drawer(
    trigger_label="Filters",
    content=html.form(
        html.fieldset(
            html.legend("Price Range"),
            # ... filter controls ...
        ),
        hx_post="/api/filter",
        hx_target="#results",
    ),
    placement=DrawerPlacement.RIGHT,
    backdrop=False,  # Allow interaction with main content
)
```

### Use Case 3: User Profile

```python
from flowbite_htmy.components import Avatar, Badge

profile_drawer = Drawer(
    trigger_label="Profile",
    content=html.div(
        Avatar(src="/user.jpg", alt="User", size=Size.LG),
        html.h4("John Doe", class_="mt-2 font-bold"),
        Badge(label="Premium", color=Color.SUCCESS),
        # ... profile details ...
    ),
    placement=DrawerPlacement.RIGHT,
    width="w-96",
)
```

### Use Case 4: Bottom Sheet (Mobile-style)

```python
bottom_sheet = Drawer(
    trigger_label="More Options",
    content=html.div(
        html.button("Share", class_="..."),
        html.button("Download", class_="..."),
        html.button("Delete", class_="..."),
    ),
    placement=DrawerPlacement.BOTTOM,
    height="h-auto",  # Auto height based on content
    edge=True,  # Show edge tab when closed
)
```

---

## Customization Tips

### 1. Custom Trigger Styling

```python
drawer = Drawer(
    trigger_label="Custom Button",
    content=html.div("..."),
    trigger_color=Color.SUCCESS,  # Green button
    trigger_size=Size.LG,  # Large button
    trigger_class="rounded-full shadow-lg",  # Additional classes
)
```

### 2. Custom Drawer Width/Height

```python
# Wide drawer for rich content
wide_drawer = Drawer(
    trigger_label="Details",
    content=html.div("..."),
    placement=DrawerPlacement.RIGHT,
    width="w-[600px]",  # Custom Tailwind width
)

# Tall drawer for long forms
tall_drawer = Drawer(
    trigger_label="Form",
    content=html.div("..."),
    placement=DrawerPlacement.TOP,
    height="h-2/3",  # 66% viewport height
)
```

### 3. Disable Backdrop

```python
# No dimming overlay - drawer without modal behavior
no_backdrop = Drawer(
    trigger_label="Info",
    content=html.div("..."),
    backdrop=False,
)
```

### 4. Enable Body Scrolling

```python
# Allow scrolling the page behind the drawer
scrollable_bg = Drawer(
    trigger_label="Help",
    content=html.div("..."),
    body_scrolling=True,
)
```

---

## Keyboard Shortcuts

When a drawer is open:

| Key | Action |
|-----|--------|
| **Escape** | Close drawer and return focus to trigger |
| **Tab** | Move to next focusable element (within drawer only) |
| **Shift+Tab** | Move to previous focusable element (within drawer only) |

---

## Troubleshooting

### Drawer doesn't open

**Problem**: Clicking trigger button does nothing

**Solution**: Ensure Flowbite JavaScript is included after the drawer HTML:

```html
<!-- Drawer HTML rendered here -->

<!-- Flowbite JS MUST come after -->
<script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"></script>
```

### Drawer doesn't close on backdrop click

**Problem**: Clicking outside drawer doesn't close it

**Solution**: Ensure `backdrop=True` (default) and backdrop element is rendered

### Focus trap not working

**Problem**: Tab key reaches elements outside drawer

**Solution**: Flowbite JavaScript handles this automatically. Ensure drawer has correct ARIA attributes (automatic with component)

### HTMX form doesn't close drawer

**Problem**: Form submits but drawer stays open

**Solution**: Server must send `HX-Trigger` header and client must have event listener:

```python
# Server
response.headers["HX-Trigger"] = f"close-drawer-{drawer_id}"
```

```javascript
// Client
document.body.addEventListener('close-drawer-{drawer_id}', () => {
    const drawer = FlowbiteInstances.getInstance('Drawer', '{drawer_id}');
    drawer.hide();
});
```

---

## Next Steps

1. **Explore showcase app**: Run `python examples/drawers.py` to see all features
2. **Read API docs**: See `contracts/drawer-component-api.md` for complete API
3. **Check tests**: Review `tests/test_components/test_drawer.py` for usage examples
4. **Customize styles**: Modify Tailwind classes to match your design system

---

## Full Example: Complete Drawer App

```python
from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html
from flowbite_htmy.components import Drawer, Input, Textarea, Button, Badge
from flowbite_htmy.types import DrawerPlacement, Color, Size

app = FastAPI()
templates = Jinja2Templates(directory="templates")
jinja = Jinja(templates)
renderer = Renderer()

@app.get("/")
@jinja.page("base.html.jinja")
async def index():
    # Navigation drawer
    nav_drawer = Drawer(
        trigger_label="☰ Menu",
        drawer_id="drawer-nav",
        content=html.div(
            html.h3("Navigation", class_="text-xl font-bold mb-4"),
            html.nav(
                html.a("Home", href="/", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                html.a("Features", href="/features", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                html.a("Pricing", href="/pricing", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
                html.a("Contact", href="/contact", class_="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-700"),
            ),
        ),
        placement=DrawerPlacement.LEFT,
        width="w-64",
    )

    # Contact form drawer
    contact_drawer = Drawer(
        trigger_label="Contact Us",
        drawer_id="drawer-contact",
        content=html.div(
            html.h3("Get in Touch", class_="text-xl font-bold mb-4"),
            html.form(
                Input(label="Name", name="name", required=True),
                Input(label="Email", name="email", type="email", required=True),
                Textarea(label="Message", name="message", rows=4),
                Button(label="Send", type="submit", color=Color.PRIMARY),
                hx_post="/api/contact",
                hx_target="#contact-result",
                class_="space-y-4",
            ),
            html.div(id="contact-result", class_="mt-4"),
        ),
        placement=DrawerPlacement.RIGHT,
    )

    # Render both drawers
    nav_html = await renderer.render(nav_drawer)
    contact_html = await renderer.render(contact_drawer)

    return {
        "title": "Drawer Demo",
        "content": f"""
            <div class="container mx-auto p-8">
                <h1 class="text-3xl font-bold mb-8">Drawer Component Demo</h1>
                <div class="space-x-4">
                    {nav_html}
                    {contact_html}
                </div>
                <div class="mt-8 p-4 bg-white dark:bg-gray-800 rounded-lg">
                    <h2 class="text-xl font-bold mb-4">Page Content</h2>
                    <p>This is the main page content. Click the buttons above to open drawers!</p>
                </div>
            </div>

            <script>
                // HTMX event listener for drawer closure
                document.body.addEventListener('close-drawer-contact', () => {{
                    const drawer = FlowbiteInstances.getInstance('Drawer', 'drawer-contact');
                    if (drawer) drawer.hide();
                }});
            </script>
        """
    }

@app.post("/api/contact")
async def contact(name: str, email: str, message: str):
    print(f"Contact from {name} ({email}): {message}")
    response = Response(
        content=f'<p class="text-green-600">Thank you, {name}! We\'ll be in touch soon.</p>'
    )
    response.headers["HX-Trigger"] = "close-drawer-contact"
    return response
```

**Run it**:

```bash
uvicorn app:app --reload
```

Visit `http://localhost:8000` and try both drawers!

---

## Summary

You've learned how to:

- ✅ Create basic drawers with navigation and forms
- ✅ Use all four placement variants (left, right, top, bottom)
- ✅ Integrate HTMX for dynamic form submissions
- ✅ Control drawer closure from server responses
- ✅ Customize styling and behavior

**Ready for production?** Review the full API contract and test suite to ensure your implementation meets all requirements.
