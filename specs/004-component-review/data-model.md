# Data Model: Component Quality Review

**Feature**: 004-component-review
**Version**: 1.0.0
**Date**: 2025-11-16

---

## Overview

This document defines the data structures used to capture findings from the component quality review process. These entities structure the analysis of early Phase 1 components (Button, Badge, Alert, Avatar) against patterns learned from later Phase 2 implementations (Toast, Modal, Select, Pagination).

**Purpose**: Provide consistent schema for recording review findings, identified issues, proposed improvements, and template usage analysis.

**Scope**: In-memory data structures (not persisted to database). Used during review process to organize findings before implementing fixes.

---

## Entity Definitions

### ComponentReview

Represents the complete analysis results for a single component.

**Purpose**: Top-level container for all findings related to one component's quality review.

#### Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `component_name` | `str` | Yes | Component being reviewed (e.g., "Button", "Badge", "Alert", "Avatar") |
| `file_path` | `str` | Yes | Absolute path to component implementation file (e.g., "/home/.../button.py") |
| `implementation_date` | `str` | Yes | Date of first implementation from git log (ISO 8601 format: "2025-11-08") |
| `current_coverage` | `float` | Yes | Test coverage percentage from pytest (0.0-100.0) |
| `test_count` | `int` | Yes | Number of test functions for this component |
| `identified_issues` | `list[Issue]` | Yes | List of problems found during review (can be empty list) |
| `proposed_improvements` | `list[Improvement]` | Yes | List of recommended changes (can be empty list) |
| `priority` | `str` | Yes | Overall priority: "high", "medium", "low" based on issue severity |
| `backward_compatible` | `bool` | Yes | Whether all proposed improvements maintain API compatibility |

#### Relationships

- **Has Many** `Issue` records (0 to N issues per component)
- **Has Many** `Improvement` records (0 to N improvements per component)

#### Validation Rules

- `component_name` must match a file in `src/flowbite_htmy/components/`
- `file_path` must exist and be absolute path
- `current_coverage` must be 0.0 ≤ coverage ≤ 100.0
- `test_count` must be ≥ 0
- `priority` must be one of: "high", "medium", "low"
- `backward_compatible` = False only if any improvement has `breaking_risk` = "high"

#### Example

```python
from dataclasses import dataclass

@dataclass
class ComponentReview:
    component_name: str = "Button"
    file_path: str = "/home/jian/Work/personal/flowbite-htmy/src/flowbite_htmy/components/button.py"
    implementation_date: str = "2025-11-08"
    current_coverage: float = 100.0
    test_count: int = 15
    identified_issues: list[Issue] = [
        Issue(
            issue_type="pattern_inconsistency",
            severity="major",
            description="Missing 5 HTMX attributes compared to Toast reference implementation",
            current_code_example="hx_get, hx_post, hx_target, hx_swap, hx_trigger (5/10)",
            file_location="button.py:74-87",
            affects_functionality=False
        )
    ]
    proposed_improvements: list[Improvement] = [
        Improvement(
            improvement_type="add_htmx_attrs",
            description="Add missing HTMX attributes: hx_put, hx_delete, hx_patch, hx_push_url, hx_select",
            target_pattern="See toast.py:22-31 for reference",
            breaking_risk="none",
            estimated_effort="small",
            depends_on=[]
        )
    ]
    priority: str = "high"
    backward_compatible: bool = True
```

---

### Issue

Represents a specific problem identified during component review.

**Purpose**: Document concrete quality issues that need addressing.

#### Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `issue_type` | `str` | Yes | Category of issue (see allowed values below) |
| `severity` | `str` | Yes | Impact level: "critical", "major", "minor" |
| `description` | `str` | Yes | Clear explanation of what's wrong and why it matters |
| `current_code_example` | `str` | Yes | Code snippet showing current problematic implementation |
| `file_location` | `str` | Yes | Reference to code location (format: "filename:line" or "filename:line-line") |
| `affects_functionality` | `bool` | Yes | Whether this issue impacts component behavior (vs. code quality only) |

#### Allowed Values

**`issue_type`** (one of):
- `"pattern_inconsistency"` - Component doesn't follow established patterns from later implementations
- `"missing_feature"` - Lacks capability present in reference components (e.g., HTMX attrs)
- `"documentation_gap"` - Missing or inadequate docstrings, examples, or comments
- `"type_hint_missing"` - Incomplete type annotations or use of `Any`
- `"naming_violation"` - Doesn't follow naming conventions (e.g., `type` vs `type_`)
- `"anti_pattern"` - Uses known anti-pattern (e.g., conditional dark mode)

**`severity`**:
- `"critical"` - Violates constitution principles or breaks functionality
- `"major"` - Inconsistent with established patterns, affects maintainability
- `"minor"` - Small inconsistency or nice-to-have improvement

#### Relationships

- **Belongs to** one `ComponentReview`
- **Addressed by** one or more `Improvement` records

#### Validation Rules

- `issue_type` must be from allowed values list
- `severity` must be one of: "critical", "major", "minor"
- `current_code_example` should be valid Python code snippet
- `file_location` format must match: `{filename}:{line}` or `{filename}:{start}-{end}`
- Critical severity issues must have `affects_functionality=True` OR be anti-patterns

#### Example

```python
@dataclass
class Issue:
    issue_type: str = "anti_pattern"
    severity: str = "major"
    description: str = (
        "Badge uses conditional dark mode classes (anti-pattern). "
        "Dark classes should always be included; Tailwind's dark: prefix "
        "handles activation automatically based on theme state."
    )
    current_code_example: str = '''
# Line 152-154 (WRONG)
dark_classes = self._get_dark_classes()
if theme.dark_mode and dark_classes:  # ANTI-PATTERN
    builder.add(dark_classes)
'''
    file_location: str = "badge.py:152-154"
    affects_functionality: bool = False  # Output unchanged, pattern is wrong
```

---

### Improvement

Represents a proposed fix or enhancement to address identified issues.

**Purpose**: Define actionable changes with risk assessment and effort estimation.

#### Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `improvement_type` | `str` | Yes | Category of improvement (see allowed values below) |
| `description` | `str` | Yes | What needs to change and expected outcome |
| `target_pattern` | `str` | Yes | Code example showing desired implementation (from Toast/Modal reference) |
| `breaking_risk` | `str` | Yes | Backward compatibility risk: "none", "low", "medium", "high" |
| `estimated_effort` | `str` | Yes | Time estimate: "trivial", "small", "medium", "large" |
| `depends_on` | `list[str]` | Yes | Other improvement IDs that must be completed first (empty if none) |

#### Allowed Values

**`improvement_type`** (one of):
- `"add_htmx_attrs"` - Add missing HTMX attributes
- `"fix_dark_mode"` - Correct dark mode class pattern (remove conditional)
- `"enhance_docs"` - Improve docstrings, add examples
- `"refactor_classbuilder"` - Improve ClassBuilder usage consistency
- `"add_type_hints"` - Add missing type annotations
- `"fix_naming"` - Rename to follow conventions (e.g., `type` → `type_`)
- `"add_tests"` - Increase test coverage for edge cases

**`breaking_risk`**:
- `"none"` - No API changes, safe to apply immediately
- `"low"` - Minor risk (e.g., adding optional props with defaults)
- `"medium"` - Moderate risk (e.g., changing internal behavior)
- `"high"` - Breaking change (e.g., renaming public props, changing defaults)

**`estimated_effort`**:
- `"trivial"` - Less than 30 minutes
- `"small"` - 1-2 hours
- `"medium"` - 2-4 hours
- `"large"` - 4+ hours

#### Relationships

- **Belongs to** one `ComponentReview`
- **Addresses** one or more `Issue` records
- **Depends on** zero or more other `Improvement` records

#### Validation Rules

- `improvement_type` must be from allowed values list
- `breaking_risk` must be one of: "none", "low", "medium", "high"
- `estimated_effort` must be one of: "trivial", "small", "medium", "large"
- `target_pattern` must be valid Python code or reference to file (e.g., "See toast.py:138")
- If `breaking_risk` = "high", must document migration strategy in `description`
- `depends_on` must reference valid improvement descriptions (no circular dependencies)

#### Example

```python
@dataclass
class Improvement:
    improvement_type: str = "fix_dark_mode"
    description: str = (
        "Remove conditional dark mode in Badge._build_classes(). "
        "Always include dark classes in ClassBuilder - Tailwind handles activation. "
        "This aligns with Toast pattern and CLAUDE.md guidance."
    )
    target_pattern: str = '''
# Correct pattern (from toast.py:138)
builder = ClassBuilder(
    "flex items-center w-full max-w-xs p-4 "
    "text-gray-500 bg-white rounded-lg shadow-sm "
    "dark:text-gray-400 dark:bg-gray-800"  # Always included
)
'''
    breaking_risk: str = "none"  # Output HTML unchanged
    estimated_effort: str = "trivial"  # ~20 min
    depends_on: list[str] = []  # No dependencies
```

---

### TemplateUsage

Represents analysis of Jinja template file usage in the examples directory.

**Purpose**: Identify unused templates for safe removal as part of technical debt cleanup.

#### Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| `template_name` | `str` | Yes | Template filename (e.g., "base.html.jinja", "showcase-layout.html.jinja") |
| `file_path` | `str` | Yes | Absolute path to template file |
| `used_by` | `list[str]` | Yes | List of Python files referencing this template (empty if unused) |
| `last_modified` | `str` | Yes | Git timestamp of last change (ISO 8601 format) |
| `can_remove` | `bool` | Yes | Whether template is safe to delete |
| `removal_blockers` | `list[str]` | Yes | Reasons why template can't be removed (empty if `can_remove=True`) |

#### Validation Rules

- `template_name` must match a file in `examples/templates/`
- `file_path` must exist and be absolute path
- `last_modified` must be valid ISO 8601 date string
- If `used_by` is empty, `can_remove` should be `True` (unless other blockers exist)
- `removal_blockers` must be empty if `can_remove=True`

#### Example: Unused Template

```python
@dataclass
class TemplateUsage:
    template_name: str = "base.html.jinja"
    file_path: str = "/home/jian/Work/personal/flowbite-htmy/examples/templates/base.html.jinja"
    used_by: list[str] = []  # No references
    last_modified: str = "2025-11-08T10:30:00Z"
    can_remove: bool = True
    removal_blockers: list[str] = []
```

#### Example: Active Template

```python
@dataclass
class TemplateUsage:
    template_name: str = "showcase-layout.html.jinja"
    file_path: str = "/home/jian/Work/personal/flowbite-htmy/examples/templates/showcase-layout.html.jinja"
    used_by: list[str] = [
        "examples/showcase.py:223",  # Homepage
        "examples/showcase.py:238",  # Buttons page
        "examples/showcase.py:253",  # Badges page
        # ... 11 more references
    ]
    last_modified: str = "2025-11-16T14:22:00Z"
    can_remove: bool = False
    removal_blockers: list[str] = [
        "Active template used by 14 showcase routes",
        "Primary layout for unified showcase application"
    ]
```

---

## State Transitions

**N/A** - This is a review and analysis task, not a workflow system. Entities are created during analysis phase and consumed during implementation phase, but do not transition between states.

---

## Usage Guidelines

### Review Process Flow

1. **Create ComponentReview** for each component being analyzed
2. **Add Issue records** as problems are identified during pattern comparison
3. **Add Improvement records** for each proposed fix, linking to issues
4. **Set priority** on ComponentReview based on aggregated issue severity
5. **Validate backward_compatible** flag based on improvement breaking risks
6. **Create TemplateUsage** records for template cleanup analysis

### Prioritization Strategy

Component review priority determined by:

**High Priority**:
- Contains "critical" severity issues
- Contains anti-patterns (conditional dark mode)
- Has ≥3 "major" severity issues
- Breaking risk is acceptable for impact

**Medium Priority**:
- Contains 1-2 "major" severity issues
- Nice-to-have improvements (doc enhancements, additional tests)
- Non-urgent pattern inconsistencies

**Low Priority**:
- Only "minor" severity issues
- Optional enhancements (e.g., more docstring examples)
- Breaking changes not worth the risk (defer to v0.2.0)

### Implementation Order

Based on improvement dependencies and effort:

1. **Trivial + No Dependencies** (quick wins)
2. **Small + No Breaking Risk** (safe improvements)
3. **Medium + Depends on Trivial** (after dependencies met)
4. **Large OR High Breaking Risk** (defer to future version)

---

## Data Integrity

### Required Validations

Before using review data for implementation:

1. **Consistency Check**: All referenced file paths must exist
2. **Dependency Check**: All `depends_on` references must resolve to valid improvements
3. **Breaking Risk Alignment**: If any improvement has `breaking_risk="high"`, component's `backward_compatible` must be `False`
4. **Coverage Baseline**: `current_coverage` must be ≥90% (project requirement)
5. **No Orphan Improvements**: Every improvement should address at least one issue (or document why it doesn't)

### Example Validation Function

```python
def validate_component_review(review: ComponentReview) -> list[str]:
    """Validate ComponentReview data integrity.

    Returns list of validation errors (empty if valid).
    """
    errors = []

    # Check file existence
    if not Path(review.file_path).exists():
        errors.append(f"Component file not found: {review.file_path}")

    # Check coverage threshold
    if review.current_coverage < 90.0:
        errors.append(f"Coverage below 90%: {review.current_coverage}%")

    # Check backward compatibility alignment
    has_breaking = any(
        imp.breaking_risk == "high"
        for imp in review.proposed_improvements
    )
    if has_breaking and review.backward_compatible:
        errors.append("backward_compatible=True but has high-risk improvements")

    # Check for orphan improvements (should address at least one issue)
    if review.proposed_improvements and not review.identified_issues:
        errors.append("Has improvements but no identified issues (document why)")

    return errors
```

---

## Real-World Examples

### Button Component Review

Based on research findings (research.md lines 283-462):

```python
button_review = ComponentReview(
    component_name="Button",
    file_path="/home/jian/Work/personal/flowbite-htmy/src/flowbite_htmy/components/button.py",
    implementation_date="2025-11-08",
    current_coverage=100.0,
    test_count=15,
    identified_issues=[
        Issue(
            issue_type="pattern_inconsistency",
            severity="major",
            description="Missing 5 HTMX attributes compared to Toast reference (hx_put, hx_delete, hx_patch, hx_push_url, hx_select)",
            current_code_example="hx_get, hx_post, hx_target, hx_swap, hx_trigger (5/10 attrs)",
            file_location="button.py:74-87",
            affects_functionality=False
        ),
        Issue(
            issue_type="naming_violation",
            severity="minor",
            description="Uses 'type' instead of 'type_' for reserved word (violates convention)",
            current_code_example="type: str = 'button'",
            file_location="button.py:70",
            affects_functionality=False
        )
    ],
    proposed_improvements=[
        Improvement(
            improvement_type="add_htmx_attrs",
            description="Add missing HTMX attributes for full coverage (hx_put, hx_delete, hx_patch, hx_push_url, hx_select)",
            target_pattern="See toast.py:22-31 for reference pattern",
            breaking_risk="none",
            estimated_effort="small",
            depends_on=[]
        ),
        Improvement(
            improvement_type="fix_naming",
            description="Rename 'type' → 'type_' to follow reserved word convention. Add deprecation support for 'type' parameter.",
            target_pattern="type_: str = 'button'",
            breaking_risk="high",
            estimated_effort="medium",
            depends_on=[]
        )
    ],
    priority="high",
    backward_compatible=False  # Due to type → type_ rename
)
```

### Badge Component Review

Based on research findings (research.md lines 386-421):

```python
badge_review = ComponentReview(
    component_name="Badge",
    file_path="/home/jian/Work/personal/flowbite-htmy/src/flowbite_htmy/components/badge.py",
    implementation_date="2025-11-08",
    current_coverage=98.0,
    test_count=12,
    identified_issues=[
        Issue(
            issue_type="anti_pattern",
            severity="major",
            description="Uses conditional dark mode classes (anti-pattern). Dark classes should always be included.",
            current_code_example="""
# Lines 152-154
dark_classes = self._get_dark_classes()
if theme.dark_mode and dark_classes:  # ANTI-PATTERN
    builder.add(dark_classes)
""",
            file_location="badge.py:152-154",
            affects_functionality=False
        ),
        Issue(
            issue_type="documentation_gap",
            severity="minor",
            description="Only has 1 basic example, should have 3+ diverse examples like Toast",
            current_code_example="# Single basic example at line 20",
            file_location="badge.py:20",
            affects_functionality=False
        )
    ],
    proposed_improvements=[
        Improvement(
            improvement_type="fix_dark_mode",
            description="Remove conditional check for dark_classes. Always add dark classes to ClassBuilder.",
            target_pattern="""
# Correct pattern (toast.py:138)
builder = ClassBuilder(
    "base-classes "
    "dark:dark-variant-classes"  # Always included
)
""",
            breaking_risk="none",
            estimated_effort="trivial",
            depends_on=[]
        ),
        Improvement(
            improvement_type="enhance_docs",
            description="Add 2-3 more docstring examples: badge with icon, dismissible badge, badge as link",
            target_pattern="See toast.py:47-62 for multi-example pattern",
            breaking_risk="none",
            estimated_effort="trivial",
            depends_on=[]
        )
    ],
    priority="high",
    backward_compatible=True
)
```

### Template Cleanup

Based on research findings (research.md lines 9-56):

```python
base_template = TemplateUsage(
    template_name="base.html.jinja",
    file_path="/home/jian/Work/personal/flowbite-htmy/examples/templates/base.html.jinja",
    used_by=[],
    last_modified="2025-11-08T10:30:00Z",
    can_remove=True,
    removal_blockers=[]
)

showcase_template = TemplateUsage(
    template_name="showcase-layout.html.jinja",
    file_path="/home/jian/Work/personal/flowbite-htmy/examples/templates/showcase-layout.html.jinja",
    used_by=[
        "examples/showcase.py:223",
        "examples/showcase.py:238",
        "examples/showcase.py:253",
        # ... 11 more
    ],
    last_modified="2025-11-16T14:22:00Z",
    can_remove=False,
    removal_blockers=[
        "Active template - 14 references in showcase.py",
        "Primary layout for unified showcase application"
    ]
)
```

---

## Reference Documentation

- **Research Findings**: `/specs/004-component-review/research.md`
- **Implementation Plan**: `/specs/004-component-review/plan.md`
- **Quality Checklist**: `/specs/004-component-review/contracts/component-quality-checklist.md`
- **TDD Workflow**: `/specs/004-component-review/quickstart.md`

---

**Document Status**: ✅ Complete - Ready for implementation phase
