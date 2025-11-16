# Implementation Plan: Dropdown Component

**Branch**: `007-dropdown` | **Date**: 2025-11-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/007-dropdown/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a toggleable dropdown menu component with Flowbite CSS styling and JavaScript integration. The component supports multiple trigger types (button, avatar, text), customization options (colors, icons, dividers, headers), positioning (top/bottom/left/right), HTMX integration for dynamic content, and multi-level nested dropdowns. Full ARIA accessibility and keyboard navigation are mandatory. The implementation follows the hybrid Jinja + htmy pattern with strict TDD, targeting >90% test coverage.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Icon system, Flowbite CSS 2.5.1, Flowbite JavaScript, HTMX 2.0.2
**Storage**: N/A (stateless UI component)
**Testing**: pytest with asyncio support, syrupy for snapshot testing
**Target Platform**: Web (server-side rendering with FastAPI + fasthx)
**Project Type**: Single project (Python library)
**Performance Goals**: Component rendering <10ms, click response <100ms (Flowbite JS handles animations)
**Constraints**: >90% test coverage, 100% type coverage (mypy strict), Flowbite CSS 2.5.1 compatibility
**Scale/Scope**: Single component with 9 entity types (Dropdown + 8 supporting classes/enums)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify this feature plan complies with constitution principles (`.specify/memory/constitution.md`):

- ✅ **TDD Compliance**: Yes - Plan explicitly includes test-first workflow with tests written before implementation (Phase 2 tasks will enforce Red-Green-Refactor cycle)
- ✅ **Type Safety**: Yes - All entity classes will use full type hints, target 100% mypy strict coverage, leverage type system for domain modeling (enums for Placement, TriggerType, TriggerMode)
- ✅ **Component Value**: Yes - Dropdown passes value validation:
  - Provides genuine convenience: Reduces boilerplate for toggleable menus with ARIA, positioning, and Flowbite JS integration
  - Enforces consistent patterns: Standardizes trigger types, positioning, and accessibility attributes
  - Handles complex logic internally: ARIA relationships, unique ID generation, Flowbite data attributes, event handling
  - Provides type safety: DropdownPlacement, DropdownTriggerType, DropdownTriggerMode enums
  - Showcase will use the component: examples/dropdowns.py will demonstrate all features
- ✅ **Architecture**: Yes - Follows hybrid Jinja + htmy pattern:
  - htmy components for type-safe dropdown structure (Python dataclasses)
  - Jinja template for showcase page layout (examples/dropdowns.py uses fasthx + Jinja)
  - No pure htmy layout components (respects architecture principle IV)
- ✅ **Quality Gates**: Yes - Explicitly includes >90% coverage requirement, mypy strict validation, ruff linting/formatting

**Result**: ✅ All constitution principles satisfied. No violations to document.

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
│   ├── dropdown.py          # NEW: Dropdown, DropdownItem, DropdownHeader, DropdownDivider classes
│   └── __init__.py          # UPDATE: Export new dropdown classes and enums
├── types/
│   └── __init__.py          # UPDATE: Export DropdownPlacement, DropdownTriggerType, DropdownTriggerMode
├── base/
│   ├── classes.py           # EXISTING: ClassBuilder for Tailwind class construction
│   └── context.py           # EXISTING: ThemeContext for dark mode
└── icons.py                 # EXISTING: Icon system for menu item icons

tests/test_components/
└── test_dropdown.py         # NEW: Comprehensive tests for dropdown component

examples/
├── dropdowns.py             # NEW: Showcase application demonstrating dropdown features
├── templates/
│   └── dropdowns.html.jinja # NEW: Jinja template for dropdown showcase
└── showcase.py              # UPDATE: Add dropdown route to consolidated showcase
```

**Structure Decision**: Single project structure (Option 1). This is a Python library component following established patterns from previous components (Accordion, Tabs, Toast). Component code lives in `src/flowbite_htmy/components/`, tests in `tests/test_components/`, and showcase in `examples/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - No constitution violations. All principles satisfied.

---

## Phase 0: Research ✅ COMPLETE

**Output**: `research.md` (6 research questions resolved)

**Key Decisions**:
- Use Flowbite JavaScript with data attributes for positioning and animations
- Implement WAI-ARIA Menu Button pattern for accessibility
- Use nested Dropdown composition for multi-level menus
- Extract Flowbite CSS classes from documentation
- Place HTMX attributes on menu items (not trigger) to avoid event conflicts
- Focus on WCAG 2.1 AA compliance (basic keyboard navigation)

**Technologies Validated**:
- Flowbite JavaScript (Dropdown class with Popper.js)
- ARIA patterns (Menu Button with keyboard navigation)
- HTMX integration strategy (coexistence with Flowbite)

---

## Phase 1: Design & Contracts ✅ COMPLETE

**Artifacts Generated**:
1. `data-model.md` - 9 entity definitions with relationships
2. `contracts/dropdown-api.md` - Component interfaces and usage contracts
3. `quickstart.md` - TDD implementation workflow guide
4. `CLAUDE.md` - Updated with Dropdown component technologies

**Entity Summary**:
- 3 Enums: DropdownPlacement, DropdownTriggerType, DropdownTriggerMode
- 4 Classes: DropdownDivider, DropdownHeader, DropdownItem, Dropdown
- 2 Imported: Color, Size (existing enums)

**Key Design Decisions**:
- Class-based components with `@dataclass(frozen=True, kw_only=True)`
- Unique ID generation using `id(self)` for ARIA relationships
- Dark mode classes always included (never conditional)
- HTMX attributes as optional props on DropdownItem
- Avatar and text triggers as alternative to button trigger

---

## Constitution Re-Check (Post-Design)

**Status**: ✅ All principles remain satisfied after design phase

- ✅ **TDD Compliance**: Quickstart guide documents strict Red-Green-Refactor workflow
- ✅ **Type Safety**: All entities fully typed with mypy-compatible signatures
- ✅ **Component Value**: Design validates component provides genuine value (reduces ARIA/Flowbite boilerplate)
- ✅ **Architecture**: Follows hybrid pattern (htmy components + Jinja showcase templates)
- ✅ **Quality Gates**: Testing checklist ensures >90% coverage, mypy strict, ruff clean

**No new violations introduced during design.**

---

## Next Steps

**Phase 2**: Task Generation

Run `/speckit.tasks` to generate dependency-ordered task breakdown from this plan.

**Phase 3**: Implementation

Run `/speckit.implement` to execute TDD implementation following the quickstart guide.

---

## Artifacts Summary

| Artifact | Status | Lines | Purpose |
|----------|--------|-------|---------|
| `spec.md` | ✅ Complete | 139 | Feature specification with 3 user stories |
| `plan.md` | ✅ Complete | ~200 | This file - implementation plan |
| `research.md` | ✅ Complete | 418 | Technical research resolving 6 questions |
| `data-model.md` | ✅ Complete | 547 | Entity definitions and relationships |
| `contracts/dropdown-api.md` | ✅ Complete | 794 | Component API contracts and usage examples |
| `quickstart.md` | ✅ Complete | 623 | TDD workflow guide with code examples |
| `checklists/requirements.md` | ✅ Complete | 67 | Spec quality validation checklist |
| `tasks.md` | ⏳ Not Yet Created | - | Task breakdown (Phase 2) |

**Total Planning Documentation**: 2,788 lines (excluding tasks.md)

---

## Estimated Complexity

**Component Size**: Medium-Large
- **Lines of Code**: ~400-500 (based on Accordion: 269 lines, Tabs: similar)
- **Test Count**: 20-25 tests (based on Accordion: 18 tests)
- **Entity Count**: 9 (3 enums + 4 classes + 2 imported)

**Implementation Time**: 1-2 sessions
- Phase 2 (Tasks): 15-30 minutes
- Phase 3 (Implementation): 2-4 hours with strict TDD

**Risk Factors**:
- Multi-level dropdown complexity (recursive composition)
- ARIA attribute correctness (extensive accessibility requirements)
- Flowbite JS integration testing (requires E2E verification)
- HTMX coexistence (event conflict prevention)
