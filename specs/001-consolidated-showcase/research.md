# Research: Consolidated Component Showcase Application

**Date**: 2025-11-13
**Feature**: Consolidated Component Showcase
**Purpose**: Research technical decisions for multi-page showcase application

---

## 1. FastAPI Multi-Page Application Patterns

### Decision: Explicit Route Pattern

**Chosen Approach**: Use explicit `@app.get("/component-name")` routes for each component showcase page.

**Rationale**:
- **Clarity**: Each route is explicitly defined, making it easy to see all available pages
- **Type Safety**: FastAPI can validate and document each route independently
- **Flexibility**: Easy to add route-specific logic, parameters, or middleware
- **Debugging**: Stack traces clearly show which route handler is active
- **SEO-Friendly**: Clean, predictable URLs (`/buttons`, `/badges`, not `/component?name=buttons`)

**Alternatives Considered**:
1. **Dynamic Routing** (`@app.get("/component/{name}")`):
   - **Rejected because**: Requires runtime validation of component names, less type-safe, harder to document individual pages
2. **Catch-All Route** (single handler for all components):
   - **Rejected because**: Loses FastAPI's automatic documentation, harder to customize per-component behavior

**Implementation Pattern**:
```python
@app.get("/")
@jinja.page("showcase-layout.html.jinja")
async def homepage() -> dict:
    return {"current_page": "home", "content": await renderer.render(homepage_content())}

@app.get("/buttons")
@jinja.page("showcase-layout.html.jinja")
async def buttons_page() -> dict:
    return {"current_page": "buttons", "content": await renderer.render(buttons_showcase())}

# Repeat for each component...
```

---

## 2. Navigation Menu Implementation

### Decision: Sidebar Navigation with Button Components

**Chosen Approach**: Vertical sidebar navigation using flowbite-htmy Button components with conditional styling for active state.

**Rationale**:
- **Component Reuse**: Demonstrates real-world usage of Button component
- **Consistent Styling**: Buttons already have proper dark mode, hover states, and accessibility
- **Space Efficiency**: Sidebar keeps navigation visible while preserving vertical space for showcases
- **Mobile-Friendly**: Can collapse to hamburger menu on small screens
- **Active State**: Button variant or color can indicate current page

**Alternatives Considered**:
1. **Top Bar Navigation with Badges**:
   - **Rejected because**: Takes up horizontal space, harder to fit 10 items without wrapping
2. **Tab Component** (if one existed):
   - **Rejected because**: Tab component doesn't exist in flowbite-htmy yet
3. **Custom HTML Links**:
   - **Rejected because**: Defeats purpose of using flowbite-htmy components for navigation

**Implementation Pattern**:
```python
def build_navigation(current_page: str) -> Component:
    components = [
        ("buttons", "Buttons"),
        ("badges", "Badges"),
        ("alerts", "Alerts"),
        ("avatars", "Avatars"),
        ("cards", "Cards"),
        ("checkboxes", "Checkboxes"),
        ("inputs", "Inputs"),
        ("modals", "Modals"),
        ("paginations", "Paginations"),
        ("selects", "Selects"),
    ]

    return html.nav(
        *[
            Button(
                label=title,
                color=Color.PRIMARY if name == current_page else Color.SECONDARY,
                variant=ButtonVariant.DEFAULT if name == current_page else ButtonVariant.OUTLINE,
                class_="w-full mb-2",
                # Use standard <a> tag for navigation (no HTMX needed)
            )
            for name, title in components
        ],
        class_="w-64 p-4 border-r border-gray-200 dark:border-gray-700"
    )
```

**Active State Strategy**:
- Current page button uses `Color.PRIMARY` with `ButtonVariant.DEFAULT` (solid fill)
- Other pages use `Color.SECONDARY` with `ButtonVariant.OUTLINE` (outline style)
- This provides clear visual distinction without custom CSS

---

## 3. Content Reuse Strategy

### Decision: Extract Showcase Functions, Keep in Original Files

**Chosen Approach**: Refactor each standalone app to separate showcase content generation from FastAPI setup. Keep functions in original files and import into consolidated app.

**Rationale**:
- **Minimal Changes**: Original apps still work independently during transition
- **Code Reuse**: Both standalone and consolidated apps can use same showcase functions
- **Maintainability**: Single source of truth for each component's showcase content
- **Gradual Migration**: Can test consolidated app while keeping standalones functional
- **Comparison**: Easy to compare standalone vs consolidated implementations

**Alternatives Considered**:
1. **Move All Content to New Module** (`examples/showcases/`):
   - **Rejected because**: Breaks existing standalone apps, creates more file churn
2. **Duplicate Content in Consolidated App**:
   - **Rejected because**: Violates DRY, creates maintenance burden
3. **Keep Everything Monolithic in showcase.py**:
   - **Rejected because**: Creates 1000+ line file, hard to maintain

**Implementation Pattern**:

**Step 1**: Refactor existing app (e.g., `buttons.py`):
```python
# buttons.py
def build_buttons_showcase() -> Component:
    """Generate button showcase content (extracted from main route)."""
    return html.div(
        html.h2("Default buttons", class_="..."),
        html.div(Button(...), Button(...)),
        # ... all showcase sections
    )

@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    return {"content": await renderer.render(build_buttons_showcase())}
```

**Step 2**: Import into consolidated app:
```python
# showcase.py
from examples.buttons import build_buttons_showcase
from examples.badges import build_badges_showcase
# ... other imports

@app.get("/buttons")
@jinja.page("showcase-layout.html.jinja")
async def buttons_page() -> dict:
    content = await renderer.render(build_buttons_showcase())
    return {"current_page": "buttons", "content": content}
```

---

## 4. Template Organization

### Decision: Create New showcase-layout.html.jinja Extending base.html.jinja

**Chosen Approach**: Create new template with sidebar navigation block, extending existing `base.html.jinja` for common elements (dark mode toggle, CSS/JS includes).

**Rationale**:
- **Template Inheritance**: Reuses existing base template's dark mode script and dependencies
- **Separation of Concerns**: Consolidated app has its own layout, doesn't affect standalone apps
- **Backward Compatibility**: Original base.html.jinja remains unchanged for standalone apps
- **Clean Navigation**: Sidebar defined in template, content passed from route handlers

**Alternatives Considered**:
1. **Modify Existing base.html.jinja**:
   - **Rejected because**: Would affect all standalone apps, creates coupling
2. **No Template Inheritance** (duplicate everything):
   - **Rejected because**: Duplicates dark mode script, CSS includes, violates DRY
3. **Single Template for All** (conditional blocks):
   - **Rejected because**: Creates complex conditionals, harder to maintain

**Implementation Pattern**:

**showcase-layout.html.jinja**:
```jinja2
{% extends "base.html.jinja" %}

{% block body %}
<div class="flex min-h-screen">
    <!-- Sidebar Navigation -->
    <aside class="w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700">
        <div class="p-4">
            <h1 class="text-2xl font-bold mb-6">Flowbite-HTMY</h1>
            <!-- Navigation buttons rendered here -->
            {{ navigation|safe }}
        </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 p-8">
        {{ content|safe }}
    </main>
</div>
{% endblock %}
```

**Route Handler**:
```python
@app.get("/buttons")
@jinja.page("showcase-layout.html.jinja")
async def buttons_page() -> dict:
    navigation = await renderer.render(build_navigation("buttons"))
    content = await renderer.render(build_buttons_showcase())
    return {
        "current_page": "buttons",
        "navigation": navigation,
        "content": content,
    }
```

---

## 5. Performance Considerations

### Analysis: No Significant Performance Concerns

**Findings**:
- **Startup Time**: Importing 10 modules minimal overhead (Python import caching)
- **Route Registration**: 11 routes (homepage + 10 components) is trivial for FastAPI
- **Memory Usage**: All showcase content generated on-demand, not cached in memory
- **Render Time**: Each page renders only its own content, same as standalone apps
- **Navigation Overhead**: Rendering navigation menu adds ~50-100ms per page (acceptable)

**Optimizations** (if needed in future):
1. Cache rendered navigation HTML (same for all pages except active state)
2. Lazy-load showcase content (import modules only when route accessed)
3. Use HTMX for client-side navigation (avoid full page reloads)

**Decision**: No optimization needed for MVP. Monitor performance during testing.

---

## 6. Dark Mode State Persistence

### Decision: Reuse Existing localStorage JavaScript

**Chosen Approach**: Extend base.html.jinja's existing dark mode toggle script. State already persists via localStorage across page reloads.

**Rationale**:
- **Already Implemented**: Current standalone apps use localStorage for dark mode
- **No Server State Needed**: Client-side persistence is sufficient for showcase app
- **Cross-Page Compatibility**: localStorage works across all routes automatically
- **Fast Implementation**: No backend changes required

**Implementation**: None required - inheritance from base.html.jinja provides this functionality.

---

## 7. Error Handling

### Decision: Simple 404 Page for Invalid Routes

**Chosen Approach**: FastAPI's built-in 404 handling with custom HTML response.

**Implementation Pattern**:
```python
from fastapi import HTTPException
from fastapi.responses import HTMLResponse

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return HTMLResponse(
        content="<h1>404 - Page Not Found</h1><p>Available pages: /, /buttons, /badges, ...</p>",
        status_code=404
    )
```

---

## Summary of Research Decisions

| Topic | Decision | Primary Rationale |
|-------|----------|-------------------|
| **Route Pattern** | Explicit routes (`@app.get("/buttons")`) | Type safety, clarity, SEO-friendly URLs |
| **Navigation** | Sidebar with Button components | Space efficiency, component reuse, mobile-friendly |
| **Active State** | Button variant + color differentiation | No custom CSS, built-in component styling |
| **Content Reuse** | Extract functions, keep in original files | Minimal changes, backward compatibility |
| **Templates** | New showcase-layout.html.jinja extending base | Clean separation, template inheritance |
| **Dark Mode** | Reuse existing localStorage script | Already implemented, no changes needed |
| **Performance** | No optimization needed | Lightweight, on-demand rendering |
| **Error Handling** | FastAPI 404 with custom HTML | Simple, sufficient for showcase app |

---

## Implementation Priority

1. **Phase 1**: Refactor one standalone app (buttons.py) to extract showcase function
2. **Phase 2**: Create showcase-layout.html.jinja with sidebar structure
3. **Phase 3**: Build showcase.py with homepage + buttons route
4. **Phase 4**: Add navigation menu using Button components
5. **Phase 5**: Test buttons page end-to-end
6. **Phase 6**: Repeat for remaining 9 components (parallel-friendly)
7. **Phase 7**: Update VS Code launch.json
8. **Phase 8**: Final E2E testing of all routes and navigation

---

## Open Questions (Resolved)

All research questions resolved. Ready to proceed to Phase 1 (Design & Contracts).
