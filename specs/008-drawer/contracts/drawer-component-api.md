# Component API Contract: Drawer

**Feature**: 008-drawer
**Date**: 2025-11-18
**Type**: Python Component API (not REST/GraphQL)

## Overview

This contract defines the public API for the Drawer component. Since this is a server-side rendered UI component (not a web service), the "API" refers to the Python class interface that developers use to instantiate and render drawers.

---

## Component API

### Drawer Class

**Import Path**: `from flowbite_htmy.components import Drawer`

**Signature**:
```python
@dataclass(frozen=True, kw_only=True)
class Drawer:
    # Required parameters
    trigger_label: str
    content: Component

    # Optional configuration (with defaults)
    placement: DrawerPlacement = DrawerPlacement.LEFT
    backdrop: bool = True
    body_scrolling: bool = False
    edge: bool = False
    trigger_color: Color = Color.PRIMARY
    trigger_size: Size = Size.MD
    drawer_id: str | None = None
    width: str = "w-80"
    height: str = "h-1/2"
    class_: str = ""
    trigger_class: str = ""
    hx_get: str | None = None
    hx_post: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render drawer component as htmy Component tree."""
```

**Parameters**:

| Parameter | Type | Required | Default | Description | Validation |
|-----------|------|----------|---------|-------------|------------|
| `trigger_label` | `str` | ✅ Yes | - | Text for trigger button | Non-empty string |
| `content` | `Component` | ✅ Yes | - | Drawer body content | htmy Component |
| `placement` | `DrawerPlacement` | No | `LEFT` | Edge positioning | Enum: LEFT, RIGHT, TOP, BOTTOM |
| `backdrop` | `bool` | No | `True` | Show overlay | Boolean |
| `body_scrolling` | `bool` | No | `False` | Allow page scroll | Boolean |
| `edge` | `bool` | No | `False` | Show tab when closed | Boolean |
| `trigger_color` | `Color` | No | `PRIMARY` | Trigger color | Color enum |
| `trigger_size` | `Size` | No | `MD` | Trigger size | Size enum |
| `drawer_id` | `str \| None` | No | `None` | Unique ID | String or None (auto-gen) |
| `width` | `str` | No | `"w-80"` | Width (left/right) | Tailwind class |
| `height` | `str` | No | `"h-1/2"` | Height (top/bottom) | Tailwind class |
| `class_` | `str` | No | `""` | Additional classes | String |
| `trigger_class` | `str` | No | `""` | Trigger classes | String |
| `hx_get` | `str \| None` | No | `None` | HTMX GET URL | URL or None |
| `hx_post` | `str \| None` | No | `None` | HTMX POST URL | URL or None |
| `hx_target` | `str \| None` | No | `None` | HTMX target | CSS selector or None |
| `hx_swap` | `str \| None` | No | `None` | HTMX swap mode | HTMX value or None |

**Returns**: `Component` (htmy component tree ready for rendering)

**Raises**:
- No exceptions raised (dataclass validation handles type errors at instantiation)

---

## Usage Examples

### Example 1: Basic Left Drawer

```python
from htmy import html
from flowbite_htmy.components import Drawer

drawer = Drawer(
    trigger_label="Open Menu",
    content=html.div(
        html.h3("Navigation", class_="text-xl font-bold mb-4"),
        html.ul(
            html.li(html.a("Home", href="/")),
            html.li(html.a("About", href="/about")),
            html.li(html.a("Contact", href="/contact")),
        ),
    ),
)
```

**Expected Output**: Drawer sliding from left edge with navigation menu

---

### Example 2: Right Drawer with Backdrop Disabled

```python
from flowbite_htmy.components import Drawer
from flowbite_htmy.types import DrawerPlacement

drawer = Drawer(
    trigger_label="Settings",
    content=html.div("Settings panel content"),
    placement=DrawerPlacement.RIGHT,
    backdrop=False,
)
```

**Expected Output**: Drawer from right without dimming overlay

---

### Example 3: Form Within Drawer with HTMX

```python
from flowbite_htmy.components import Drawer, Input, Button

contact_form = html.form(
    Input(label="Name", name="name", required=True),
    Input(label="Email", name="email", type="email", required=True),
    Textarea(label="Message", name="message", rows=4),
    Button(label="Submit", type="submit"),
    hx_post="/api/contact",
    hx_target="#form-result",
)

drawer = Drawer(
    trigger_label="Contact Us",
    content=html.div(
        html.h3("Get in Touch"),
        contact_form,
        html.div(id="form-result"),  # HTMX target
    ),
)
```

**Expected Output**: Drawer with contact form, HTMX submission, server controls closure

**Server Response** (FastAPI):
```python
from fastapi import Response

@app.post("/api/contact")
async def contact(name: str, email: str, message: str):
    # Process form...
    response = Response(content="<p>Thank you! We'll be in touch.</p>")
    response.headers["HX-Trigger"] = "close-drawer-{drawer_id}"
    return response
```

---

### Example 4: Bottom Drawer with Edge Tab

```python
drawer = Drawer(
    trigger_label="Show Filters",
    content=html.div("Filter controls..."),
    placement=DrawerPlacement.BOTTOM,
    edge=True,
    height="h-1/3",
)
```

**Expected Output**: Drawer from bottom with visible tab, 1/3 viewport height

---

### Example 5: Customized Styling

```python
from flowbite_htmy.types import Color, Size

drawer = Drawer(
    trigger_label="Profile",
    content=html.div("User profile..."),
    trigger_color=Color.SUCCESS,
    trigger_size=Size.LG,
    width="w-96",  # Custom width
    class_="bg-gray-100 dark:bg-gray-800",  # Custom drawer bg
    trigger_class="rounded-full",  # Custom trigger style
)
```

**Expected Output**: Green large trigger button, wider drawer, custom background

---

## Enum Types

### DrawerPlacement

**Import**: `from flowbite_htmy.types import DrawerPlacement`

```python
class DrawerPlacement(str, Enum):
    LEFT = "left"    # Slides from left edge (default)
    RIGHT = "right"  # Slides from right edge
    TOP = "top"      # Slides from top edge
    BOTTOM = "bottom"  # Slides from bottom edge
```

---

## Integration with Other Components

### Composing with Existing Components

```python
from flowbite_htmy.components import Drawer, Button, Badge, Avatar

# Navigation drawer with avatar and badges
nav_drawer = Drawer(
    trigger_label="Menu",
    content=html.div(
        Avatar(src="/user.jpg", alt="User", size=Size.LG),
        html.h4("John Doe", class_="mt-2"),
        Badge(label="Premium", color=Color.SUCCESS),
        html.nav(
            html.a("Dashboard", href="/dashboard"),
            html.a("Settings", href="/settings"),
        ),
    ),
)
```

---

## JavaScript Integration Points

### Flowbite JavaScript API

Developers can access drawer instance from JavaScript:

```javascript
// Get drawer instance by ID
const drawer = FlowbiteInstances.getInstance('Drawer', 'drawer-example');

// Programmatically control drawer
drawer.show();   // Open drawer
drawer.hide();   // Close drawer
drawer.toggle(); // Toggle state
drawer.isVisible(); // Check if open
```

### HTMX Event Handling

Server sends closure trigger via header:

```python
# FastAPI endpoint
response.headers["HX-Trigger"] = "close-drawer-example"
```

Client listens for event:

```javascript
// In Jinja template
document.body.addEventListener('close-drawer-example', () => {
  const drawer = FlowbiteInstances.getInstance('Drawer', 'drawer-example');
  drawer.hide();
});
```

---

## Accessibility Attributes

The component automatically generates:

| Attribute | Value | Purpose |
|-----------|-------|---------|
| `id` | `drawer-{id}` | Unique drawer identifier |
| `aria-labelledby` | `drawer-{id}-label` | Links to header for screen readers |
| `aria-hidden` | `"true"` (initial) | Hides from assistive tech when closed |
| `tabindex` | `"-1"` | Makes drawer focusable programmatically |
| `role` | Implied (div) | Drawer as container role |
| `data-drawer-target` | `drawer-{id}` | Flowbite JS target |
| `data-drawer-placement` | `left/right/top/bottom` | Flowbite JS placement config |

Focus trap automatically enabled - Tab/Shift+Tab cycle through drawer elements only.

---

## Error Handling

**Type Errors**: Caught at instantiation by Python type system

```python
# ❌ Type error - caught by mypy and runtime
drawer = Drawer(
    trigger_label=123,  # Should be str
    content="not a component",  # Should be Component
)
```

**Invalid Enum Values**: Prevented by type system

```python
# ❌ Type error - DrawerPlacement.MIDDLE doesn't exist
drawer = Drawer(
    trigger_label="Open",
    content=html.div("..."),
    placement="middle",  # Should be DrawerPlacement enum
)
```

**Missing Required Parameters**: Caught by dataclass

```python
# ❌ Missing required positional argument
drawer = Drawer()  # Needs trigger_label and content
```

---

## Versioning and Compatibility

**Component Version**: Introduced in flowbite-htmy 0.1.0 (Phase 2C)

**Dependency Requirements**:
- htmy >= 0.1.0
- Flowbite CSS 2.5.1+ (CDN or npm)
- Flowbite JavaScript 2.5.1+ (CDN or npm)
- HTMX 2.0.2+ (optional, for dynamic content)

**Breaking Changes**:
- None (initial release)

**Backward Compatibility**:
- Component follows project's dataclass pattern (same as Button, Badge, Alert, etc.)
- Props follow naming conventions (class_, hx_* attributes)
- Integrates with existing ThemeContext, ClassBuilder, Icon utilities

---

## Testing Contract

### Unit Test Requirements

**Minimum Test Coverage**: >90% (per constitution)

**Required Test Cases**:
1. Default rendering (minimal props)
2. All placement variants (LEFT, RIGHT, TOP, BOTTOM)
3. Backdrop enabled/disabled
4. Edge tab enabled/disabled
5. Dark mode classes present
6. ARIA attributes correct
7. Data attributes for Flowbite
8. HTMX attributes passthrough
9. Custom CSS class merging
10. Unique ID generation

**Snapshot Tests**:
- HTML output for each placement
- With/without backdrop
- With/without edge tab

### Integration Test Requirements

**Manual Browser Testing**:
- Focus trap behavior (Tab/Shift+Tab)
- Escape key closes drawer
- Click-outside closes drawer
- Auto-close on multiple drawers
- Debouncing during rapid clicks
- Internal scrolling with long content
- HTMX form submission and closure

---

## Performance Contract

**Rendering Performance**:
- Component instantiation: <10ms
- HTML generation: <100ms (SC-001 target: 5 lines of code)
- Browser animation: 300ms (SC-002)

**Runtime Performance**:
- Focus trap activation: <50ms
- Debounce delay: 300ms (during animation)
- Maximum internal scroll: 5000px (SC-008)

---

## Security Considerations

**XSS Prevention**:
- All user-provided content must be passed as htmy Components (auto-escaped)
- Do NOT pass raw HTML strings directly to content parameter
- HTMX URLs should be validated server-side

**Content Security Policy**:
- Flowbite JavaScript uses inline event handlers (may require CSP adjustments)
- HTMX requires `unsafe-eval` for some features (consult HTMX docs)

**Example - Safe Content**:
```python
# ✅ Safe - htmy escapes HTML
user_input = "<script>alert('xss')</script>"
drawer = Drawer(
    trigger_label="User Content",
    content=html.div(user_input),  # Escaped automatically
)
```

**Example - Unsafe Content**:
```python
# ❌ Unsafe - raw HTML injection risk
user_html = "<div onclick='malicious()'>Click me</div>"
drawer = Drawer(
    trigger_label="Unsafe",
    content=user_html,  # Type error (not Component), but illustrates risk
)
```

---

## Deprecation Policy

No deprecated features in initial release. Future deprecations will follow semantic versioning:

- **Major version**: Breaking changes (signature changes, removed props)
- **Minor version**: New features (new props, new variants)
- **Patch version**: Bug fixes (no API changes)

Deprecated features will be marked with warnings for one minor version before removal.
