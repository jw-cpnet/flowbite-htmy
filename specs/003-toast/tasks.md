# Tasks: Toast Component

**Input**: Design documents from `/specs/003-toast/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/toast-component.md

**Tests**: TDD approach (Test-Driven Development) is mandatory per constitution. Tests MUST be written before implementation for each user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/flowbite_htmy/`, `tests/`, `examples/` at repository root
- Component: `src/flowbite_htmy/components/toast.py`
- Types: `src/flowbite_htmy/types/toast.py`
- Tests: `tests/test_components/test_toast.py`
- Showcase: `examples/toasts.py`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create file structure and enum for Toast component

- [ ] T001 [P] Create ToastVariant enum in src/flowbite_htmy/types/toast.py
- [ ] T002 [P] Export ToastVariant from src/flowbite_htmy/types/__init__.py
- [ ] T003 [P] Create empty Toast component file in src/flowbite_htmy/components/toast.py
- [ ] T004 [P] Create test file tests/test_components/test_toast.py
- [ ] T005 Verify pytest runs without errors on new test file

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core Toast component structure that MUST be complete before user story implementation

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 [P] Define ToastActionButton dataclass in src/flowbite_htmy/components/toast.py with HTMX attributes
- [ ] T007 [P] Define Toast dataclass skeleton with all fields (message, variant, icon, dismissible, id, action_button, avatar_src, class_) in src/flowbite_htmy/components/toast.py
- [ ] T008 [P] Add Toast import to src/flowbite_htmy/components/__init__.py
- [ ] T009 Verify imports work correctly (from flowbite_htmy.components import Toast, ToastActionButton)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Simple Toast Notifications (Priority: P1) 🎯 MVP

**Goal**: Implement basic toast with message, 4 variants (SUCCESS, DANGER, WARNING, INFO), default icons, and dismissible close button. This is the core MVP functionality that delivers a complete notification system.

**Independent Test**: Create toasts with different variants, verify icon display, message rendering, and dismiss button. Each variant renders with correct colors and icons. Dismissible flag controls close button visibility.

### Tests for User Story 1 - RED Phase (Write Failing Tests)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Write test_toast_renders_default in tests/test_components/test_toast.py - test minimal props (message only)
- [ ] T011 [P] [US1] Write test_toast_variant_success in tests/test_components/test_toast.py - verify green colors and checkmark icon
- [ ] T012 [P] [US1] Write test_toast_variant_danger in tests/test_components/test_toast.py - verify red colors and X icon
- [ ] T013 [P] [US1] Write test_toast_variant_warning in tests/test_components/test_toast.py - verify yellow colors and exclamation icon
- [ ] T014 [P] [US1] Write test_toast_variant_info in tests/test_components/test_toast.py - verify blue colors and info icon
- [ ] T015 [P] [US1] Write test_toast_dismissible_true in tests/test_components/test_toast.py - verify close button with data-dismiss-target
- [ ] T016 [P] [US1] Write test_toast_dismissible_false in tests/test_components/test_toast.py - verify no close button rendered
- [ ] T017 [P] [US1] Write test_toast_auto_generates_id in tests/test_components/test_toast.py - verify unique ID when id=None
- [ ] T018 [P] [US1] Write test_toast_uses_custom_id in tests/test_components/test_toast.py - verify custom ID used when provided
- [ ] T019 [US1] Run all US1 tests - verify they FAIL (RED phase complete)

### Implementation for User Story 1 - GREEN Phase (Make Tests Pass)

- [ ] T020 [P] [US1] Implement Toast._get_icon() method in src/flowbite_htmy/components/toast.py - map variants to default icons
- [ ] T021 [P] [US1] Define VARIANT_ICON_CLASSES dictionary in src/flowbite_htmy/components/toast.py - map variants to Tailwind classes
- [ ] T022 [US1] Implement Toast._build_classes() method in src/flowbite_htmy/components/toast.py - build container classes with dark mode
- [ ] T023 [US1] Implement Toast._render_icon_container() method in src/flowbite_htmy/components/toast.py - render icon with variant colors
- [ ] T024 [US1] Implement Toast._render_close_button() method in src/flowbite_htmy/components/toast.py - render dismissible button with data-dismiss-target
- [ ] T025 [US1] Implement Toast.htmy() method in src/flowbite_htmy/components/toast.py - compose full toast structure (icon + message + close button)
- [ ] T026 [US1] Run all US1 tests - verify they PASS (GREEN phase complete)

### Refactor Phase for User Story 1

- [ ] T027 [US1] Run mypy on src/flowbite_htmy/components/toast.py and src/flowbite_htmy/types/toast.py - verify 100% type coverage
- [ ] T028 [US1] Run ruff check on src/flowbite_htmy/components/toast.py and src/flowbite_htmy/types/toast.py - verify no linting errors
- [ ] T029 [US1] Run ruff format on src/flowbite_htmy/components/toast.py and src/flowbite_htmy/types/toast.py - auto-format code
- [ ] T030 [US1] Run coverage on tests/test_components/test_toast.py - verify >90% coverage for US1 code

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. Basic toasts with all 4 variants work correctly.

---

## Phase 4: User Story 2 - Interactive Toast (Priority: P2)

**Goal**: Extend toast to support action buttons with HTMX integration and rich content (avatars). Enables interactive notifications like "Reply", "Undo", chat messages with user avatars.

**Independent Test**: Create toasts with action buttons and verify HTMX attributes render correctly (hx-get, hx-post, hx-target). Create toasts with avatar_src and verify image renders. All US1 functionality continues to work.

### Tests for User Story 2 - RED Phase (Write Failing Tests)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T031 [P] [US2] Write test_toast_with_action_button in tests/test_components/test_toast.py - verify action button label renders
- [ ] T032 [P] [US2] Write test_toast_action_button_htmx_get in tests/test_components/test_toast.py - verify hx-get attribute renders
- [ ] T033 [P] [US2] Write test_toast_action_button_htmx_post in tests/test_components/test_toast.py - verify hx-post and hx-target attributes
- [ ] T034 [P] [US2] Write test_toast_without_action_button in tests/test_components/test_toast.py - verify no button when action_button=None
- [ ] T035 [P] [US2] Write test_toast_with_avatar in tests/test_components/test_toast.py - verify avatar image renders with src
- [ ] T036 [P] [US2] Write test_toast_without_avatar in tests/test_components/test_toast.py - verify no avatar when avatar_src=None
- [ ] T037 [US2] Run all US2 tests - verify they FAIL (RED phase complete)

### Implementation for User Story 2 - GREEN Phase (Make Tests Pass)

- [ ] T038 [P] [US2] Implement Toast._render_action_button() method in src/flowbite_htmy/components/toast.py - render button with HTMX attributes
- [ ] T039 [P] [US2] Implement Toast._render_avatar() method in src/flowbite_htmy/components/toast.py - render circular avatar image
- [ ] T040 [US2] Update Toast.htmy() method in src/flowbite_htmy/components/toast.py - integrate action button and avatar rendering
- [ ] T041 [US2] Update Toast._render_content() structure in src/flowbite_htmy/components/toast.py - handle rich content layout with avatar
- [ ] T042 [US2] Run all US2 tests - verify they PASS (GREEN phase complete)
- [ ] T043 [US2] Run all US1 tests again - verify US1 still works (regression check)

### Refactor Phase for User Story 2

- [ ] T044 [US2] Run mypy on updated toast.py - verify 100% type coverage including new methods
- [ ] T045 [US2] Run ruff check and format on toast.py - verify clean code
- [ ] T046 [US2] Run coverage on test_toast.py - verify >95% coverage for US1+US2 combined

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. Interactive toasts with buttons and avatars function correctly.

---

## Phase 5: User Story 3 - Custom Styling and Accessibility (Priority: P3)

**Goal**: Ensure toasts support custom CSS classes (class_ prop), include proper ARIA attributes for screen readers, and always include dark mode styling. Production-ready accessibility and customization.

**Independent Test**: Verify role="alert" on container, aria-hidden="true" on icons, sr-only labels on close button, dark: classes always present, custom classes merge correctly. All US1 and US2 functionality continues to work.

### Tests for User Story 3 - RED Phase (Write Failing Tests)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T047 [P] [US3] Write test_toast_role_alert in tests/test_components/test_toast.py - verify role="alert" attribute present
- [ ] T048 [P] [US3] Write test_toast_aria_hidden_on_icon in tests/test_components/test_toast.py - verify aria-hidden="true" on icon SVG
- [ ] T049 [P] [US3] Write test_toast_sr_only_close_label in tests/test_components/test_toast.py - verify sr-only "Close" text in close button
- [ ] T050 [P] [US3] Write test_toast_dark_mode_classes in tests/test_components/test_toast.py - verify dark:bg-gray-800, dark:text-gray-400 classes present
- [ ] T051 [P] [US3] Write test_toast_custom_classes in tests/test_components/test_toast.py - verify class_ parameter merges with component classes
- [ ] T052 [P] [US3] Write test_toast_custom_icon_override in tests/test_components/test_toast.py - verify icon prop overrides default variant icon
- [ ] T053 [US3] Run all US3 tests - verify they FAIL (RED phase complete)

### Implementation for User Story 3 - GREEN Phase (Make Tests Pass)

- [ ] T054 [US3] Update Toast._render_icon_container() in src/flowbite_htmy/components/toast.py - add aria-hidden="true" to icon SVG
- [ ] T055 [US3] Update Toast._render_close_button() in src/flowbite_htmy/components/toast.py - add <span class="sr-only">Close</span>
- [ ] T056 [US3] Update Toast.htmy() in src/flowbite_htmy/components/toast.py - ensure role="alert" attribute on container
- [ ] T057 [US3] Verify Toast._build_classes() in src/flowbite_htmy/components/toast.py - confirm dark mode classes always included (already implemented in US1)
- [ ] T058 [US3] Verify Toast._build_classes() merges self.class_ correctly (already implemented in US1)
- [ ] T059 [US3] Verify Toast._get_icon() respects self.icon override (already implemented in US1)
- [ ] T060 [US3] Run all US3 tests - verify they PASS (GREEN phase complete)
- [ ] T061 [US3] Run all US1 and US2 tests again - verify no regressions

### Refactor Phase for User Story 3

- [ ] T062 [US3] Run mypy on complete toast.py - verify 100% type coverage for all code
- [ ] T063 [US3] Run ruff check and format on toast.py - final cleanup
- [ ] T064 [US3] Run full test suite on test_toast.py - verify >95% coverage across all user stories
- [ ] T065 [US3] Add docstrings to all Toast methods in src/flowbite_htmy/components/toast.py - document public API

**Checkpoint**: All user stories should now be independently functional. Toast component is feature-complete with accessibility and customization.

---

## Phase 6: Edge Cases and Error Handling

**Purpose**: Handle edge cases and add validation for Toast component

- [ ] T066 [P] Write test_toast_long_message in tests/test_components/test_toast.py - verify text wraps within max-w-xs
- [ ] T067 [P] Write test_toast_message_with_html_entities in tests/test_components/test_toast.py - verify htmy escapes HTML correctly
- [ ] T068 [P] Write test_toast_empty_message_validation in tests/test_components/test_toast.py - verify ValueError on empty message (optional validation)
- [ ] T069 [P] Implement message validation in Toast.__post_init__() in src/flowbite_htmy/components/toast.py (if desired)
- [ ] T070 Run all edge case tests - verify they pass

---

## Phase 7: Showcase Application

**Purpose**: Create comprehensive showcase demonstrating all Toast features

- [ ] T071 [P] Create examples/toasts.py file with build_toasts_showcase() function
- [ ] T072 [P] Implement _section_basic_variants() in examples/toasts.py - showcase all 4 variants
- [ ] T073 [P] Implement _section_custom_icons() in examples/toasts.py - showcase custom icon override
- [ ] T074 [P] Implement _section_dismissible() in examples/toasts.py - showcase dismissible=True and False
- [ ] T075 [P] Implement _section_interactive() in examples/toasts.py - showcase action buttons with HTMX
- [ ] T076 [P] Implement _section_rich_content() in examples/toasts.py - showcase avatars and formatted content
- [ ] T077 [P] Implement _section_custom_styling() in examples/toasts.py - showcase class_ parameter customization
- [ ] T078 Add /toasts route to examples/showcase.py - integrate build_toasts_showcase()
- [ ] T079 Add "Toasts" navigation entry to ROUTES in examples/showcase.py
- [ ] T080 Test showcase locally - run python examples/showcase.py and visit http://localhost:8000/toasts
- [ ] T081 Verify all 6 showcase sections render correctly in browser
- [ ] T082 Test dark mode toggle in showcase - verify dark classes activate

**Checkpoint**: Showcase complete with 6 comprehensive sections demonstrating all Toast features

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and documentation

- [ ] T083 Run full pytest suite - verify all 164+ existing tests plus 22+ new Toast tests pass
- [ ] T084 Run pytest coverage - verify Toast component has >95% coverage
- [ ] T085 Run mypy strict mode on entire src/flowbite_htmy/ - verify 100% type coverage
- [ ] T086 Run ruff check on entire src/flowbite_htmy/ - verify no linting errors
- [ ] T087 Run ruff format on entire src/flowbite_htmy/ - auto-format all code
- [ ] T088 [P] Review Toast docstrings - ensure all public methods documented
- [ ] T089 [P] Review ToastVariant docstring - ensure enum values documented
- [ ] T090 [P] Review ToastActionButton docstring - ensure props documented
- [ ] T091 Verify ToastVariant exported from flowbite_htmy root - test import flowbite_htmy
- [ ] T092 Verify Toast exported from flowbite_htmy root - test from flowbite_htmy import Toast
- [ ] T093 Update CLAUDE.md if needed - add Toast component to completed components list
- [ ] T094 Run final validation - verify quickstart.md success criteria checklist complete

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories SHOULD proceed sequentially in priority order (P1 → P2 → P3) for TDD clarity
  - But CAN proceed in parallel if team has multiple developers
- **Edge Cases (Phase 6)**: Depends on Phase 3-5 completion
- **Showcase (Phase 7)**: Depends on all user stories being complete
- **Polish (Phase 8)**: Depends on Showcase completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories - MVP target
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Extends US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Adds quality features but should be independently testable

### Within Each User Story (TDD Cycle)

1. **RED Phase**: Write tests, verify they FAIL
2. **GREEN Phase**: Implement code, verify tests PASS
3. **REFACTOR Phase**: Type check, lint, format, optimize
4. **REGRESSION**: Run previous user story tests to ensure no breakage

### Parallel Opportunities

**Within Setup (Phase 1)**:
- T001, T002, T003, T004 can all run in parallel (different files)

**Within Foundational (Phase 2)**:
- T006, T007, T008 can run in parallel (different parts of same file, but independent)

**Within User Story RED Phases**:
- All test writing tasks marked [P] can run in parallel (different test functions)

**Within User Story GREEN Phases**:
- Some implementation tasks marked [P] can run in parallel (different helper methods)

**Within Showcase (Phase 7)**:
- T071-T077 can all run in parallel (different section functions)
- T088, T089, T090 can run in parallel (different docstrings)

**Across User Stories** (if team has capacity):
- US1, US2, US3 can be worked on in parallel by different developers AFTER Foundational phase

---

## Parallel Example: User Story 1 RED Phase

```bash
# Launch all test writing tasks for User Story 1 together:
Task T010: "Write test_toast_renders_default in tests/test_components/test_toast.py"
Task T011: "Write test_toast_variant_success in tests/test_components/test_toast.py"
Task T012: "Write test_toast_variant_danger in tests/test_components/test_toast.py"
Task T013: "Write test_toast_variant_warning in tests/test_components/test_toast.py"
Task T014: "Write test_toast_variant_info in tests/test_components/test_toast.py"
Task T015: "Write test_toast_dismissible_true in tests/test_components/test_toast.py"
Task T016: "Write test_toast_dismissible_false in tests/test_components/test_toast.py"
Task T017: "Write test_toast_auto_generates_id in tests/test_components/test_toast.py"
Task T018: "Write test_toast_uses_custom_id in tests/test_components/test_toast.py"

# Then run T019 to verify all tests FAIL
```

## Parallel Example: User Story 1 GREEN Phase

```bash
# Launch independent implementation tasks together:
Task T020: "Implement Toast._get_icon() method" (independent)
Task T021: "Define VARIANT_ICON_CLASSES dictionary" (independent)

# Then proceed with dependent tasks:
Task T022: "Implement Toast._build_classes() method"
Task T023: "Implement Toast._render_icon_container() method"
Task T024: "Implement Toast._render_close_button() method"
Task T025: "Implement Toast.htmy() method" (depends on all helpers)
```

## Parallel Example: Showcase Sections

```bash
# Launch all showcase section implementations together:
Task T072: "Implement _section_basic_variants() in examples/toasts.py"
Task T073: "Implement _section_custom_icons() in examples/toasts.py"
Task T074: "Implement _section_dismissible() in examples/toasts.py"
Task T075: "Implement _section_interactive() in examples/toasts.py"
Task T076: "Implement _section_rich_content() in examples/toasts.py"
Task T077: "Implement _section_custom_styling() in examples/toasts.py"

# All sections are independent and can be developed in parallel
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T006-T009) - CRITICAL blocker
3. Complete Phase 3: User Story 1 (T010-T030)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Optional: Create minimal showcase for US1 only
6. Decision point: Deploy MVP or continue to US2/US3

**MVP Deliverable**: Basic toast notifications with 4 variants, icons, and dismiss button (22 tests, >95% coverage)

### Incremental Delivery (Recommended)

1. Complete Setup + Foundational (T001-T009) → Foundation ready
2. Add User Story 1 (T010-T030) → Test independently → **MVP Complete**
3. Add User Story 2 (T031-T046) → Test independently → **Interactive Toasts Ready**
4. Add User Story 3 (T047-T065) → Test independently → **Accessible & Customizable**
5. Add Edge Cases (T066-T070) → **Robust Error Handling**
6. Add Showcase (T071-T082) → **Complete Documentation**
7. Polish (T083-T094) → **Production Ready**

Each user story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T009)
2. Once Foundational is done:
   - **Developer A**: User Story 1 (T010-T030) - Priority focus
   - **Developer B**: User Story 2 (T031-T046) - Can start in parallel
   - **Developer C**: User Story 3 (T047-T065) - Can start in parallel
3. Synchronize and test integration
4. Team completes Showcase together (T071-T082)
5. Team completes Polish together (T083-T094)

---

## Task Count Summary

- **Phase 1 (Setup)**: 5 tasks
- **Phase 2 (Foundational)**: 4 tasks (BLOCKING)
- **Phase 3 (US1 - Simple Toast)**: 21 tasks (RED: 10, GREEN: 7, REFACTOR: 4)
- **Phase 4 (US2 - Interactive)**: 16 tasks (RED: 7, GREEN: 6, REFACTOR: 3)
- **Phase 5 (US3 - Accessibility)**: 18 tasks (RED: 7, GREEN: 8, REFACTOR: 3)
- **Phase 6 (Edge Cases)**: 5 tasks
- **Phase 7 (Showcase)**: 12 tasks
- **Phase 8 (Polish)**: 12 tasks

**Total**: 93 tasks

**Parallelizable**: 41 tasks marked [P] (44% can run in parallel)

**Independent User Stories**: 3 stories can be tested independently

**MVP Scope**: 30 tasks (Setup + Foundational + US1) for basic toast functionality

---

## Notes

- **[P] tasks** = different files or independent sections, no dependencies within their phase
- **[Story] label** maps task to specific user story for traceability and independent testing
- **Each user story** follows strict TDD cycle: RED → GREEN → REFACTOR
- **Tests written FIRST** (RED phase) before any implementation (GREEN phase)
- **Regression checks** after each user story to ensure previous stories still work
- **Verify tests fail** before implementing (critical for TDD validity)
- **Commit strategy**: Commit after each phase completion (RED complete, GREEN complete, REFACTOR complete)
- **Stop at any checkpoint** to validate story independently
- **Constitution compliance**:
  - ✅ TDD enforced (RED-GREEN-REFACTOR per story)
  - ✅ Type safety (mypy tasks in each REFACTOR phase)
  - ✅ Quality gates (coverage >95%, ruff checks)
  - ✅ Component value (Toast reduces boilerplate, enforces patterns)
  - ✅ Architecture (dataclass with htmy() method, ClassBuilder, dark mode)
