# Tasks: Accordion Component

**Input**: Design documents from `/specs/005-accordion/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/accordion-api.md, quickstart.md

**Tests**: This feature uses strict TDD approach. Tests MUST be written before implementation (project constitution requirement).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and test infrastructure

- [x] T001 Create test file tests/test_components/test_accordion.py with required imports
- [x] T002 Create accordion component file src/flowbite_htmy/components/accordion.py with module docstring

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data structures that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Define AccordionMode enum (COLLAPSE="collapse", ALWAYS_OPEN="open") in src/flowbite_htmy/components/accordion.py
- [x] T004 Define AccordionVariant enum (DEFAULT="default", FLUSH="flush") in src/flowbite_htmy/components/accordion.py
- [x] T005 [P] Define Panel dataclass with title, content, is_open, icon, hx_get, hx_trigger, class_ fields in src/flowbite_htmy/components/accordion.py
- [x] T006 Define Accordion dataclass with panels, mode, variant, color, class_, accordion_id fields in src/flowbite_htmy/components/accordion.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Accordion Creation (Priority: P1) 🎯 MVP

**Goal**: Developers can create an accordion with multiple collapsible panels containing FAQ content with proper HTML structure, ARIA attributes, and Flowbite classes.

**Independent Test**: Creating an Accordion instance with multiple panels and verifying the rendered HTML contains proper structure, ARIA attributes, and Flowbite classes.

### Tests for User Story 1 (TDD REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [P] [US1] Write test_accordion_default_rendering - verify accordion renders with collapse mode and default variant in tests/test_components/test_accordion.py
- [x] T008 [P] [US1] Write test_accordion_generates_unique_ids - verify each panel gets unique heading and body IDs in tests/test_components/test_accordion.py
- [x] T009 [P] [US1] Write test_accordion_aria_attributes - verify aria-expanded, aria-controls, aria-labelledby present in tests/test_components/test_accordion.py
- [x] T010 [P] [US1] Write test_accordion_flowbite_classes - verify Flowbite CSS classes applied to buttons and panels in tests/test_components/test_accordion.py
- [x] T011 [P] [US1] Write test_accordion_data_attribute_collapse - verify collapse mode sets data-accordion="collapse" in tests/test_components/test_accordion.py
- [x] T012 [P] [US1] Write test_accordion_data_attribute_always_open - verify always-open mode sets data-accordion="open" in tests/test_components/test_accordion.py

**Checkpoint**: All US1 tests written and failing

### Implementation for User Story 1

- [x] T013 [US1] Implement Accordion.htmy() method skeleton returning html.div with data-accordion attribute in src/flowbite_htmy/components/accordion.py
- [x] T014 [US1] Implement ID generation logic using id(self) or custom accordion_id in src/flowbite_htmy/components/accordion.py
- [x] T015 [US1] Implement panel iteration and h2 + button + div structure rendering in src/flowbite_htmy/components/accordion.py
- [x] T016 [US1] Implement ARIA attributes (aria-expanded, aria-controls, aria-labelledby, data-accordion-target) in src/flowbite_htmy/components/accordion.py
- [x] T017 [US1] Implement _build_button_classes() method with ClassBuilder for button styling in src/flowbite_htmy/components/accordion.py
- [x] T018 [US1] Implement _build_body_classes() method with ClassBuilder for panel body styling in src/flowbite_htmy/components/accordion.py
- [x] T019 [US1] Add default chevron icon using get_icon(Icon.CHEVRON_DOWN) with data-accordion-icon attribute in src/flowbite_htmy/components/accordion.py
- [x] T020 [US1] Run all US1 tests and verify they pass

**Checkpoint**: User Story 1 should be fully functional - accordion renders with proper structure, IDs, ARIA, and Flowbite classes

---

## Phase 4: User Story 2 - Accordion Customization (Priority: P2)

**Goal**: Developers can customize accordion appearance (colors, icons, borders, flush style) and behavior (always-open vs collapse mode) to match their application's design system.

**Independent Test**: Creating accordions with different variant options (default, flush) and color schemes, verifying correct Tailwind classes are applied and dark mode classes are included.

### Tests for User Story 2 (TDD REQUIRED) ⚠️

- [x] T021 [P] [US2] Write test_accordion_flush_variant - verify flush variant removes side borders and rounding in tests/test_components/test_accordion.py
- [x] T022 [P] [US2] Write test_accordion_color_customization - verify color prop applies header background classes in tests/test_components/test_accordion.py
- [x] T023 [P] [US2] Write test_accordion_dark_mode_classes_always_included - verify dark classes present in light mode in tests/test_components/test_accordion.py
- [x] T024 [P] [US2] Write test_accordion_always_open_mode - verify always-open mode allows multiple panels open in tests/test_components/test_accordion.py
- [x] T025 [P] [US2] Write test_accordion_custom_panel_icons - verify custom icons replace default chevron in tests/test_components/test_accordion.py

**Checkpoint**: All US2 tests written and failing

### Implementation for User Story 2

- [x] T026 [US2] Enhance _build_button_classes() to support variant-based class logic (DEFAULT vs FLUSH) in src/flowbite_htmy/components/accordion.py
- [x] T027 [US2] Enhance _build_body_classes() to support variant-based class logic (DEFAULT vs FLUSH) in src/flowbite_htmy/components/accordion.py
- [x] T028 [US2] Define COLOR_CLASSES dictionary mapping Color enum to hover classes in src/flowbite_htmy/components/accordion.py
- [x] T029 [US2] Integrate color prop into _build_button_classes() for color-specific hover states in src/flowbite_htmy/components/accordion.py
- [x] T030 [US2] Verify dark mode classes always included (no conditional theme.dark_mode checks) in src/flowbite_htmy/components/accordion.py
- [x] T031 [US2] Implement custom icon support in panel rendering (check panel.icon, use default if None) in src/flowbite_htmy/components/accordion.py
- [x] T032 [US2] Run all US2 tests and verify they pass

**Checkpoint**: User Stories 1 AND 2 should both work independently - accordion supports all variants and customization

---

## Phase 5: User Story 3 - HTMX Integration (Priority: P3)

**Goal**: Developers can integrate accordions with HTMX for dynamic content loading, where panel content can be fetched from the server when expanded.

**Independent Test**: Creating an accordion with HTMX attributes on panels (hx-get, hx-trigger), verifying the HTMX attributes render correctly on panel body.

### Tests for User Story 3 (TDD REQUIRED) ⚠️

- [x] T033 [P] [US3] Write test_accordion_htmx_get_attribute - verify hx-get attribute renders on panel body in tests/test_components/test_accordion.py
- [x] T034 [P] [US3] Write test_accordion_htmx_trigger_attribute - verify hx-trigger attribute configurable in tests/test_components/test_accordion.py
- [x] T035 [P] [US3] Write test_accordion_multiple_htmx_attributes - verify multiple HTMX attributes supported in tests/test_components/test_accordion.py

**Checkpoint**: All US3 tests written and passing

### Implementation for User Story 3

- [x] T036 [US3] Add hx_swap and hx_target props to Panel dataclass in src/flowbite_htmy/components/accordion.py
- [x] T037 [US3] Implement HTMX attribute rendering on panel body div (hx_get, hx_trigger, hx_swap, hx_target) in src/flowbite_htmy/components/accordion.py
- [x] T038 [US3] Run all US3 tests and verify they pass

**Checkpoint**: All user stories should now be independently functional - accordion supports full HTMX integration

---

## Phase 6: Edge Cases (Quality Assurance)

**Goal**: Handle boundary conditions and unusual inputs gracefully to ensure robustness.

**Independent Test**: Creating accordions with edge case scenarios (single panel, empty content, invalid indices, custom classes) and verifying correct behavior.

### Tests for Edge Cases (TDD REQUIRED) ⚠️

- [x] T039 [P] Write test_accordion_single_panel - verify single-panel accordion works correctly in tests/test_components/test_accordion.py
- [x] T040 [P] Write test_accordion_empty_content - verify panels with empty content render in tests/test_components/test_accordion.py
- [x] T041 [P] Write test_accordion_handles_invalid_open_index - verify is_open handles gracefully in tests/test_components/test_accordion.py
- [x] T042 [P] Write test_accordion_custom_classes - verify custom classes merge with component classes in tests/test_components/test_accordion.py

**Checkpoint**: All edge case tests written and passing

### Implementation for Edge Cases

- [x] T043 Verify single panel accordion works (first panel: rounded-t-xl, last panel: border-t-0) in src/flowbite_htmy/components/accordion.py
- [x] T044 Verify empty content panels render empty div wrapper in src/flowbite_htmy/components/accordion.py
- [x] T045 Verify is_open is per-panel (no index-based logic needed) in src/flowbite_htmy/components/accordion.py
- [x] T046 Implement custom class merging using ClassBuilder().merge(self.class_) on container div in src/flowbite_htmy/components/accordion.py
- [x] T047 Run all edge case tests and verify they pass

**Checkpoint**: All 17 tests passing, edge cases handled

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Integration, documentation, and quality assurance

- [x] T048 [P] Export Accordion, Panel, AccordionMode, AccordionVariant from src/flowbite_htmy/components/__init__.py
- [x] T049 Run full test suite: pytest tests/test_components/test_accordion.py --cov=src/flowbite_htmy/components/accordion
- [x] T050 Verify >90% test coverage (expected: 95-99%) - ACHIEVED: 100% coverage!
- [x] T051 Run type checking: mypy src/flowbite_htmy/components/accordion.py --strict
- [x] T052 [P] Run linting: ruff check src/flowbite_htmy/components/accordion.py
- [x] T053 [P] Run formatting: ruff format src/flowbite_htmy/components/accordion.py
- [x] T054 Add accordion section to showcase app in examples/showcase.py
- [x] T055 Create accordion showcase template section (FAQ example with 3-5 panels) in examples/accordions.py
- [x] T056 Test accordion showcase in browser: python examples/showcase.py and verify Flowbite JavaScript initializes correctly
- [x] T057 Update CLAUDE.md with accordion component status (Phase 2C complete, coverage %, test count)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User Story 1 (Phase 3): Can start after Foundational - No dependencies on other stories
  - User Story 2 (Phase 4): Can start after Foundational - No dependencies on other stories
  - User Story 3 (Phase 5): Can start after Foundational - No dependencies on other stories
- **Edge Cases (Phase 6)**: Can start after Foundational - No dependencies on user stories
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Enhances US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Extends US1/US2 but independently testable

### Within Each User Story (TDD Cycle)

1. Write ALL tests for the story FIRST (marked [P] within phase - can write in parallel)
2. Verify tests FAIL for correct reason
3. Implement to make tests pass (sequential dependencies)
4. Verify ALL tests for that story pass
5. Refactor while keeping tests green

### Parallel Opportunities

- **Phase 1 Setup**: Both tasks (T001-T002) can run in parallel
- **Phase 2 Foundational**: All enum/dataclass definitions (T003-T006) can run in parallel if using different sections
- **Phase 3 Tests (US1)**: All 6 test writing tasks (T007-T012) can run in parallel
- **Phase 4 Tests (US2)**: All 5 test writing tasks (T021-T025) can run in parallel
- **Phase 5 Tests (US3)**: All 3 test writing tasks (T033-T035) can run in parallel
- **Phase 6 Tests (Edge)**: All 4 test writing tasks (T039-T042) can run in parallel
- **Phase 7 Polish**: Export, coverage, type check, linting, formatting (T048, T049-T053) can run in parallel
- **User Stories**: Once Foundational is complete, US1, US2, US3 can start in parallel (different team members)

---

## Parallel Example: User Story 1 Tests

```bash
# Launch all test writing tasks for User Story 1 together:
Task T007: "Write test_accordion_default_rendering in tests/test_components/test_accordion.py"
Task T008: "Write test_accordion_generates_unique_ids in tests/test_components/test_accordion.py"
Task T009: "Write test_accordion_aria_attributes in tests/test_components/test_accordion.py"
Task T010: "Write test_accordion_flowbite_classes in tests/test_components/test_accordion.py"
Task T011: "Write test_accordion_data_attribute_collapse in tests/test_components/test_accordion.py"
Task T012: "Write test_accordion_data_attribute_always_open in tests/test_components/test_accordion.py"
```

**Result**: All US1 tests written simultaneously, all failing, ready for implementation

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T006) - CRITICAL blocks all stories
3. Complete Phase 3: User Story 1 (T007-T020)
   - Write all 6 tests first (T007-T012)
   - Verify tests fail
   - Implement (T013-T019)
   - Verify tests pass (T020)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo basic accordion with FAQ example

### Incremental Delivery (Recommended)

1. **Foundation**: Complete Setup + Foundational (T001-T006)
2. **MVP**: Add User Story 1 (T007-T020) → Test → Showcase → **v0.1 Release**
3. **Customization**: Add User Story 2 (T021-T032) → Test → Showcase variants → **v0.2 Release**
4. **HTMX**: Add User Story 3 (T033-T038) → Test → Showcase lazy loading → **v0.3 Release**
5. **Polish**: Add Edge Cases (T039-T047) + Polish (T048-T057) → **v1.0 Release**

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T006)
2. Once Foundational is done:
   - **Developer A**: User Story 1 (T007-T020) - Basic accordion
   - **Developer B**: User Story 2 (T021-T032) - Customization (starts after US1 tests pass)
   - **Developer C**: Edge Cases (T039-T047) - Quality (can start early)
3. **Integrator**: Polish phase (T048-T057) - after all stories complete

---

## TDD Checkpoints

### After Each Test Writing Phase
- [ ] All tests for the story/phase are written
- [ ] Run pytest - ALL new tests should FAIL
- [ ] Failure messages indicate correct missing functionality

### After Each Implementation Phase
- [ ] Run pytest - ALL tests for that story should PASS
- [ ] Run pytest --cov - coverage should increase
- [ ] No regressions - old tests still pass

### After Each Refactoring
- [ ] Run pytest - ALL tests still PASS
- [ ] Code is cleaner but behavior unchanged
- [ ] Coverage maintained or improved

---

## Notes

- **[P] tasks**: Different files or file sections, no data dependencies, safe to run in parallel
- **[Story] label**: Maps task to specific user story for traceability and independent testing
- **TDD CRITICAL**: Tests MUST be written before implementation (project constitution)
- **Strict sequence**: Write test → Verify fail → Implement → Verify pass → Refactor → Repeat
- **Each user story**: Independently completable and testable
- **Checkpoints**: Stop after each phase to validate independently
- **Commit strategy**: After each task or logical group of parallel tasks

---

## Task Summary

**Total Tasks**: 57

**By Phase**:
- Setup: 2 tasks
- Foundational: 4 tasks
- User Story 1 (MVP): 14 tasks (6 tests + 8 implementation)
- User Story 2: 12 tasks (5 tests + 7 implementation)
- User Story 3: 6 tasks (3 tests + 3 implementation)
- Edge Cases: 9 tasks (4 tests + 5 implementation)
- Polish: 10 tasks

**By Type**:
- Test Writing: 18 tasks (strict TDD requirement)
- Implementation: 29 tasks
- Quality/Integration: 10 tasks

**Parallel Opportunities**: 23 tasks marked [P] can run in parallel within their phase

**Independent Stories**: 3 user stories can be implemented and tested independently after Foundational phase

**Coverage Goal**: >90% (expected 95-99% with 17 tests)

**MVP Scope**: Phases 1-3 (20 tasks) delivers basic accordion functionality
