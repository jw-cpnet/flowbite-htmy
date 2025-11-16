# Implementation Plan: Accordion Component

**Branch**: `005-accordion` | **Date**: 2025-11-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/005-accordion/spec.md`

## Summary

Implement an Accordion component (Phase 2C, rank #6) that provides collapsible panel functionality with proper ARIA attributes, keyboard navigation, Flowbite JavaScript integration, and HTMX support. The component significantly reduces boilerplate (50+ lines of HTML to ~10 lines of Python) while enforcing consistent patterns for FAQ sections, documentation, and content organization. Technical approach follows established class-based component pattern with automatic ID generation, comprehensive ARIA attribute management, and seamless integration between Flowbite JavaScript and HTMX event system.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Flowbite CSS 2.5.1, Flowbite JavaScript (initAccordions), HTMX 2.0.2
**Storage**: N/A (stateless UI component)
**Testing**: pytest with asyncio, syrupy (snapshot testing), coverage >90%
**Target Platform**: Web (server-side rendered HTML with client-side JavaScript)
**Project Type**: Single project (Python component library)
**Performance Goals**: Component renders <10ms, generates unique IDs in O(n) time
**Constraints**: Must integrate with Flowbite JavaScript without conflicts, HTMX events must coexist with collapse behavior
**Scale/Scope**: Support 1-20 panels per accordion, handle nested accordions, WCAG 2.1 AA compliance

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

✅ **TDD Compliance**: Plan includes test-first approach with tests written before implementation. Each feature (basic accordion, variants, HTMX) has corresponding test suite created first.

✅ **Type Safety**: Plan requires complete type annotations (Panel dataclass, Accordion component props), mypy strict mode validation, type-driven design with enums for variants and modes.

✅ **Component Value**: Accordion passes value validation criteria:
- ✅ Provides genuine convenience (reduces 50+ lines of HTML to ~10 lines Python)
- ✅ Enforces consistent patterns (ARIA attributes, Flowbite classes, ID generation)
- ✅ Handles complex logic internally (unique ID generation, ARIA relationships, JavaScript initialization)
- ✅ Provides type safety (AccordionMode enum, AccordionVariant enum, Panel dataclass)
- ✅ Showcase will use the component (FAQ section, documentation sections)

✅ **Architecture**: Follows hybrid Jinja + htmy pattern correctly:
- Component uses class-based pattern with `@dataclass(frozen=True, kw_only=True)`
- Implements `htmy(self, context: Context) -> Component` method
- No layout concerns (those remain in Jinja templates)

✅ **Quality Gates**: Coverage >90%, mypy strict mode, ruff linting and formatting, all tests passing

**Status**: ✅ All constitution principles satisfied, no violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/005-accordion/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (ARIA patterns, Flowbite integration)
├── data-model.md        # Phase 1 output (Accordion, Panel entities)
├── quickstart.md        # Phase 1 output (TDD workflow guide)
├── contracts/           # Phase 1 output (component API contract)
└── checklists/
    └── requirements.md  # Spec validation checklist (complete)
```

### Source Code (repository root)

```text
src/flowbite_htmy/
├── components/
│   ├── __init__.py         # Export Accordion
│   └── accordion.py        # Accordion component implementation
├── base/
│   ├── classes.py          # ClassBuilder (existing)
│   └── context.py          # ThemeContext (existing)
└── types/
    ├── __init__.py
    ├── color.py            # Color enum (existing)
    └── size.py             # Size enum (existing)

tests/
├── conftest.py             # Fixtures: renderer, context, dark_context
└── test_components/
    └── test_accordion.py   # Accordion test suite (TDD)

examples/
├── templates/
│   └── showcase-layout.html.jinja  # Base layout (existing)
└── showcase.py             # Add accordion section
```

**Structure Decision**: Single project structure (Option 1). Component follows established pattern in `src/flowbite_htmy/components/` with tests in `tests/test_components/`. No new directories needed - fits cleanly into existing structure.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations to justify - all constitution principles are satisfied.

## Phase 0: Research & Technical Discovery

**Objective**: Resolve all technical unknowns and establish patterns for implementation.

### Research Tasks

1. **ARIA Accordion Pattern** (W3C WAI-ARIA Authoring Practices)
   - Required attributes: `aria-expanded`, `aria-controls`, `aria-labelledby`
   - Button vs h2+button structure
   - Keyboard navigation requirements (Tab, Enter, Space, Arrow keys)
   - Focus management on expand/collapse

2. **Flowbite Accordion Implementation** (flowbite-llms-full.txt)
   - HTML structure: `div[data-accordion]` → `h2` → `button[data-accordion-target]` → `div[aria-labelledby]`
   - JavaScript initialization: `initAccordions()` function
   - Data attributes: `data-accordion="collapse|open"`, `data-accordion-target="#id"`
   - Class patterns: Default vs flush variants
   - Icon rotation: `rotate-180` transform on expand

3. **Flowbite + HTMX Integration Pattern**
   - Event coexistence: Flowbite click handlers vs HTMX triggers
   - Re-initialization after HTMX swap: `htmx:afterSwap` event
   - Content loading patterns: `hx-get` on panel body vs header
   - Preventing event conflicts: Event bubbling and stopPropagation

4. **Unique ID Generation Strategy**
   - Pattern: `accordion-{component_id}-panel-{index}`
   - Component ID source: Python `id()` function or custom counter
   - Collision avoidance for nested accordions
   - Accessibility requirements: IDs must be unique per page

5. **Icon System Integration**
   - Default chevron icon from existing Icon enum
   - Custom icon support: Accept Component (htmy SVG component)
   - Icon rotation CSS: `transition-transform` + `rotate-180`
   - Dark mode icon colors

**Output**: `research.md` with decisions, rationale, and code examples for each topic.

## Phase 1: Data Model & Contracts

**Prerequisites**: Phase 0 research complete

### Data Model (`data-model.md`)

**Entities**:

1. **Accordion** (Component)
   - `panels: list[Panel]` - Collection of accordion panels
   - `mode: AccordionMode = AccordionMode.COLLAPSE` - Collapse (single) or always-open (multiple)
   - `variant: AccordionVariant = AccordionVariant.DEFAULT` - Default or flush styling
   - `color: Color = Color.PRIMARY` - Header background color
   - `class_: str = ""` - Custom CSS classes
   - `accordion_id: str | None = None` - Custom ID (auto-generated if None)

2. **Panel** (Data Class)
   - `title: str` - Panel header text
   - `content: str | Component` - Panel body content (string or htmy component)
   - `is_open: bool = False` - Default expanded state
   - `icon: Component | None = None` - Custom expand/collapse icon
   - `hx_get: str | None = None` - HTMX GET endpoint for lazy loading
   - `hx_trigger: str = "revealed"` - HTMX trigger event
   - `class_: str = ""` - Custom panel CSS classes

3. **AccordionMode** (Enum)
   - `COLLAPSE = "collapse"` - Only one panel open at a time
   - `ALWAYS_OPEN = "open"` - Multiple panels can be open

4. **AccordionVariant** (Enum)
   - `DEFAULT = "default"` - Standard bordered accordion
   - `FLUSH = "flush"` - No borders, flush with container

### Component API Contract (`contracts/accordion-api.md`)

**Constructor Signature**:
```python
@dataclass(frozen=True, kw_only=True)
class Accordion:
    panels: list[Panel]
    mode: AccordionMode = AccordionMode.COLLAPSE
    variant: AccordionVariant = AccordionVariant.DEFAULT
    color: Color = Color.PRIMARY
    class_: str = ""
    accordion_id: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render accordion with all panels."""
        ...
```

**Rendering Contract**:
- **Input**: Accordion instance with 1+ panels
- **Output**: HTML `<div>` with `data-accordion` attribute, containing `<h2>` → `<button>` → `<div>` structure per panel
- **Guarantees**:
  - Unique IDs generated for each panel
  - All ARIA attributes present and correctly linked
  - Flowbite classes applied per variant
  - Dark mode classes always included
  - HTMX attributes passed through to panel bodies

**Example Usage**:
```python
accordion = Accordion(
    panels=[
        Panel(title="What is Flowbite?", content="Flowbite is..."),
        Panel(title="How to install?", content="Run pip install...", is_open=True),
    ],
    mode=AccordionMode.COLLAPSE,
    variant=AccordionVariant.DEFAULT,
)
```

### TDD Quickstart (`quickstart.md`)

**Test-First Workflow** for Accordion component:

1. **Phase 1: Basic Structure** (P1 - Basic Accordion Creation)
   - Test 1: Accordion renders with default mode and variant
   - Test 2: Unique IDs generated for each panel
   - Test 3: ARIA attributes present (aria-expanded, aria-controls, aria-labelledby)
   - Test 4: Flowbite classes applied to container
   - Test 5: data-accordion attribute set correctly

2. **Phase 2: Variants & Customization** (P2 - Accordion Customization)
   - Test 6: Flush variant removes borders
   - Test 7: Color prop applies header background classes
   - Test 8: Dark mode classes always included
   - Test 9: Always-open mode sets data-accordion="open"
   - Test 10: Custom icons replace default chevron

3. **Phase 3: HTMX Integration** (P3 - HTMX Integration)
   - Test 11: hx-get attribute renders on panel body
   - Test 12: hx-trigger attribute configurable
   - Test 13: Multiple HTMX attributes supported (hx-swap, hx-target)

4. **Phase 4: Edge Cases**
   - Test 14: Single panel accordion works correctly
   - Test 15: Empty content panels render
   - Test 16: Invalid default open index ignored
   - Test 17: Custom class_ merges with component classes

### Agent Context Update

**Script**: `.specify/scripts/bash/update-agent-context.sh claude`

**Technology Additions** (to Active Technologies section):
- Python 3.11+ + htmy 0.1.0+, ClassBuilder, ThemeContext, Flowbite CSS 2.5.1, Flowbite JavaScript (initAccordions), HTMX 2.0.2 (005-accordion)
- N/A (stateless UI component) (005-accordion)

**Output**: Updated `.specify/memory/context_claude.md` with new accordion component technology.

## Phase 2: Task Generation (Future)

**Note**: Phase 2 task generation is handled by the `/speckit.tasks` command (NOT part of `/speckit.plan`).

The tasks command will generate `tasks.md` with dependency-ordered implementation tasks based on this plan, the data model, and contracts.

Expected task structure:
1. Setup phase (create test file, import dependencies)
2. Basic accordion tests (TDD - write tests first)
3. Basic accordion implementation (make tests pass)
4. Variant tests and implementation
5. HTMX integration tests and implementation
6. Edge case tests and implementation
7. Showcase integration
8. Documentation updates

## Post-Design Constitution Re-Check

*Re-evaluate constitution compliance after Phase 1 design is complete.*

✅ **TDD Compliance**: Quickstart defines clear test-first workflow with 17 tests across 4 phases. Each test written before implementation.

✅ **Type Safety**: Data model uses full type annotations:
- `panels: list[Panel]` (generic type)
- `mode: AccordionMode` (enum type)
- `content: str | Component` (union type)
- All props have explicit types with defaults

✅ **Component Value**: Accordion component value confirmed:
- Reduces 50+ lines HTML to ~10 lines Python (quantified)
- Enforces ARIA patterns (complex logic internal)
- Showcase will demonstrate value with FAQ section

✅ **Architecture**: Design follows hybrid pattern:
- Accordion is htmy component (not Jinja template)
- Class-based with dataclass pattern
- No layout responsibilities (only UI element)

✅ **Quality Gates**: Quickstart specifies >90% coverage requirement, 17 tests ensure comprehensive coverage, mypy strict mode enforced by project config.

**Final Status**: ✅ All constitution principles remain satisfied post-design.

## Artifacts Status

- [x] plan.md (this file)
- [x] research.md (Phase 0 - COMPLETE)
- [x] data-model.md (Phase 1 - COMPLETE)
- [x] contracts/accordion-api.md (Phase 1 - COMPLETE)
- [x] quickstart.md (Phase 1 - COMPLETE)
- [x] Agent context update (Phase 1 - COMPLETE)

**Planning Complete**: All Phase 0 and Phase 1 artifacts generated. Ready for `/speckit.tasks` command to generate implementation tasks.
