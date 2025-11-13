# API Contracts: Consolidated Component Showcase Routes

**Date**: 2025-11-13
**Feature**: Consolidated Component Showcase
**Purpose**: Define all HTTP routes and their contracts

---

## Base URL

- **Development**: `http://localhost:8000`
- **Protocol**: HTTP/1.1
- **Content-Type**: `text/html; charset=utf-8`

---

## Route Definitions

### `GET /`

**Description**: Homepage with welcome message and component gallery

**Parameters**: None

**Response**: HTML page

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "home",
    "title": "Flowbite-HTMY Component Showcase",
    "navigation": "<nav>...</nav>",  # Rendered navigation menu
    "content": "<div>...</div>"      # Homepage content with component grid
}
```

**Content Structure**:
- Welcome header with project description
- Grid of component cards (10 total)
- Each card shows component name, description, and link to showcase page
- Dark mode toggle button (inherited from base template)

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /buttons`

**Description**: Button component comprehensive showcase

**Parameters**: None

**Response**: HTML page with all button examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "buttons",
    "title": "Buttons - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"  # All button showcase sections
}
```

**Showcase Sections** (from `build_buttons_showcase()`):
1. Default buttons (colors)
2. Button sizes
3. Button variants (outline, gradient)
4. Buttons with icons
5. Buttons with badges
6. Icon-only buttons
7. Social buttons
8. Payment buttons
9. HTMX examples
10. Loading states

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /badges`

**Description**: Badge component showcase

**Parameters**: None

**Response**: HTML page with all badge examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "badges",
    "title": "Badges - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_badges_showcase()`):
1. Default badges
2. Large badges
3. Badges with icons
4. Pill badges
5. Bordered badges
6. Icon-only badges
7. Badge combinations

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /alerts`

**Description**: Alert component showcase

**Parameters**: None

**Response**: HTML page with all alert examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "alerts",
    "title": "Alerts - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_alerts_showcase()`):
1. Default alerts
2. Alerts with icons
3. Dismissible alerts
4. Border alerts
5. Alerts with lists
6. Alerts with additional content

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /avatars`

**Description**: Avatar component showcase

**Parameters**: None

**Response**: HTML page with all avatar examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "avatars",
    "title": "Avatars - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_avatars_showcase()`):
1. Default avatars
2. Avatar sizes
3. Avatar with placeholder
4. Avatar groups
5. Stacked avatars
6. Avatar with indicators
7. Avatar with border
8. Avatar with text fallback

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /cards`

**Description**: Card component showcase

**Parameters**: None

**Response**: HTML page with all card examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "cards",
    "title": "Cards - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_cards_showcase()`):
1. Default card
2. Card with image
3. Card with action buttons
4. Horizontal card
5. Card grid
6. Pricing cards
7. Testimonial cards
8. Product cards

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /checkboxes`

**Description**: Checkbox component showcase

**Parameters**: None

**Response**: HTML page with all checkbox examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "checkboxes",
    "title": "Checkboxes - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_checkboxes_showcase()`):
1. Default checkbox
2. Checkbox with helper text
3. Checkbox validation states
4. Disabled checkbox
5. Checkbox groups
6. Inline checkboxes

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /inputs`

**Description**: Input component showcase

**Parameters**: None

**Response**: HTML page with all input examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "inputs",
    "title": "Inputs - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_inputs_showcase()`):
1. Default input
2. Input with helper text
3. Input validation states
4. Required input
5. Disabled input
6. Input sizes
7. Input with icons

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /modals`

**Description**: Modal component showcase

**Parameters**: None

**Response**: HTML page with all modal examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "modals",
    "title": "Modals - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_modals_showcase()`):
1. Default modal
2. Small/large modals
3. Modal with form
4. Confirmation modal
5. Modal with image
6. Modal with footer

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /paginations`

**Description**: Pagination component showcase

**Parameters**: None

**Response**: HTML page with all pagination examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "paginations",
    "title": "Paginations - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_paginations_showcase()`):
1. Default pagination
2. Pagination sizes
3. Pagination with icons
4. Pagination with info text
5. Table pagination
6. Edge cases (first/last page)

**Status Codes**:
- `200 OK`: Page rendered successfully

---

### `GET /selects`

**Description**: Select component showcase

**Parameters**: None

**Response**: HTML page with all select examples

**Template**: `showcase-layout.html.jinja`

**Context**:
```python
{
    "current_page": "selects",
    "title": "Selects - Flowbite-HTMY Showcase",
    "navigation": "<nav>...</nav>",
    "content": "<div>...</div>"
}
```

**Showcase Sections** (from `build_selects_showcase()`):
1. Default select
2. Select with helper text
3. Select validation states
4. Required select
5. Disabled select
6. Multiple select
7. Select with groups

**Status Codes**:
- `200 OK`: Page rendered successfully

---

## Error Responses

### `404 Not Found`

**Triggered By**: Accessing undefined route (e.g., `/nonexistent`)

**Response**: Custom HTML error page

**Content**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page does not exist.</p>
    <h2>Available Pages:</h2>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/buttons">Buttons</a></li>
        <li><a href="/badges">Badges</a></li>
        <!-- ... list all component pages -->
    </ul>
</body>
</html>
```

**Status Code**: `404 Not Found`

---

## Navigation State Contract

**Every Page Response Includes**:

1. **Navigation Menu** (rendered htmy component):
   - List of 10 component links
   - Current page indicated by button variant/color
   - All links use standard `<a>` tags (no JavaScript required)

2. **Dark Mode Toggle** (inherited from base template):
   - Button in top-right corner
   - State persisted via localStorage
   - Works across all pages

3. **Page Title** (in `<title>` tag):
   - Format: `{Component Name} - Flowbite-HTMY Showcase`
   - Example: `Buttons - Flowbite-HTMY Showcase`

---

## Optional: JSON API (Future Enhancement)

### `GET /api/components`

**Description**: JSON endpoint listing all available components

**Parameters**: None

**Response**: JSON array

**Example Response**:
```json
{
  "components": [
    {
      "name": "buttons",
      "path": "/buttons",
      "title": "Buttons",
      "description": "Interactive buttons with colors, sizes, variants, and icons",
      "order": 1
    },
    {
      "name": "badges",
      "path": "/badges",
      "title": "Badges",
      "description": "Labels and indicators with color variants",
      "order": 2
    }
    // ... 8 more components
  ]
}
```

**Status Codes**:
- `200 OK`: JSON returned successfully

**Note**: This endpoint is **optional** for MVP. Can be added later for programmatic access or testing.

---

## Performance Expectations

- **Cold Start**: < 3 seconds (app initialization)
- **Page Load**: < 1 second (per route)
- **Navigation**: < 500ms (server render + transfer)
- **Concurrent Users**: 100+ (sufficient for local showcase)

---

## Browser Compatibility

- **Supported**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Features Used**: HTML5, CSS3, JavaScript ES6+
- **Progressive Enhancement**: Core content accessible without JavaScript
- **Dark Mode**: Requires JavaScript for localStorage (degrades gracefully)

---

## Testing Contract

### Manual E2E Testing Checklist:

1. **Homepage** (`/`):
   - [ ] Component grid displays all 10 components
   - [ ] Each card links to correct showcase page
   - [ ] Dark mode toggle works

2. **Each Component Page** (`/buttons`, `/badges`, etc.):
   - [ ] All showcase sections render correctly
   - [ ] Navigation menu shows current page as active
   - [ ] Clicking other nav items navigates correctly
   - [ ] Dark mode persists across navigation
   - [ ] Interactive examples work (modals open, checkboxes toggle, etc.)

3. **Browser Navigation**:
   - [ ] Back button returns to previous page
   - [ ] Forward button works
   - [ ] Bookmarking a component page works
   - [ ] Direct URL entry works

4. **Error Handling**:
   - [ ] Invalid URL shows 404 page
   - [ ] 404 page lists all available routes

---

## Summary

All routes follow consistent pattern:
- Same template (`showcase-layout.html.jinja`)
- Same context structure (`PageContext`)
- Same navigation menu (with active state)
- Same dark mode support
- Same HTML response format

This consistency simplifies implementation and maintenance.
