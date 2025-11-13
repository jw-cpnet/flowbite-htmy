# Tasks: Consolidated Component Showcase Application

**Input**: Design documents from `/specs/001-consolidated-showcase/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No unit tests required for this feature (showcase application demonstrating already-tested components). Manual E2E testing sufficient.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Project type**: Single project - `examples/` at repository root
- All new files go in `examples/` directory
- Templates in `examples/templates/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic file structure

- [X] T001 Create type definitions file at examples/showcase_types.py
- [X] T002 Create new Jinja template at examples/templates/showcase-layout.html.jinja extending base.html.jinja
- [X] T003 [P] Update .vscode/launch.json to add consolidated showcase debug configuration

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Extract showcase content from examples/buttons.py into build_buttons_showcase() function
- [X] T005 [P] Extract showcase content from examples/badges.py into build_badges_showcase() function
- [X] T006 [P] Extract showcase content from examples/alerts.py into build_alerts_showcase() function
- [X] T007 [P] Extract showcase content from examples/avatars.py into build_avatars_showcase() function
- [X] T008 [P] Extract showcase content from examples/cards.py into build_cards_showcase() function
- [X] T009 [P] Extract showcase content from examples/checkboxes.py into build_checkboxes_showcase() function
- [X] T010 [P] Extract showcase content from examples/inputs.py into build_inputs_showcase() function
- [X] T011 [P] Extract showcase content from examples/modals.py into build_modals_showcase() function
- [X] T012 [P] Extract showcase content from examples/paginations.py into build_paginations_showcase() function
- [X] T013 [P] Extract showcase content from examples/selects.py into build_selects_showcase() function

**Checkpoint**: All showcase content extraction complete - consolidated app implementation can now begin

---

## Phase 3: User Story 1 - Browse All Components from Main Navigation (Priority: P1) 🎯 MVP

**Goal**: Implement navigation menu and routing system so developers can access all component showcases from a single application with a persistent sidebar menu.

**Independent Test**: Launch `python examples/showcase.py`, visit homepage at http://localhost:8000, verify navigation menu shows all 10 components, click each nav link and verify it navigates to the correct component page.

### Implementation for User Story 1

- [X] T014 [US1] Create examples/showcase.py with FastAPI app initialization and component routes constant
- [X] T015 [US1] Implement build_navigation() function in examples/showcase.py to generate sidebar menu using Button components
- [X] T016 [US1] Implement homepage route (GET /) in examples/showcase.py with component gallery
- [X] T017 [US1] Implement buttons route (GET /buttons) in examples/showcase.py
- [X] T018 [P] [US1] Implement badges route (GET /badges) in examples/showcase.py
- [X] T019 [P] [US1] Implement alerts route (GET /alerts) in examples/showcase.py
- [X] T020 [P] [US1] Implement avatars route (GET /avatars) in examples/showcase.py
- [X] T021 [P] [US1] Implement cards route (GET /cards) in examples/showcase.py
- [X] T022 [P] [US1] Implement checkboxes route (GET /checkboxes) in examples/showcase.py
- [X] T023 [P] [US1] Implement inputs route (GET /inputs) in examples/showcase.py
- [X] T024 [P] [US1] Implement modals route (GET /modals) in examples/showcase.py
- [X] T025 [P] [US1] Implement paginations route (GET /paginations) in examples/showcase.py
- [X] T026 [P] [US1] Implement selects route (GET /selects) in examples/showcase.py
- [X] T027 [US1] Add 404 error handler in examples/showcase.py with custom HTML response
- [X] T028 [US1] Add main block in examples/showcase.py with uvicorn.run() for direct execution

**Checkpoint**: At this point, User Story 1 should be fully functional - all component pages accessible through navigation menu

---

## Phase 4: User Story 2 - View Individual Component Showcases (Priority: P2)

**Goal**: Ensure all existing showcase content from standalone apps is preserved and functional in the consolidated app, with all interactive examples working correctly.

**Independent Test**: Navigate to each of the 10 component pages and verify: (1) all showcase sections from original standalone apps are present, (2) section headers and descriptions display correctly, (3) interactive features work (modals open, checkboxes toggle, pagination links work), (4) page refresh keeps you on the same component page.

### Implementation for User Story 2

- [ ] T029 [P] [US2] Manual E2E test - Verify buttons page shows all 10 sections (default, sizes, variants, icons, badges, social, payment, HTMX) with Chrome DevTools
- [ ] T030 [P] [US2] Manual E2E test - Verify badges page shows all 7 sections (default, large, icons, pill, bordered, icon-only, combinations) with Chrome DevTools
- [ ] T031 [P] [US2] Manual E2E test - Verify alerts page shows all 6 sections (default, icons, dismissible, border, lists, additional content) with Chrome DevTools
- [ ] T032 [P] [US2] Manual E2E test - Verify avatars page shows all 8 sections (default, sizes, placeholder, groups, stacked, indicators, border, text fallback) with Chrome DevTools
- [ ] T033 [P] [US2] Manual E2E test - Verify cards page shows all 8 sections (default, image, action buttons, horizontal, grid, pricing, testimonial, product) with Chrome DevTools
- [ ] T034 [P] [US2] Manual E2E test - Verify checkboxes page shows all 6 sections (default, helper text, validation, disabled, groups, inline) with Chrome DevTools
- [ ] T035 [P] [US2] Manual E2E test - Verify inputs page shows all 7 sections (default, helper text, validation, required, disabled, sizes, icons) with Chrome DevTools
- [ ] T036 [P] [US2] Manual E2E test - Verify modals page shows all 6 sections (default, sizes, form, confirmation, image, footer) with Chrome DevTools
- [ ] T037 [P] [US2] Manual E2E test - Verify paginations page shows all 6 sections (default, sizes, icons, info text, table, edge cases) with Chrome DevTools
- [ ] T038 [P] [US2] Manual E2E test - Verify selects page shows all 7 sections (default, helper text, validation, required, disabled, multiple, groups) with Chrome DevTools
- [ ] T039 [P] [US2] Test interactive features - Open modal dialogs on modals page and verify they display/close correctly
- [ ] T040 [P] [US2] Test interactive features - Toggle checkboxes on checkboxes page and verify state changes work
- [ ] T041 [P] [US2] Test interactive features - Click pagination page numbers and verify URL changes correctly
- [ ] T042 [US2] Test page refresh behavior - Navigate to buttons page, refresh browser, verify still on buttons page

**Checkpoint**: All component showcases verified complete and functional - content preservation validated

---

## Phase 5: User Story 3 - Quick Component Search and Reference (Priority: P3)

**Goal**: Implement active page indication in navigation menu so developers can easily see which component page they're currently viewing.

**Independent Test**: Navigate to each component page and verify the navigation menu highlights the current page (button has PRIMARY color and DEFAULT variant). Navigate to a different page and verify the highlight moves to the new page. Visit homepage and verify no component button is highlighted.

### Implementation for User Story 3

- [ ] T043 [US3] Update build_navigation() function to accept current_page parameter and apply conditional styling
- [ ] T044 [US3] Update all route handlers to pass current page name to build_navigation() function
- [ ] T045 [P] [US3] Manual E2E test - Navigate to buttons page, verify Buttons nav button is PRIMARY/DEFAULT (highlighted)
- [ ] T046 [P] [US3] Manual E2E test - Verify all other nav buttons are SECONDARY/OUTLINE (not highlighted)
- [ ] T047 [P] [US3] Manual E2E test - Navigate from buttons to badges, verify highlight moves to Badges button
- [ ] T048 [P] [US3] Manual E2E test - Visit homepage, verify no component nav button is highlighted

**Checkpoint**: Active page indication working correctly - navigation UX complete

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements that affect multiple user stories

- [ ] T049 [P] Run ruff format on examples/showcase.py to ensure code formatting compliance
- [ ] T050 [P] Run mypy on examples/showcase.py to verify type hints are correct
- [ ] T051 [P] Add docstrings to all functions in examples/showcase.py
- [ ] T052 Test dark mode persistence - Toggle dark mode on homepage, navigate to buttons page, verify dark mode persists
- [ ] T053 Test browser navigation - Use browser back button from buttons to homepage, verify it works correctly
- [ ] T054 Test direct URL access - Enter http://localhost:8000/badges directly in browser, verify page loads correctly
- [ ] T055 Test bookmarking - Bookmark buttons page, close browser, reopen bookmark, verify it navigates to buttons page
- [ ] T056 Test 404 error - Navigate to http://localhost:8000/nonexistent, verify 404 page shows with links to all routes
- [ ] T057 [P] Add deprecation notice at top of examples/buttons.py pointing users to consolidated showcase
- [ ] T058 [P] Add deprecation notice at top of examples/badges.py pointing users to consolidated showcase
- [ ] T059 [P] Add deprecation notice at top of examples/alerts.py pointing users to consolidated showcase
- [ ] T060 [P] Add deprecation notice at top of examples/avatars.py pointing users to consolidated showcase
- [ ] T061 [P] Add deprecation notice at top of examples/cards.py pointing users to consolidated showcase
- [ ] T062 [P] Add deprecation notice at top of examples/checkboxes.py pointing users to consolidated showcase
- [ ] T063 [P] Add deprecation notice at top of examples/inputs.py pointing users to consolidated showcase
- [ ] T064 [P] Add deprecation notice at top of examples/modals.py pointing users to consolidated showcase
- [ ] T065 [P] Add deprecation notice at top of examples/paginations.py pointing users to consolidated showcase
- [ ] T066 [P] Add deprecation notice at top of examples/selects.py pointing users to consolidated showcase

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001-T003) - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational phase completion (T004-T013) - Core navigation and routing
- **User Story 2 (Phase 4)**: Depends on User Story 1 completion (T014-T028) - Requires routes to exist for testing
- **User Story 3 (Phase 5)**: Depends on User Story 1 completion (T014-T028) - Enhances existing navigation
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Depends on User Story 1 (navigation must exist to test content)
- **User Story 3 (P3)**: Can start in parallel with User Story 2 after User Story 1 completes

### Within Each User Story

**User Story 1**:
- T014 (app initialization) must complete first
- T015 (navigation function) before route implementations
- T016 (homepage route) can be done in parallel with component routes
- T017-T026 (component routes) can all run in parallel after T014-T015 complete
- T027-T028 (error handler and main block) after routes complete

**User Story 2**:
- All E2E test tasks (T029-T038) can run in parallel after US1 complete
- Interactive feature tests (T039-T041) can run in parallel
- T042 (refresh test) can run anytime after routes exist

**User Story 3**:
- T043 (update navigation function) must complete first
- T044 (update routes) depends on T043
- T045-T048 (E2E tests) can all run in parallel after T044 completes

### Parallel Opportunities

- **Setup phase**: All 3 tasks can run in parallel (different files)
- **Foundational phase**: Tasks T005-T013 can run in parallel (extracting from different files)
- **US1 component routes**: Tasks T018-T026 can run in parallel (different routes, same file but different functions)
- **US2 E2E tests**: Tasks T029-T038 can run in parallel (testing different pages)
- **US2 interactive tests**: Tasks T039-T041 can run in parallel (testing different features)
- **US3 E2E tests**: Tasks T045-T048 can run in parallel (testing different navigation states)
- **Polish deprecation notices**: Tasks T057-T066 can run in parallel (updating different files)

---

## Parallel Example: Foundational Phase

```bash
# Launch all showcase extraction tasks together (Phase 2):
Task T005: "Extract showcase content from examples/badges.py into build_badges_showcase() function"
Task T006: "Extract showcase content from examples/alerts.py into build_alerts_showcase() function"
Task T007: "Extract showcase content from examples/avatars.py into build_avatars_showcase() function"
Task T008: "Extract showcase content from examples/cards.py into build_cards_showcase() function"
Task T009: "Extract showcase content from examples/checkboxes.py into build_checkboxes_showcase() function"
Task T010: "Extract showcase content from examples/inputs.py into build_inputs_showcase() function"
Task T011: "Extract showcase content from examples/modals.py into build_modals_showcase() function"
Task T012: "Extract showcase content from examples/paginations.py into build_paginations_showcase() function"
Task T013: "Extract showcase content from examples/selects.py into build_selects_showcase() function"
```

---

## Parallel Example: User Story 1 (Component Routes)

```bash
# After T014-T016 complete, launch all component route implementations together:
Task T018: "Implement badges route (GET /badges) in examples/showcase.py"
Task T019: "Implement alerts route (GET /alerts) in examples/showcase.py"
Task T020: "Implement avatars route (GET /avatars) in examples/showcase.py"
Task T021: "Implement cards route (GET /cards) in examples/showcase.py"
Task T022: "Implement checkboxes route (GET /checkboxes) in examples/showcase.py"
Task T023: "Implement inputs route (GET /inputs) in examples/showcase.py"
Task T024: "Implement modals route (GET /modals) in examples/showcase.py"
Task T025: "Implement paginations route (GET /paginations) in examples/showcase.py"
Task T026: "Implement selects route (GET /selects) in examples/showcase.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T013) - CRITICAL blocking phase
3. Complete Phase 3: User Story 1 (T014-T028)
4. **STOP and VALIDATE**: Test User Story 1 independently:
   - Run `python examples/showcase.py`
   - Verify all 10 component routes accessible
   - Verify navigation menu works
   - Verify each page displays its content
5. If US1 works correctly, proceed to US2 and US3

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **MVP DONE** (basic navigation works!)
3. Add User Story 2 → Test independently → Content validation complete
4. Add User Story 3 → Test independently → Active page indication working
5. Add Polish → Final cleanup and deprecation notices

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (or one developer does sequentially)
2. Once Foundational is done:
   - Developer A: User Story 1 (navigation and routing)
   - Developer B: Prepare for User Story 2 (review standalone apps to understand content)
3. After US1 complete:
   - Developer A: User Story 3 (active page indication)
   - Developer B: User Story 2 (E2E content testing)
4. Both: Polish phase (parallel on different files)

---

## Notes

- **No Unit Tests Required**: This is a showcase application demonstrating already-tested components (>90% test coverage). Manual E2E testing sufficient per constitution exemption.
- **[P] tasks**: Different files or different routes, no dependencies - can run in parallel
- **[Story] labels**: Map tasks to specific user stories for traceability
- **File Paths**: All tasks include specific file paths for clarity
- **Independent Stories**: US1 must complete before US2/US3, but US2 and US3 can run in parallel after US1
- **Commit Strategy**: Commit after each phase or major milestone
- **Testing Points**: Explicit checkpoints after each phase to validate story completion
- **Deprecation**: Standalone apps kept for comparison, marked with deprecation notices
- **Error Handling**: 404 handler (T027) ensures graceful handling of invalid routes

---

## Task Count Summary

- **Total Tasks**: 66
- **Setup**: 3 tasks
- **Foundational**: 10 tasks (CRITICAL - blocks all stories)
- **User Story 1 (P1)**: 15 tasks - Core navigation and routing
- **User Story 2 (P2)**: 14 tasks - Content validation and testing
- **User Story 3 (P3)**: 6 tasks - Active page indication
- **Polish**: 18 tasks - Code quality and deprecation notices

**Parallel Opportunities**: 51 tasks marked with [P] (77% of tasks can run in parallel within their phases)

**MVP Scope**: Phases 1-3 (28 tasks) delivers fully functional consolidated showcase with navigation

---

## Independent Test Criteria

### User Story 1 (MVP)
- [ ] Application starts successfully with `python examples/showcase.py`
- [ ] Homepage (/) loads with component gallery
- [ ] All 10 component pages accessible via navigation menu
- [ ] Clicking navigation links navigates to correct pages
- [ ] Dark mode toggle inherited from base template works

### User Story 2
- [ ] Each component page displays all its showcase sections
- [ ] Section headers and descriptions present on all pages
- [ ] Modal buttons open/close modals correctly
- [ ] Checkbox toggles change state visually
- [ ] Pagination links update URL
- [ ] Page refresh maintains current page

### User Story 3
- [ ] Current page button highlighted in navigation (PRIMARY/DEFAULT)
- [ ] Other page buttons not highlighted (SECONDARY/OUTLINE)
- [ ] Highlight moves when navigating to different page
- [ ] Homepage shows no component button highlighted
