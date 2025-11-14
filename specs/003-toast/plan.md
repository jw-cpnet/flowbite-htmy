# Implementation Plan: Toast Component

**Branch**: `003-toast` | **Date**: 2025-11-14 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-toast/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a Toast notification component for temporary messages (success, danger, warning, info) with icon, color variant, dismissible close button, optional action buttons, and rich content support (avatars). The component will follow the established dataclass pattern, integrate with HTMX for server-side notifications, support Flowbite JavaScript dismiss functionality, and include comprehensive showcase with all Flowbite toast examples.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Icon system, Button component (optional), Avatar component (optional), Flowbite CSS 2.5.1, Flowbite JavaScript (optional)
**Storage**: N/A (stateless UI component)
**Testing**: pytest with asyncio support, syrupy for snapshot testing
**Target Platform**: Server-side rendering (FastAPI + htmy + Jinja2)
**Project Type**: Single library project (UI component library)
**Performance Goals**: Component render time <5ms for simple toasts, <15ms for rich content toasts
**Constraints**: Max-width 320px (max-w-xs), must support HTMX responses, must not require JavaScript for basic rendering
**Scale/Scope**: Single component with 4 variants, comprehensive test suite (22+ tests estimated), showcase with 6+ examples

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify this feature plan complies with constitution principles (`.specify/memory/constitution.md`):

- ✅ **TDD Compliance**: Yes - Plan follows strict Red-Green-Refactor cycle. All tests will be written before implementation for each user story.
- ✅ **Type Safety**: Yes - Component will use dataclass with type hints, mypy strict mode enforcement, Color/Size enums for type safety.
- ✅ **Component Value**: Yes - Toast passes value validation:
  - Provides genuine convenience (reduces 30+ lines to 5 lines)
  - Enforces consistent patterns (4 variants with proper icons/colors)
  - Handles complex logic (icon positioning, dismiss button, ARIA attributes, dark mode)
  - Provides type safety (ToastVariant enum)
  - Showcase will use the component for all examples (not bypass it)
- ✅ **Architecture**: Yes - Follows hybrid Jinja + htmy pattern. Toast is an htmy component (not Jinja layout). Uses dataclass pattern with htmy() method.
- ✅ **Quality Gates**: Yes - Plan includes 95%+ coverage requirement, mypy strict mode, ruff linting, and formatting checks.

**Result**: ✅ All constitution principles satisfied. No violations. Proceed to Phase 0.

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
│   ├── __init__.py         # Export Toast
│   └── toast.py            # NEW: Toast component implementation
├── types/
│   ├── __init__.py         # Export ToastVariant
│   └── toast.py            # NEW: ToastVariant enum
├── base/
│   ├── classes.py          # ClassBuilder (existing)
│   └── context.py          # ThemeContext (existing)
└── icons.py                # Icon system (existing)

tests/
└── test_components/
    └── test_toast.py       # NEW: Toast component tests (22+ tests)

examples/
├── showcase.py             # Existing consolidated showcase
├── toasts.py               # NEW: Toast showcase content function
└── templates/
    └── showcase-layout.html.jinja  # Existing layout template
```

**Structure Decision**: Single library project structure. Toast component follows established pattern in `src/flowbite_htmy/components/`. New ToastVariant enum in `src/flowbite_htmy/types/` (similar to ValidationState, ButtonVariant). Tests mirror source structure. Showcase function in `examples/toasts.py` following consolidated pattern (Radio, Textarea precedent).

## Complexity Tracking

**No constitution violations** - This section is empty as all principles are satisfied.
