# Tasks: Radio Component

**Input**: Design documents from `/specs/002-phase-2b-radio/`
**Prerequisites**: plan.md (complete), spec.md (complete), research.md (complete), data-model.md (complete), contracts/ (complete)

**Tests**: This project follows strict TDD (Test-Driven Development). All test tasks precede implementation tasks per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/flowbite_htmy/`, `tests/test_components/`, `examples/` at repository root
- All paths use Python package structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and ValidationState enum (if needed)

- [ ] T001 Check if src/flowbite_htmy/types/validation.py exists, create if needed
- [ ] T002 [P] If validation.py created, add ValidationState enum with DEFAULT, ERROR, SUCCESS values
- [ ] T003 [P] If validation.py created, export ValidationState from src/flowbite_htmy/types/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Test file and fixture setup that MUST be complete before ANY user story implementation

**⚠️ CRITICAL**: No implementation work can begin until test infrastructure is ready (TDD principle)

- [ ] T004 Create test file tests/test_components/test_radio.py with pytest imports and markers
- [ ] T005 Verify fixtures (renderer, context, dark_context) are available from tests/conftest.py

**Checkpoint**: Test infrastructure ready - TDD implementation can now begin for each user story

---

## Phase 3: User Story 1 - Basic Radio Button Selection (Priority: P1) 🎯 MVP

**Goal**: Core functionality - render radio buttons with labels, handle checked state, support name/value attributes, auto-generate IDs

**Independent Test**: Can be fully tested by rendering a group of radio buttons with labels, checking that IDs are auto-generated, labels are properly associated, and checked state works correctly

### Tests for User Story 1 (TDD: Write FIRST, ensure FAIL)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T006 [P] [US1] Write test_radio_default_rendering in tests/test_components/test_radio.py (minimal props, verify label and type="radio")
- [ ] T007 [P] [US1] Write test_radio_with_name_and_value in tests/test_components/test_radio.py (verify name and value attributes)
- [ ] T008 [P] [US1] Write test_radio_checked_state in tests/test_components/test_radio.py (checked=True renders checked)
- [ ] T009 [P] [US1] Write test_radio_auto_generated_id in tests/test_components/test_radio.py (ID generated when not provided)
- [ ] T010 [P] [US1] Write test_radio_custom_id in tests/test_components/test_radio.py (custom ID when provided)
- [ ] T011 [P] [US1] Write test_radio_label_for_attribute in tests/test_components/test_radio.py (label for= matches input id=)
- [ ] T012 [US1] Run tests with pytest tests/test_components/test_radio.py to confirm ALL tests FAIL

### Implementation for User Story 1

- [ ] T013 [US1] Create src/flowbite_htmy/components/radio.py with imports (dataclass, htmy, ClassBuilder, ThemeContext, ValidationState)
- [ ] T014 [US1] Add module-level _radio_counter and _generate_radio_id() function for ID generation
- [ ] T015 [US1] Define Radio dataclass with frozen=True, kw_only=True and core attributes (label, name, value, checked, id)
- [ ] T016 [US1] Implement __post_init__() validation (raise ValueError if both label and aria_label are empty)
- [ ] T017 [US1] Implement htmy() method: generate ID, build basic input element with type="radio"
- [ ] T018 [US1] Implement htmy() method: build label element with for= attribute matching input ID
- [ ] T019 [US1] Implement htmy() method: create container structure (flex layout per Flowbite)
- [ ] T020 [US1] Implement _build_input_classes() with base Flowbite classes (w-4 h-4 bg-gray-100 etc.)
- [ ] T021 [US1] Implement _build_label_classes() with base classes (font-medium text-gray-900 dark:text-gray-300)
- [ ] T022 [US1] Export Radio from src/flowbite_htmy/components/__init__.py
- [ ] T023 [US1] Run tests with pytest tests/test_components/test_radio.py to confirm US1 tests PASS
- [ ] T024 [US1] Run mypy src/flowbite_htmy/components/radio.py to verify type safety
- [ ] T025 [US1] Run ruff check and ruff format on src/flowbite_htmy/components/radio.py

**Checkpoint**: At this point, User Story 1 should be fully functional - basic radio rendering with labels and IDs working

---

## Phase 4: User Story 2 - Validation States and Helper Text (Priority: P2)

**Goal**: Add validation state support (default, error, success) with color styling and helper text display

**Independent Test**: Can be tested by rendering Radio components with different validation states and helper text, verifying that colors change appropriately

### Tests for User Story 2 (TDD: Write FIRST, ensure FAIL)

- [ ] T026 [P] [US2] Write test_radio_validation_default_state in tests/test_components/test_radio.py (default blue colors)
- [ ] T027 [P] [US2] Write test_radio_validation_error_state in tests/test_components/test_radio.py (red colors for error)
- [ ] T028 [P] [US2] Write test_radio_validation_success_state in tests/test_components/test_radio.py (green colors for success)
- [ ] T029 [P] [US2] Write test_radio_helper_text_rendering in tests/test_components/test_radio.py (helper text appears below radio)
- [ ] T030 [P] [US2] Write test_radio_helper_text_error_color in tests/test_components/test_radio.py (helper text red when validation=error)
- [ ] T031 [P] [US2] Write test_radio_helper_text_success_color in tests/test_components/test_radio.py (helper text green when validation=success)
- [ ] T032 [US2] Run tests to confirm US2 tests FAIL (US1 tests should still PASS)

### Implementation for User Story 2

- [ ] T033 [US2] Add validation_state and helper_text attributes to Radio dataclass in src/flowbite_htmy/components/radio.py
- [ ] T034 [US2] Update _build_input_classes() to add validation state colors (error: red, success: green, default: blue)
- [ ] T035 [US2] Update _build_label_classes() to add validation state text colors
- [ ] T036 [US2] Implement _build_helper_classes() method with validation state colors
- [ ] T037 [US2] Update htmy() method to render helper text <p> element when helper_text provided
- [ ] T038 [US2] Update htmy() method container to include helper text in proper position
- [ ] T039 [US2] Run tests with pytest tests/test_components/test_radio.py to confirm US1 and US2 tests PASS
- [ ] T040 [US2] Run mypy to verify type safety after changes
- [ ] T041 [US2] Run ruff check and ruff format

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - radio rendering + validation states

---

## Phase 5: User Story 3 - Disabled State and Dark Mode (Priority: P3)

**Goal**: Add disabled state handling and ensure dark mode classes are always present

**Independent Test**: Can be tested by rendering disabled radios and verifying dark mode classes exist in output

### Tests for User Story 3 (TDD: Write FIRST, ensure FAIL)

- [ ] T042 [P] [US3] Write test_radio_disabled_state in tests/test_components/test_radio.py (disabled attribute and opacity classes)
- [ ] T043 [P] [US3] Write test_radio_disabled_checked_state in tests/test_components/test_radio.py (disabled + checked combination)
- [ ] T044 [P] [US3] Write test_radio_disabled_label_color in tests/test_components/test_radio.py (gray label when disabled)
- [ ] T045 [P] [US3] Write test_radio_dark_mode_classes_always_present in tests/test_components/test_radio.py (dark: classes in output)
- [ ] T046 [P] [US3] Write test_radio_custom_classes_merge in tests/test_components/test_radio.py (class_ prop merges correctly)
- [ ] T047 [US3] Run tests to confirm US3 tests FAIL (US1 and US2 tests should still PASS)

### Implementation for User Story 3

- [ ] T048 [US3] Add disabled and class_ attributes to Radio dataclass in src/flowbite_htmy/components/radio.py
- [ ] T049 [US3] Update _build_input_classes() to add disabled classes (disabled:opacity-50 disabled:cursor-not-allowed)
- [ ] T050 [US3] Update _build_input_classes() to merge custom classes via ClassBuilder.merge(self.class_)
- [ ] T051 [US3] Update _build_label_classes() to handle disabled state (gray text when disabled)
- [ ] T052 [US3] Verify all dark mode classes are present in _build_input_classes() and _build_label_classes()
- [ ] T053 [US3] Update htmy() method to pass disabled attribute to input element
- [ ] T054 [US3] Run tests with pytest tests/test_components/test_radio.py to confirm ALL tests PASS (US1, US2, US3)
- [ ] T055 [US3] Run pytest with coverage: pytest tests/test_components/test_radio.py --cov=src/flowbite_htmy/components/radio --cov-report=term-missing
- [ ] T056 [US3] Verify coverage >90% (constitution requirement), add tests if needed
- [ ] T057 [US3] Run mypy to verify type safety
- [ ] T058 [US3] Run ruff check and ruff format

**Checkpoint**: All user stories should now be independently functional - complete Radio component

---

## Phase 6: HTMX Integration & Edge Cases

**Goal**: Add HTMX support, handle empty labels with aria-label, and test edge cases

**Independent Test**: Test HTMX attributes render correctly, empty labels work with aria-label, edge cases handled

### Tests for HTMX & Edge Cases (TDD: Write FIRST, ensure FAIL)

- [ ] T059 [P] Write test_radio_htmx_get_attribute in tests/test_components/test_radio.py (hx-get renders)
- [ ] T060 [P] Write test_radio_htmx_multiple_attributes in tests/test_components/test_radio.py (hx-get, hx-target, hx-swap all render)
- [ ] T061 [P] Write test_radio_empty_label_with_aria_label in tests/test_components/test_radio.py (valid: empty label + aria-label)
- [ ] T062 [P] Write test_radio_empty_label_without_aria_label_raises_error in tests/test_components/test_radio.py (ValueError raised)
- [ ] T063 [P] Write test_radio_long_label_text in tests/test_components/test_radio.py (label wraps gracefully)
- [ ] T064 Run tests to confirm HTMX and edge case tests FAIL

### Implementation for HTMX & Edge Cases

- [ ] T065 Add HTMX attributes to Radio dataclass (hx_get, hx_post, hx_put, hx_delete, hx_patch, hx_target, hx_swap, hx_trigger, hx_push_url, hx_select)
- [ ] T066 Add aria_label attribute to Radio dataclass in src/flowbite_htmy/components/radio.py
- [ ] T067 Update __post_init__() to verify __post_init__ validation (raise ValueError if both label and aria_label empty) - should already exist from T016
- [ ] T068 Update htmy() method to pass all HTMX attributes to input element
- [ ] T069 Update htmy() method to pass aria_label to input element when provided
- [ ] T070 Update htmy() method to handle empty label case (don't render label element if label is empty)
- [ ] T071 Run tests with pytest tests/test_components/test_radio.py to confirm ALL tests PASS
- [ ] T072 Run coverage check, verify >90%
- [ ] T073 Run mypy and ruff checks

**Checkpoint**: Radio component feature-complete with HTMX support and edge cases handled

---

## Phase 7: Showcase Application

**Goal**: Create standalone showcase application demonstrating all Radio component features

**Independent Test**: Run showcase app and visually verify all examples work correctly

### Showcase Implementation

- [ ] T074 [P] Create examples/templates/radio-layout.html.jinja with Flowbite CSS and HTMX script tags
- [ ] T075 Create examples/radios.py with FastAPI app and Jinja setup
- [ ] T076 Implement build_radios_showcase() function with basic radio group examples (shipping methods, payment options)
- [ ] T077 Add validation states section to build_radios_showcase() (error, success, default states)
- [ ] T078 Add disabled states section to build_radios_showcase() (disabled + checked combinations)
- [ ] T079 Add HTMX integration section to build_radios_showcase() (dynamic updates example)
- [ ] T080 Add accessibility examples to build_radios_showcase() (empty label with aria-label)
- [ ] T081 Add helper text examples to build_radios_showcase()
- [ ] T082 Implement GET / route handler in examples/radios.py to render showcase
- [ ] T083 Add HTMX demo endpoint (e.g., GET /update-options) for interactive examples
- [ ] T084 Test standalone showcase: python examples/radios.py and visit http://localhost:8000
- [ ] T085 Verify all showcase sections render correctly and demonstrate component features

**Checkpoint**: Standalone showcase complete and functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, documentation, and integration

- [ ] T086 [P] Run full test suite with pytest to ensure all tests pass
- [ ] T087 [P] Run pytest with coverage on entire package to verify >90% overall
- [ ] T088 [P] Run mypy src/flowbite_htmy to verify type safety across package
- [ ] T089 [P] Run ruff check src/flowbite_htmy and ruff format to ensure code quality
- [ ] T090 Verify quickstart.md accuracy by following steps manually
- [ ] T091 Update VS Code launch.json with "Radio Showcase" debug configuration (if desired)
- [ ] T092 Test component compiles: python -m py_compile src/flowbite_htmy/components/radio.py
- [ ] T093 Extract build_radios_showcase() function to module level in examples/radios.py for reuse
- [ ] T094 [P] Add Radio component to consolidated showcase app (examples/showcase.py) by importing build_radios_showcase()
- [ ] T095 [P] Add /radios route to consolidated showcase app
- [ ] T096 Test consolidated showcase includes Radio component correctly
- [ ] T097 Create session note in Basic Memory documenting Radio component completion

**Checkpoint**: Radio component complete, tested, documented, and integrated into showcase

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational phase completion
- **User Story 2 (Phase 4)**: Depends on User Story 1 completion (builds on basic rendering)
- **User Story 3 (Phase 5)**: Depends on User Stories 1 & 2 completion (adds disabled/dark mode to existing implementation)
- **HTMX & Edge Cases (Phase 6)**: Depends on User Stories 1-3 completion (extends complete component)
- **Showcase (Phase 7)**: Depends on HTMX & Edge Cases completion (demonstrates all features)
- **Polish (Phase 8)**: Depends on Showcase completion

### User Story Dependencies

**Sequential Implementation Required** (not parallel due to shared file):

- User Story 1 → User Story 2 → User Story 3 (all modify same file: src/flowbite_htmy/components/radio.py)
- Each story builds incrementally on previous story's implementation
- Tests can be written in parallel initially, but implementation must be sequential

### Within Each User Story

**TDD Cycle (STRICT):**

1. Write ALL tests for the user story (these can be parallel - different test functions)
2. Run tests to confirm they FAIL
3. Implement feature to make tests PASS
4. Refactor if needed while keeping tests green
5. Run type checking and linting
6. Move to next user story

### Parallel Opportunities

**Tests within a story** (Phase 3-6):
- All test writing tasks marked [P] can be written in parallel (different test functions)
- Example: T006, T007, T008, T009, T010, T011 can all be written together for US1

**Showcase sections** (Phase 7):
- Template creation (T074) can happen in parallel with showcase.py initial setup (T075)

**Polish tasks** (Phase 8):
- T086, T087, T088, T089 can run in parallel (different validation tools)
- T094, T095 can run in parallel (different files in showcase integration)

---

## Parallel Example: User Story 1 Tests

```bash
# Launch all test writing for User Story 1 together (different test functions):
Task T006: "Write test_radio_default_rendering"
Task T007: "Write test_radio_with_name_and_value"
Task T008: "Write test_radio_checked_state"
Task T009: "Write test_radio_auto_generated_id"
Task T010: "Write test_radio_custom_id"
Task T011: "Write test_radio_label_for_attribute"

# Then run T012 to confirm all fail, then proceed with sequential implementation T013-T025
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T005) - CRITICAL TEST SETUP
3. Complete Phase 3: User Story 1 (T006-T025)
4. **STOP and VALIDATE**: Test User Story 1 independently with pytest
5. **MVP DELIVERABLE**: Basic Radio component with labels, IDs, checked state

### Incremental Delivery (TDD Approach)

1. Setup + Foundational → Test infrastructure ready
2. Add User Story 1 → Test independently → **MVP READY**
3. Add User Story 2 → Test independently → **Validation States READY**
4. Add User Story 3 → Test independently → **Disabled/Dark Mode READY**
5. Add HTMX & Edge Cases → Test independently → **Feature-Complete READY**
6. Add Showcase → Visual demonstration → **Demo READY**
7. Polish → Final validation → **Production READY**

### TDD Workflow Per User Story

**For each user story phase:**

1. **Red Phase**: Write ALL tests for the story (T006-T011 for US1)
2. **Confirm Red**: Run tests to ensure they FAIL (T012 for US1)
3. **Green Phase**: Implement features to make tests PASS (T013-T023 for US1)
4. **Refactor Phase**: Clean up code while keeping tests green (T024-T025 for US1)
5. **Checkpoint**: Verify story works independently before moving to next

---

## Notes

- **[P] tasks** = Can run in parallel (different files or independent test functions)
- **[Story] label** = Maps task to specific user story for traceability
- **TDD CRITICAL**: Tests MUST be written first and MUST fail before implementation (constitution requirement)
- **Sequential Implementation**: All user stories modify the same file, so implementation must be sequential even though test writing can be parallel
- Each user story builds on previous stories incrementally
- Stop at any checkpoint to validate story independently
- Commit after each completed user story or logical group of tasks
- **Coverage requirement**: >90% per constitution (verified in T055, T056, T087)

---

## Task Summary

**Total Tasks**: 97
- **Phase 1 (Setup)**: 3 tasks
- **Phase 2 (Foundational)**: 2 tasks
- **Phase 3 (User Story 1)**: 20 tasks (7 tests + 13 implementation)
- **Phase 4 (User Story 2)**: 16 tasks (7 tests + 9 implementation)
- **Phase 5 (User Story 3)**: 17 tasks (6 tests + 11 implementation)
- **Phase 6 (HTMX & Edge Cases)**: 15 tasks (6 tests + 9 implementation)
- **Phase 7 (Showcase)**: 12 tasks
- **Phase 8 (Polish)**: 12 tasks

**Parallel Opportunities**: 41 tasks marked [P] (42% of total)

**Independent Test Criteria**:
- **US1**: Render radio groups with labels and IDs, verify mutual exclusivity
- **US2**: Display validation states with correct colors and helper text
- **US3**: Handle disabled state and dark mode classes correctly

**Suggested MVP Scope**: Phase 1 + Phase 2 + Phase 3 (User Story 1 only) = 25 tasks for basic functional Radio component
