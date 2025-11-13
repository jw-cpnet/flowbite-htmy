# Implementation Plan: Consolidated Component Showcase Application

**Branch**: `001-consolidated-showcase` | **Date**: 2025-11-13 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-consolidated-showcase/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Consolidate 10 standalone component showcase applications into a single multi-page FastAPI application with navigation. The application will use the hybrid Jinja + htmy architecture to provide unified access to all component examples through a persistent navigation menu. Each component will have its own route (`/buttons`, `/badges`, etc.) and all existing showcase content will be preserved. The navigation menu will be built using flowbite-htmy components, demonstrating real-world usage of the library.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI 0.104.0+, fasthx 0.1.0+, htmy 0.1.0+, Jinja2 3.1+, flowbite-htmy (current), uvicorn (ASGI server)
**Storage**: N/A (showcase application, no data persistence)
**Testing**: Manual E2E testing with Chrome DevTools (no new unit tests - showcases existing tested components)
**Target Platform**: Local development server (localhost:8000)
**Project Type**: Single web application (examples showcase)
**Performance Goals**: Page load < 1 second, app startup < 3 seconds, navigation transition < 500ms
**Constraints**: Must preserve all existing showcase content, must use hybrid Jinja + htmy pattern, must use existing components for navigation
**Scale/Scope**: 10 component pages, 1 main app file, 1-2 Jinja templates, ~500-1000 lines total

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify this feature plan complies with constitution principles (`.specify/memory/constitution.md`):

- **TDD Compliance**: ✅ EXEMPT - This is a showcase/example application that demonstrates already-tested components. No new components being created. Existing components have >90% test coverage. Manual E2E testing sufficient for showcase functionality.

- **Type Safety**: ✅ COMPLIANT - FastAPI routes will have type hints for return types. Template variables will be typed dicts. No new component logic requires type coverage.

- **Component Value**: ✅ COMPLIANT - No new components being created. Navigation menu will use existing Button or Badge components, demonstrating their value in real-world usage.

- **Architecture**: ✅ COMPLIANT - Plan explicitly uses hybrid Jinja + htmy pattern: Jinja templates for layout/navigation structure, htmy components for UI elements, fasthx for integration.

- **Quality Gates**: ✅ COMPLIANT - Code will be formatted with ruff, type-checked where applicable. Manual testing will verify all showcase functionality works correctly.

**Summary**: All principles compliant or appropriately exempted. No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-consolidated-showcase/
├── plan.md              # This file (/speckit.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0: Navigation patterns and route organization
├── data-model.md        # Phase 1: Route and navigation data structures
├── quickstart.md        # Phase 1: Developer guide for running consolidated app
├── contracts/           # Phase 1: Route definitions and navigation API
└── checklists/          # Quality validation checklists
    └── requirements.md  # Spec quality checklist (completed)
```

### Source Code (repository root)

```text
examples/
├── showcase.py          # NEW: Main consolidated application file
├── templates/
│   ├── base.html.jinja       # EXISTING: Base layout (may need updates)
│   └── showcase-layout.html.jinja  # NEW: Layout with persistent navigation
├── buttons.py           # EXISTING: Keep for reference/comparison
├── badges.py            # EXISTING: Keep for reference/comparison
├── alerts.py            # EXISTING: Keep for reference/comparison
├── avatars.py           # EXISTING: Keep for reference/comparison
├── cards.py             # EXISTING: Keep for reference/comparison
├── checkboxes.py        # EXISTING: Keep for reference/comparison
├── inputs.py            # EXISTING: Keep for reference/comparison
├── modals.py            # EXISTING: Keep for reference/comparison
├── paginations.py       # EXISTING: Keep for reference/comparison
└── selects.py           # EXISTING: Keep for reference/comparison

.vscode/
└── launch.json          # UPDATE: Add consolidated showcase debug config
```

**Structure Decision**: Single project structure. The consolidated app (`examples/showcase.py`) will be a new FastAPI application that imports and reuses the showcase content generation logic from existing apps. All showcase rendering functions can be extracted into reusable functions and called from different routes. The original 10 standalone apps will be kept for comparison but marked as deprecated in favor of the consolidated app.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations. All principles are compliant or appropriately exempted (TDD exemption justified for showcase application).

---

## Phase 0: Research & Navigation Patterns

### Research Topics

1. **FastAPI Multi-Page Application Patterns**
   - Research: How to structure FastAPI app with multiple page routes
   - Research: Best practices for route organization and URL patterns
   - Decision needed: Use `@app.get("/buttons")` for each component or dynamic routing

2. **Navigation Menu Implementation**
   - Research: Which flowbite-htmy components best suit navigation (Button, Badge, or combination)
   - Research: How to indicate active page in navigation menu
   - Decision needed: Sidebar navigation vs top bar vs both

3. **Content Reuse Strategy**
   - Research: How to extract showcase content from existing apps into reusable functions
   - Research: Whether to keep showcase generation in existing files or move to new module
   - Decision needed: Monolithic showcase.py vs modular approach with imports

4. **Template Organization**
   - Research: Whether to extend existing base.html.jinja or create new template
   - Research: How to pass current page/route info to template for active navigation
   - Decision needed: Template inheritance structure

### Research Output

Results will be documented in `research.md` covering:
- Recommended FastAPI route structure (explicit routes vs dynamic)
- Navigation component choice and implementation approach
- Content extraction and reuse strategy
- Template organization and inheritance pattern
- Performance considerations for multi-page app

---

## Phase 1: Design & Contracts

### Data Models

Will be documented in `data-model.md`:

1. **ComponentRoute**
   - Attributes: name (str), path (str), title (str), icon (optional), order (int)
   - Purpose: Define each component showcase page route
   - Example: `{ name: "buttons", path: "/buttons", title: "Buttons", icon: None, order: 1 }`

2. **NavigationItem**
   - Attributes: label (str), url (str), is_active (bool), badge (optional str)
   - Purpose: Represent navigation menu items with state
   - Example: `{ label: "Buttons", url: "/buttons", is_active: True, badge: "10 examples" }`

3. **ShowcaseSection**
   - Attributes: title (str), description (str), content (Component), order (int)
   - Purpose: Logical grouping of examples within a component page
   - Example: `{ title: "Default Buttons", description: "Basic button styles...", content: html.div(...), order: 1 }`

### API Contracts

Will be documented in `contracts/routes.md`:

```
GET /
  Description: Homepage with welcome message and navigation to all components
  Response: HTML page with navigation menu and component gallery

GET /buttons
  Description: Button component showcase page
  Response: HTML page with all button examples

GET /badges
  Description: Badge component showcase page
  Response: HTML page with all badge examples

... (repeat for all 10 components)

GET /api/components
  Description: JSON endpoint listing all available component routes (optional)
  Response: { "components": [{ "name": "buttons", "path": "/buttons", "title": "Buttons" }, ...] }
```

### Quickstart Guide

Will be documented in `quickstart.md`:

```markdown
# Running the Consolidated Showcase

## Quick Start

1. Activate virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Run the consolidated showcase:
   ```bash
   python examples/showcase.py
   ```

3. Open browser to http://localhost:8000

4. Navigate between component pages using the menu

## Available Pages

- / - Homepage with component gallery
- /buttons - Button showcase
- /badges - Badge showcase
- /alerts - Alert showcase
- /avatars - Avatar showcase
- /cards - Card showcase
- /checkboxes - Checkbox showcase
- /inputs - Input showcase
- /modals - Modal showcase
- /paginations - Pagination showcase
- /selects - Select showcase

## Development

Toggle dark mode using the button in the top-right corner (state persists across pages).

Navigate using browser back/forward buttons (fully supported).

Bookmark any component page for direct access.
```

---

## Phase 2: Task Generation (NOT DONE BY THIS COMMAND)

Task generation will be handled by `/speckit.tasks` command after this planning phase is complete.

Expected task structure:
- Phase 1: Setup (create new files, update templates)
- Phase 2: Extract showcase content from existing apps
- Phase 3: Build navigation component
- Phase 4: Create consolidated routes
- Phase 5: Testing and refinement

---

## Next Steps

After this plan is approved:

1. **Review research.md** - Validate technology choices and patterns
2. **Review data-model.md** - Confirm data structures meet requirements
3. **Review contracts/routes.md** - Verify route definitions are complete
4. **Review quickstart.md** - Ensure developer experience is clear
5. **Run `/speckit.tasks`** - Generate implementation task list
6. **Run `/speckit.implement`** - Execute implementation

---

## Notes

- Original 10 showcase apps will be kept but marked as deprecated
- VS Code launch.json will be updated with new consolidated app debug config
- Dark mode toggle state persistence may require localStorage or cookies (research in Phase 0)
- Navigation menu could use HTMX for client-side routing (optional enhancement)
- Consider adding search/filter functionality in future iteration (out of scope for MVP)
