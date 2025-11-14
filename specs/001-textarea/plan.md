# Implementation Plan: Textarea Component

**Branch**: `001-textarea` | **Date**: 2025-11-14 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-textarea/spec.md`

## Summary

Implement a Textarea component that provides multi-line text input with Flowbite styling, validation states (success/error), helper text, and full dark mode support. The component follows the established Input component pattern for consistency, supporting pre-filled values, configurable rows, required/disabled/readonly states, and HTMX integration. Implementation uses class-based dataclass pattern with strict TDD, targeting 95%+ test coverage.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: htmy 0.1.0+, ClassBuilder, ThemeContext, Flowbite CSS 2.5.1
**Storage**: N/A (stateless UI component)
**Testing**: pytest with asyncio support, syrupy for snapshot testing
**Target Platform**: Server-side rendering (FastAPI + htmy)
**Project Type**: Single project (Python library)
**Performance Goals**: Instant rendering (synchronous component construction, <1ms)
**Constraints**: 100% type coverage (mypy strict), >90% test coverage, follows Flowbite CSS class patterns
**Scale/Scope**: Single component (~200-250 lines), 20-25 tests, one showcase application

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify this feature plan complies with constitution principles (`.specify/memory/constitution.md`):

- ✅ **TDD Compliance**: Plan includes test-first approach. Tests will be written before implementation following Red-Green-Refactor cycle.
- ✅ **Type Safety**: All code will have complete type annotations. ValidationState will use `Literal["success", "error"] | None` pattern from Input component.
- ✅ **Component Value**: Textarea passes value validation - provides genuine convenience (generates textarea + label + helper text structure), enforces consistent validation patterns, handles complex dark mode logic internally, and provides type safety via dataclass.
- ✅ **Architecture**: Follows hybrid Jinja + htmy pattern. Textarea is an htmy component (Python dataclass), showcase will use Jinja template for layout.
- ✅ **Quality Gates**: Plan includes pytest (>90% coverage target), mypy strict mode (100% type coverage), ruff linting, and ruff formatting requirements.

**Result**: All principles satisfied. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-textarea/
├── plan.md              # This file (/speckit.plan output)
├── spec.md              # Feature specification (completed)
├── research.md          # Phase 0 output (patterns analysis)
├── data-model.md        # Phase 1 output (component structure)
├── quickstart.md        # Phase 1 output (usage examples)
├── contracts/           # Phase 1 output (component API contract)
│   └── textarea-api.md  # Component props and rendering contract
└── tasks.md             # Phase 2 output (/speckit.tasks - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/flowbite_htmy/
├── components/
│   ├── __init__.py          # Export Textarea component
│   ├── textarea.py          # NEW: Textarea component implementation
│   ├── input.py             # Reference pattern for validation/helper text
│   ├── checkbox.py          # Reference pattern for label handling
│   └── radio.py             # Reference pattern for required indicators
├── base/
│   ├── classes.py           # ClassBuilder utility (existing)
│   └── context.py           # ThemeContext (existing)
└── types/
    ├── __init__.py          # Export ValidationState if needed
    └── validation.py        # ValidationState type definition (may need creation)

tests/
├── test_components/
│   ├── test_textarea.py     # NEW: Textarea component tests (20-25 tests)
│   ├── test_input.py        # Reference for validation test patterns
│   └── test_checkbox.py     # Reference for required field test patterns
└── conftest.py              # Fixtures: renderer, context, dark_context (existing)

examples/
├── showcase.py              # Consolidated showcase (will add Textarea section)
├── textareas.py             # NEW: Standalone Textarea showcase (optional)
└── templates/
    └── showcase.html.jinja  # Will add Textarea section to consolidated showcase
```

**Structure Decision**: Single project structure following existing flowbite-htmy patterns. Component implementation in `src/flowbite_htmy/components/textarea.py`, tests in `tests/test_components/test_textarea.py`, showcase integration in consolidated `examples/showcase.py`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

*No violations detected. This section intentionally left empty.*

---

## Phase 0: Research & Patterns Analysis

### Objective

Analyze existing Input, Checkbox, and Radio components to extract proven patterns for Textarea implementation. Identify Flowbite CSS classes for textarea elements and document design decisions for edge cases.

### Research Tasks

1. **Pattern Analysis - Validation States**
   - Study Input component's validation state implementation (success/error/default)
   - Extract helper text rendering pattern with color matching
   - Document ClassBuilder usage for state-dependent classes
   - **Output**: Validation pattern documentation in research.md

2. **Pattern Analysis - Required Field Indicator**
   - Study how existing components handle required attribute
   - Review clarification decision: asterisk appended to label text
   - Extract pattern for label text modification when required=True
   - **Output**: Required field pattern documentation in research.md

3. **Pattern Analysis - Label and ID Association**
   - Study Input component's label-for-id association
   - Review auto-generated ID pattern (if used in existing components)
   - Document best practice for aria-label handling when label is empty
   - **Output**: Accessibility pattern documentation in research.md

4. **Flowbite CSS Research - Textarea Styling**
   - Extract Flowbite CSS classes for textarea elements from flowbite-llms-full.txt
   - Document base classes (border, padding, rounded corners, focus ring)
   - Document dark mode classes for textarea
   - Document validation state classes (success border, error border)
   - **Output**: CSS class reference in research.md

5. **Pattern Analysis - Edge Case Handling**
   - Study how Input handles disabled state (cursor, background color)
   - Document decision on rows clamping (minimum of 1)
   - Document decision on disabled precedence over readonly
   - **Output**: Edge case handling patterns in research.md

6. **HTMX Integration Pattern**
   - Review how existing components handle HTMX attributes (hx_get, hx_post, etc.)
   - Document passthrough attributes pattern via attrs dict
   - **Output**: HTMX integration pattern in research.md

### Deliverables

- **research.md** containing:
  - Validation state pattern (extracted from Input)
  - Required field indicator pattern (asterisk appending)
  - Label/ID association pattern
  - Flowbite CSS class reference for textarea
  - Edge case handling decisions
  - HTMX integration pattern
  - All NEEDS CLARIFICATION items resolved

---

## Phase 1: Design & Contracts

### Prerequisites

- Phase 0 research.md complete
- All patterns extracted from existing components
- Flowbite CSS classes documented

### Design Tasks

1. **Data Model Definition**
   - Define Textarea dataclass structure with all props
   - Document prop types following Input component pattern
   - Define ValidationState type (Literal["success", "error"] | None)
   - **Output**: data-model.md with complete component structure

2. **Component API Contract**
   - Document all component props with types and defaults
   - Define htmy() method signature and return type
   - Document internal helper methods (_build_label_classes, _build_textarea_classes, etc.)
   - **Output**: contracts/textarea-api.md

3. **Quickstart Documentation**
   - Create basic usage example (minimal props)
   - Create validation example (error and success states)
   - Create edit form example (with pre-filled value)
   - Create required field example (with asterisk)
   - **Output**: quickstart.md

4. **Agent Context Update**
   - Run `.specify/scripts/bash/update-agent-context.sh claude`
   - Add Textarea component to Active Technologies
   - **Output**: Updated .claude/context/agent-file-claude.md

### Deliverables

- **data-model.md**: Complete Textarea component structure
- **contracts/textarea-api.md**: Component API contract
- **quickstart.md**: Usage examples and patterns
- **agent-file-claude.md**: Updated with Textarea technology

---

## Phase 2: Implementation Planning (Tasks Generation)

**NOTE**: This phase is NOT executed by `/speckit.plan`. Run `/speckit.tasks` after completing Phase 1 to generate tasks.md.

The tasks.md will include:
- TDD workflow tasks (write test → run → implement → verify)
- Component implementation tasks
- Showcase application tasks
- Quality validation tasks (coverage, mypy, ruff)

---

## Implementation Notes

### Key Design Decisions

1. **Value Parameter**: Added based on clarification Q4 - essential for edit forms
2. **Name Attribute**: Optional with no default (clarification Q5) - gives developers control
3. **Rows Clamping**: Minimum of 1 (clarification Q2) - prevents broken UI states
4. **Required Indicator**: Asterisk appended to label text (clarification Q1) - matches WCAG best practices
5. **State Precedence**: Disabled overrides readonly (clarification Q3) - follows HTML5 semantics

### Component Props Summary

Based on specification and clarifications:

- **Required**: id (str), label (str)
- **Optional**: name (str | None), value (str | None), placeholder (str | None)
- **Sizing**: rows (int, default=4, clamped to min 1)
- **States**: required (bool), disabled (bool), readonly (bool)
- **Validation**: validation (ValidationState), helper_text (str | None)
- **Integration**: attrs (dict[str, Any] | None), class_ (str)
- **HTMX**: hx_get, hx_post, hx_target, hx_swap, etc. (all str | None)

### Testing Strategy

Following TDD principle:
1. Write test for default rendering
2. Run test (should fail - component doesn't exist)
3. Create minimal Textarea class
4. Run test (should pass)
5. Refactor
6. Repeat for each feature (validation, required, disabled, rows, etc.)

Target: 95%+ coverage with 20-25 tests covering all functional requirements.

### Quality Gates

Before committing:
- ✅ All tests pass: `pytest`
- ✅ Coverage >90%: `pytest --cov`
- ✅ Type check passes: `mypy src/flowbite_htmy`
- ✅ Linting passes: `ruff check src/flowbite_htmy`
- ✅ Formatting passes: `ruff format src/flowbite_htmy`

---

**Next Step**: Execute Phase 0 research by analyzing existing components and Flowbite CSS patterns. This plan will guide the implementation through TDD cycles to deliver a production-ready Textarea component consistent with the project's quality standards and architectural patterns.
