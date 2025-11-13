# Quickstart Guide: Consolidated Component Showcase

**Date**: 2025-11-13
**Feature**: Consolidated Component Showcase
**Purpose**: Quick reference for running and using the consolidated showcase application

---

## Quick Start

### 1. Activate Virtual Environment

```bash
cd /home/jian/Work/personal/flowbite-htmy
source .venv/bin/activate
```

### 2. Run the Consolidated Showcase

```bash
python examples/showcase.py
```

Expected output:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 3. Open Your Browser

Navigate to: **http://localhost:8000**

---

## Available Pages

| URL | Component | Description |
|-----|-----------|-------------|
| `/` | Homepage | Component gallery with navigation |
| `/buttons` | Buttons | Interactive buttons (colors, sizes, variants, icons) |
| `/badges` | Badges | Labels and indicators |
| `/alerts` | Alerts | Notification messages |
| `/avatars` | Avatars | User profile pictures |
| `/cards` | Cards | Content containers |
| `/checkboxes` | Checkboxes | Checkbox inputs |
| `/inputs` | Inputs | Text input fields |
| `/modals` | Modals | Dialog boxes |
| `/paginations` | Paginations | Page navigation |
| `/selects` | Selects | Dropdown selections |

---

## Features

### Navigation

- **Sidebar Menu**: Persistent navigation on all pages
- **Active Page Indicator**: Current page highlighted in navigation
- **Direct URL Access**: Bookmark any component page
- **Browser Navigation**: Back/forward buttons fully supported

### Dark Mode

- **Toggle**: Button in top-right corner
- **Persistence**: State saved in browser localStorage
- **Cross-Page**: Dark mode setting persists across navigation

### Interactive Examples

- **Modals**: Click buttons to open modal dialogs
- **Checkboxes**: Toggle to see validation states
- **Pagination**: Click page numbers to see URL changes
- **Buttons**: Hover to see all interactive states

---

## Development Workflow

### Running in Debug Mode

**VS Code**:
1. Open VS Code in the project root
2. Go to Run and Debug panel (Ctrl+Shift+D)
3. Select "Consolidated Showcase" from dropdown
4. Press F5 or click green play button

**Manual**:
```bash
uvicorn examples.showcase:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reload on code changes.

### Stopping the Server

Press `Ctrl+C` in the terminal running the showcase.

---

## Comparison with Standalone Apps

### Before (Standalone Apps)

To view different components, you had to:
1. Stop the current app (Ctrl+C)
2. Run a different app: `python examples/buttons.py`
3. Refresh browser
4. Repeat for each component

**10 separate files**:
- `examples/buttons.py`
- `examples/badges.py`
- `examples/alerts.py`
- ... (7 more)

### After (Consolidated App)

To view different components:
1. Click navigation link
2. Done!

**1 main file**:
- `examples/showcase.py`

**Benefits**:
- ✅ Single command to see all components
- ✅ Easy navigation between components
- ✅ Consistent layout across all pages
- ✅ Dark mode persists across pages
- ✅ Better developer experience

---

## Troubleshooting

### Port Already in Use

**Error**:
```
ERROR:    [Errno 48] error while attempting to bind on address ('127.0.0.1', 8000): address already in use
```

**Solution**:
1. Check if another showcase app is running: `ps aux | grep python`
2. Kill the process: `kill <PID>`
3. Or use a different port: `uvicorn examples.showcase:app --port 8001`

### Import Errors

**Error**:
```
ModuleNotFoundError: No module named 'flowbite_htmy'
```

**Solution**:
1. Ensure virtual environment is activated: `source .venv/bin/activate`
2. Install dependencies: `pip install -e .`
3. Verify installation: `pip show flowbite-htmy`

### Template Not Found

**Error**:
```
jinja2.exceptions.TemplateNotFound: showcase-layout.html.jinja
```

**Solution**:
1. Ensure you're running from project root, not `examples/` directory
2. Check template exists: `ls examples/templates/showcase-layout.html.jinja`
3. Verify `templates` directory path in code: `Jinja2Templates(directory="examples/templates")`

### Dark Mode Not Working

**Issue**: Dark mode toggle doesn't persist across pages

**Solution**:
1. Ensure JavaScript is enabled in browser
2. Check browser console for errors (F12 → Console tab)
3. Clear localStorage: Open console, run `localStorage.clear()`, refresh page
4. Try different browser (Chrome, Firefox, Safari)

---

## Testing the Showcase

### Manual E2E Testing

After starting the showcase, verify:

1. **Homepage** (`/`):
   - [ ] See "Flowbite-HTMY Component Showcase" title
   - [ ] See grid of 10 component cards
   - [ ] Each card shows component name and description
   - [ ] Clicking a card navigates to that component's page

2. **Navigation Menu**:
   - [ ] Sidebar visible on all pages
   - [ ] Current page button is highlighted (filled, not outline)
   - [ ] Other pages have outline style
   - [ ] Clicking a nav button navigates to that page

3. **Component Pages**:
   - [ ] `/buttons` shows all button examples
   - [ ] `/badges` shows all badge examples
   - [ ] (Repeat for all 10 components)

4. **Dark Mode**:
   - [ ] Toggle button visible in top-right
   - [ ] Clicking toggle switches dark/light mode
   - [ ] Mode persists when navigating between pages
   - [ ] Mode persists after page refresh

5. **Browser Features**:
   - [ ] Back button returns to previous page
   - [ ] Forward button navigates forward
   - [ ] Bookmarking a page works
   - [ ] Direct URL entry works (e.g., type `/buttons` in address bar)

6. **Errors**:
   - [ ] Invalid URL (`/nonexistent`) shows 404 page
   - [ ] 404 page lists all available routes
   - [ ] No console errors (F12 → Console)

---

## Performance Expectations

- **Startup**: < 3 seconds
- **Page Load**: < 1 second per page
- **Navigation**: < 500ms between pages
- **Memory**: ~50-100MB (typical for FastAPI app)

---

## File Structure

```
examples/
├── showcase.py                      # Main consolidated app (NEW)
├── showcase_types.py                # Type definitions (NEW)
├── templates/
│   ├── base.html.jinja              # Base template (EXISTING)
│   └── showcase-layout.html.jinja   # Showcase layout (NEW)
├── buttons.py                       # Standalone app (keep for reference)
├── badges.py                        # Standalone app (keep for reference)
└── ...                              # Other standalone apps
```

---

## Next Steps

After verifying the showcase works:

1. **Update Documentation**: Point users to consolidated app instead of standalone apps
2. **Update VS Code Launch Config**: Add consolidated app debug configuration
3. **Deprecate Standalone Apps**: Add notices at top of standalone app files
4. **Share with Team**: Demo the consolidated showcase to other developers

---

## FAQ

### Q: What happened to the standalone apps?

**A**: They still exist in `examples/` directory for reference, but the consolidated app is now the recommended way to view all components.

### Q: Can I still run standalone apps?

**A**: Yes! All standalone apps still work independently. Example: `python examples/buttons.py`

### Q: How do I add a new component to the showcase?

**A**:
1. Create standalone showcase app (e.g., `examples/radio.py`)
2. Extract showcase function (e.g., `build_radio_showcase()`)
3. Add component to `COMPONENT_ROUTES` in `showcase.py`
4. Add route handler in `showcase.py`
5. Import and call showcase function

### Q: Does the consolidated app affect production code?

**A**: No! This is only for the `examples/` directory. The library code (`src/flowbite_htmy/`) is unchanged.

### Q: Can I use the consolidated app in production?

**A**: The showcase is for **development/demo purposes only**. For production, use flowbite-htmy components in your own FastAPI app.

---

## Additional Resources

- **Project README**: `/home/jian/Work/personal/flowbite-htmy/README.md`
- **Component Documentation**: `/home/jian/Work/personal/flowbite-htmy/CLAUDE.md`
- **Feature Spec**: `/home/jian/Work/personal/flowbite-htmy/specs/001-consolidated-showcase/spec.md`
- **Implementation Plan**: `/home/jian/Work/personal/flowbite-htmy/specs/001-consolidated-showcase/plan.md`

---

## Support

If you encounter issues:
1. Check this quickstart guide first
2. Review troubleshooting section above
3. Check git commit history for recent changes
4. File an issue in the project repository
