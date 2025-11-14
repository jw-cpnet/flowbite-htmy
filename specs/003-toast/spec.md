# Feature Specification: Toast Component

**Feature Branch**: `003-toast`
**Created**: 2025-11-14
**Status**: Draft
**Input**: User description: "let's implement toast component in this session"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Simple Toast Notifications (Priority: P1)

Users need to display temporary notification messages to inform them of actions or events (success, error, warning, info). Toast notifications should appear with appropriate visual styling (icon, color) and automatically dismiss or be manually closed.

**Why this priority**: This is the core MVP functionality - a simple toast with icon, message, color variant, and dismiss capability. This is the most common use case for toast notifications (e.g., "Item saved successfully", "Error: Connection failed").

**Independent Test**: Can be fully tested by creating toasts with different color variants (success, danger, warning, info), verifying icon display, message rendering, and dismiss functionality. Delivers a complete notification system.

**Acceptance Scenarios**:

1. **Given** a user completes a successful action, **When** the server returns a success message, **Then** a green toast with checkmark icon and success message appears
2. **Given** a toast notification is displayed, **When** the user clicks the close button, **Then** the toast is dismissed from view
3. **Given** a validation error occurs, **When** the server returns an error, **Then** a red toast with error icon and error message appears
4. **Given** a user needs a warning notification, **When** the warning is triggered, **Then** a yellow toast with warning icon and message appears
5. **Given** a user needs informational feedback, **When** info notification is triggered, **Then** a blue toast with info icon and message appears

---

### User Story 2 - Interactive Toast (Priority: P2)

Users need to interact with toast notifications beyond dismissing them - including action buttons (e.g., "Reply", "Undo", "View Details") and rich content (e.g., user avatars, formatted text, links).

**Why this priority**: This extends the basic toast to support more complex interactions like chat message notifications, comment notifications, or actions that can be taken directly from the toast (e.g., "Undo delete"). This is common in modern web applications.

**Independent Test**: Can be tested independently by creating toasts with custom action buttons and verifying button click handling (HTMX integration). Delivers value for interactive notification scenarios.

**Acceptance Scenarios**:

1. **Given** a user receives a chat message notification, **When** the toast displays, **Then** it shows sender avatar, message preview, and a "Reply" button
2. **Given** a toast with an action button is displayed, **When** the user clicks the action button, **Then** the appropriate HTMX request is triggered (e.g., hx-get to reply endpoint)
3. **Given** a user deletes an item, **When** the success toast appears, **Then** an "Undo" button allows the user to reverse the action

---

### User Story 3 - Custom Styling and Accessibility (Priority: P3)

Users need toasts that support custom styling (additional CSS classes), accessibility features (ARIA attributes, keyboard navigation), and dark mode. This ensures toasts work for all users and can be customized to match application branding.

**Why this priority**: While important for production readiness, this is lower priority than core functionality. Accessibility and dark mode are critical for quality but don't change the fundamental value proposition.

**Independent Test**: Can be tested by verifying ARIA role="alert", screen reader announcements, dark mode styling, and custom CSS class application. Delivers accessible, customizable toasts.

**Acceptance Scenarios**:

1. **Given** dark mode is enabled, **When** a toast is displayed, **Then** it uses dark mode background and text colors
2. **Given** a toast is displayed, **When** a screen reader user is present, **Then** the toast is announced with role="alert"
3. **Given** a developer needs custom styling, **When** passing class_ parameter, **Then** custom CSS classes are applied to the toast

---

### Edge Cases

- What happens when multiple toasts are displayed simultaneously? (Not handled by component - positioning/stacking managed by parent container or JavaScript library)
- What happens when toast message is extremely long? (Component should handle text wrapping within max-width constraints)
- What happens when toast icon is not provided? (Toast renders without icon section - message only)
- What happens when dismiss button is not needed? (Component supports dismissible=False to hide close button)
- What happens when action button has no HTMX attributes? (Renders as standard button - developer can add onclick handler externally)
- What happens when toast is used with HTMX responses? (Component generates HTML that can be returned from HTMX endpoints - perfect integration pattern)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST render toast notifications with four color variants (success, danger, warning, info) matching Flowbite design system colors
- **FR-002**: System MUST display appropriate icons for each toast variant (checkmark for success, X for danger, exclamation for warning, info icon for info)
- **FR-003**: System MUST support custom icons in addition to default variant icons
- **FR-004**: System MUST render toast message text with proper typography (font size, weight, color)
- **FR-005**: System MUST include a dismissible close button that can be enabled or disabled
- **FR-006**: System MUST apply role="alert" for accessibility and screen reader support
- **FR-007**: System MUST support dark mode styling with appropriate dark: prefixed Tailwind classes
- **FR-008**: System MUST support custom CSS classes via class_ parameter
- **FR-009**: System MUST support optional action buttons with label and HTMX attributes (hx_get, hx_post, hx_target, etc.)
- **FR-010**: System MUST support optional avatar/image display for rich notifications (e.g., chat messages)
- **FR-011**: System MUST handle icon positioning (left side of message, consistent 8x8 icon container)
- **FR-012**: System MUST handle close button positioning (right side, auto margin)
- **FR-013**: System MUST render with max-width constraint (max-w-xs = 320px) and flexible width
- **FR-014**: System MUST support unique IDs for dismiss targeting (data-dismiss-target attribute)
- **FR-015**: System MUST generate ARIA-hidden="true" for decorative icons and sr-only labels for close button

### Key Entities *(include if feature involves data)*

- **Toast**: A temporary notification with message, color variant, icon, optional action buttons, and optional dismiss button
  - Attributes: message, variant (success/danger/warning/info), icon (optional), dismissible (boolean), action_button (optional), avatar (optional), custom_id (for dismiss targeting)
  - Relationships: Contains Icon component, contains Button (for close button and action buttons), optionally contains Avatar

- **ToastVariant**: An enumeration of toast types
  - Values: SUCCESS (green), DANGER (red), WARNING (yellow), INFO (blue)
  - Determines icon, background color, text color, and icon container color

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developers can implement toast notifications in under 5 lines of Python code (vs 30+ lines of raw HTML)
- **SC-002**: Toast component handles all Flowbite toast variants (4 variants: success, danger, warning, info) with consistent styling
- **SC-003**: Toast component integrates seamlessly with HTMX - can be returned from any hx-get/hx-post endpoint and rendered in target
- **SC-004**: Toast component achieves 95%+ test coverage with comprehensive TDD implementation
- **SC-005**: Toast showcase demonstrates all variants and features (minimum 6 examples: basic variants, dismissible, interactive, rich content)
- **SC-006**: Screen readers correctly announce toast messages with role="alert" (verified via accessibility testing)
- **SC-007**: Dark mode styling renders correctly for all toast variants (verified visually and with E2E tests)

## Scope *(mandatory)*

### In Scope

- Basic toast component with message, variant, icon
- Dismissible close button with data-dismiss-target integration
- Support for custom icons beyond default variant icons
- Interactive toast with action buttons (HTMX integration)
- Rich content toast (avatar, formatted text)
- Dark mode styling
- Accessibility (ARIA role, screen reader support)
- Custom CSS class support
- Comprehensive showcase with all Flowbite toast examples

### Out of Scope

- Toast positioning system (top-right, bottom-left, etc.) - handled by parent container or external library
- Toast animation/transitions - handled by Flowbite JavaScript or Tailwind transitions
- Toast auto-dismiss timers - requires JavaScript, not part of component (application-level concern)
- Toast queue/stack management - application-level concern, not component responsibility
- Toast notification service/manager - server-side or client-side JavaScript concern

## Assumptions *(mandatory)*

- Flowbite JavaScript is available for dismiss functionality (data-dismiss-target attribute)
- Icons are provided via existing icon system (Icon enum, get_icon() helper)
- HTMX is available for interactive toast actions
- Parent application handles toast positioning (component only renders the toast HTML)
- Developers will manage toast lifecycle (display, auto-dismiss, removal) via JavaScript or HTMX
- Toast max-width of 320px (max-w-xs) is appropriate for most use cases
- Four color variants (success, danger, warning, info) cover 90%+ of use cases

## Dependencies *(mandatory)*

- htmy library (Component rendering)
- ClassBuilder utility (Tailwind class construction)
- ThemeContext (Dark mode support)
- Icon system (Icon enum, get_icon() helper)
- Button component (For action buttons - optional dependency)
- Avatar component (For rich notifications - optional dependency)
- Flowbite CSS 2.5.1 (Styling)
- Flowbite JavaScript (Dismiss functionality - optional if dismissible=False)

## Notes *(optional)*

### Design Decisions

**Why Toast is Valuable:**
- Ranked #2 in component viability (now #8 in implementation priority after Phase 2A/2B)
- Perfect for HTMX server responses (hx-trigger for toast events)
- Icon + color + dismiss logic abstraction reduces significant boilerplate
- Common pattern with high reuse potential across applications

**Component Pattern:**
- Follow established dataclass pattern: `@dataclass(frozen=True, kw_only=True)`
- Implement `htmy(self, context: Context) -> Component` method
- Use ClassBuilder for variant-based class construction
- Always include dark: prefixed classes (Tailwind handles activation)

**HTMX Integration:**
- Toast component perfect for server-side notification responses
- Can be returned from any HTMX endpoint and rendered via hx-swap
- Action buttons support full HTMX attribute set (hx_get, hx_post, hx_target, etc.)

**Flowbite JavaScript (Optional):**
- Dismiss functionality requires Flowbite JS (data-dismiss-target attribute)
- If dismissible=False, no JavaScript dependency
- Application can implement custom dismiss logic if needed

**Testing Strategy:**
- Test all four variants (success, danger, warning, info)
- Test with/without icons, with/without dismiss button
- Test interactive toast with action buttons
- Test rich content toast with avatar
- Test dark mode styling
- Test custom CSS classes
- Test accessibility (ARIA attributes)

### Related Components

- Button: Used for close button and action buttons
- Icon: Used for variant icons and custom icons
- Avatar: Used for rich notification display (chat messages, user actions)
- Alert: Similar notification pattern but static (not dismissible by default in Flowbite)
