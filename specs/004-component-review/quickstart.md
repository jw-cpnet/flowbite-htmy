# Component Review TDD Workflow

**Feature**: 004-component-review
**Version**: 1.0.0
**Date**: 2025-11-16

---

## Purpose

This guide provides a step-by-step TDD workflow for reviewing and improving Phase 1 components (Button, Badge, Alert, Avatar) based on patterns learned from Phase 2 implementations (Toast, Modal, Select).

**Key Principles**:
1. **Test-First** - Validate with tests before changing code
2. **Backward Compatible** - All 187 existing tests must continue passing
3. **Incremental** - One improvement at a time, commit frequently
4. **Quality Gates** - Every change validated by pytest, mypy, ruff

---

## Prerequisites

### Environment Setup

- [ ] **Python 3.11+** installed
- [ ] **Development dependencies** installed: `pip install -e ".[dev]"`
- [ ] **Working directory**: `/home/jian/Work/personal/flowbite-htmy`
- [ ] **Branch**: `004-component-review` (create if doesn't exist)

### Required Artifacts

- [ ] **Research complete**: `specs/004-component-review/research.md` exists and contains findings
- [ ] **Data model defined**: `specs/004-component-review/data-model.md` for structuring findings
- [ ] **Quality checklist**: `specs/004-component-review/contracts/component-quality-checklist.md` for validation

### Baseline Validation

Run these commands to confirm starting state:

```bash
# Ensure all tests pass
pytest

# Verify test count (should be 187 tests)
pytest --collect-only | grep "test session starts"

# Check current coverage
pytest --cov=src/flowbite_htmy/components

# Type check entire package
mypy --strict src/flowbite_htmy

# Lint check
ruff check src/flowbite_htmy

# Verify showcase runs
python examples/showcase.py &
# Open http://localhost:8000, verify all components work, then Ctrl+C
```

**All commands must succeed before proceeding.**

---

## Workflow Steps

### Step 1: Baseline Validation

**Goal**: Establish known-good state before making any changes.

#### 1.1 Run Full Test Suite

```bash
# Run all tests with coverage
pytest --cov=src/flowbite_htmy/components

# Expected output:
# - 187 tests collected
# - All tests PASSED
# - Coverage: >90%
```

**Validation**:
- [ ] 187 tests collected and passed
- [ ] Coverage >90% overall
- [ ] Zero failures, zero errors

#### 1.2 Record Component Coverage Baseline

Run coverage for each Phase 1 component:

```bash
# Button coverage
pytest --cov=src/flowbite_htmy/components/button \
       --cov-report=term-missing \
       tests/test_components/test_button.py

# Badge coverage
pytest --cov=src/flowbite_htmy/components/badge \
       --cov-report=term-missing \
       tests/test_components/test_badge.py

# Alert coverage
pytest --cov=src/flowbite_htmy/components/alert \
       --cov-report=term-missing \
       tests/test_components/test_alert.py

# Avatar coverage
pytest --cov=src/flowbite_htmy/components/avatar \
       --cov-report=term-missing \
       tests/test_components/test_avatar.py
```

**Record baseline** in table format:

| Component | Coverage % | Tests | Untested Lines |
|-----------|-----------|-------|----------------|
| Button | ? | ? | (from --cov-report=term-missing) |
| Badge | ? | ? | |
| Alert | ? | ? | |
| Avatar | ? | ? | |

#### 1.3 Commit Baseline State

```bash
# Commit current state as baseline
git add -A
git commit -m "Baseline: Record pre-review state

- 187 tests passing
- Coverage: [record % from step 1.2]
- Component baselines documented in specs/004-component-review/baseline.md

This commit serves as rollback point for review process."
```

---

### Step 2: Component-by-Component Review

**Process**: Review each component systematically against quality checklist.

**Order** (by implementation date, oldest first):
1. Button (earliest Phase 1 component)
2. Badge
3. Alert
4. Avatar (latest Phase 1 component)

---

#### 2.1 Read Current Implementation

**For each component** (example: Button):

##### Open Files

```bash
# Component implementation
vim src/flowbite_htmy/components/button.py

# Test file
vim tests/test_components/test_button.py

# Reference implementation (Toast)
vim src/flowbite_htmy/components/toast.py
```

##### Review Against Checklist

Open `specs/004-component-review/contracts/component-quality-checklist.md` and check:

**Critical Criteria**:
- [ ] Type Safety: All props typed, mypy passes
- [ ] Test Coverage: >90%
- [ ] Backward Compatibility: No breaking changes allowed

**Important Criteria**:
- [ ] Dark Mode: Always-included pattern (not conditional)
- [ ] ClassBuilder: Consistent usage

**Nice-to-Have**:
- [ ] HTMX: Full coverage for interactive components
- [ ] Documentation: Multiple examples
- [ ] Props: Naming conventions (e.g., `type_` not `type`)

---

#### 2.2 Identify Improvements

**Cross-reference with research findings**:

```bash
# View research findings for component
grep -A 30 "Button Component" specs/004-component-review/research.md
```

**Create improvement list** using data model from `data-model.md`:

**Example** (Button):

```python
# Record in notebook or comment file
button_improvements = [
    {
        "type": "add_htmx_attrs",
        "description": "Add missing 5 HTMX attrs (hx_put, hx_delete, hx_patch, hx_push_url, hx_select)",
        "priority": "high",
        "breaking_risk": "none",
        "effort": "small",
    },
    {
        "type": "fix_naming",
        "description": "Rename 'type' → 'type_' for convention",
        "priority": "low",
        "breaking_risk": "high",  # DEFER to v0.2.0
        "effort": "medium",
    }
]
```

**Filter for backward compatible changes only**:
- High priority + breaking_risk="none"
- Medium priority + breaking_risk="none"
- Skip breaking_risk="high" (defer to major version)

---

#### 2.3 TDD Cycle for Each Improvement

**For each improvement** (starting with highest priority):

##### Phase: RED (Write Failing Test)

**Determine if new test needed**:
- **Behavioral change**: Write new test
- **Non-behavioral** (refactoring, docs): Existing tests sufficient

**Example** (Adding HTMX attrs to Button):

```bash
# Edit test file
vim tests/test_components/test_button.py
```

Add new test:

```python
@pytest.mark.asyncio
async def test_button_full_htmx_support(renderer):
    """Test button supports all 10 HTMX attributes."""
    button = Button(
        label="Delete",
        hx_delete="/api/item/123",
        hx_target="#item-list",
        hx_swap="outerHTML",
        hx_push_url="/items",
        hx_select="#updated-content",
    )
    html = await renderer.render(button)

    assert 'hx-delete="/api/item/123"' in html
    assert 'hx-target="#item-list"' in html
    assert 'hx-swap="outerHTML"' in html
    assert 'hx-push-url="/items"' in html
    assert 'hx-select="#updated-content"' in html
```

Run test (should fail):

```bash
pytest tests/test_components/test_button.py::test_button_full_htmx_support -v

# Expected: FAILED (attribute not recognized)
```

**If test fails correctly**: Proceed to GREEN phase.
**If test passes unexpectedly**: Review test logic.

---

##### Phase: GREEN (Implement Improvement)

**Make minimal change** to pass test.

Example (Button HTMX attrs):

```bash
vim src/flowbite_htmy/components/button.py
```

Add missing HTMX props (after line 87):

```python
# Existing HTMX attrs (lines 74-78)
hx_get: str | None = None
hx_post: str | None = None
hx_target: str | None = None
hx_swap: str | None = None
hx_trigger: str | None = None

# ADD MISSING ATTRS
hx_put: str | None = None
"""HTMX PUT request URL."""

hx_delete: str | None = None
"""HTMX DELETE request URL."""

hx_patch: str | None = None
"""HTMX PATCH request URL."""

hx_push_url: str | bool | None = None
"""HTMX push URL to browser history (true/false/url)."""

hx_select: str | None = None
"""HTMX selector for response content."""
```

Update `htmy()` method to include new attrs (around line 214):

```python
button_attrs = {
    "type": self.type,
    "disabled": self.disabled or None,
    "hx-get": self.hx_get,
    "hx-post": self.hx_post,
    # ADD NEW ATTRS
    "hx-put": self.hx_put,
    "hx-delete": self.hx_delete,
    "hx-patch": self.hx_patch,
    "hx-target": self.hx_target,
    "hx-swap": self.hx_swap,
    "hx-trigger": self.hx_trigger,
    "hx-push-url": self.hx_push_url,
    "hx-select": self.hx_select,
}
```

Run new test (should pass):

```bash
pytest tests/test_components/test_button.py::test_button_full_htmx_support -v

# Expected: PASSED
```

Verify all existing tests still pass:

```bash
pytest

# Expected: 187 tests PASSED (or 188 if new test added)
```

**If all tests pass**: Proceed to REFACTOR phase.
**If tests fail**: Debug, fix, repeat.

---

##### Phase: REFACTOR (Clean Up)

**Review implementation** for:
- Code clarity
- Consistency with other components
- Documentation completeness

Example refactoring:

```python
# Ensure HTMX attrs are grouped and ordered consistently
# (May already be correct from GREEN phase)

# Add docstring note about full HTMX support
@dataclass(frozen=True, kw_only=True)
class Button:
    """Flowbite button component.

    Supports full HTMX integration with all 10 HTMX attributes
    for dynamic interactions.

    Examples:
        # ... existing examples ...

        HTMX DELETE request:
        >>> Button(
        ...     label="Delete",
        ...     hx_delete="/api/item/123",
        ...     hx_target="#item-list",
        ...     hx_swap="outerHTML"
        ... )
    """
```

Run tests again (should still pass):

```bash
pytest

# Expected: All tests PASSED
```

---

#### 2.4 Validation Checklist

**After each improvement**, run full validation:

```bash
# 1. All tests pass
pytest
# Expected: 187+ tests PASSED

# 2. Coverage maintained/improved
pytest --cov=src/flowbite_htmy/components
# Expected: >90% overall

# 3. Type checking passes
mypy --strict src/flowbite_htmy
# Expected: Success: no issues found

# 4. Linting passes
ruff check src/flowbite_htmy
# Expected: All checks passed!

# 5. Formatting clean
ruff format --check src/flowbite_htmy
# Expected: Would reformat 0 files (or auto-format if needed)

# 6. Showcase app runs
python examples/showcase.py
# Open http://localhost:8000, test changed component manually
```

**Checklist**:
- [ ] All 187+ tests pass
- [ ] Coverage >90%
- [ ] `mypy --strict src/flowbite_htmy` passes
- [ ] `ruff check src/flowbite_htmy` passes
- [ ] `ruff format src/flowbite_htmy` clean
- [ ] Showcase app runs without errors
- [ ] Manual test of component in showcase confirms behavior

**If all pass**: Commit improvement.
**If any fail**: Fix issue, re-run validation.

---

#### 2.5 Commit Improvement

After validation passes, commit with clear message:

```bash
git add src/flowbite_htmy/components/button.py
git add tests/test_components/test_button.py

git commit -m "feat(button): Add full HTMX attribute support

Add 5 missing HTMX attributes to Button component:
- hx_put: PUT request URL
- hx_delete: DELETE request URL
- hx_patch: PATCH request URL
- hx_push_url: Push URL to browser history
- hx_select: Selector for response content

This brings Button to full HTMX coverage (10/10 attributes)
matching Toast reference implementation pattern.

Breaking: None (adds optional props with None defaults)
Tests: Added test_button_full_htmx_support
Coverage: Maintained >90%

Refs: specs/004-component-review/research.md (HP-2)"
```

**Commit message structure**:
- **Type**: `feat`, `fix`, `refactor`, `docs`, `test`
- **Scope**: Component name
- **Summary**: One-line description
- **Body**: What changed, why, impact
- **Footer**: Breaking changes (if any), test info, references

---

#### 2.6 Repeat for Next Improvement

**Return to 2.3** (TDD Cycle) for next improvement in component.

**When all improvements complete for component**: Move to next component.

---

### Step 3: Template Cleanup

**Goal**: Remove unused `base.html.jinja` template identified in research.

#### 3.1 Verify Unused Template

**Confirm findings** from `research.md`:

```bash
# Search for any references to base.html.jinja
grep -r "base\.html\.jinja" examples/

# Expected: No results (template is unused)

# Check git history
git log --all --full-history -- examples/templates/base.html.jinja

# Review: When was it last used? (Should be commit 5bd52b9, Nov 8)
```

**Validation**:
- [ ] Zero references in `examples/` directory
- [ ] Last use was commit 5bd52b9 (refactor to hybrid pattern)
- [ ] Replaced by `showcase-layout.html.jinja`

---

#### 3.2 Remove Template File

```bash
# Remove unused template
rm examples/templates/base.html.jinja

# Verify file deleted
ls examples/templates/

# Expected: Only showcase-layout.html.jinja remains
```

---

#### 3.3 Verify Showcase Still Works

```bash
# Run showcase app
python examples/showcase.py

# Open browser to http://localhost:8000
# Click through all component pages
# Verify layout renders correctly

# Expected: No errors, all pages load
```

**Manual validation**:
- [ ] Homepage loads with sidebar navigation
- [ ] All component pages accessible from sidebar
- [ ] Dark mode toggle works
- [ ] No console errors in browser

Stop showcase: Ctrl+C

---

#### 3.4 Commit Template Removal

```bash
git add examples/templates/base.html.jinja  # Git tracks deletion
git commit -m "chore: Remove unused base.html.jinja template

Removed examples/templates/base.html.jinja - no longer referenced
in codebase since refactor to unified showcase (commit 5bd52b9).

Replaced by: showcase-layout.html.jinja (multi-page layout)
Last used: Nov 8, 2025 (commit 5bd52b9)
References: 0 (confirmed via grep)

Validation:
- Showcase app runs without errors
- All component pages load correctly
- Layout rendering unchanged

Refs: specs/004-component-review/research.md (R1: Template Usage)"
```

---

### Step 4: Documentation

**Optional but recommended**: Document learned patterns.

#### 4.1 Create Component Quality Standards (If Needed)

**User Story 3 (P3)** from spec:
> "As a project maintainer, I want component quality standards documented so future components follow established patterns."

If pursuing this story:

```bash
# Create docs directory if not exists
mkdir -p docs

# Create quality standards doc
vim docs/component-quality-standards.md
```

**Content structure**:
```markdown
# Component Quality Standards

## Purpose
Standards for flowbite-htmy component implementations.

## Patterns

### Dark Mode Classes
- Always include `dark:` prefixed classes
- Never use conditional: `if theme.dark_mode`
- Reference: toast.py:138

### HTMX Integration
- Interactive components: Full 10 attrs
- Display components: Optional
- Reference: toast.py:22-31

### ClassBuilder Usage
- Base classes in constructor
- Conditional with .add_if()
- Custom classes last with .merge()
- Reference: All components

## Component Checklist
[Link to component-quality-checklist.md]
```

---

#### 4.2 Update CLAUDE.md (If Patterns Change)

**Only if new patterns emerge** that aren't already documented:

```bash
vim CLAUDE.md
```

**Example additions**:
- New component patterns discovered during review
- Updated examples using improved components
- Additional TDD workflow notes

**Note**: CLAUDE.md already documents most patterns. Only update if review reveals gaps.

---

#### 4.3 Update Basic Memory

**Record review progress** in project knowledge base:

```bash
# Example: Record review completion
# (Use Basic Memory MCP tools if available)
```

---

## Safety Checks

**Before committing ANY change**, verify:

### Pre-Commit Validation

```bash
# 1. Full test suite
pytest
# MUST PASS: 187+ tests

# 2. Type checking
mypy --strict src/flowbite_htmy
# MUST PASS: Success: no issues found

# 3. Linting
ruff check src/flowbite_htmy
# MUST PASS: All checks passed

# 4. Formatting
ruff format src/flowbite_htmy
# Auto-formats code

# 5. Showcase app
python examples/showcase.py &
SHOWCASE_PID=$!
# Open http://localhost:8000, manual test
kill $SHOWCASE_PID
```

**All checks must pass before commit.**

---

### Post-Commit Verification

After committing improvement:

```bash
# 1. Verify clean working tree
git status
# Expected: nothing to commit, working tree clean

# 2. Review commit
git log -1 --stat
# Verify: Files changed as expected, message clear

# 3. Quick smoke test
pytest --lf  # Run only last-failed tests (should be none)
# Expected: No tests ran (all passing)
```

---

## Troubleshooting

### Tests Fail After Change

**Symptom**: `pytest` shows failures after implementing improvement.

**Steps**:
1. Read failure message carefully
2. Identify which test failed and why
3. Check if failure is expected (new test) or regression (existing test)
4. If regression: Undo change, analyze impact
5. Fix implementation or update test (if test was wrong)
6. Re-run full suite

```bash
# See detailed failure output
pytest -vv

# Run only failing test
pytest tests/test_components/test_button.py::test_that_failed -vv

# Check coverage for changed file
pytest --cov=src/flowbite_htmy/components/button --cov-report=term-missing
```

---

### Mypy Type Errors

**Symptom**: `mypy --strict` reports type errors after change.

**Common issues**:
- Missing type hint on new prop
- Return type doesn't match signature
- Attribute access on potentially None value

```bash
# Verbose mypy output
mypy --strict --show-error-codes src/flowbite_htmy/components/button.py

# Check specific line
mypy --strict src/flowbite_htmy/components/button.py | grep "error:"
```

**Fix patterns**:
```python
# Missing type hint
# Before:
icon = None

# After:
icon: str | None = None

# Potential None access
# Before:
return self.icon.upper()

# After:
return self.icon.upper() if self.icon else None
```

---

### Coverage Drops Below 90%

**Symptom**: Coverage report shows <90% after adding code.

**Steps**:
1. Identify untested lines: `pytest --cov-report=term-missing`
2. Write test cases for uncovered code paths
3. Re-run coverage check

```bash
# See which lines are untested
pytest --cov=src/flowbite_htmy/components/button --cov-report=term-missing

# Example output:
# button.py:150-152  3  (lines not covered)

# Add test for those lines
vim tests/test_components/test_button.py
```

---

### Showcase App Errors

**Symptom**: `python examples/showcase.py` crashes or component doesn't render.

**Steps**:
1. Read error traceback
2. Check if component import works: `python -c "from flowbite_htmy import Button; print(Button)"`
3. Verify component can be instantiated: `Button(label="Test")`
4. Check for missing required props or type errors

```bash
# Debug component directly
python -c "
from flowbite_htmy import Button
b = Button(label='Test')
print(b)
"

# Check showcase imports
grep "Button" examples/showcase.py
```

---

### Git Conflict or Confusion

**Symptom**: Unsure what changed, want to revert.

```bash
# See what changed since baseline commit
git diff <baseline-commit-hash>

# Revert to baseline (DESTRUCTIVE - loses all changes)
git reset --hard <baseline-commit-hash>

# Revert specific file
git checkout <baseline-commit-hash> -- src/flowbite_htmy/components/button.py

# Create new branch to experiment
git checkout -b experiment-branch
```

---

## Success Criteria

Review is complete when:

- [ ] **All 4 components reviewed** (Button, Badge, Alert, Avatar)
- [ ] **All high-priority improvements implemented** (from research.md)
- [ ] **Unused template removed** (base.html.jinja)
- [ ] **All 187+ tests passing**
- [ ] **Coverage >90% maintained**
- [ ] **mypy --strict passes** (zero errors)
- [ ] **ruff checks pass** (zero issues)
- [ ] **Showcase app runs** without errors
- [ ] **All changes committed** with clear messages
- [ ] **Documentation updated** (if pursuing P3)

---

## Next Steps

After completing review workflow:

1. **Merge to main** (if on feature branch):
   ```bash
   git checkout master
   git merge 004-component-review
   git push origin master
   ```

2. **Update project version** (if merging to release):
   ```bash
   # Update version in pyproject.toml
   vim pyproject.toml
   # Change version: 0.1.0 → 0.1.1 (patch release, no breaking changes)
   ```

3. **Create release notes**:
   ```bash
   # Document improvements in CHANGELOG
   vim CHANGELOG.md
   ```

4. **Archive review artifacts** (optional):
   ```bash
   # Move specs to docs/completed/
   mkdir -p docs/completed/reviews
   mv specs/004-component-review docs/completed/reviews/
   ```

---

## Reference Commands

Quick copy-paste commands for common tasks:

```bash
# Full validation suite (run before every commit)
pytest && \
mypy --strict src/flowbite_htmy && \
ruff check src/flowbite_htmy && \
ruff format src/flowbite_htmy

# Component-specific coverage
pytest --cov=src/flowbite_htmy/components/button \
       --cov-report=term-missing \
       tests/test_components/test_button.py

# Run showcase for manual testing
python examples/showcase.py

# View research findings for component
grep -A 20 "Button Component" specs/004-component-review/research.md

# Check template usage
grep -r "base\.html\.jinja" examples/

# Create baseline commit
git add -A && \
git commit -m "Baseline: Record pre-review state"
```

---

## Appendix: TDD Cycle Template

**Copy this for each improvement**:

### Improvement: [Name]

**Component**: [Button/Badge/Alert/Avatar]
**Type**: [add_htmx_attrs/fix_dark_mode/enhance_docs/etc.]
**Priority**: [high/medium/low]
**Breaking Risk**: [none/low/medium/high]
**Effort**: [trivial/small/medium/large]

#### RED Phase
- [ ] Test written: `tests/test_components/test_[component].py::[test_name]`
- [ ] Test fails as expected

```bash
pytest tests/test_components/test_[component].py::[test_name] -v
# Expected: FAILED
```

#### GREEN Phase
- [ ] Implementation changes: `src/flowbite_htmy/components/[component].py`
- [ ] Test passes

```bash
pytest tests/test_components/test_[component].py::[test_name] -v
# Expected: PASSED
```

#### REFACTOR Phase
- [ ] Code cleaned up
- [ ] Documentation updated
- [ ] All tests still pass

```bash
pytest
# Expected: All PASSED
```

#### Validation
- [ ] All 187+ tests pass
- [ ] Coverage >90%
- [ ] mypy --strict passes
- [ ] ruff check passes
- [ ] Showcase app works

#### Commit
```bash
git add [files]
git commit -m "[type]([scope]): [summary]

[detailed description]

Breaking: [none/description]
Tests: [test names]
Coverage: [maintained/improved]

Refs: specs/004-component-review/research.md ([reference])"
```

---

**Workflow Status**: ✅ Ready for use - Begin with Step 1: Baseline Validation
