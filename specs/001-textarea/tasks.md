# Tasks: Textarea Component

**Input**: Design documents from `/specs/001-textarea/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: This project follows TDD (constitution principle I). All tests are REQUIRED and must be written FIRST before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/flowbite_htmy/`, `tests/test_components/`, `examples/`
- All paths are at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and ensure development environment is ready

- [ ] T001 Verify Python 3.11+ virtual environment is activated
- [ ] T002 [P] Verify pytest, mypy, ruff are installed and configured
- [ ] T003 [P] Review existing Input component pattern in src/flowbite_htmy/components/input.py for validation reference
- [ ] T004 [P] Review existing Checkbox component pattern in src/flowbite_htmy/components/checkbox.py for label handling reference
- [ ] T005 [P] Review research.md for extracted patterns and design decisions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core type definitions and test fixtures - MUST be complete before ANY user story implementation

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Check if ValidationState type exists in src/flowbite_htmy/types/validation.py (if not, define inline in textarea.py following Input pattern)
- [ ] T007 Verify test fixtures (renderer, context, dark_context) exist in tests/conftest.py

**Checkpoint**: Foundation ready - user story implementation can now begin (TDD: write tests first!)

---

## Phase 3: User Story 1 - Basic Multi-line Text Input (Priority: P1) 🎯 MVP

**Goal**: Implement core textarea rendering with label, placeholder, and value support. Users can enter multi-line text with proper Flowbite styling and dark mode classes.

**Independent Test**: Render a textarea with label, verify HTML structure, Flowbite classes present, dark mode classes included, label-for-id association working, placeholder visible, and pre-filled value displays correctly.

### Tests for User Story 1 (TDD: WRITE THESE FIRST) ⚠️

> **CRITICAL TDD WORKFLOW**:
> 1. Write test
> 2. Run test → Should FAIL (component doesn't exist yet)
> 3. Implement minimal code
> 4. Run test → Should PASS
> 5. Refactor if needed
> 6. Move to next test

- [ ] T008 [P] [US1] Write test for default textarea rendering (label + textarea structure) in tests/test_components/test_textarea.py
- [ ] T009 [P] [US1] Write test for textarea with ID and label-for-id association in tests/test_components/test_textarea.py
- [ ] T010 [P] [US1] Write test for placeholder attribute rendering in tests/test_components/test_textarea.py
- [ ] T011 [P] [US1] Write test for value (pre-filled content) rendering in tests/test_components/test_textarea.py
- [ ] T012 [P] [US1] Write test for default rows=4 rendering in tests/test_components/test_textarea.py
- [ ] T013 [P] [US1] Write test for dark mode classes always present in tests/test_components/test_textarea.py
- [ ] T014 [P] [US1] Write test for Flowbite CSS base classes (block p-2.5 w-full text-sm rounded-lg border) in tests/test_components/test_textarea.py
- [ ] T015 [P] [US1] Write test for focus ring classes (focus:ring-blue-500 focus:border-blue-500) in tests/test_components/test_textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 8 tests should FAIL

### Implementation for User Story 1

- [ ] T016 [US1] Create Textarea component skeleton (dataclass with id, label props only) in src/flowbite_htmy/components/textarea.py
- [ ] T017 [US1] Implement htmy() method with basic label + textarea rendering in src/flowbite_htmy/components/textarea.py
- [ ] T018 [US1] Add placeholder prop and rendering logic in src/flowbite_htmy/components/textarea.py
- [ ] T019 [US1] Add value prop for pre-filled content in src/flowbite_htmy/components/textarea.py
- [ ] T020 [US1] Add rows prop (default=4) in src/flowbite_htmy/components/textarea.py
- [ ] T021 [US1] Implement _build_label_classes() method (base classes only, no validation yet) in src/flowbite_htmy/components/textarea.py
- [ ] T022 [US1] Implement _build_textarea_classes() method with Flowbite base classes and dark mode in src/flowbite_htmy/components/textarea.py
- [ ] T023 [US1] Implement _build_textarea_attrs() method (id, rows, placeholder, value) in src/flowbite_htmy/components/textarea.py
- [ ] T024 [US1] Export Textarea from src/flowbite_htmy/components/__init__.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 8 tests should PASS

**Type Check**: `mypy src/flowbite_htmy/components/textarea.py --strict` → Should pass with 100% coverage

**Checkpoint**: Basic textarea rendering complete. Component can render with label, placeholder, value, and proper styling. This is the MVP - fully functional for basic use cases.

---

## Phase 4: User Story 2 - Validation Feedback (Priority: P2)

**Goal**: Add validation states (success, error) with colored borders and helper text that matches validation state. Users get visual feedback on form validation.

**Independent Test**: Render textareas in success/error/default states, verify border colors (green/red/default), verify helper text colors match, verify label colors match validation state.

### Tests for User Story 2 (TDD: WRITE THESE FIRST) ⚠️

- [ ] T025 [P] [US2] Write test for validation="success" with green border and text classes in tests/test_components/test_textarea.py
- [ ] T026 [P] [US2] Write test for validation="error" with red border and text classes in tests/test_components/test_textarea.py
- [ ] T027 [P] [US2] Write test for validation=None (default) with neutral colors in tests/test_components/test_textarea.py
- [ ] T028 [P] [US2] Write test for helper text rendering with id="{id}-helper" in tests/test_components/test_textarea.py
- [ ] T029 [P] [US2] Write test for helper text color matching validation state (green/red/gray) in tests/test_components/test_textarea.py
- [ ] T030 [P] [US2] Write test for label color matching validation state in tests/test_components/test_textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py::test_validation* -v` → All 6 new tests should FAIL

### Implementation for User Story 2

- [ ] T031 [US2] Add validation prop (ValidationState type) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T032 [US2] Add helper_text prop to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T033 [US2] Update _build_label_classes() to handle validation state colors in src/flowbite_htmy/components/textarea.py
- [ ] T034 [US2] Update _build_textarea_classes() to handle success/error validation styling in src/flowbite_htmy/components/textarea.py
- [ ] T035 [US2] Implement _render_helper_text() method with color matching in src/flowbite_htmy/components/textarea.py
- [ ] T036 [US2] Update htmy() method to conditionally render helper text in src/flowbite_htmy/components/textarea.py
- [ ] T037 [US2] Add aria_describedby attribute to textarea when helper_text exists in src/flowbite_htmy/components/textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 14 tests (8 from US1 + 6 from US2) should PASS

**Type Check**: `mypy src/flowbite_htmy/components/textarea.py --strict` → Should pass

**Checkpoint**: Validation feedback complete. Component now supports visual feedback for form validation with helper text.

---

## Phase 5: User Story 3 - Size and Layout Control (Priority: P3)

**Goal**: Allow users to control textarea height via rows parameter and support custom width via class_ parameter. Handles edge case of invalid rows (clamping to minimum of 1).

**Independent Test**: Render textareas with different row counts (3, 5, 10, default), verify rows attribute in HTML, test rows clamping (rows=0 becomes 1, rows=-5 becomes 1), verify custom class_ parameter merges with component classes.

### Tests for User Story 3 (TDD: WRITE THESE FIRST) ⚠️

- [ ] T038 [P] [US3] Write test for custom rows=3 rendering in tests/test_components/test_textarea.py
- [ ] T039 [P] [US3] Write test for custom rows=10 rendering in tests/test_components/test_textarea.py
- [ ] T040 [P] [US3] Write test for rows=0 clamping to rows=1 in tests/test_components/test_textarea.py
- [ ] T041 [P] [US3] Write test for rows=-5 clamping to rows=1 in tests/test_components/test_textarea.py
- [ ] T042 [P] [US3] Write test for class_ parameter merging with component classes in tests/test_components/test_textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py::test_rows* tests/test_components/test_textarea.py::test_class* -v` → All 5 new tests should FAIL

### Implementation for User Story 3

- [ ] T043 [US3] Add class_ prop to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T044 [US3] Implement rows clamping logic (max(1, self.rows)) in _build_textarea_attrs() in src/flowbite_htmy/components/textarea.py
- [ ] T045 [US3] Update htmy() method to apply class_ to wrapper div in src/flowbite_htmy/components/textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 19 tests should PASS

**Type Check**: `mypy src/flowbite_htmy/components/textarea.py --strict` → Should pass

**Checkpoint**: Size control complete. Users can customize textarea height and width.

---

## Phase 6: User Story 4 - Accessibility and States (Priority: P4)

**Goal**: Support required, disabled, readonly states with proper visual indicators and ARIA attributes. Required fields show asterisk in label. Disabled state overrides readonly. All states have proper accessibility markup.

**Independent Test**: Render textareas in required/disabled/readonly states, verify HTML attributes, verify label asterisk for required, verify disabled styling (grayed out, cursor-not-allowed), verify readonly attribute, verify disabled takes precedence over readonly, verify ARIA attributes.

### Tests for User Story 4 (TDD: WRITE THESE FIRST) ⚠️

- [ ] T046 [P] [US4] Write test for required attribute rendering in tests/test_components/test_textarea.py
- [ ] T047 [P] [US4] Write test for required=True appending asterisk to label (e.g., "Comment" → "Comment *") in tests/test_components/test_textarea.py
- [ ] T048 [P] [US4] Write test for disabled attribute rendering with grayed styling in tests/test_components/test_textarea.py
- [ ] T049 [P] [US4] Write test for disabled cursor-not-allowed class in tests/test_components/test_textarea.py
- [ ] T050 [P] [US4] Write test for readonly attribute rendering in tests/test_components/test_textarea.py
- [ ] T051 [P] [US4] Write test for disabled=True with readonly=True (disabled should win, no readonly attribute) in tests/test_components/test_textarea.py
- [ ] T052 [P] [US4] Write test for name attribute (optional, None by default) in tests/test_components/test_textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py::test_required* tests/test_components/test_textarea.py::test_disabled* tests/test_components/test_textarea.py::test_readonly* tests/test_components/test_textarea.py::test_name* -v` → All 7 new tests should FAIL

### Implementation for User Story 4

- [ ] T053 [US4] Add required prop (bool, default=False) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T054 [US4] Add disabled prop (bool, default=False) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T055 [US4] Add readonly prop (bool, default=False) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T056 [US4] Add name prop (str | None = None) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T057 [US4] Implement _get_display_label() method that appends " *" when required=True in src/flowbite_htmy/components/textarea.py
- [ ] T058 [US4] Update htmy() method to use _get_display_label() for label text in src/flowbite_htmy/components/textarea.py
- [ ] T059 [US4] Update _build_textarea_classes() to add disabled styling (cursor-not-allowed, bg-gray-100) when disabled=True in src/flowbite_htmy/components/textarea.py
- [ ] T060 [US4] Update _build_textarea_attrs() to add required attribute when required=True in src/flowbite_htmy/components/textarea.py
- [ ] T061 [US4] Update _build_textarea_attrs() to add disabled attribute when disabled=True in src/flowbite_htmy/components/textarea.py
- [ ] T062 [US4] Update _build_textarea_attrs() to add readonly attribute when readonly=True AND disabled=False in src/flowbite_htmy/components/textarea.py
- [ ] T063 [US4] Update _build_textarea_attrs() to add name attribute when name is provided in src/flowbite_htmy/components/textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 26 tests should PASS

**Type Check**: `mypy src/flowbite_htmy/components/textarea.py --strict` → Should pass

**Checkpoint**: Accessibility and states complete. Component supports all standard form field states with proper ARIA markup.

---

## Phase 7: HTMX Integration & Passthrough Attributes

**Goal**: Support HTMX attributes for dynamic interactions and passthrough attrs dict for any additional HTML attributes.

**Independent Test**: Render textareas with HTMX attributes (hx_get, hx_post, etc.), verify they appear as hx-get, hx-post in HTML. Test attrs dict for custom attributes like spellcheck, maxlength.

### Tests for HTMX Integration (TDD: WRITE THESE FIRST) ⚠️

- [ ] T064 [P] Write test for hx_get attribute rendering as hx-get in tests/test_components/test_textarea.py
- [ ] T065 [P] Write test for hx_post attribute rendering as hx-post in tests/test_components/test_textarea.py
- [ ] T066 [P] Write test for multiple HTMX attributes (hx_get, hx_target, hx_swap) in tests/test_components/test_textarea.py
- [ ] T067 [P] Write test for attrs dict passthrough (spellcheck, maxlength) in tests/test_components/test_textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py::test_htmx* tests/test_components/test_textarea.py::test_attrs* -v` → All 4 new tests should FAIL

### Implementation for HTMX Integration

- [ ] T068 [P] Add HTMX props (hx_get, hx_post, hx_put, hx_patch, hx_delete, hx_target, hx_swap, hx_trigger) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T069 [P] Add attrs prop (dict[str, Any] | None = None) to Textarea dataclass in src/flowbite_htmy/components/textarea.py
- [ ] T070 Update _build_textarea_attrs() to include HTMX attributes when provided in src/flowbite_htmy/components/textarea.py
- [ ] T071 Update _build_textarea_attrs() to merge attrs dict (last, can override) in src/flowbite_htmy/components/textarea.py

**Run Tests**: `pytest tests/test_components/test_textarea.py -v` → All 30 tests should PASS

**Type Check**: `mypy src/flowbite_htmy/components/textarea.py --strict` → Should pass

**Checkpoint**: HTMX integration complete. Component ready for dynamic web applications.

---

## Phase 8: Showcase Application

**Goal**: Create visual examples demonstrating all Textarea features in a browser-testable application.

**Independent Test**: Run showcase app, navigate to Textarea section, verify all examples render correctly in both light and dark modes.

### Showcase Implementation

- [ ] T072 Create standalone showcase file examples/textareas.py with FastAPI app and Jinja template
- [ ] T073 Add Textarea section to examples/templates/showcase.html.jinja (for consolidated showcase)
- [ ] T074 Add Textarea examples (basic, validation, required, disabled, readonly, rows) to showcase
- [ ] T075 [P] Update examples/showcase.py to include Textarea in navigation if using consolidated showcase
- [ ] T076 [P] Add VS Code launch.json entry for Textarea showcase debugging

**Manual Test**: `python examples/textareas.py` → Navigate to http://localhost:8000 → Verify all examples render correctly

**Checkpoint**: Showcase complete. Users can see all Textarea features in action.

---

## Phase 9: Quality Validation & Documentation

**Goal**: Ensure code meets all quality gates and is production-ready.

### Quality Gates (ALL MUST PASS)

- [ ] T077 Run full test suite: `pytest tests/test_components/test_textarea.py -v` → All tests pass
- [ ] T078 Check test coverage: `pytest tests/test_components/test_textarea.py --cov=src/flowbite_htmy/components/textarea --cov-report=term-missing` → >95% coverage
- [ ] T079 Type check (strict mode): `mypy src/flowbite_htmy/components/textarea.py --strict` → 100% type coverage, no errors
- [ ] T080 Lint check: `ruff check src/flowbite_htmy/components/textarea.py` → No warnings or errors
- [ ] T081 Format check: `ruff format --check src/flowbite_htmy/components/textarea.py` → Already formatted
- [ ] T082 Format code: `ruff format src/flowbite_htmy/components/textarea.py` → Code formatted
- [ ] T083 Run full project test suite: `pytest` → All tests pass (including existing components)
- [ ] T084 Run full project type check: `mypy src/flowbite_htmy` → No errors
- [ ] T085 Run full project lint: `ruff check src/flowbite_htmy` → No errors

### Documentation Validation

- [ ] T086 [P] Verify quickstart.md examples are accurate and match implementation
- [ ] T087 [P] Verify API contract (contracts/textarea-api.md) matches implementation
- [ ] T088 [P] Add docstring examples to Textarea class in src/flowbite_htmy/components/textarea.py
- [ ] T089 Update CLAUDE.md Active Technologies section with Textarea component (if needed)

**Checkpoint**: All quality gates passed. Component is production-ready.

---

## Phase 10: Git Commit & Integration

**Goal**: Commit the complete, tested Textarea component to version control.

### Git Operations

- [ ] T090 Review all changes: `git status` and `git diff`
- [ ] T091 Stage component: `git add src/flowbite_htmy/components/textarea.py src/flowbite_htmy/components/__init__.py`
- [ ] T092 Stage tests: `git add tests/test_components/test_textarea.py`
- [ ] T093 Stage showcase: `git add examples/textareas.py examples/templates/`
- [ ] T094 Stage documentation: `git add specs/001-textarea/`
- [ ] T095 Create commit with message: "Implement Textarea component with full TDD (Phase 2B #2)"
- [ ] T096 Verify commit: `git log -1 --stat`

**Final Checkpoint**: Textarea component complete and committed. Ready for code review or merge.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all user stories
- **User Stories (Phases 3-6)**: All depend on Foundational completion
  - Can proceed in priority order (P1 → P2 → P3 → P4)
  - Higher priority stories MUST be tested independently before moving to next
- **HTMX Integration (Phase 7)**: Depends on US1-US4 completion
- **Showcase (Phase 8)**: Depends on all component features being complete
- **Quality (Phase 9)**: Depends on all implementation phases
- **Git Commit (Phase 10)**: Depends on quality validation passing

### User Story Dependencies

- **User Story 1 (P1)**: MVP - No dependencies on other stories
- **User Story 2 (P2)**: Builds on US1 but independently testable
- **User Story 3 (P3)**: Works with US1 but independently testable
- **User Story 4 (P4)**: Works with US1-US3 but independently testable

### Within Each User Story (TDD CRITICAL)

1. Write ALL tests for the story FIRST (marked [P] can be parallel)
2. Run tests → Verify ALL FAIL
3. Implement features sequentially
4. Run tests after each implementation → Should pass incrementally
5. Final test run → ALL story tests pass
6. Type check, lint, format
7. Story complete → Move to next priority

### Parallel Opportunities

**Setup Phase**:
- T002, T003, T004, T005 can all run in parallel (reading different files)

**Within Each User Story - Tests**:
- All test-writing tasks marked [P] can run in parallel (different test functions)

**Within Each User Story - Implementation**:
- Some tasks are sequential (must complete in order)
- Tasks marked [P] in implementation can run in parallel

**Cross-Story Parallelization** (if team capacity):
- After Foundational phase, different developers can work on different user stories simultaneously
- US1, US2, US3, US4 are independently testable

**Quality Validation**:
- T086, T087, T088, T089 can run in parallel (different documentation files)

---

## Parallel Example: User Story 1 - Basic Multi-line Text Input

### Tests Phase (All Parallel):
```bash
# Launch all test-writing tasks together:
Task: "Write test for default textarea rendering in tests/test_components/test_textarea.py"
Task: "Write test for ID and label-for-id association in tests/test_components/test_textarea.py"
Task: "Write test for placeholder attribute in tests/test_components/test_textarea.py"
Task: "Write test for value rendering in tests/test_components/test_textarea.py"
Task: "Write test for default rows=4 in tests/test_components/test_textarea.py"
Task: "Write test for dark mode classes in tests/test_components/test_textarea.py"
Task: "Write test for Flowbite base classes in tests/test_components/test_textarea.py"
Task: "Write test for focus ring classes in tests/test_components/test_textarea.py"

# Then run: pytest tests/test_components/test_textarea.py -v
# Result: All 8 tests FAIL (expected - component doesn't exist)
```

### Implementation Phase (Sequential TDD):
```bash
# T016: Create skeleton → Run tests (8 fail)
# T017: Implement htmy() → Run tests (2-3 pass)
# T018: Add placeholder → Run tests (4-5 pass)
# T019: Add value → Run tests (6 pass)
# T020: Add rows → Run tests (7 pass)
# T021: Implement _build_label_classes() → Run tests (7 pass)
# T022: Implement _build_textarea_classes() → Run tests (8 pass - ALL PASS!)
# T023: Implement _build_textarea_attrs() → Run tests (8 pass)
# T024: Export from __init__ → Run tests (8 pass)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only) - Fastest Path to Value

1. ✅ Complete Phase 1: Setup (5 tasks, ~10 minutes)
2. ✅ Complete Phase 2: Foundational (2 tasks, ~5 minutes)
3. ✅ Complete Phase 3: User Story 1 (16 tasks, ~1.5 hours TDD)
4. **STOP and VALIDATE**:
   - Run tests: All 8 US1 tests pass
   - Type check: 100% coverage
   - Manual test: Render basic textarea in showcase
5. **MVP COMPLETE**: Basic textarea component functional and tested

**Total MVP Time**: ~2 hours

### Incremental Delivery (All User Stories)

1. Foundation → US1 (MVP) → Validate → ~2 hours
2. Add US2 (Validation) → Validate → +1 hour
3. Add US3 (Size Control) → Validate → +30 minutes
4. Add US4 (Accessibility) → Validate → +1 hour
5. Add HTMX (Phase 7) → Validate → +30 minutes
6. Add Showcase (Phase 8) → Validate → +45 minutes
7. Quality Gates (Phase 9) → Pass → +30 minutes
8. Git Commit (Phase 10) → Done → +15 minutes

**Total Feature Time**: ~6.5 hours (includes all quality validation)

### Team Parallelization (If Multiple Developers)

**Option 1: Story-per-Developer**
- Foundation complete → Developer A does US1, Developer B does US2, Developer C does US3+US4
- Merge and integrate after each story completes

**Option 2: Test-then-Implementation**
- One developer writes ALL tests (T008-T067)
- Another developer implements sequentially after tests are written
- Reduces context switching, maintains TDD discipline

---

## Notes

### TDD Discipline (CRITICAL)
- **NEVER** implement before writing tests
- **ALWAYS** verify tests fail before implementing
- **ALWAYS** run tests after each implementation task
- **NEVER** skip type checking or linting
- Commit after each user story completes all tests

### Quality Checklist Before Commit
- [ ] All tests pass (pytest)
- [ ] Coverage >95% (pytest --cov)
- [ ] Type check 100% (mypy --strict)
- [ ] No lint warnings (ruff check)
- [ ] Code formatted (ruff format)
- [ ] Showcase renders correctly
- [ ] Documentation updated

### Common Pitfalls to Avoid
- ❌ Implementing without tests (violates TDD)
- ❌ Skipping mypy type check (violates constitution principle II)
- ❌ Forgetting dark mode classes (violates established pattern)
- ❌ Not using ClassBuilder (violates consistency)
- ❌ Conditional dark mode logic (wrong - always include dark: classes)
- ❌ Committing without running full test suite

### Success Criteria
- ✅ 30+ tests written and passing
- ✅ >95% test coverage achieved
- ✅ 100% type coverage (mypy strict)
- ✅ All quality gates passed
- ✅ Showcase demonstrates all features
- ✅ Documentation accurate and complete
- ✅ Component exported and usable
- ✅ Follows all constitution principles

---

**Total Tasks**: 96 tasks
**Estimated Time**: 6.5 hours (with TDD, all quality gates)
**MVP Time**: 2 hours (User Story 1 only)
**Test Count**: 30+ tests (22 required minimum, may add more during implementation)
**Test Coverage Target**: >95%
**Type Coverage Target**: 100%

**Ready to Execute**: All tasks are specific, have file paths, and follow TDD workflow. Execute in order for best results.
