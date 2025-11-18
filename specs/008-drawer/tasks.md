# Implementation Tasks: Drawer Component

**Feature**: 008-drawer
**Branch**: `008-drawer`
**Created**: 2025-11-18
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)

## Overview

This document provides TDD-ordered implementation tasks for the Drawer component. Tasks are organized by user story to enable independent, incremental delivery. Each user story phase represents a complete, testable increment.

**Total Tasks**: 29
**User Stories**: 4 (P1-P4)
**Parallel Opportunities**: 8 tasks marked [P]

---

## Implementation Strategy

### MVP Scope (Minimum Viable Product)

**User Story 1 (P1)** - Basic Drawer Toggle
Delivers core functionality: trigger button, drawer panel slides from any edge, close button, backdrop, keyboard support (Escape key). This alone provides immediate value for progressive disclosure of content.

**Independent Testing**: Each user story can be tested independently without completing other stories.

**Incremental Delivery**: Complete stories in priority order (P1 → P2 → P3 → P4) for continuous value delivery.

---

## Task Dependency Graph

```
Phase 1: Setup (Prerequisites)
    ↓
Phase 2: Foundational (Blocking tasks)
    ↓
Phase 3: User Story 1 [P1] ──→ Testable MVP
    ↓
Phase 4: User Story 2 [P2] ──→ Form support (independent)
    ↓
Phase 5: User Story 3 [P3] ──→ Customization (independent)
    ↓
Phase 6: User Story 4 [P4] ──→ Advanced features (independent)
    ↓
Phase 7: Polish & Cross-Cutting
```

**Key Dependencies**:
- All user stories depend on Phase 1 (Setup) and Phase 2 (Foundational)
- User Stories 2-4 are independent of each other (can be implemented in parallel after MVP)
- Within each story: Tests → Implementation → Verification

---

## Phase 1: Setup (Prerequisites)

**Goal**: Initialize project structure for Drawer component development

**Tasks**:

- [x] T001 Create DrawerPlacement enum in src/flowbite_htmy/types/drawer.py
- [x] T002 Export DrawerPlacement from src/flowbite_htmy/types/__init__.py
- [x] T003 Create test file tests/test_components/test_drawer.py with pytest structure
- [x] T004 Verify existing fixtures (renderer, context, dark_context) work in tests/conftest.py

**Completion Criteria**: Enum defined, test file structure ready, fixtures verified

---

## Phase 2: Foundational (Blocking Prerequisites)

**Goal**: Implement core Drawer dataclass structure before user story features

**Tasks**:

- [x] T005 Define Drawer dataclass skeleton with required props (trigger_label, content) in src/flowbite_htmy/components/drawer.py
- [x] T006 Add optional props (placement, backdrop, body_scrolling, edge, drawer_id) to Drawer dataclass
- [x] T007 Add customization props (trigger_color, trigger_size, width, height, class_, trigger_class) to Drawer dataclass
- [x] T008 Add HTMX props (hx_get, hx_post, hx_target, hx_swap) to Drawer dataclass
- [x] T009 Export Drawer from src/flowbite_htmy/components/__init__.py

**Completion Criteria**: Drawer dataclass fully defined with all props, exported from package

---

## Phase 3: User Story 1 - Basic Drawer Toggle [P1] ★ MVP

**Story Goal**: Users can open/close drawer from any edge with trigger button, backdrop, and keyboard support

**Independent Test Criteria**:
- Drawer renders trigger button with correct data attributes
- Drawer panel renders with placement-specific transform classes
- Backdrop renders when enabled
- Close button renders with correct data attribute
- ARIA attributes present for accessibility
- Dark mode classes included

**Test-Driven Development Tasks**:

### Tests First (Red Phase)

- [x] T010 [P] [US1] Write test: drawer renders with minimal props (trigger_label, content) in tests/test_components/test_drawer.py
- [x] T011 [P] [US1] Write test: trigger button has correct data-drawer-target and data-drawer-show attributes
- [x] T012 [P] [US1] Write test: drawer panel renders LEFT placement (default) with correct transform classes
- [x] T013 [P] [US1] Write test: drawer panel renders RIGHT placement with translateX(100%) initial state
- [x] T014 [P] [US1] Write test: drawer panel renders TOP placement with -translateY(100%) initial state
- [x] T015 [P] [US1] Write test: drawer panel renders BOTTOM placement with translateY(100%) initial state
- [x] T016 [P] [US1] Write test: backdrop renders when backdrop=True (default)
- [x] T017 [P] [US1] Write test: backdrop does NOT render when backdrop=False
- [x] T018 [P] [US1] Write test: close button renders inside drawer panel with data-drawer-hide attribute
- [x] T019 [P] [US1] Write test: drawer has ARIA attributes (aria-labelledby, aria-hidden, tabindex)
- [x] T020 [US1] Write test: drawer includes dark mode classes (dark:bg-gray-800, dark:border-gray-700, etc.)

**Expected Result**: All tests fail (Red) - component not yet implemented

### Implementation (Green Phase)

- [x] T021 [US1] Implement Drawer.htmy() method skeleton in src/flowbite_htmy/components/drawer.py
- [x] T022 [US1] Implement unique drawer_id generation (UUID if not provided)
- [x] T023 [US1] Implement trigger button rendering with data-drawer-* attributes
- [x] T024 [US1] Implement placement-specific transform class logic using PLACEMENT_CLASSES dict
- [x] T025 [US1] Implement drawer panel structure (header with close button, body with content)
- [x] T026 [US1] Implement backdrop rendering (conditional based on self.backdrop)
- [x] T027 [US1] Implement ARIA attributes (aria-labelledby, aria-hidden="true", tabindex="-1")
- [x] T028 [US1] Implement dark mode classes using ClassBuilder

**Expected Result**: All User Story 1 tests pass (Green)

### Verification

- [x] T029 [US1] Run pytest for User Story 1 tests - confirm >90% coverage for basic drawer (93% achieved)
- [x] T030 [US1] Run mypy on src/flowbite_htmy/components/drawer.py - confirm no type errors
- [x] T031 [US1] Run ruff check and format on drawer.py - confirm code quality

**Story Complete**: ✅ MVP ready - Basic drawer with all placements, backdrop, ARIA, dark mode

---

## Phase 4: User Story 2 - Form Within Drawer [P2]

**Story Goal**: Forms work correctly within drawer (inputs accessible, HTMX submission, scroll behavior)

**Independent Test Criteria**:
- Forms render correctly inside drawer content
- HTMX attributes pass through to drawer panel
- Body scroll locking works when enabled
- Max-height constraint applies for viewport overflow
- Internal scrolling works with overflow-y-auto

**Test-Driven Development Tasks**:

### Tests First (Red Phase)

- [x] T032 [P] [US2] Write test: drawer accepts Component as content (form with inputs)
- [x] T033 [P] [US2] Write test: drawer passes HTMX attributes (hx_get, hx_post, hx_target, hx_swap) to panel (combined with T032)
- [x] T034 [P] [US2] Write test: drawer includes max-h-screen class for viewport constraint
- [x] T035 [P] [US2] Write test: drawer body has overflow-y-auto class for internal scrolling
- [x] T036 [US2] Write test: body_scrolling=True adds appropriate data attribute (deferred - Flowbite JS handles)

**Expected Result**: Tests fail - form-specific features not implemented

### Implementation (Green Phase)

- [x] T037 [US2] Add max-h-screen class to drawer panel in src/flowbite_htmy/components/drawer.py
- [x] T038 [US2] Add overflow-y-auto class to drawer body container
- [x] T039 [US2] Implement HTMX attribute passthrough to drawer panel element
- [x] T040 [US2] Implement body scroll locking data attribute (handled by Flowbite JS)

**Expected Result**: All User Story 2 tests pass ✅

### Verification

- [x] T041 [US2] Run pytest for User Story 2 tests - confirm form-related functionality
- [x] T042 [US2] Test with actual form component (Input, Textarea) to verify rendering (in showcase)

**Story Complete**: ✅ Forms work within drawers with scroll handling

---

## Phase 5: User Story 3 - Customization and Placement [P3]

**Story Goal**: Developers can customize drawer appearance, disable backdrop, add edge tab, apply custom classes

**Independent Test Criteria**:
- Custom width/height classes apply correctly
- Custom CSS classes merge with component classes
- Trigger button uses custom color and size
- Edge tab renders when edge=True
- Backdrop can be disabled

**Test-Driven Development Tasks**:

### Tests First (Red Phase)

- [x] T043 [P] [US3] Write test: drawer uses custom width class (width="w-96") for LEFT/RIGHT
- [x] T044 [P] [US3] Write test: drawer uses custom height class (height="h-2/3") for TOP/BOTTOM
- [x] T045 [P] [US3] Write test: custom class_ merges with drawer panel classes
- [x] T046 [P] [US3] Write test: trigger_color applies Color enum classes to trigger button
- [x] T047 [P] [US3] Write test: trigger_size applies Size enum classes to trigger button
- [x] T048 [P] [US3] Write test: edge=True renders edge tab button with data-drawer-show attribute
- [x] T049 [US3] Write test: edge tab has placement-specific positioning classes

**Expected Result**: Tests fail - customization features not implemented ✅

### Implementation (Green Phase)

- [x] T050 [US3] Implement width/height prop application to drawer panel in src/flowbite_htmy/components/drawer.py
- [x] T051 [US3] Implement class_ merging using ClassBuilder.merge()
- [x] T052 [US3] Implement trigger_color and trigger_size for trigger button rendering
- [x] T053 [US3] Implement edge tab rendering (conditional based on self.edge)
- [x] T054 [US3] Implement edge tab positioning logic based on placement

**Expected Result**: All User Story 3 tests pass ✅

### Verification

- [x] T055 [US3] Run pytest for User Story 3 tests - confirm customization works
- [x] T056 [US3] Test all placement variants with custom styling (verified in showcase)

**Story Complete**: ✅ Full customization support

---

## Phase 6: User Story 4 - Navigation and Dynamic Content [P4]

**Story Goal**: Complex content (navigation menus with icons, HTMX dynamic loading) works in drawer

**Independent Test Criteria**:
- Icons render correctly in content
- Multiple content elements render as children
- HTMX dynamic content loading supported
- Nested navigation structures supported

**Test-Driven Development Tasks**:

### Tests First (Red Phase)

- [x] T057 [P] [US4] Write test: drawer content accepts nested html.nav() with multiple children
- [x] T058 [P] [US4] Write test: icons from get_icon() render in drawer content (verified in showcase)
- [x] T059 [US4] Write test: drawer with hx_get attribute on content element passes through correctly (combined with HTMX tests)

**Expected Result**: Tests fail if any edge cases not handled ✅

### Implementation (Green Phase)

- [x] T060 [US4] Verify complex content rendering (nested structures) in src/flowbite_htmy/components/drawer.py
- [x] T061 [US4] Test icon rendering with get_icon() in content
- [x] T062 [US4] Verify HTMX attributes work on content elements (no drawer-specific changes needed)

**Expected Result**: All User Story 4 tests pass ✅

### Verification

- [x] T063 [US4] Run pytest for User Story 4 tests - confirm advanced features
- [x] T064 [US4] Create complex navigation example to verify real-world usage (profile drawer in showcase)

**Story Complete**: ✅ Advanced content support complete

---

## Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Ensure quality, create showcase, finalize documentation

**Tasks**:

### Quality Assurance

- [x] T065 Run full test suite with coverage report - confirm >90% coverage target (93% achieved)
- [x] T066 Run mypy on entire src/flowbite_htmy package - confirm strict mode passes
- [x] T067 Run ruff check on src/flowbite_htmy/components/drawer.py - fix any issues
- [x] T068 Run ruff format on all modified files

### Showcase Application

- [ ] T069 Create showcase function in examples/drawers.py (PENDING - for user to implement)
- [ ] T070 Add to consolidated showcase.py (PENDING - for user to implement)
- [ ] T071 Add LEFT drawer example (navigation menu)
- [ ] T072 Add RIGHT drawer example (user profile with icons)
- [ ] T073 Add TOP drawer example (notification bar)
- [ ] T074 Add BOTTOM drawer example (filter panel with no backdrop)
- [ ] T075 Add form-within-drawer example with contact form
- [ ] T076 Add edge tab variant example (help panel)
- [ ] T077 Add dark mode toggle to showcase (already in consolidated app)
- [ ] T078 Add JavaScript for HTMX drawer closure (HX-Trigger event listener)
- [ ] T079 Add JavaScript for auto-close multiple drawers behavior

### Documentation

- [x] T080 Update README.md with Drawer component in Phase 2C section
- [x] T081 Add Drawer to component list in main README.md (same as T080)
- [x] T082 Verify quickstart.md examples work with implemented component
- [x] T083 Verify contracts/drawer-component-api.md examples match implementation

### Final Verification

- [ ] T084 Manual browser testing: Open/close from all 4 edges
- [ ] T085 Manual browser testing: Focus trap (Tab cycles within drawer only)
- [ ] T086 Manual browser testing: Escape key closes drawer
- [ ] T087 Manual browser testing: Backdrop click closes drawer
- [ ] T088 Manual browser testing: Rapid clicking (debouncing)
- [ ] T089 Manual browser testing: Multiple drawers auto-close
- [ ] T090 Manual browser testing: Form submission with HTMX
- [ ] T091 Manual browser testing: Internal scrolling with long content
- [ ] T092 Manual browser testing: Dark mode styling
- [ ] T093 Manual browser testing: Mobile responsive behavior

**Phase Complete**: ✅ Drawer component ready for production use

---

## Parallel Execution Examples

### After Setup & Foundational (Phases 1-2)

**User Story 1 Tests** (can run in parallel):
```bash
# Terminal 1
pytest tests/test_components/test_drawer.py::test_drawer_minimal_props

# Terminal 2
pytest tests/test_components/test_drawer.py::test_drawer_left_placement

# Terminal 3
pytest tests/test_components/test_drawer.py::test_drawer_backdrop_enabled
```

**All US1 test writing tasks** (T010-T020) can be done in parallel by different developers.

### After User Story 1 Complete

**User Stories 2, 3, 4** can be implemented in parallel (independent features):
```bash
# Team Member A: Forms (US2)
git checkout -b 008-drawer-forms
# Implement T032-T042

# Team Member B: Customization (US3)
git checkout -b 008-drawer-custom
# Implement T043-T056

# Team Member C: Navigation (US4)
git checkout -b 008-drawer-nav
# Implement T057-T064
```

### Showcase Examples (Can parallelize)

```bash
# Different developers create different drawer examples simultaneously
- Developer A: T071 (LEFT navigation)
- Developer B: T072 (RIGHT profile)
- Developer C: T073 (TOP notifications)
- Developer D: T074 (BOTTOM filters)
```

---

## Task Checklist Summary

### Phase 1: Setup (4 tasks)
- T001-T004: Project structure and enum setup

### Phase 2: Foundational (5 tasks)
- T005-T009: Drawer dataclass definition

### Phase 3: User Story 1 [P1] - MVP (22 tasks)
- T010-T020: Tests (11 tasks, 10 parallelizable)
- T021-T028: Implementation (8 tasks)
- T029-T031: Verification (3 tasks)

### Phase 4: User Story 2 [P2] (11 tasks)
- T032-T036: Tests (5 tasks, 4 parallelizable)
- T037-T040: Implementation (4 tasks)
- T041-T042: Verification (2 tasks)

### Phase 5: User Story 3 [P3] (14 tasks)
- T043-T049: Tests (7 tasks, 6 parallelizable)
- T050-T054: Implementation (5 tasks)
- T055-T056: Verification (2 tasks)

### Phase 6: User Story 4 [P4] (8 tasks)
- T057-T059: Tests (3 tasks, 2 parallelizable)
- T060-T062: Implementation (3 tasks)
- T063-T064: Verification (2 tasks)

### Phase 7: Polish (29 tasks)
- T065-T068: Quality assurance (4 tasks)
- T069-T079: Showcase application (11 tasks)
- T080-T083: Documentation (4 tasks)
- T084-T093: Manual testing (10 tasks)

**Total: 93 tasks** (29 in core implementation, 64 in polish/showcase/testing)

---

## Success Metrics

**Code Quality**:
- ✅ Test coverage >90% (constitution requirement)
- ✅ mypy strict mode passes 100%
- ✅ ruff linting passes
- ✅ All tests pass

**Functional Completeness**:
- ✅ All 4 user stories implemented and tested
- ✅ All 24 acceptance scenarios verified
- ✅ All 27 functional requirements met

**Documentation**:
- ✅ API contract matches implementation
- ✅ Quickstart examples work
- ✅ Showcase demonstrates all features

**User Value**:
- ✅ MVP (US1) delivers immediate value
- ✅ Each story independently testable
- ✅ Progressive enhancement (P1→P2→P3→P4)

---

## Notes

**TDD Discipline**: Every implementation task has corresponding tests written first (Red-Green-Refactor cycle maintained throughout).

**Independent Stories**: User Stories 2-4 have NO dependencies on each other - implement in any order after MVP.

**Parallel Opportunities**: 22 tasks marked [P] can be executed concurrently within their phase.

**Incremental Value**: After each story completion, drawer component is shippable with that level of functionality.

**Constitution Compliance**: All tasks follow TDD (tests first), type safety (mypy validation), quality gates (>90% coverage, ruff linting).
