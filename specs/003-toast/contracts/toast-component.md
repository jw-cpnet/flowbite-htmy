# Toast Component API Contract

**Feature**: Toast notification component
**Branch**: 003-toast
**Date**: 2025-11-14
**Status**: Draft

## Overview

This contract defines the public API for the Toast component, including props, methods, rendering behavior, and integration patterns. This contract ensures backward compatibility and clear expectations for component consumers.

## Component API

### Import Paths

```python
# Primary imports
from flowbite_htmy.components import Toast, ToastActionButton
from flowbite_htmy.types import ToastVariant
from flowbite_htmy.icons import Icon

# Alternative: Import from root
from flowbite_htmy import Toast, ToastVariant
```

### Constructor Signature

```python
@dataclass(frozen=True, kw_only=True)
class Toast:
    # Required
    message: str

    # Optional - Styling
    variant: ToastVariant = ToastVariant.INFO
    icon: Icon | None = None
    class_: str = ""

    # Optional - Functionality
    dismissible: bool = True
    id: str | None = None

    # Optional - Interactivity
    action_button: ToastActionButton | None = None

    # Optional - Rich Content
    avatar_src: str | None = None
```

### Props Reference

| Prop | Type | Required | Default | Description | Validation |
|------|------|----------|---------|-------------|------------|
| `message` | str | ✅ Yes | - | Toast message text | MUST NOT be empty |
| `variant` | ToastVariant | No | INFO | Toast color variant | MUST be valid enum value |
| `icon` | Icon \| None | No | None | Custom icon (None = default) | If set, MUST be valid Icon enum |
| `class_` | str | No | "" | Additional CSS classes | Merged with component classes |
| `dismissible` | bool | No | True | Show close button | - |
| `id` | str \| None | No | None | HTML element ID | If None, auto-generated |
| `action_button` | ToastActionButton \| None | No | None | Interactive button | - |
| `avatar_src` | str \| None | No | None | Avatar image URL | MUST be valid URL |

### ToastActionButton API

```python
@dataclass(frozen=True, kw_only=True)
class ToastActionButton:
    # Required
    label: str

    # HTMX attributes (all optional)
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | bool | None = None
    hx_select: str | None = None

    # Standard attributes
    type_: str = "button"
    class_: str = ""
```

## Rendering Contract

### HTML Output Structure

**Simple Toast** (message + icon + close button):
```html
<div id="toast-{id}" class="flex items-center w-full max-w-xs p-4 text-gray-500 bg-white rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800" role="alert">
    <div class="inline-flex items-center justify-center shrink-0 w-8 h-8 text-{color}-500 bg-{color}-100 rounded-lg dark:bg-{color}-800 dark:text-{color}-200">
        <svg class="w-4 h-4" aria-hidden="true">...</svg>
        <span class="sr-only">{Icon name}</span>
    </div>
    <div class="ms-3 text-sm font-normal">{message}</div>
    <button type="button" class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700" data-dismiss-target="#toast-{id}" aria-label="Close">
        <span class="sr-only">Close</span>
        <svg class="w-3 h-3">...</svg>
    </button>
</div>
```

**Interactive Toast** (with action button):
```html
<div id="toast-{id}" class="..." role="alert">
    <div class="flex">
        <!-- Icon container -->
        <div class="...">...</div>

        <!-- Message content -->
        <div class="ms-3 text-sm font-normal">
            {message}
            <div class="mt-2">
                <button type="button" class="inline-flex px-2.5 py-1.5 text-xs font-medium text-center text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800" hx-get="{url}" hx-target="{target}">
                    {action_button.label}
                </button>
            </div>
        </div>

        <!-- Close button -->
        <button type="button" class="ms-auto ...">...</button>
    </div>
</div>
```

**Rich Content Toast** (with avatar):
```html
<div id="toast-{id}" class="..." role="alert">
    <div class="flex">
        <img class="w-8 h-8 rounded-full" src="{avatar_src}" alt="Avatar"/>
        <div class="ms-3 text-sm font-normal">
            {message}
            <!-- Optional action button -->
        </div>
        <button type="button" class="ms-auto ...">...</button>
    </div>
</div>
```

### Guaranteed HTML Attributes

**Container Element** (`<div>`):
- `id`: Always present (auto-generated or custom)
- `class`: Always includes Flowbite base classes + custom classes
- `role="alert"`: Always present for accessibility

**Icon Container** (`<div>`):
- `class`: Variant-specific color classes (green-*, red-*, yellow-*, blue-*)
- Always includes dark mode classes (dark:bg-*, dark:text-*)

**Icon SVG** (`<svg>`):
- `aria-hidden="true"`: Always present (icon is decorative)
- `class`: Standard icon sizing (w-4 h-4)

**Close Button** (`<button>`) (if dismissible=True):
- `type="button"`: Always present
- `data-dismiss-target="#{id}"`: Always present for Flowbite JS integration
- `aria-label="Close"`: Always present for accessibility
- `<span class="sr-only">Close</span>`: Always present for screen readers

**Action Button** (`<button>`) (if action_button provided):
- `type="button"`: Always present
- HTMX attributes: Present if specified in ToastActionButton
- Standard Flowbite button styling

## Variant Behavior

### ToastVariant.SUCCESS
- **Icon**: Icon.CHECK (checkmark)
- **Colors**: Green (text-green-500, bg-green-100, dark:bg-green-800, dark:text-green-200)
- **Use Cases**: Operation success, save confirmation, upload complete

### ToastVariant.DANGER
- **Icon**: Icon.CLOSE (X mark)
- **Colors**: Red (text-red-500, bg-red-100, dark:bg-red-800, dark:text-red-200)
- **Use Cases**: Error messages, validation failures, operation failures

### ToastVariant.WARNING
- **Icon**: Icon.EXCLAMATION (exclamation mark)
- **Colors**: Yellow (text-yellow-500, bg-yellow-100, dark:bg-yellow-800, dark:text-yellow-200)
- **Use Cases**: Warnings, cautionary messages, pending actions

### ToastVariant.INFO
- **Icon**: Icon.INFO (info "i")
- **Colors**: Blue (text-blue-500, bg-blue-100, dark:bg-blue-800, dark:text-blue-200)
- **Use Cases**: Informational messages, tips, notifications

## Integration Patterns

### Pattern 1: Simple Toast in FastAPI Route

```python
from fastapi import FastAPI
from htmy import Renderer
from flowbite_htmy import Toast, ToastVariant

app = FastAPI()
renderer = Renderer()

@app.post("/save")
async def save_item():
    # ... save logic
    toast = Toast(
        message="Item saved successfully",
        variant=ToastVariant.SUCCESS
    )
    return {"html": await renderer.render(toast)}
```

### Pattern 2: HTMX Response Toast

```python
@app.post("/update")
async def update_item():
    # ... update logic
    toast = Toast(
        message="Update complete",
        variant=ToastVariant.SUCCESS
    )
    return await renderer.render(toast)
```

**HTML (client-side)**:
```html
<button hx-post="/update" hx-target="#toast-container" hx-swap="innerHTML">
    Update
</button>
<div id="toast-container"></div>
```

### Pattern 3: Interactive Toast with Action

```python
from flowbite_htmy import ToastActionButton

@app.post("/upload")
async def upload_file():
    # ... upload logic
    toast = Toast(
        message="File uploaded successfully. Share with your team?",
        variant=ToastVariant.SUCCESS,
        action_button=ToastActionButton(
            label="Share",
            hx_post="/share/file",
            hx_target="#share-modal"
        )
    )
    return await renderer.render(toast)
```

### Pattern 4: Rich Content Toast (Chat Notification)

```python
@app.get("/notifications/latest")
async def get_latest_notification():
    toast = Toast(
        message="Alice: Thanks for the quick response!",
        variant=ToastVariant.INFO,
        avatar_src="/static/avatars/alice.jpg",
        action_button=ToastActionButton(
            label="Reply",
            hx_get="/messages/reply/123",
            hx_target="#chat-window"
        )
    )
    return await renderer.render(toast)
```

### Pattern 5: Positioned Toast Container

```python
# Application layout (Jinja template)
```
```html
<!-- Fixed position container for toasts -->
<div id="toast-container" class="fixed top-4 right-4 z-50 space-y-2">
    <!-- Toasts rendered here via HTMX -->
</div>

<!-- HTMX triggers toast updates -->
<button hx-post="/action" hx-target="#toast-container" hx-swap="afterbegin">
    Perform Action
</button>
```

## Accessibility Contract

### ARIA Attributes

**REQUIRED**:
- `role="alert"` on container element - Announces toast to screen readers
- `aria-hidden="true"` on icon SVG - Icon is decorative only
- `aria-label="Close"` on close button - Describes button purpose

**OPTIONAL**:
- `aria-live="assertive"` can be added via class_ prop for critical toasts

### Screen Reader Behavior

**Guaranteed Announcements**:
1. Toast message text - Read when toast appears (via role="alert")
2. Close button - "Close button" read when focused
3. Action button - Button label read when focused

**SR-Only Elements**:
- Close button includes `<span class="sr-only">Close</span>`
- Icon includes `<span class="sr-only">{Icon name}</span>`

### Keyboard Navigation

**Expected Behavior** (handled by browser/Flowbite JS):
- Tab: Focus close button
- Tab: Focus action button (if present)
- Enter/Space: Activate focused button
- Escape: Dismiss toast (if Flowbite JS configured)

## Performance Guarantees

### Rendering Performance

- **Simple Toast**: < 5ms render time (average)
- **Interactive Toast**: < 10ms render time (average)
- **Rich Content Toast**: < 15ms render time (average)

### Memory Footprint

- Component instances: ~500 bytes each (frozen dataclass)
- No memory leaks (stateless, no event listeners in Python)

### Scalability

- Supports unlimited toast instances per page (limited by browser DOM)
- No performance degradation with multiple toasts (each independent)

## Error Handling

### Invalid Props

**Empty Message**:
```python
Toast(message="")  # ValueError: message cannot be empty
```

**Invalid Variant**:
```python
Toast(message="Test", variant="invalid")  # TypeError: not a ToastVariant
```

**Empty Action Button Label**:
```python
ToastActionButton(label="")  # ValueError: label cannot be empty
```

### Graceful Degradation

**Missing Icon File**: Falls back to default icon for variant

**Invalid Avatar URL**: Browser handles (shows broken image icon)

**Missing Flowbite JS**: Close button renders but dismiss functionality unavailable

**No HTMX**: Action button renders as standard button (no interaction)

## Backward Compatibility

**Versioning**: Component follows semantic versioning

**Breaking Changes** (will require major version bump):
- Removing/renaming required props
- Changing prop types in incompatible ways
- Removing ToastVariant enum values
- Changing HTML structure in ways that break CSS selectors

**Non-Breaking Changes** (minor/patch versions):
- Adding new optional props
- Adding new ToastVariant values
- Adding new ToastActionButton attributes
- Improving performance
- Bug fixes

## Testing Contract

**Component MUST pass these tests**:
1. Renders with minimal props (message only)
2. Renders all 4 variants with correct colors
3. Renders custom icon when provided
4. Renders without close button when dismissible=False
5. Renders action button with HTMX attributes
6. Renders avatar when avatar_src provided
7. Applies custom classes via class_ prop
8. Generates unique ID when id not provided
9. Uses custom ID when provided
10. Includes role="alert" attribute
11. Includes dark mode classes
12. Renders sr-only labels for accessibility

**Minimum Coverage**: 95%

## Deprecation Policy

**Notice Period**: 6 months minimum for prop deprecations

**Deprecation Process**:
1. Add deprecation warning in docstring
2. Update CHANGELOG with deprecation notice
3. Maintain backward compatibility during notice period
4. Remove in next major version

## Examples

### Example 1: Minimal Toast
```python
Toast(message="Hello World")
# Uses default: variant=INFO, icon=Icon.INFO, dismissible=True
```

### Example 2: Success Toast with Custom ID
```python
Toast(
    message="Operation successful",
    variant=ToastVariant.SUCCESS,
    id="success-toast-1"
)
```

### Example 3: Error Toast (Non-dismissible)
```python
Toast(
    message="Critical error occurred",
    variant=ToastVariant.DANGER,
    dismissible=False
)
```

### Example 4: Toast with Custom Icon
```python
Toast(
    message="Payment processed",
    variant=ToastVariant.SUCCESS,
    icon=Icon.PAYMENT  # Override default CHECK icon
)
```

### Example 5: Interactive Toast
```python
Toast(
    message="New comment on your post",
    variant=ToastVariant.INFO,
    action_button=ToastActionButton(
        label="View",
        hx_get="/comments/123",
        hx_target="#comment-section"
    )
)
```

### Example 6: Rich Content Toast
```python
Toast(
    message="Alice sent you a message",
    variant=ToastVariant.INFO,
    avatar_src="/avatars/alice.jpg",
    action_button=ToastActionButton(
        label="Reply",
        hx_get="/reply/alice"
    )
)
```

### Example 7: Custom Styled Toast
```python
Toast(
    message="Custom notification",
    variant=ToastVariant.WARNING,
    class_="border-2 border-yellow-600 shadow-lg"
)
# Custom classes merged with base classes
```

## Change Log

**Version 1.0.0** (2025-11-14):
- Initial API contract
- Supports 4 variants (SUCCESS, DANGER, WARNING, INFO)
- Supports action buttons with HTMX
- Supports rich content with avatars
- Supports dismissible functionality
