# Tasks: Component Quality Review and Template Cleanup

**Input**: Design documents from `/specs/004-component-review/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/component-quality-checklist.md, quickstart.md

**Tests**: This feature follows TDD principles. All 187 existing tests must pass before and after each change. No new tests required (refactoring only).

**Organization**: Tasks are grouped by user story (P1, P2, P3) to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

All paths relative to repository root: `/home/jian/Work/personal/flowbite-htmy/`

- Components: `src/flowbite_htmy/components/*.py`
- Tests: `tests/test_components/*.py`
- Templates: `examples/templates/*.jinja`
- Showcase: `examples/showcase.py`

---

## Phase 1: Setup (Validation & Baseline)

**Purpose**: Establish baseline and validate prerequisites before making any changes

- [ ] T001 Verify all 187 existing tests pass by running `pytest`
- [ ] T002 Run coverage baseline: `pytest --cov=src/flowbite_htmy/components --cov-report=term-missing`
- [ ] T003 [P] Verify showcase application runs: `python examples/showcase.py`
- [ ] T004 [P] Run mypy strict mode: `mypy src/flowbite_htmy`
- [ ] T005 [P] Run ruff linting: `ruff check src/flowbite_htmy`
- [ ] T006 Create baseline git commit for rollback safety

**Checkpoint**: All quality gates pass - ready to begin improvements

---

## Phase 2: User Story 1 - Template Cleanup (Priority: P1) 🎯 Quick Win

**Goal**: Remove unused `base.html.jinja` template to eliminate technical debt and simplify codebase

**Independent Test**: Showcase application runs without errors after template deletion (verify at http://localhost:8000)

**Research Findings** (from research.md lines 9-55):
- `base.html.jinja` has zero references in codebase
- `showcase-layout.html.jinja` is actively used (14 references)
- Template was replaced 8 days ago (commit 5bd52b9)
- Safe to delete with no breaking changes

### Implementation for User Story 1

- [ ] T007 [US1] Verify no references to base.html.jinja: `grep -r "base\.html\.jinja" examples/`
- [ ] T008 [US1] Check git history for last use: `git log --all --full-history -- examples/templates/base.html.jinja`
- [ ] T009 [US1] Delete unused template file: `rm examples/templates/base.html.jinja`
- [ ] T010 [US1] Run showcase application to verify no breakage: `python examples/showcase.py`
- [ ] T011 [US1] Visit all showcase pages to confirm layout works (http://localhost:8000)
- [ ] T012 [US1] Commit template cleanup: `git commit -m "Remove unused base.html.jinja template"`

**Checkpoint**: Template cleanup complete - only showcase-layout.html.jinja remains, showcase fully functional

---

## Phase 3: User Story 2 - Early Component Review (Priority: P2)

**Goal**: Fix critical quality issues and standardize patterns in Button, Badge, Alert, and Avatar components

**Independent Test**: All 187 tests pass, coverage maintains >90%, components render correctly in showcase

**Research Findings** (from research.md lines 59-210):
- **HP-1**: Badge and Alert use conditional dark mode (anti-pattern)
- **HP-2**: Button missing 5 HTMX attributes (compared to Toast reference)
- **HP-3**: Button.type naming convention violation (should be type_)
- **HP-4**: Docstrings good but can be enhanced with more examples

### Badge Component Improvements

**Issue**: Conditional dark mode pattern (research.md lines 84-104)
- Current: `if theme.dark_mode and dark_classes: builder.add(dark_classes)` (badge.py:152-154)
- Target: Always include dark mode classes (Toast pattern)

- [ ] T013 [P] [US2] Read Badge component: `src/flowbite_htmy/components/badge.py`
- [ ] T014 [US2] Review Badge tests to understand coverage: `tests/test_components/test_badge.py`
- [ ] T015 [US2] Run baseline tests for Badge: `pytest tests/test_components/test_badge.py -v`
- [ ] T016 [US2] Fix dark mode anti-pattern in Badge component at line 152-154 in src/flowbite_htmy/components/badge.py
- [ ] T017 [US2] Remove conditional `if theme.dark_mode` check, always include dark classes in src/flowbite_htmy/components/badge.py
- [ ] T018 [US2] Update `_get_dark_classes()` method to return classes without conditional in src/flowbite_htmy/components/badge.py
- [ ] T019 [US2] Verify all Badge tests pass: `pytest tests/test_components/test_badge.py -v`
- [ ] T020 [US2] Check Badge coverage: `pytest --cov=src/flowbite_htmy/components/badge tests/test_components/test_badge.py`
- [ ] T021 [US2] Visual verification: Check Badge in showcase at http://localhost:8000/badges
- [ ] T022 [US2] Commit Badge dark mode fix: `git commit -m "Fix Badge dark mode anti-pattern - always include dark classes"`

**Checkpoint**: Badge component fixed - dark mode pattern correct, all tests pass

### Alert Component Improvements

**Issue**: Conditional dark mode pattern (research.md lines 84-104)
- Current: `if dark_classes: builder.add(dark_classes)` (alert.py:137-139)
- Target: Always include dark mode classes

- [ ] T023 [P] [US2] Read Alert component: `src/flowbite_htmy/components/alert.py`
- [ ] T024 [US2] Review Alert tests: `tests/test_components/test_alert.py`
- [ ] T025 [US2] Run baseline tests for Alert: `pytest tests/test_components/test_alert.py -v`
- [ ] T026 [US2] Fix dark mode anti-pattern in Alert component at line 137-139 in src/flowbite_htmy/components/alert.py
- [ ] T027 [US2] Remove conditional check, always include dark classes in src/flowbite_htmy/components/alert.py
- [ ] T028 [US2] Update dark class handling in `_build_classes()` method in src/flowbite_htmy/components/alert.py
- [ ] T029 [US2] Verify all Alert tests pass: `pytest tests/test_components/test_alert.py -v`
- [ ] T030 [US2] Check Alert coverage: `pytest --cov=src/flowbite_htmy/components/alert tests/test_components/test_alert.py`
- [ ] T031 [US2] Visual verification: Check Alert in showcase at http://localhost:8000/alerts
- [ ] T032 [US2] Commit Alert dark mode fix: `git commit -m "Fix Alert dark mode anti-pattern - always include dark classes"`

**Checkpoint**: Alert component fixed - dark mode pattern correct, all tests pass

### Button Component Improvements

**Issue 1**: Missing HTMX attributes (research.md lines 62-77)
- Current: 5/10 attrs (hx_get, hx_post, hx_target, hx_swap, hx_trigger)
- Missing: hx_put, hx_delete, hx_patch, hx_push_url, hx_select
- Target: Full HTMX coverage like Toast (toast.py:22-31)

- [ ] T033 [P] [US2] Read Button component: `src/flowbite_htmy/components/button.py`
- [ ] T034 [US2] Review Button tests: `tests/test_components/test_button.py`
- [ ] T035 [US2] Run baseline tests for Button: `pytest tests/test_components/test_button.py -v`
- [ ] T036 [US2] Add hx_put prop (str | None = None) to Button at line ~88 in src/flowbite_htmy/components/button.py
- [ ] T037 [US2] Add hx_delete prop (str | None = None) to Button in src/flowbite_htmy/components/button.py
- [ ] T038 [US2] Add hx_patch prop (str | None = None) to Button in src/flowbite_htmy/components/button.py
- [ ] T039 [US2] Add hx_push_url prop (str | bool | None = None) to Button in src/flowbite_htmy/components/button.py
- [ ] T040 [US2] Add hx_select prop (str | None = None) to Button in src/flowbite_htmy/components/button.py
- [ ] T041 [US2] Add docstrings for new HTMX props in src/flowbite_htmy/components/button.py
- [ ] T042 [US2] Pass new HTMX attrs to html.button() in htmy() method in src/flowbite_htmy/components/button.py
- [ ] T043 [US2] Verify Button tests pass: `pytest tests/test_components/test_button.py -v`
- [ ] T044 [US2] Check Button coverage: `pytest --cov=src/flowbite_htmy/components/button tests/test_components/test_button.py`
- [ ] T045 [US2] Verify Button in showcase: http://localhost:8000/buttons
- [ ] T046 [US2] Commit Button HTMX expansion: `git commit -m "Add missing HTMX attributes to Button (hx_put, hx_delete, hx_patch, hx_push_url, hx_select)"`

**Issue 2**: Prop naming convention violation (research.md lines 165-182)
- Current: `type: str` (button.py:70)
- Target: `type_: str` (Toast pattern)
- **WARNING**: This is a BREAKING CHANGE - requires careful consideration

- [ ] T047 [US2] Document breaking change risk for Button.type → Button.type_ rename
- [ ] T048 [US2] Search codebase for Button.type usage: `grep -r "Button.*type" examples/`
- [ ] T049 [US2] Check test assertions for type prop: `grep "type" tests/test_components/test_button.py`
- [ ] T050 [US2] DECISION POINT: Consult user on whether to proceed with breaking change or defer to v2.0
- [ ] T051 [US2] IF APPROVED: Rename type → type_ in Button dataclass in src/flowbite_htmy/components/button.py
- [ ] T052 [US2] IF APPROVED: Update all showcase examples using Button type in examples/showcase.py and examples/buttons.py
- [ ] T053 [US2] IF APPROVED: Run all tests: `pytest`
- [ ] T054 [US2] IF APPROVED: Commit Button.type rename: `git commit -m "BREAKING: Rename Button.type → Button.type_ for consistency"`
- [ ] T055 [US2] IF DEFERRED: Document as known issue for v2.0 in specs/004-component-review/research.md

**Checkpoint**: Button improvements complete (HTMX attrs added, type rename decision made)

### Avatar Component Verification

**Finding**: Avatar already follows all patterns correctly (research.md lines 83-89, 125, 141)
- Dark mode: Always-included ✅
- ClassBuilder: Consistent ✅
- Type hints: 100% ✅
- Coverage: 94% ✅

- [ ] T056 [P] [US2] Review Avatar component against quality checklist: `src/flowbite_htmy/components/avatar.py`
- [ ] T057 [US2] Verify Avatar tests pass: `pytest tests/test_components/test_avatar.py -v`
- [ ] T058 [US2] Confirm Avatar coverage >90%: `pytest --cov=src/flowbite_htmy/components/avatar tests/test_components/test_avatar.py`
- [ ] T059 [US2] Document Avatar as reference implementation (no changes needed) in research.md

**Checkpoint**: All 4 early components reviewed - Badge/Alert fixed, Button improved, Avatar verified

### Final Validation for User Story 2

- [ ] T060 [US2] Run full test suite: `pytest`
- [ ] T061 [US2] Verify all 187 tests pass
- [ ] T062 [US2] Check overall coverage: `pytest --cov=src/flowbite_htmy/components`
- [ ] T063 [US2] Verify coverage >90% maintained
- [ ] T064 [US2] Run mypy strict: `mypy src/flowbite_htmy`
- [ ] T065 [US2] Run ruff linting: `ruff check src/flowbite_htmy`
- [ ] T066 [US2] Run ruff formatting: `ruff format src/flowbite_htmy`
- [ ] T067 [US2] Start showcase application: `python examples/showcase.py`
- [ ] T068 [US2] Manual verification: Visit all component pages in showcase
  - http://localhost:8000/buttons - Check Button variants
  - http://localhost:8000/badges - Verify Badge dark mode works
  - http://localhost:8000/alerts - Verify Alert dark mode works
  - http://localhost:8000/avatars - Check Avatar rendering
- [ ] T069 [US2] Create summary of improvements in specs/004-component-review/IMPROVEMENTS.md

**Checkpoint**: Component review complete - all improvements implemented, all tests pass, quality gates satisfied

---

## Phase 4: User Story 3 - Component Quality Standards Documentation (Priority: P3)

**Goal**: Document quality patterns learned from component review to prevent regression in future work

**Independent Test**: Quality standards document can be used to review any component and identify both strengths and issues

**Research Findings**:
- Quality checklist already created: `specs/004-component-review/contracts/component-quality-checklist.md`
- Need to create user-facing documentation in docs/ folder

### Implementation for User Story 3

- [ ] T070 [P] [US3] Create docs directory if not exists: `mkdir -p docs/`
- [ ] T071 [US3] Create component quality standards document: `docs/component-quality-standards.md`
- [ ] T072 [US3] Copy quality criteria from contracts/component-quality-checklist.md
- [ ] T073 [US3] Add real examples from Button, Badge, Alert, Avatar showing correct patterns
- [ ] T074 [US3] Add anti-pattern examples (conditional dark mode) with explanations
- [ ] T075 [US3] Document HTMX attribute coverage expectations for interactive vs display components
- [ ] T076 [US3] Add reference implementations section (Toast, Modal, Avatar)
- [ ] T077 [US3] Create quick checklist for new component PRs
- [ ] T078 [US3] Add validation commands (pytest, mypy, ruff) to standards doc
- [ ] T079 [US3] Link to quality standards from CLAUDE.md under "Component Implementation Pattern"
- [ ] T080 [US3] Commit quality standards documentation: `git commit -m "Add component quality standards documentation"`

**Checkpoint**: Quality standards documented - future components have clear reference guide

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final cleanup and documentation updates

- [ ] T081 [P] Update CLAUDE.md with lessons learned from component review
- [ ] T082 [P] Add "Component Review Findings" section to CLAUDE.md documenting anti-patterns
- [ ] T083 Document dark mode pattern explicitly in CLAUDE.md (always-included, not conditional)
- [ ] T084 Update constitution.md if new principles emerged (likely not needed)
- [ ] T085 Create session note in Basic Memory documenting this review session
- [ ] T086 [P] Final test run: `pytest`
- [ ] T087 Final coverage check: `pytest --cov=src/flowbite_htmy`
- [ ] T088 Final mypy check: `mypy src/flowbite_htmy`
- [ ] T089 Final ruff check: `ruff check src/flowbite_htmy`
- [ ] T090 Final showcase verification: Visit all pages and verify dark mode toggle works
- [ ] T091 Create PR summary documenting all improvements
- [ ] T092 Run quickstart.md validation workflow from specs/004-component-review/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **User Story 1 (Phase 2)**: Depends on Setup - Independent of other stories
- **User Story 2 (Phase 3)**: Depends on Setup - Independent of US1
- **User Story 3 (Phase 4)**: Depends on US2 completion (needs learned patterns)
- **Polish (Phase 5)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Template Cleanup - INDEPENDENT, can start after Setup
- **User Story 2 (P2)**: Component Review - INDEPENDENT, can start after Setup (parallel with US1)
- **User Story 3 (P3)**: Documentation - DEPENDS on US2 (needs review findings)

### Within Each User Story

**US1: Template Cleanup** (Sequential):
1. Verify no references (T007-T008)
2. Delete template (T009)
3. Validate (T010-T011)
4. Commit (T012)

**US2: Component Review** (Mixed):
- Badge improvements (T013-T022) can run PARALLEL to Alert improvements (T023-T032)
- Badge improvements (T013-T022) can run PARALLEL to Avatar verification (T056-T059)
- Alert improvements (T023-T032) can run PARALLEL to Avatar verification (T056-T059)
- Button improvements (T033-T055) should run AFTER one component is complete to learn from it
- Final validation (T060-T069) must wait for ALL components

**US3: Documentation** (Sequential):
1. Create directory (T070)
2. Write standards (T071-T079)
3. Link from CLAUDE.md (T079)
4. Commit (T080)

### Parallel Opportunities

**Within Phase 1 (Setup)**:
- T003 (showcase verification) PARALLEL with T004 (mypy) PARALLEL with T005 (ruff)

**Within Phase 3 (User Story 2)**:
- T013 (Read Badge) PARALLEL with T023 (Read Alert) PARALLEL with T033 (Read Button) PARALLEL with T056 (Review Avatar)
- Badge fixes (T013-T022) PARALLEL with Alert fixes (T023-T032) - Different files
- Avatar verification (T056-T059) PARALLEL with Badge/Alert fixes

**Within Phase 4 (User Story 3)**:
- T070 (mkdir docs) PARALLEL with reading existing artifacts

**Within Phase 5 (Polish)**:
- T081 (Update CLAUDE.md) PARALLEL with T085 (Create session note) PARALLEL with T086 (Final test run)

---

## Parallel Example: Badge and Alert Fixes

```bash
# These can run simultaneously (different files, no dependencies):
Task T013-T022: "Fix Badge dark mode pattern in src/flowbite_htmy/components/badge.py"
Task T023-T032: "Fix Alert dark mode pattern in src/flowbite_htmy/components/alert.py"
Task T056-T059: "Verify Avatar component in src/flowbite_htmy/components/avatar.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only - Quick Win)

1. Complete Phase 1: Setup (T001-T006) - Baseline validation
2. Complete Phase 2: User Story 1 (T007-T012) - Template cleanup
3. **STOP and VALIDATE**: Showcase runs without unused template
4. Commit and optionally merge quick win

**Time Estimate**: 15-30 minutes

### Incremental Delivery (Recommended)

1. Complete Setup (Phase 1) → Foundation ready
2. Add US1 (Template Cleanup) → Test independently → Commit (Quick Win! ✅)
3. Add US2 (Component Review) → Test independently → Commit (Quality Fixes! ✅)
4. Add US3 (Documentation) → Test independently → Commit (Standards! ✅)
5. Polish → Final validation → Merge to master

**Time Estimate**: 3-6 hours total

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup together (Phase 1)
2. Once Setup done:
   - Developer A: User Story 1 (Template Cleanup - 15 min)
   - Developer B: User Story 2.1 (Badge/Alert fixes - 1 hr)
   - Developer C: User Story 2.2 (Button improvements - 2 hrs)
3. After US2 complete:
   - Any developer: User Story 3 (Documentation - 1 hr)

---

## Breaking Change Considerations

**Button.type → Button.type_ Rename** (Tasks T050-T055):

This is a **BREAKING CHANGE** that should be discussed with the user:

**Arguments FOR**:
- Fixes naming convention inconsistency
- Aligns with Toast pattern (type_)
- Matches Python best practices (trailing underscore for reserved words)

**Arguments AGAINST**:
- Breaks existing code using Button(type="submit")
- Requires updating all showcase examples
- May break user code in production
- Could be deferred to v2.0 with deprecation warning

**Recommendation**: Defer to v2.0 OR get explicit user approval before proceeding with tasks T051-T054.

---

## Success Criteria Validation

- **SC-001** ✅: Unused template removed (T009), showcase works (T010-T011)
- **SC-002** ✅: >3 improvements identified (7 total: HP-1 Badge dark mode, HP-2 Alert dark mode, HP-3 Button HTMX attrs, HP-4 Button type naming, MP-1 docstrings, LP-1 test patterns, LP-2 standards doc)
- **SC-003** ✅: All 187 tests pass validated at T001, T060-T061, T086
- **SC-004** ✅: Coverage >90% validated at T002, T062-T063, T087
- **SC-005** ✅: No new clarifications - all decisions informed by research.md

---

## Notes

- [P] tasks = different files, no blocking dependencies within same phase
- [Story] label maps task to specific user story for traceability and independent testing
- Each user story independently testable at its checkpoint
- TDD enforced: All 187 existing tests must pass before/after each change
- Breaking change (Button.type) requires explicit user approval (T050)
- Commit after each major improvement (T012, T022, T032, T046, T054, T080)
- Quality gates (pytest, mypy, ruff, showcase) validated repeatedly (T001-T005, T060-T068, T086-T090)
- Dark mode pattern is CRITICAL: Always include dark: classes, never conditional

**Total Tasks**: 92 tasks across 5 phases
**Estimated Time**: 3-6 hours (with MVP in 15-30 min)
**Breaking Changes**: 1 (Button.type → type_, requires approval)
**Quality Improvements**: 7 identified (3 high priority, 2 medium, 2 low)
