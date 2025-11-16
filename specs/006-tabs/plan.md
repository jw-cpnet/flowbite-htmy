# Implementation Plan: Tabs Component

**Branch**: `006-tabs` | **Date**: 2025-01-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/006-tabs/spec.md`

## Summary

Implement a Tabs component for flowbite-htmy that provides tabbed navigation with multiple visual variants (default, underline, pills, full-width), full ARIA accessibility support, Flowbite JavaScript integration for keyboard navigation, HTMX lazy loading capabilities, and comprehensive icon positioning. The component will follow the class-based dataclass pattern with frozen, keyword-only arguments, implement the htmy() method for rendering, and achieve 90%+ test coverage through strict TDD.

**Primary Requirements**:
- Tab and Tabs dataclasses with 18 functional requirements
- 4 visual variants (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH)
- Full ARIA support (role="tablist", role="tab", role="tabpanel", aria-selected, aria-controls)
- Flowbite JavaScript integration for tab switching and keyboard navigation (arrow keys, Enter/Space)
- HTMX attribute support for lazy loading (hx-get, hx-post, hx-trigger, hx-target, hx-swap)
- Icon support with left/right positioning
- Disabled tab state with visual and functional restrictions
- Dark mode classes always included
- Color customization (8 color options)
- Unique ID generation for tab/panel associations

**Technical Approach** (from Phase 0 research):
- Research Flowbite tabs classes from flowbite-llms-full.txt for pixel-perfect implementation
- Study W3C ARIA Authoring Practices for tabs pattern compliance
- Investigate Flowbite JavaScript tabs API for data attribute requirements
- Analyze HTMX event coexistence patterns with Flowbite tab switching
- Define Tab and Tabs dataclasses with comprehensive prop coverage
- Use ClassBuilder for variant-specific class construction
- Implement unique ID generation using Python id(self) with custom override support

## Technical Context

**Language/Version**: Python 3.11+ (existing project requirement)
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Icon system (get_icon()), Color enum, Flowbite CSS 2.5.1, Flowbite JavaScript, HTMX 2.0.2
**Storage**: N/A (stateless UI component library)
**Testing**: pytest with async support (@pytest.mark.asyncio for htmy rendering), syrupy for snapshot testing
**Target Platform**: Server-side rendering for web applications (FastAPI + fasthx integration)
**Project Type**: Single project (Python library)
**Performance Goals**: Component rendering <10ms, HTMX lazy loading without blocking UI
**Constraints**: Must achieve 90%+ test coverage, 100% type coverage (mypy strict), pixel-perfect alignment with Flowbite reference implementation
**Scale/Scope**: Single component with 5 user stories, 18 functional requirements, 4 variants, estimated 20+ unit tests

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Verification** (against `.specify/memory/constitution.md`):

✅ **TDD Compliance**:
- Plan includes strict test-first approach with Red-Green-Refactor cycle
- All user stories have acceptance scenarios that translate to tests
- Tests written before implementation (explicitly stated in spec)
- Test coverage goal: 90%+ (exceeds constitution requirement)

✅ **Type Safety**:
- Plan specifies @dataclass(frozen=True, kw_only=True) pattern
- All props will have explicit type hints (str, Component | None, Icon | None, bool, Color, TabVariant, IconPosition)
- mypy strict mode compliance required (100% type coverage)
- Type-driven design using enums (TabVariant, IconPosition, Color)

✅ **Component Value**:
- Tabs component provides genuine convenience (replaces 50+ lines of repetitive HTML/ARIA with 5-10 line component usage)
- Enforces consistent patterns (ARIA attributes, unique IDs, keyboard navigation)
- Handles complex logic (variant classes, disabled states, HTMX integration, Flowbite JS data attributes)
- Provides type safety (TabVariant enum prevents invalid variants, Color enum ensures valid colors)
- Showcase will demonstrate component value with all 4 variants and HTMX integration

**Component Value Validation**:
- ❌ NOT just a wrapper around a single `<div>` - manages tablist container + multiple tab buttons + multiple panels
- ❌ NOT forcing verbose HTML inside - users provide simple Tab objects, component handles all ARIA/Flowbite complexity
- ❌ NOT too generic - tabs have specific structure (buttons + panels) unlike generic containers
- ✅ Reduces boilerplate significantly (ARIA attributes, unique IDs, Flowbite data attributes, variant classes)
- ✅ Showcase examples will use the Tabs component directly (not bypass with raw HTML)

✅ **Architecture**:
- Follows hybrid Jinja + htmy pattern correctly
- Tabs is an htmy component (Python dataclass with htmy() method)
- Showcase uses Jinja template for page layout, Tabs component for UI element
- No JavaScript escaping issues (icons via get_icon() helper, no inline JS in component)

✅ **Quality Gates**:
- Coverage: 90%+ test coverage goal (constitution requires >90%)
- Type coverage: 100% mypy strict (constitution requires 100%)
- Linting: All ruff checks must pass (constitution requirement)
- Formatting: ruff format applied (constitution requirement)
- Line length: 100 chars max (constitution standard)

**Constitution Compliance**: ✅ ALL PRINCIPLES SATISFIED

## Project Structure

### Documentation (this feature)

```text
specs/006-tabs/
├── spec.md              # Feature specification (/speckit.specify output)
├── plan.md              # This file (/speckit.plan output)
├── research.md          # Phase 0: Flowbite classes, ARIA patterns, HTMX integration
├── data-model.md        # Phase 1: Tab and Tabs entity definitions
├── quickstart.md        # Phase 1: TDD workflow guide for implementation
├── contracts/
│   └── tabs-api.md      # Phase 1: Component API contract (props, rendering, examples)
├── checklists/
│   └── requirements.md  # Spec validation checklist (created by /speckit.specify)
└── tasks.md             # Phase 2: Task breakdown (NOT created by /speckit.plan, created by /speckit.tasks)
```

### Source Code (repository root)

```text
# Single project structure (Python library)
src/flowbite_htmy/
├── components/
│   ├── __init__.py          # Export Tab, Tabs, TabVariant, IconPosition
│   └── tabs.py              # Tab and Tabs dataclass implementations (NEW)
├── types/
│   ├── __init__.py
│   └── color.py             # Color enum (existing)
├── base/
│   ├── classes.py           # ClassBuilder (existing)
│   └── context.py           # ThemeContext (existing)
└── icons.py                 # get_icon() helper (existing)

tests/
├── conftest.py              # Fixtures: renderer, context, dark_context (existing)
└── test_components/
    └── test_tabs.py         # Tabs component tests (NEW, 20+ tests)

examples/
├── tabs.py                  # Tabs showcase app (NEW)
└── showcase.py              # Consolidated showcase (UPDATE - add tabs route)
```

**Structure Decision**: Using single project structure (Option 1) as flowbite-htmy is a Python library with components in `src/flowbite_htmy/components/`, tests in `tests/test_components/`, and showcase examples in `examples/`. This aligns with the existing project structure established in Phase 1 components (Button, Badge, Alert, Avatar) and Phase 2 components (Modal, Input, Select, Pagination, Checkbox, Radio, Textarea, Toast, Accordion).

## Complexity Tracking

**No constitution violations** - This section is empty as all constitution principles are satisfied.

---

# Phase 0: Outline & Research

## Research Tasks

1. **Flowbite Tabs Classes**: Extract exact Tailwind CSS classes for all 4 tab variants (default, underline, pills, full-width) from flowbite-llms-full.txt
2. **ARIA Tabs Pattern**: Research W3C ARIA Authoring Practices for tabs, including required roles, states, and keyboard interaction
3. **Flowbite JavaScript Integration**: Investigate Flowbite's tabs JavaScript API, required data attributes (data-tabs-toggle, data-tabs-target), and initialization requirements
4. **HTMX Event Coexistence**: Research how HTMX events interact with Flowbite tab switching, including event timing and conflicts
5. **Icon Positioning Patterns**: Analyze icon placement patterns in existing components (Button, Badge) for consistent implementation
6. **Unique ID Generation**: Research ID collision avoidance strategies for tab/panel associations in server-side rendering
7. **Disabled Tab Behavior**: Investigate Flowbite's disabled tab handling and ARIA aria-disabled vs disabled attribute patterns

## Research Output

See [research.md](./research.md) for consolidated findings, decisions, and rationale.

---

# Phase 1: Design & Contracts

## Design Artifacts

1. **Data Model** ([data-model.md](./data-model.md)):
   - Tab entity: label, content, icon, icon_position, disabled, is_active, HTMX attributes, class_
   - Tabs entity: tabs list, variant, color, tabs_id, class_
   - TabVariant enum: DEFAULT, UNDERLINE, PILLS, FULL_WIDTH
   - IconPosition enum: LEFT, RIGHT

2. **API Contracts** ([contracts/tabs-api.md](./contracts/tabs-api.md)):
   - Tab dataclass API specification
   - Tabs dataclass API specification
   - Rendering examples for all variants
   - HTMX integration examples
   - Icon positioning examples

3. **Quickstart Guide** ([quickstart.md](./quickstart.md)):
   - TDD workflow for Tabs implementation
   - Test structure and organization (20+ tests)
   - Example test cases for each user story
   - Implementation checklist

## Agent Context Update

After Phase 1 completion, run:
```bash
.specify/scripts/bash/update-agent-context.sh claude
```

This updates `CLAUDE.md` with new technologies from this plan while preserving manual additions.

---

# Phase 2: Planning Complete

This command (`/speckit.plan`) ends here. Next steps:

1. **Review Phase 0 research.md** - Validate technical decisions
2. **Review Phase 1 artifacts** - Ensure data model and contracts are complete
3. **Run `/speckit.tasks`** - Generate task breakdown for implementation
4. **Run `/speckit.implement`** - Execute tasks following TDD workflow
