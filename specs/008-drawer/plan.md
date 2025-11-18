# Implementation Plan: Drawer Component

**Branch**: `008-drawer` | **Date**: 2025-11-18 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/008-drawer/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a Drawer component - a flexible off-canvas panel that slides in from any edge of the screen (left, right, top, bottom). The drawer supports multiple use cases including navigation menus, contact forms, settings panels, and filtering interfaces. Core features include four placement options with transform animations, optional backdrop overlay, body scroll locking, focus trap for accessibility, edge/swipeable variant, and full HTMX integration for dynamic content loading. The component follows the dataclass pattern with DrawerPlacement enum and integrates with Flowbite JavaScript for animations and state management.

## Technical Context

**Language/Version**: Python 3.11+ (existing project requirement)
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Icon system (get_icon()), Flowbite CSS 2.5.1, Flowbite JavaScript 2.5.1, HTMX 2.0.2 (optional)
**Storage**: N/A (stateless UI component)
**Testing**: pytest with asyncio support, syrupy for snapshot testing, renderer/context fixtures from conftest.py
**Target Platform**: Web browsers (desktop and mobile) via FastAPI + Jinja2 + htmy rendering
**Project Type**: Single project (Python library for UI components)
**Performance Goals**: Animation completion within 300ms, focus trap activation immediate (<50ms), drawer rendering <100ms
**Constraints**: Must constrain to viewport with max-height, debounce clicks during 300ms animation, auto-close previous drawer when new one opens, support focus trap for accessibility
**Scale/Scope**: Single component with 4 placement variants, multiple content types (forms, navigation, arbitrary content), >90% test coverage target

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify this feature plan complies with constitution principles (`.specify/memory/constitution.md`):

- **TDD Compliance**: ✅ PASS - Plan follows Red-Green-Refactor cycle. Tests will be written first for all drawer functionality (placement variants, focus trap, overflow handling, HTMX integration). Test tasks precede implementation in task breakdown.

- **Type Safety**: ✅ PASS - Component uses `@dataclass(frozen=True, kw_only=True)` with full type hints. DrawerPlacement enum for type-safe positioning. All props typed (str, bool, DrawerPlacement, etc.). Will pass mypy strict mode with 100% type coverage.

- **Component Value**: ✅ PASS - Drawer passes value validation criteria:
  - Genuine convenience: Reduces complex HTML structure (container + backdrop + panel + close button + ARIA + data attributes) to single Python component
  - Enforces consistent patterns: Placement-specific transforms, focus trap, HTMX integration, Flowbite JS initialization
  - Handles complex logic: Focus management, viewport constraints, auto-close behavior, animation debouncing, scroll locking
  - Type safety: DrawerPlacement enum prevents invalid positioning
  - Showcase will use component to demonstrate form-within-drawer pattern and all placement variants

- **Architecture**: ✅ PASS - Follows hybrid Jinja + htmy pattern. Drawer is htmy component (Python dataclass). Showcase will use Jinja template for page layout with embedded drawer components. Uses fasthx for FastAPI integration. No pure htmy JavaScript issues.

- **Quality Gates**: ✅ PASS - Target >90% test coverage (pytest config enforced), mypy strict mode validation, ruff linting and formatting checks. All quality standards from constitution principle V will be met.

**Pre-Phase 0 Status**: ✅ ALL GATES PASSED - No constitution violations. Ready for Phase 0 research.

**Post-Phase 1 Re-Check**: ✅ ALL GATES PASSED
- TDD: ✅ research.md decisions support test-first (e.g., focus trap testable via ARIA, placement transforms testable via CSS classes)
- Type Safety: ✅ DrawerPlacement enum defined in data-model.md, all props fully typed in component API
- Component Value: ✅ research.md confirms complex logic (focus trap via Flowbite JS, viewport constraints, HTMX integration) justifies component
- Architecture: ✅ design follows hybrid pattern (htmy component, Jinja template for showcase, Flowbite JS for runtime)
- Quality Gates: ✅ quickstart.md and contract include testing guidance, >90% coverage target maintained

No design decisions violate constitution principles. Ready for Phase 2 (task generation via `/speckit.tasks`).

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/flowbite_htmy/
├── components/
│   ├── __init__.py          # Export Drawer
│   └── drawer.py            # Drawer component implementation
├── types/
│   ├── __init__.py          # Export DrawerPlacement enum
│   └── enums.py             # DrawerPlacement enum definition
├── base/
│   ├── classes.py           # ClassBuilder (existing)
│   └── context.py           # ThemeContext (existing)
├── icons/
│   └── __init__.py          # get_icon() for close button (existing)
└── __init__.py              # Version constants (existing)

tests/
├── conftest.py              # Fixtures: renderer, context, dark_context (existing)
└── test_components/
    └── test_drawer.py       # Drawer component tests (NEW)

examples/
└── drawers.py               # Showcase application (NEW)
```

**Structure Decision**: Single project structure (Option 1). This is a Python library for UI components, following the established flowbite-htmy architecture. The Drawer component will be added to `src/flowbite_htmy/components/` alongside existing components (Button, Badge, Alert, etc.). The DrawerPlacement enum will be added to `src/flowbite_htmy/types/enums.py` with other enums (Color, Size). Tests follow the existing pattern in `tests/test_components/`. A showcase example app will demonstrate drawer usage patterns.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations. This section intentionally left empty.
