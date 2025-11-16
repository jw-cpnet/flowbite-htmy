# Tasks: Dropdown Component

**Input**: Design documents from `/specs/007-dropdown/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/dropdown-api.md

**Tests**: This project follows strict TDD. Test tasks are included and MUST be completed before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Component code**: `src/flowbite_htmy/components/`
- **Type definitions**: `src/flowbite_htmy/types/`
- **Tests**: `tests/test_components/`
- **Examples**: `examples/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Test file initialization and enum definitions (used across all user stories)

- [X] T001 Create test file tests/test_components/test_dropdown.py with imports and fixtures
- [X] T002 [P] Write enum tests for DropdownPlacement in tests/test_components/test_dropdown.py
- [X] T003 [P] Write enum tests for DropdownTriggerType in tests/test_components/test_dropdown.py
- [X] T004 [P] Write enum tests for DropdownTriggerMode in tests/test_components/test_dropdown.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement enums needed by all user stories - MUST complete before any user story work

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Implement DropdownPlacement enum in src/flowbite_htmy/types/__init__.py
- [X] T006 Implement DropdownTriggerType enum in src/flowbite_htmy/types/__init__.py
- [X] T007 Implement DropdownTriggerMode enum in src/flowbite_htmy/types/__init__.py
- [X] T008 Update src/flowbite_htmy/types/__init__.py __all__ to export new enums
- [X] T009 Run enum tests to verify Phase 2 completion (pytest tests/test_components/test_dropdown.py::test_dropdown_placement_enum -v)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Dropdown Menu (Priority: P1) 🎯 MVP

**Goal**: Implement core dropdown functionality with button trigger and menu items

**Independent Test**: Create a dropdown with 3-5 menu items, click trigger to open/close menu, and verify menu items are clickable. Test ARIA attributes and Flowbite data attributes.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Write test for DropdownDivider rendering in tests/test_components/test_dropdown.py
- [X] T011 [P] [US1] Write test for DropdownDivider with custom class in tests/test_components/test_dropdown.py
- [X] T012 [P] [US1] Write test for DropdownHeader rendering in tests/test_components/test_dropdown.py
- [X] T013 [P] [US1] Write test for DropdownHeader with custom class in tests/test_components/test_dropdown.py
- [X] T014 [P] [US1] Write test for DropdownItem simple rendering in tests/test_components/test_dropdown.py
- [X] T015 [P] [US1] Write test for Dropdown basic rendering with button trigger in tests/test_components/test_dropdown.py
- [X] T016 [P] [US1] Write test for Dropdown ARIA attributes in tests/test_components/test_dropdown.py
- [X] T017 [P] [US1] Write test for Dropdown Flowbite data attributes in tests/test_components/test_dropdown.py
- [X] T018 [US1] Run US1 tests to confirm they FAIL (pytest tests/test_components/test_dropdown.py -k "test_dropdown_divider or test_dropdown_header or test_dropdown_item_simple or test_dropdown_basic" -v)

### Implementation for User Story 1

- [X] T019 [US1] Create src/flowbite_htmy/components/dropdown.py with dataclass imports
- [X] T020 [P] [US1] Implement DropdownDivider class in src/flowbite_htmy/components/dropdown.py
- [X] T021 [P] [US1] Implement DropdownHeader class in src/flowbite_htmy/components/dropdown.py
- [X] T022 [US1] Implement DropdownItem class (basic version without icon/HTMX) in src/flowbite_htmy/components/dropdown.py
- [X] T023 [US1] Implement Dropdown class with button trigger rendering in src/flowbite_htmy/components/dropdown.py
- [X] T024 [US1] Add _render_button_trigger method to Dropdown class in src/flowbite_htmy/components/dropdown.py
- [X] T025 [US1] Add _render_menu method to Dropdown class in src/flowbite_htmy/components/dropdown.py
- [X] T026 [US1] Add _build_trigger_classes method with Color/Size mapping in src/flowbite_htmy/components/dropdown.py
- [X] T027 [US1] Add _build_menu_classes method in src/flowbite_htmy/components/dropdown.py
- [X] T028 [US1] Add _get_dropdown_id method with id(self) generation in src/flowbite_htmy/components/dropdown.py
- [X] T029 [US1] Export DropdownDivider, DropdownHeader, DropdownItem, Dropdown in src/flowbite_htmy/components/__init__.py
- [X] T030 [US1] Run US1 tests to confirm they PASS (pytest tests/test_components/test_dropdown.py -k "test_dropdown_divider or test_dropdown_header or test_dropdown_item_simple or test_dropdown_basic" -v)
- [X] T031 [US1] Run type checking on dropdown module (mypy src/flowbite_htmy/components/dropdown.py --strict)
- [X] T032 [US1] Run linting on dropdown module (ruff check src/flowbite_htmy/components/dropdown.py)

**Checkpoint**: At this point, User Story 1 should be fully functional - basic dropdown with button trigger and simple menu items works independently

---

## Phase 4: User Story 2 - Dropdown Customization (Priority: P2)

**Goal**: Add color customization, icons in menu items, headers, dividers, and dark mode support

**Independent Test**: Create dropdown with custom color (Color.GREEN), icons in menu items (Icon.DASHBOARD), header sections, dividers, and verify dark mode classes are present.

### Tests for User Story 2

- [X] T033 [P] [US2] Write test for Dropdown with custom color and size in tests/test_components/test_dropdown.py
- [X] T034 [P] [US2] Write test for DropdownItem with icon in tests/test_components/test_dropdown.py
- [X] T035 [P] [US2] Write test for DropdownItem disabled state in tests/test_components/test_dropdown.py
- [X] T036 [P] [US2] Write test for Dropdown dark mode classes in tests/test_components/test_dropdown.py
- [X] T037 [P] [US2] Write test for Dropdown with custom trigger_class and menu_class in tests/test_components/test_dropdown.py
- [X] T038 [US2] Run US2 tests to confirm they FAIL (pytest tests/test_components/test_dropdown.py -k "color_and_size or with_icon or disabled or dark_mode or custom_class" -v)

### Implementation for User Story 2

- [X] T039 [US2] Enhance DropdownItem to support icon prop in src/flowbite_htmy/components/dropdown.py
- [X] T040 [US2] Add get_icon() call in DropdownItem.htmy() method for icon rendering in src/flowbite_htmy/components/dropdown.py
- [X] T041 [US2] Add disabled state styling to DropdownItem._build_classes() in src/flowbite_htmy/components/dropdown.py
- [X] T042 [US2] Complete COLOR_CLASSES mapping for all 8 colors in Dropdown._build_trigger_classes() in src/flowbite_htmy/components/dropdown.py
- [X] T043 [US2] Complete SIZE_CLASSES mapping for all 5 sizes in Dropdown._build_trigger_classes() in src/flowbite_htmy/components/dropdown.py
- [X] T044 [US2] Ensure dark mode classes are always included (not conditional) in all _build_classes methods in src/flowbite_htmy/components/dropdown.py
- [X] T045 [US2] Add trigger_class and menu_class merging in Dropdown class in src/flowbite_htmy/components/dropdown.py
- [X] T046 [US2] Run US2 tests to confirm they PASS (pytest tests/test_components/test_dropdown.py -k "color_and_size or with_icon or disabled or dark_mode or custom_class" -v)
- [X] T047 [US2] Run type checking (mypy src/flowbite_htmy/components/dropdown.py --strict)

**Checkpoint**: User Stories 1 AND 2 both work independently - basic dropdowns + full customization

---

## Phase 5: User Story 3 - Advanced Dropdown Features (Priority: P3)

**Goal**: Add positioning options, avatar/text triggers, hover mode, HTMX integration, and multi-level nesting

**Independent Test**: Test each advanced feature independently: (1) placement=TOP, (2) trigger_type=AVATAR, (3) trigger_type=TEXT, (4) trigger_mode=HOVER, (5) HTMX attributes on items, (6) nested dropdowns.

### Tests for User Story 3

- [X] T048 [P] [US3] Write test for Dropdown with placement options (top, bottom, left, right) in tests/test_components/test_dropdown.py
- [X] T049 [P] [US3] Write test for Dropdown with avatar trigger in tests/test_components/test_dropdown.py
- [X] T050 [P] [US3] Write test for Dropdown with text trigger in tests/test_components/test_dropdown.py
- [X] T051 [P] [US3] Write test for Dropdown with hover trigger mode in tests/test_components/test_dropdown.py
- [X] T052 [P] [US3] Write test for DropdownItem with HTMX attributes in tests/test_components/test_dropdown.py
- [X] T053 [P] [US3] Write test for nested dropdown (DropdownItem with dropdown prop) in tests/test_components/test_dropdown.py
- [X] T054 [US3] Run US3 tests to confirm they FAIL (pytest tests/test_components/test_dropdown.py -k "placement or avatar or text_trigger or hover or htmx or nested" -v)

### Implementation for User Story 3

- [X] T055 [P] [US3] Implement _render_avatar_trigger method in Dropdown class in src/flowbite_htmy/components/dropdown.py
- [X] T056 [P] [US3] Implement _render_text_trigger method in Dropdown class in src/flowbite_htmy/components/dropdown.py
- [X] T057 [US3] Update _render_trigger to dispatch based on trigger_type in src/flowbite_htmy/components/dropdown.py
- [X] T058 [US3] Add data-dropdown-placement attribute rendering in _render_button_trigger in src/flowbite_htmy/components/dropdown.py
- [X] T059 [US3] Add data-dropdown-trigger attribute rendering for hover mode in src/flowbite_htmy/components/dropdown.py
- [X] T060 [US3] Add all HTMX attributes (hx_get, hx_post, hx_put, hx_delete, hx_patch, hx_target, hx_swap, hx_trigger, hx_push_url) to DropdownItem.htmy() in src/flowbite_htmy/components/dropdown.py
- [X] T061 [US3] Add nested dropdown support in DropdownItem (check if dropdown prop exists, render nested Dropdown) in src/flowbite_htmy/components/dropdown.py
- [X] T062 [US3] Add chevron icon SVG to button trigger in src/flowbite_htmy/components/dropdown.py
- [X] T063 [US3] Run US3 tests to confirm they PASS (pytest tests/test_components/test_dropdown.py -k "placement or avatar or text_trigger or hover or htmx or nested" -v)
- [X] T064 [US3] Run type checking (mypy src/flowbite_htmy/components/dropdown.py --strict)

**Checkpoint**: All user stories now independently functional - full dropdown feature set complete

---

## Phase 6: Showcase & Integration

**Purpose**: Create showcase application and integrate with consolidated showcase

- [X] T065 [P] Create examples/dropdowns.py with FastAPI app and basic dropdown section
- [X] T066 [P] Create examples/templates/dropdowns.html.jinja with Flowbite CSS/JS includes
- [X] T067 Add Section 1 (Basic dropdown) to examples/dropdowns.py
- [X] T068 Add Section 2 (Dropdown with header and dividers) to examples/dropdowns.py
- [X] T069 Add Section 3 (Color variants) to examples/dropdowns.py
- [X] T070 Add Section 4 (Size variants) to examples/dropdowns.py
- [X] T071 Add Section 5 (Placement options) to examples/dropdowns.py
- [X] T072 Add Section 6 (Avatar trigger - user menu) to examples/dropdowns.py
- [X] T073 Add Section 7 (Text trigger) to examples/dropdowns.py
- [X] T074 Add Section 8 (Hover trigger) to examples/dropdowns.py
- [X] T075 Add Section 9 (Dropdowns with icons) to examples/dropdowns.py
- [X] T076 Add Section 10 (Multi-level dropdown) to examples/dropdowns.py
- [X] T077 Test standalone showcase by running python examples/dropdowns.py and visiting http://localhost:8000
- [X] T078 Add dropdown route to examples/showcase.py for consolidated showcase
- [X] T079 Add dropdown navigation link to consolidated showcase sidebar

---

## Phase 7: Polish & Quality Assurance

**Purpose**: Ensure code quality, documentation, and test coverage

- [X] T080 [P] Run full test suite and verify >90% coverage (pytest --cov=src/flowbite_htmy/components/dropdown --cov-report=term-missing)
- [X] T081 [P] Add docstrings to all Dropdown component classes and methods in src/flowbite_htmy/components/dropdown.py
- [X] T082 [P] Run mypy strict type checking on entire component (mypy src/flowbite_htmy/components/dropdown.py --strict)
- [X] T083 [P] Run ruff linting and fix any issues (ruff check src/flowbite_htmy/components/dropdown.py --fix)
- [X] T084 [P] Run ruff formatting (ruff format src/flowbite_htmy/components/dropdown.py)
- [X] T085 Add edge case tests (empty items list, disabled dropdown, custom dropdown_id) in tests/test_components/test_dropdown.py
- [ ] T086 Test keyboard navigation (Tab, Escape) via Chrome DevTools E2E testing (document findings in session note)
- [ ] T087 Test ARIA attributes with screen reader or accessibility inspector (document findings in session note)
- [ ] T088 Update CLAUDE.md if any new patterns or gotchas discovered
- [X] T089 Run final verification: pytest && mypy src/flowbite_htmy && ruff check src/flowbite_htmy

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - US1 can start after Phase 2
  - US2 can start after Phase 2 (builds on US1 but independently testable)
  - US3 can start after Phase 2 (builds on US1 & US2 but independently testable)
- **Showcase (Phase 6)**: Depends on at least US1 being complete (ideally all stories)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Enhances US1 components but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Adds advanced features to US1/US2 but independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation (strict TDD)
- Enums before classes
- Simple classes (Divider, Header, Item) before complex class (Dropdown)
- Core Dropdown methods before trigger variants
- Basic functionality before advanced features

### Parallel Opportunities

- All Setup enum tests (T002-T004) can run in parallel
- All Foundational enum implementations (T005-T007) can run in parallel
- All US1 test writing (T010-T017) can run in parallel
- All US1 simple class implementations (T020-T021) can run in parallel
- All US2 test writing (T033-T037) can run in parallel
- All US2 enhancements can run in parallel (different methods)
- All US3 test writing (T048-T053) can run in parallel
- US3 trigger implementations (T055-T056) can run in parallel
- Showcase sections (T067-T076) can be added in parallel
- Polish tasks (T080-T084) can run in parallel

---

## Parallel Example: User Story 1 Tests

```bash
# Launch all US1 tests together (write in parallel):
Task T010: "Write test for DropdownDivider rendering"
Task T011: "Write test for DropdownDivider with custom class"
Task T012: "Write test for DropdownHeader rendering"
Task T013: "Write test for DropdownHeader with custom class"
Task T014: "Write test for DropdownItem simple rendering"
Task T015: "Write test for Dropdown basic rendering"
Task T016: "Write test for Dropdown ARIA attributes"
Task T017: "Write test for Dropdown Flowbite data attributes"

# Then run all tests to confirm FAIL:
Task T018: pytest tests/test_components/test_dropdown.py -k "US1" -v
```

---

## Parallel Example: User Story 1 Implementation

```bash
# Launch simple classes in parallel (different files not needed, just independent logic):
Task T020: "Implement DropdownDivider class"
Task T021: "Implement DropdownHeader class"

# Then implement DropdownItem and Dropdown sequentially (Dropdown depends on Item)
Task T022: "Implement DropdownItem class"
Task T023-T028: "Implement Dropdown class methods"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T009) - CRITICAL
3. Complete Phase 3: User Story 1 (T010-T032)
4. **STOP and VALIDATE**: Run all US1 tests independently
5. Optional: Create minimal showcase (just Section 1) to demo

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Basic dropdown works! (MVP)
3. Add User Story 2 → Test independently → Customization added!
4. Add User Story 3 → Test independently → Full feature set!
5. Add Showcase → Visual demonstration
6. Polish → Production ready

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T009)
2. Once Phase 2 done:
   - Developer A: User Story 1 (T010-T032) - Core dropdown
   - Developer B: User Story 2 tests (T033-T038) - Prepare customization tests
   - Developer C: User Story 3 tests (T048-T054) - Prepare advanced tests
3. After US1 complete:
   - Developer A: Showcase (T065-T079)
   - Developer B: User Story 2 implementation (T039-T047)
   - Developer C: User Story 3 implementation (T055-T064)
4. All converge on Polish (T080-T089)

---

## Notes

- [P] tasks = different files or independent logic, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (TDD Red-Green-Refactor)
- Run tests frequently: after each implementation task
- Commit after each logical group of tasks
- Stop at any checkpoint to validate story independently
- Coverage target: >90% (enforced by pytest config)
- Type coverage: 100% (mypy strict mode)
- Follow quickstart.md TDD workflow for detailed step-by-step guidance

---

## Task Count Summary

- **Phase 1 (Setup)**: 4 tasks
- **Phase 2 (Foundational)**: 5 tasks
- **Phase 3 (User Story 1)**: 23 tasks (8 tests + 15 implementation)
- **Phase 4 (User Story 2)**: 15 tasks (6 tests + 9 implementation)
- **Phase 5 (User Story 3)**: 17 tasks (7 tests + 10 implementation)
- **Phase 6 (Showcase)**: 15 tasks
- **Phase 7 (Polish)**: 10 tasks

**Total**: 89 tasks

**Test Tasks**: 21 (strict TDD approach)
**Implementation Tasks**: 34
**Showcase Tasks**: 15
**Quality Tasks**: 10
**Setup/Foundational Tasks**: 9

**Parallel Opportunities**: 35+ tasks marked [P]
