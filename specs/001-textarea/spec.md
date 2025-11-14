# Feature Specification: Textarea Component

**Feature Branch**: `001-textarea`
**Created**: 2025-11-14
**Status**: Draft
**Input**: User description: "let's start implementing Textarea component"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Multi-line Text Input (Priority: P1)

A user needs to enter multi-line text content such as comments, descriptions, messages, or feedback in a web form. The textarea component provides a clear, accessible, and styled input field that adapts to the Flowbite design system.

**Why this priority**: This is the core functionality - without basic textarea rendering and text input capability, the component provides no value. This represents the MVP that can be independently tested and deployed.

**Independent Test**: Can be fully tested by rendering a textarea with a label, typing multi-line text, and verifying the text is captured. Delivers immediate value for any form requiring multi-line input.

**Acceptance Scenarios**:

1. **Given** a form needs multi-line text input, **When** a textarea component is rendered with a label, **Then** the textarea displays with proper Flowbite styling (border, focus ring, dark mode classes)
2. **Given** a textarea is displayed, **When** the user types text including line breaks, **Then** the text is captured exactly as entered with preserved formatting
3. **Given** a textarea with a placeholder, **When** the textarea is empty, **Then** the placeholder text is visible in the appropriate color
4. **Given** a textarea is rendered, **When** the user clicks on the label, **Then** focus moves to the textarea input field
5. **Given** an edit form with existing content, **When** a textarea is rendered with a value parameter, **Then** the textarea displays the pre-filled content

---

### User Story 2 - Validation Feedback (Priority: P2)

A user submits a form with a textarea field that has validation requirements. The textarea shows clear visual feedback about validation state (success, error) with helpful context messages to guide the user toward correct input.

**Why this priority**: Validation feedback is essential for form usability and follows the established pattern from Input, Select, Checkbox, and Radio components. It significantly improves user experience but the component is still functional without it.

**Independent Test**: Can be tested by rendering textareas in different validation states (default, success, error) and verifying the correct colors, icons, and helper text appear. Works independently of P1.

**Acceptance Scenarios**:

1. **Given** a textarea with validation error, **When** the component renders, **Then** the textarea shows red border, red helper text, and appropriate error message
2. **Given** a textarea with validation success, **When** the component renders, **Then** the textarea shows green border, green helper text, and appropriate success message
3. **Given** a textarea with no validation state, **When** the component renders, **Then** the textarea shows default blue focus ring with neutral helper text
4. **Given** a textarea with helper text, **When** validation state changes, **Then** the helper text color updates to match validation state

---

### User Story 3 - Size and Layout Control (Priority: P3)

A user needs to control the visible height and width of the textarea to fit the expected content length. The component allows specifying the number of visible rows and supports custom sizing through Tailwind classes.

**Why this priority**: Size control improves UX for specific use cases (short comments vs long essays) but the component works fine with default sizing. This is a refinement feature.

**Independent Test**: Can be tested by rendering textareas with different row counts (3, 5, 10) and custom width classes, verifying the visual size matches expectations. Works independently of validation features.

**Acceptance Scenarios**:

1. **Given** a textarea for short comments, **When** rendered with rows=3, **Then** the textarea displays 3 visible lines of text
2. **Given** a textarea for long content, **When** rendered with rows=10, **Then** the textarea displays 10 visible lines of text
3. **Given** a textarea with custom width class, **When** the class is applied, **Then** the textarea width adjusts accordingly while maintaining Flowbite styling
4. **Given** a textarea with default settings, **When** no rows specified, **Then** the textarea displays with a reasonable default height (4 rows)

---

### User Story 4 - Accessibility and States (Priority: P4)

A user with accessibility needs or specific form requirements interacts with a textarea that may be required, disabled, or readonly. The component properly communicates these states visually and to assistive technologies.

**Why this priority**: Accessibility and state management are important but the component delivers core value without them. These features enhance robustness and compliance.

**Independent Test**: Can be tested by rendering textareas in different states (required, disabled, readonly) and verifying ARIA attributes, visual styling, and interaction behavior. Works independently of other features.

**Acceptance Scenarios**:

1. **Given** a required textarea, **When** the component renders, **Then** the textarea has required attribute and label displays with asterisk appended (e.g., "Comment *")
2. **Given** a disabled textarea, **When** the component renders, **Then** the textarea is grayed out, cursor shows not-allowed, and input is blocked
3. **Given** a readonly textarea, **When** the component renders, **Then** the textarea displays content but prevents editing
4. **Given** a textarea with aria-label, **When** screen reader focuses the field, **Then** the accessible label is announced correctly

---

### Edge Cases

- What happens when a textarea has extremely long text content (10,000+ characters)?
- How does the component handle special characters and HTML/script injection attempts?
- How does dark mode interact with validation states (error/success colors)?
- What happens when label is empty but no aria-label is provided?
- What happens when placeholder text is very long (100+ characters)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST render a textarea element with proper Flowbite styling (border radius, padding, focus ring)
- **FR-001a**: System MUST support optional name attribute (None if not provided, for form submission)
- **FR-002**: System MUST support label element properly associated with textarea via for/id attributes
- **FR-003**: System MUST include dark mode classes for all visual states (default, focus, disabled, validation)
- **FR-004**: System MUST support three validation states: default, success (green), error (red)
- **FR-005**: System MUST display helper text below textarea with color matching validation state
- **FR-006**: System MUST support placeholder text attribute
- **FR-006a**: System MUST support value parameter for pre-filled content (initial textarea value)
- **FR-007**: System MUST support configurable rows attribute for height control
- **FR-008**: System MUST support required attribute with proper ARIA and HTML5 validation
- **FR-009**: System MUST support disabled state with visual feedback (grayed out, cursor change)
- **FR-010**: System MUST support readonly state maintaining visibility while preventing editing
- **FR-011**: System MUST auto-generate unique IDs when not explicitly provided
- **FR-012**: System MUST support custom CSS classes via class_ parameter
- **FR-013**: System MUST support HTMX attributes (hx_get, hx_post, hx_target, hx_swap, etc.)
- **FR-014**: System MUST support passthrough attributes via attrs dict for uncommon HTML attributes
- **FR-015**: System MUST use ClassBuilder for consistent class construction and merging
- **FR-016**: System MUST retrieve theme context via ThemeContext.from_context(context)
- **FR-017**: System MUST follow dataclass pattern with frozen=True and kw_only=True
- **FR-018**: System MUST implement htmy(self, context) method returning Component
- **FR-019**: System MUST raise ValueError when label is empty and no aria_label is provided
- **FR-020**: System MUST default to 4 rows when rows parameter is not specified
- **FR-021**: System MUST append asterisk to label text when required=True (e.g., "Comment" becomes "Comment *")
- **FR-022**: System MUST clamp rows to minimum of 1 when rows value is zero or negative
- **FR-023**: System MUST prioritize disabled state over readonly when both are True (readonly is ignored)

### Key Entities

- **Textarea Component**: Python dataclass representing a multi-line text input field with label, validation states, helper text, and Flowbite styling. Attributes include id, name, label, value (initial content), placeholder, rows, validation state, helper text, required flag, disabled flag, readonly flag, HTMX attributes, and custom classes.

- **ValidationState**: Enum or string literal defining validation states (default, success, error) that control border color, helper text color, and visual feedback.

- **ThemeContext**: Context object providing dark mode state and theme settings to the component for consistent styling across light/dark modes.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Component achieves 95%+ test coverage with all functional requirements validated
- **SC-002**: Component renders correctly in both light and dark modes without visual artifacts
- **SC-003**: All validation states (default, success, error) display visually distinct colors that meet WCAG contrast requirements
- **SC-004**: Component passes strict mypy type checking with 100% type coverage
- **SC-005**: Showcase application demonstrates all component features with working examples users can interact with
- **SC-006**: Component integrates seamlessly with existing Input, Select, Checkbox, Radio pattern (consistent API and behavior)
- **SC-007**: Zero accessibility violations when tested with screen readers and keyboard navigation
- **SC-008**: Component documentation includes clear examples for all major use cases (basic, validation, sizing, states)

## Clarifications

### Session 2025-11-14

- Q: How should required textareas visually indicate the required state to users? → A: Asterisk appended to label text (e.g., "Comment *")
- Q: How should the component handle invalid rows values (zero, negative, or non-numeric)? → A: Clamp to minimum of 1 (rows <= 0 becomes rows = 1)
- Q: What should happen when both disabled and readonly are set to True simultaneously? → A: Disabled takes precedence (readonly is ignored)
- Q: Should the Textarea component support an initial value (pre-filled content)? → A: Yes, add value parameter for initial content
- Q: Should the name attribute be required, optional with default, or optional without default? → A: Optional, no default (None if not provided)

## Assumptions

- **Assumption 1**: Default rows count of 4 provides reasonable balance between compact layout and usability for most use cases
- **Assumption 2**: Validation pattern follows established Input component pattern (validation property with "success"/"error" values)
- **Assumption 3**: Helper text is optional and displayed below the textarea when provided
- **Assumption 4**: Component does not implement character count feature (can be added later if needed)
- **Assumption 5**: Component does not implement auto-resize feature (can be added later if needed)
- **Assumption 6**: HTMX attribute support matches existing component patterns (hx_get, hx_post, etc.)
- **Assumption 7**: Dark mode classes are always included in the component output (not conditional on theme.dark_mode)
- **Assumption 8**: Component follows TDD workflow: write test, run test (fail), implement, run test (pass), refactor
- **Assumption 9**: Flowbite CSS version 2.5.1 classes are used as reference for styling
- **Assumption 10**: Component does not handle client-side validation logic (server-side validation determines state)

## Dependencies

- **htmy**: Core rendering engine for component output
- **ClassBuilder**: Utility for constructing Tailwind CSS class strings
- **ThemeContext**: Context provider for theme settings
- **ValidationState type**: Enum or type definition for validation states (may need creation if not exists)
- **Flowbite CSS 2.5.1**: Styling framework providing base classes
- **pytest**: Testing framework for TDD implementation
- **mypy**: Type checking tool for strict type validation

## Out of Scope

- **Character counter**: Displaying remaining/used characters is not included in this implementation
- **Auto-resize**: Automatically adjusting height based on content length is not included
- **Rich text editing**: WYSIWYG editing capabilities are not included
- **Markdown preview**: Live preview of markdown formatting is not included
- **Spell checking UI**: Custom spell check interface is not included (browser default is acceptable)
- **Template/snippet insertion**: Pre-defined text templates or shortcuts are not included
- **Custom scrollbar styling**: Using default browser scrollbar styles
- **Drag-and-drop file upload**: Drag-drop into textarea for file upload is not included
