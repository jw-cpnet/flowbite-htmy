# Tasks: Tabs Component

**Input**: Design documents from `/specs/006-tabs/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Following strict TDD approach - tests are written BEFORE implementation for all user stories

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/flowbite_htmy/`, `tests/test_components/` at repository root
- This is a Python library with components in `src/flowbite_htmy/components/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Minimal setup - most infrastructure already exists from previous components

- [ ] T001 Create TabVariant and IconPosition enums in src/flowbite_htmy/components/tabs.py
- [ ] T002 Create Tab dataclass skeleton in src/flowbite_htmy/components/tabs.py
- [ ] T003 Create Tabs dataclass skeleton in src/flowbite_htmy/components/tabs.py
- [ ] T004 Export Tab, Tabs, TabVariant, IconPosition from src/flowbite_htmy/components/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: No blocking prerequisites - all infrastructure exists (ClassBuilder, ThemeContext, Icon system, Color enum)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Basic Tab Navigation (Priority: P1) 🎯 MVP

**Goal**: Implement core tab rendering with ARIA attributes, Flowbite JavaScript integration, active tab logic, and panel visibility control

**Independent Test**: Can be fully tested by rendering a tabs component with 3 tabs containing different text content, clicking each tab button in browser, and verifying that only the selected tab's content panel is visible while others are hidden. Keyboard navigation (Tab, Enter) works without mouse.

### Tests for User Story 1 (TDD - Write FIRST, ensure FAIL)

> **⚠️ CRITICAL TDD**: Write these tests FIRST, run them to verify they FAIL, then implement

- [ ] T005 [P] [US1] Write test_tabs_renders_default_first_tab_active in tests/test_components/test_tabs.py
- [ ] T006 [P] [US1] Write test_tabs_renders_custom_active_tab in tests/test_components/test_tabs.py
- [ ] T007 [P] [US1] Write test_tabs_generates_unique_ids in tests/test_components/test_tabs.py
- [ ] T008 [P] [US1] Write test_tabs_includes_aria_attributes in tests/test_components/test_tabs.py
- [ ] T009 [P] [US1] Write test_tabs_includes_flowbite_data_attributes in tests/test_components/test_tabs.py
- [ ] T010 [P] [US1] Write test_tabs_hides_inactive_panels in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 6 tests MUST FAIL before proceeding

### Implementation for User Story 1

- [ ] T011 [US1] Implement Tab dataclass with label and content props in src/flowbite_htmy/components/tabs.py
- [ ] T012 [US1] Implement Tabs dataclass with tabs list prop in src/flowbite_htmy/components/tabs.py
- [ ] T013 [US1] Implement _get_base_id() method for unique ID generation in src/flowbite_htmy/components/tabs.py
- [ ] T014 [US1] Implement htmy() method rendering tablist container with role="tablist" in src/flowbite_htmy/components/tabs.py
- [ ] T015 [US1] Implement _render_tab() method rendering tab buttons with ARIA attributes in src/flowbite_htmy/components/tabs.py
- [ ] T016 [US1] Implement active tab logic (first tab default or is_active=True) in src/flowbite_htmy/components/tabs.py
- [ ] T017 [US1] Implement panel rendering with role="tabpanel" and hidden class logic in src/flowbite_htmy/components/tabs.py
- [ ] T018 [US1] Add Flowbite data attributes (data-tabs-toggle, data-tabs-target) in src/flowbite_htmy/components/tabs.py
- [ ] T019 [US1] Run tests for US1 → All 6 tests must PASS

**Checkpoint**: User Story 1 fully functional - basic tab navigation works with ARIA and Flowbite JS

---

## Phase 4: User Story 2 - Tab Variants and Visual Customization (Priority: P2)

**Goal**: Implement 4 visual variants (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH) with color customization and dark mode support

**Independent Test**: Can be fully tested by rendering separate tabs components with each variant, verifying Tailwind classes match Flowbite specifications via HTML inspection, testing color customization with Color.BLUE, Color.GREEN, etc., and toggling dark mode to verify dark classes apply.

### Tests for User Story 2 (TDD - Write FIRST, ensure FAIL)

- [ ] T020 [P] [US2] Write test_tabs_default_variant in tests/test_components/test_tabs.py
- [ ] T021 [P] [US2] Write test_tabs_underline_variant in tests/test_components/test_tabs.py
- [ ] T022 [P] [US2] Write test_tabs_pills_variant in tests/test_components/test_tabs.py
- [ ] T023 [P] [US2] Write test_tabs_full_width_variant in tests/test_components/test_tabs.py
- [ ] T024 [P] [US2] Write test_tabs_color_customization in tests/test_components/test_tabs.py
- [ ] T025 [P] [US2] Write test_tabs_dark_mode_classes in tests/test_components/test_tabs.py
- [ ] T026 [P] [US2] Write test_tabs_custom_classes_merged in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 7 tests MUST FAIL before proceeding

### Implementation for User Story 2

- [ ] T027 [US2] Add variant prop to Tabs dataclass (default TabVariant.DEFAULT) in src/flowbite_htmy/components/tabs.py
- [ ] T028 [US2] Add color prop to Tabs dataclass (default Color.BLUE) in src/flowbite_htmy/components/tabs.py
- [ ] T029 [US2] Implement _build_tablist_classes() method for variant-specific tablist classes in src/flowbite_htmy/components/tabs.py
- [ ] T030 [US2] Implement _build_tab_classes() method for variant-specific tab button classes in src/flowbite_htmy/components/tabs.py
- [ ] T031 [US2] Implement DEFAULT variant class logic (border-b, bg-gray-100 active) in src/flowbite_htmy/components/tabs.py
- [ ] T032 [US2] Implement UNDERLINE variant class logic (border-b-2, border-{color} active) in src/flowbite_htmy/components/tabs.py
- [ ] T033 [US2] Implement PILLS variant class logic (rounded-lg, bg-{color} active) in src/flowbite_htmy/components/tabs.py
- [ ] T034 [US2] Implement FULL_WIDTH variant class logic (w-full, rounded edges, shadow) in src/flowbite_htmy/components/tabs.py
- [ ] T035 [US2] Implement color customization via _get_color_classes() method in src/flowbite_htmy/components/tabs.py
- [ ] T036 [US2] Add dark mode classes to all variant class builders (dark:bg-*, dark:text-*, dark:border-*) in src/flowbite_htmy/components/tabs.py
- [ ] T037 [US2] Add custom class_ prop support with ClassBuilder.merge() in src/flowbite_htmy/components/tabs.py
- [ ] T038 [US2] Run tests for US2 → All 7 tests must PASS

**Checkpoint**: User Stories 1 AND 2 work independently - all 4 variants render correctly with color options

---

## Phase 5: User Story 3 - HTMX Lazy Loading and Dynamic Content (Priority: P3)

**Goal**: Support HTMX attributes for lazy loading tab content from server with revealed trigger strategy

**Independent Test**: Can be fully tested by creating a tabs component where one tab has hx_get="/api/content", rendering the HTML, verifying hx-get attribute appears on panel div (not button), and using Chrome DevTools or curl to simulate tab activation and observe HTMX request.

### Tests for User Story 3 (TDD - Write FIRST, ensure FAIL)

- [ ] T039 [P] [US3] Write test_tabs_htmx_get_attribute in tests/test_components/test_tabs.py
- [ ] T040 [P] [US3] Write test_tabs_htmx_trigger_attribute in tests/test_components/test_tabs.py
- [ ] T041 [P] [US3] Write test_tabs_htmx_multiple_attributes in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 3 tests MUST FAIL before proceeding

### Implementation for User Story 3

- [ ] T042 [P] [US3] Add HTMX props to Tab dataclass (hx_get, hx_post, hx_trigger, hx_target, hx_swap) in src/flowbite_htmy/components/tabs.py
- [ ] T043 [US3] Apply HTMX attributes to panel div (not button) in _render_tab() method in src/flowbite_htmy/components/tabs.py
- [ ] T044 [US3] Run tests for US3 → All 3 tests must PASS

**Checkpoint**: User Stories 1, 2, AND 3 work independently - HTMX lazy loading functional

---

## Phase 6: User Story 4 - Icons and Enhanced Tab Labels (Priority: P3)

**Goal**: Add icon support with left/right positioning using existing icon system

**Independent Test**: Can be fully tested by rendering tabs with Icon.USER, Icon.DASHBOARD, Icon.SETTINGS icons, inspecting HTML to verify icons appear next to labels with w-4 h-4 classes, and testing both left (default) and right icon positions via icon_position prop.

### Tests for User Story 4 (TDD - Write FIRST, ensure FAIL)

- [ ] T045 [P] [US4] Write test_tab_with_icon_left in tests/test_components/test_tabs.py
- [ ] T046 [P] [US4] Write test_tab_with_icon_right in tests/test_components/test_tabs.py
- [ ] T047 [P] [US4] Write test_tab_icon_in_disabled_state in tests/test_components/test_tabs.py
- [ ] T048 [P] [US4] Write test_tab_icons_across_variants in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 4 tests MUST FAIL before proceeding

### Implementation for User Story 4

- [ ] T049 [P] [US4] Add icon and icon_position props to Tab dataclass in src/flowbite_htmy/components/tabs.py
- [ ] T050 [US4] Import get_icon() helper from flowbite_htmy.icons in src/flowbite_htmy/components/tabs.py
- [ ] T051 [US4] Implement _render_tab_content() method for icon + label rendering in src/flowbite_htmy/components/tabs.py
- [ ] T052 [US4] Add icon left positioning logic (me-2 spacing, icon before label) in src/flowbite_htmy/components/tabs.py
- [ ] T053 [US4] Add icon right positioning logic (ms-2 spacing, icon after label) in src/flowbite_htmy/components/tabs.py
- [ ] T054 [US4] Update tab button to use inline-flex items-center for icon alignment in src/flowbite_htmy/components/tabs.py
- [ ] T055 [US4] Run tests for US4 → All 4 tests must PASS

**Checkpoint**: User Stories 1-4 work independently - icons render with correct positioning

---

## Phase 7: User Story 5 - Disabled Tabs (Priority: P3)

**Goal**: Implement disabled tab state with non-interactive rendering and disabled styling

**Independent Test**: Can be fully tested by rendering a tabs component where one tab has disabled=True, inspecting HTML to verify it renders as <a> (not <button>), has no href attribute, shows cursor-not-allowed and gray colors, and attempting to click/focus it in browser to confirm it's non-interactive.

### Tests for User Story 5 (TDD - Write FIRST, ensure FAIL)

- [ ] T056 [P] [US5] Write test_disabled_tab_styling in tests/test_components/test_tabs.py
- [ ] T057 [P] [US5] Write test_disabled_tab_cannot_be_active in tests/test_components/test_tabs.py
- [ ] T058 [P] [US5] Write test_disabled_tab_dark_mode in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 3 tests MUST FAIL before proceeding

### Implementation for User Story 5

- [ ] T059 [US5] Add disabled prop to Tab dataclass (default False) in src/flowbite_htmy/components/tabs.py
- [ ] T060 [US5] Update _render_tab() to render disabled tabs as html.a() without href in src/flowbite_htmy/components/tabs.py
- [ ] T061 [US5] Add disabled tab classes (text-gray-400, cursor-not-allowed, dark:text-gray-500) in src/flowbite_htmy/components/tabs.py
- [ ] T062 [US5] Update active tab logic to ignore is_active=True if disabled=True in src/flowbite_htmy/components/tabs.py
- [ ] T063 [US5] Run tests for US5 → All 3 tests must PASS

**Checkpoint**: All 5 user stories work independently - disabled tabs non-interactive

---

## Phase 8: Edge Cases & Validation

**Goal**: Handle edge cases for robustness

**Independent Test**: Test single tab, empty content, multiple active tabs, and custom tabs_id scenarios

### Tests for Edge Cases (TDD - Write FIRST, ensure FAIL)

- [ ] T064 [P] Write test_single_tab in tests/test_components/test_tabs.py
- [ ] T065 [P] Write test_empty_content in tests/test_components/test_tabs.py
- [ ] T066 [P] Write test_multiple_active_tabs_first_wins in tests/test_components/test_tabs.py
- [ ] T067 [P] Write test_custom_tabs_id_override in tests/test_components/test_tabs.py

**TDD Checkpoint**: Run tests → All 4 tests MUST FAIL before proceeding

### Implementation for Edge Cases

- [ ] T068 [P] Implement single tab handling (renders full tablist UI) in src/flowbite_htmy/components/tabs.py
- [ ] T069 [P] Implement empty content handling (render panel with no content child) in src/flowbite_htmy/components/tabs.py
- [ ] T070 [P] Implement multiple active tabs logic (first wins) in src/flowbite_htmy/components/tabs.py
- [ ] T071 [P] Implement custom tabs_id override support in _get_base_id() in src/flowbite_htmy/components/tabs.py
- [ ] T072 Run edge case tests → All 4 tests must PASS

**Checkpoint**: All edge cases handled - component is robust

---

## Phase 9: Showcase & Integration

**Purpose**: Create showcase app and integrate into consolidated showcase

- [ ] T073 Create examples/tabs.py with Jinja template in examples/templates/tabs.html.jinja
- [ ] T074 [P] Add DEFAULT variant showcase section in examples/tabs.py
- [ ] T075 [P] Add UNDERLINE variant showcase section in examples/tabs.py
- [ ] T076 [P] Add PILLS variant showcase section in examples/tabs.py
- [ ] T077 [P] Add FULL_WIDTH variant showcase section in examples/tabs.py
- [ ] T078 [P] Add color customization examples in examples/tabs.py
- [ ] T079 [P] Add HTMX lazy loading example with /api/dashboard endpoint in examples/tabs.py
- [ ] T080 [P] Add icon examples (left and right positioning) in examples/tabs.py
- [ ] T081 [P] Add disabled tab example in examples/tabs.py
- [ ] T082 Update examples/showcase.py to add tabs route and navigation link
- [ ] T083 Test showcase app → Run python examples/tabs.py and verify all features work in browser

**Checkpoint**: Showcase demonstrates all features - ready for manual testing

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and documentation

- [ ] T084 [P] Run full test suite → pytest (verify 232 tests pass: 205 existing + 27 new)
- [ ] T085 [P] Check test coverage → pytest --cov (verify >90% on tabs.py)
- [ ] T086 [P] Type check → mypy src/flowbite_htmy (verify 100% type coverage, strict mode)
- [ ] T087 [P] Lint → ruff check src/flowbite_htmy (verify clean)
- [ ] T088 [P] Format → ruff format src/flowbite_htmy (apply formatting)
- [ ] T089 Test keyboard navigation in browser (arrow keys, Enter, Tab) with Flowbite JS
- [ ] T090 Test dark mode toggle in showcase (verify dark classes apply correctly)
- [ ] T091 [P] Test HTMX lazy loading in browser (verify revealed trigger fires, content loads)
- [ ] T092 Update CLAUDE.md if needed (already updated by .specify/scripts/bash/update-agent-context.sh)

**Checkpoint**: All quality gates passed - ready for commit

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Skipped (no blocking prerequisites)
- **User Stories (Phase 3-7)**: Independent - can proceed in any order after Setup
  - Recommended: P1 → P2 → P3 → P4 → P5 (priority order)
  - Alternative: Parallel execution if multiple developers
- **Edge Cases (Phase 8)**: Depends on core implementation from US1
- **Showcase (Phase 9)**: Depends on all user stories being complete
- **Polish (Phase 10)**: Depends on Showcase completion

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies - fully independent (basic tab navigation)
- **User Story 2 (P2)**: No dependencies - fully independent (visual variants, builds on US1 structure)
- **User Story 3 (P3)**: No dependencies - fully independent (HTMX attributes, orthogonal to US1/US2)
- **User Story 4 (P3)**: No dependencies - fully independent (icon rendering, orthogonal to others)
- **User Story 5 (P3)**: No dependencies - fully independent (disabled state, orthogonal to others)

**All user stories are independently testable and deliverable**

### Within Each User Story (TDD Workflow)

1. **Tests FIRST**: Write all tests for the story, run them, verify they FAIL
2. **Implementation**: Implement minimal code to pass tests
3. **Verification**: Run tests again, verify they PASS
4. **Refactor**: Clean up code while keeping tests green
5. **Story Complete**: Move to next priority

### Parallel Opportunities

**Setup Phase (Phase 1)**:
- T001, T002, T003, T004 can run in parallel (different concerns)

**User Story Tests** (within each story):
- All tests for a given user story marked [P] can be written in parallel

**User Story Implementation**:
- Different user stories (US1-US5) can be implemented in parallel by different developers
- Within US2: T031, T032, T033, T034 (variant classes) can run in parallel
- Within US3: T042, T043 can run in parallel
- Within US4: T049, T050 can run in parallel
- Within US5: T059, T060, T061 can run in parallel

**Showcase Phase (Phase 9)**:
- T074-T081 (showcase sections) can run in parallel

**Polish Phase (Phase 10)**:
- T084, T085, T086, T087, T088 can run in parallel

---

## Parallel Example: User Story 1

```bash
# Step 1: Write all tests in parallel
Task: "Write test_tabs_renders_default_first_tab_active in tests/test_components/test_tabs.py"
Task: "Write test_tabs_renders_custom_active_tab in tests/test_components/test_tabs.py"
Task: "Write test_tabs_generates_unique_ids in tests/test_components/test_tabs.py"
Task: "Write test_tabs_includes_aria_attributes in tests/test_components/test_tabs.py"
Task: "Write test_tabs_includes_flowbite_data_attributes in tests/test_components/test_tabs.py"
Task: "Write test_tabs_hides_inactive_panels in tests/test_components/test_tabs.py"

# Step 2: Run tests → ALL FAIL (Red)

# Step 3: Implement sequentially (dependencies exist)
# T011 → T012 → T013 → T014 → T015 → T016 → T017 → T018

# Step 4: Run tests → ALL PASS (Green)
```

---

## Parallel Example: User Story 2

```bash
# Step 1: Write all tests in parallel
Task: "Write test_tabs_default_variant in tests/test_components/test_tabs.py"
Task: "Write test_tabs_underline_variant in tests/test_components/test_tabs.py"
Task: "Write test_tabs_pills_variant in tests/test_components/test_tabs.py"
Task: "Write test_tabs_full_width_variant in tests/test_components/test_tabs.py"
Task: "Write test_tabs_color_customization in tests/test_components/test_tabs.py"
Task: "Write test_tabs_dark_mode_classes in tests/test_components/test_tabs.py"
Task: "Write test_tabs_custom_classes_merged in tests/test_components/test_tabs.py"

# Step 2: Run tests → ALL FAIL (Red)

# Step 3: Implement variant classes in parallel
Task: "Implement DEFAULT variant class logic"
Task: "Implement UNDERLINE variant class logic"
Task: "Implement PILLS variant class logic"
Task: "Implement FULL_WIDTH variant class logic"

# Step 4: Run tests → ALL PASS (Green)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 3: User Story 1 (T005-T019)
   - Write tests (T005-T010)
   - Verify tests FAIL
   - Implement (T011-T018)
   - Verify tests PASS (T019)
3. **STOP and VALIDATE**: Test basic tab navigation in browser
4. MVP complete! Basic tabs work with ARIA and Flowbite JS

### Incremental Delivery (Recommended)

1. **Setup** → Enums and skeletons ready (T001-T004)
2. **US1** → Basic tab navigation (T005-T019) → **Deploy/Demo MVP!**
3. **US2** → Add 4 variants + colors (T020-T038) → **Deploy/Demo**
4. **US3** → Add HTMX lazy loading (T039-T044) → **Deploy/Demo**
5. **US4** → Add icons (T045-T055) → **Deploy/Demo**
6. **US5** → Add disabled state (T056-T063) → **Deploy/Demo**
7. **Edge Cases** → Robustness (T064-T072)
8. **Showcase** → Demo all features (T073-T083)
9. **Polish** → Quality gates (T084-T092) → **Ready for PR**

Each story adds value without breaking previous stories!

### Parallel Team Strategy

With multiple developers after Setup:

1. **Setup** (all together): T001-T004
2. Once Setup done (parallel user stories):
   - Developer A: US1 Basic Navigation (T005-T019)
   - Developer B: US2 Variants (T020-T038)
   - Developer C: US3 HTMX + US4 Icons (T039-T055)
   - Developer D: US5 Disabled (T056-T063)
3. Integrate and test independently
4. All together: Showcase (T073-T083) + Polish (T084-T092)

---

## Task Summary

**Total Tasks**: 92

### By Phase:
- **Phase 1 (Setup)**: 4 tasks
- **Phase 2 (Foundational)**: 0 tasks (no blocking prerequisites)
- **Phase 3 (US1 - Basic Navigation)**: 15 tasks (6 tests + 9 implementation)
- **Phase 4 (US2 - Variants)**: 19 tasks (7 tests + 12 implementation)
- **Phase 5 (US3 - HTMX)**: 6 tasks (3 tests + 3 implementation)
- **Phase 6 (US4 - Icons)**: 11 tasks (4 tests + 7 implementation)
- **Phase 7 (US5 - Disabled)**: 9 tasks (3 tests + 6 implementation)
- **Phase 8 (Edge Cases)**: 9 tasks (4 tests + 5 implementation)
- **Phase 9 (Showcase)**: 11 tasks
- **Phase 10 (Polish)**: 9 tasks

### By Category:
- **Tests**: 27 tasks (strict TDD)
- **Implementation**: 42 tasks
- **Showcase**: 11 tasks
- **Quality**: 9 tasks
- **Setup**: 4 tasks

### Parallel Opportunities:
- Setup: 4 tasks can run in parallel
- Tests within each story: All marked [P]
- Variant implementations (US2): 4 tasks in parallel
- User stories (US1-US5): Can run in parallel if multiple developers
- Showcase sections: 8 tasks in parallel
- Quality checks: 5 tasks in parallel

**Estimated**: ~30-40 tasks can run in parallel across the project

---

## Notes

- **Strict TDD**: All tests written BEFORE implementation, verify FAIL before coding
- **[P] tasks**: Different files or independent concerns, can run in parallel
- **[Story] labels**: Map each task to specific user story for traceability
- **Independent stories**: Each US1-US5 is independently completable and testable
- **Red-Green-Refactor**: Write test (Red) → Implement (Green) → Refactor
- **Commit frequently**: After each task or logical group
- **Quality gates**: All must pass before PR (tests, coverage, mypy, ruff)
- **Avoid**: Vague tasks, same file conflicts, cross-story dependencies

---

## Format Validation

✅ **All 92 tasks follow checklist format**:
- Start with `- [ ]` (checkbox)
- Include task ID (T001-T092)
- Mark [P] if parallelizable
- Mark [Story] for user story phases (US1-US5)
- Include exact file paths in descriptions

✅ **All user stories independently testable**:
- US1: Basic tab navigation with ARIA
- US2: 4 variants with color customization
- US3: HTMX lazy loading
- US4: Icons with positioning
- US5: Disabled tab state

✅ **MVP scope clearly defined**: US1 only (basic tab navigation)

**Ready for implementation via `/speckit.implement`**
