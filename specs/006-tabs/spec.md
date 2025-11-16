# Feature Specification: Tabs Component

**Feature Branch**: `006-tabs`
**Created**: 2025-01-16
**Status**: Draft
**Input**: User description: "Implement a Tabs component for flowbite-htmy following the class-based dataclass pattern. The component should provide tabbed navigation with multiple tab panels, supporting Flowbite's tab styles (default, underline, pills, full-width). Key requirements: 1) Tab dataclass for individual tabs with label, content, icon, disabled state, and HTMX attributes (hx-get for lazy loading). 2) Tabs container component with tabs list, default active tab, variant selection, and color customization. 3) Full ARIA support (role=\"tablist\", role=\"tab\", role=\"tabpanel\", aria-selected, aria-controls). 4) Flowbite JavaScript integration for tab switching with keyboard navigation (arrow keys, Home/End). 5) Support for both static content tabs and HTMX lazy-loaded tabs. 6) Dark mode classes always included. 7) Icon positioning (left/right of label) using existing icon system. 8) Unique ID generation for tab/panel associations. Follow strict TDD with 90%+ coverage, create showcase in examples/tabs.py demonstrating all variants and HTMX integration, and ensure pixel-perfect alignment with Flowbite's tab component using classes from flowbite-llms-full.txt."

## User Scenarios & Testing

### User Story 1 - Basic Tab Navigation (Priority: P1)

Users need to organize related content into separate panels that can be viewed one at a time by clicking tab buttons. This is the core functionality that makes tabs valuable - allowing users to access multiple sections without scrolling or navigating to different pages.

**Why this priority**: This is the fundamental value proposition of tabs. Without basic tab switching, the component has no purpose. All other features depend on this working correctly.

**Independent Test**: Can be fully tested by rendering a tabs component with 3 tabs containing different text content, clicking each tab button, and verifying that only the selected tab's content panel is visible while others are hidden.

**Acceptance Scenarios**:

1. **Given** a tabs component with 3 tabs (Profile, Dashboard, Settings), **When** the component renders, **Then** the first tab (Profile) is active by default and its content panel is visible while other panels are hidden.
2. **Given** the Profile tab is active, **When** user clicks the Dashboard tab button, **Then** the Dashboard panel becomes visible, Profile panel is hidden, and the Dashboard button shows active styling.
3. **Given** any tab is active, **When** user clicks on the already-active tab button, **Then** the tab remains active and its panel stays visible.
4. **Given** a tabs component, **When** user uses keyboard navigation (Tab key to focus, Enter to activate), **Then** tabs can be navigated and activated without a mouse.

---

### User Story 2 - Tab Variants and Visual Customization (Priority: P2)

Users need tabs that match their application's design system by choosing from different visual styles (default, underline, pills, full-width) and customizing colors to maintain brand consistency.

**Why this priority**: Visual flexibility is essential for component adoption. Different applications need different tab styles (e.g., underline for minimal design, pills for modern UI, full-width for mobile). This should be implemented after basic functionality works but before advanced features.

**Independent Test**: Can be fully tested by rendering separate tabs components with each variant (default, underline, pills, full-width), verifying Tailwind classes match Flowbite specifications, and testing color customization with Color.BLUE, Color.GREEN, etc.

**Acceptance Scenarios**:

1. **Given** a tabs component with variant="default", **When** the component renders, **Then** tab buttons have border styling with background color changes on active state.
2. **Given** a tabs component with variant="underline", **When** the component renders, **Then** tab buttons have no borders and show an underline indicator on the active tab.
3. **Given** a tabs component with variant="pills", **When** the component renders, **Then** tab buttons have rounded pill shapes with background colors.
4. **Given** a tabs component with variant="full-width", **When** the component renders, **Then** tab buttons stretch equally to fill the full container width.
5. **Given** a tabs component with color=Color.BLUE, **When** a tab becomes active, **Then** the active indicator uses blue color (bg-blue-600, text-blue-600, border-blue-600 as appropriate for variant).
6. **Given** any tabs component, **When** viewed in dark mode, **Then** all variants apply dark mode classes (dark:bg-gray-800, dark:text-white, dark:border-gray-700, etc.).

---

### User Story 3 - HTMX Lazy Loading and Dynamic Content (Priority: P3)

Users need tabs to load content dynamically from the server when activated, reducing initial page load time and allowing fresh data to be fetched when tabs are opened.

**Why this priority**: This is an advanced feature that enhances performance and enables dynamic content patterns. It should be implemented after core functionality and visual variants work correctly, as it builds on top of the basic tab switching mechanism.

**Independent Test**: Can be fully tested by creating a tabs component where one tab has hx_get="/api/content" attribute, clicking that tab, and verifying that an HTMX GET request is sent and the response replaces the tab panel content.

**Acceptance Scenarios**:

1. **Given** a tab with hx_get="/api/dashboard", **When** the tab is clicked for the first time, **Then** an HTMX GET request is sent to /api/dashboard and the response replaces the panel content.
2. **Given** a tab with hx_get and hx_trigger="click", **When** the tab is clicked, **Then** content is loaded on click instead of on tab activation.
3. **Given** a tab with hx_get, hx_target="#custom-target", **When** the tab loads content, **Then** the content is inserted into the custom target element instead of the default panel.
4. **Given** a tab with hx_get and hx_swap="innerHTML", **When** content loads, **Then** the swap strategy replaces the panel's inner HTML as specified.
5. **Given** tabs with HTMX attributes, **When** tab switching occurs, **Then** Flowbite JavaScript and HTMX events coexist without conflicts.

---

### User Story 4 - Icons and Enhanced Tab Labels (Priority: P3)

Users need to add icons to tab labels to improve visual recognition and make tabs more scannable, supporting both left and right icon positioning.

**Why this priority**: Icons enhance usability but aren't essential for basic tab functionality. This should be implemented alongside or after HTMX support as a visual enhancement.

**Independent Test**: Can be fully tested by rendering tabs with Icon.USER, Icon.DASHBOARD, Icon.SETTINGS icons, verifying icons appear next to labels, and testing both left (default) and right icon positions.

**Acceptance Scenarios**:

1. **Given** a tab with icon=Icon.USER, **When** the tab renders, **Then** the user icon appears to the left of the label text with proper spacing (gap-2).
2. **Given** a tab with icon=Icon.SETTINGS and icon_position="right", **When** the tab renders, **Then** the settings icon appears to the right of the label text.
3. **Given** a tab with an icon, **When** the tab is disabled, **Then** the icon's opacity matches the disabled state (text-gray-400 dark:text-gray-500).
4. **Given** tabs with icons in different variants (default, underline, pills), **When** rendered, **Then** icons maintain proper size (w-4 h-4) and alignment across all variants.

---

### User Story 5 - Disabled Tabs (Priority: P3)

Users need to disable certain tabs to prevent access to incomplete features or content that's unavailable based on user permissions or application state.

**Why this priority**: Disabled states are important for user guidance but don't affect core functionality. This can be implemented after basic tab switching works.

**Independent Test**: Can be fully tested by rendering a tabs component where one tab has disabled=True, clicking the disabled tab button, and verifying it cannot be activated and shows disabled styling.

**Acceptance Scenarios**:

1. **Given** a tab with disabled=True, **When** the component renders, **Then** the tab button shows disabled styling (opacity-50 cursor-not-allowed) and cannot be clicked.
2. **Given** a disabled tab, **When** user attempts to click it, **Then** the tab does not activate and no content panel change occurs.
3. **Given** a disabled tab, **When** user navigates via keyboard, **Then** the disabled tab can receive focus but cannot be activated with Enter/Space keys.
4. **Given** a disabled tab, **When** rendered in dark mode, **Then** disabled styling adapts to dark mode (dark:text-gray-500 dark:opacity-50).

---

### Edge Cases

- **Empty tabs list**: What happens when a Tabs component is rendered with an empty list of tabs? Should raise a validation error or render an empty container.
- **No active tab**: What happens if all tabs have is_active=False? Should default to first tab being active.
- **Multiple active tabs**: What happens if multiple tabs have is_active=True? Should activate only the first marked tab or the last one (need consistent behavior).
- **Single tab**: What happens when only one tab exists? Should still render with tab navigation UI or just show content directly.
- **HTMX loading state**: How does the component indicate loading when HTMX is fetching content? Should rely on HTMX's default indicators or provide custom loading state.
- **Icon without label**: What happens if a tab has an icon but no label text? Should render icon-only tab or require label for accessibility.
- **Very long tab labels**: How do tabs handle long label text? Should truncate with ellipsis or wrap to multiple lines.
- **Custom classes**: How do custom classes interact with variant classes? Should merge using ClassBuilder.merge() pattern.
- **Keyboard navigation across disabled tabs**: When using arrow keys, should navigation skip disabled tabs or allow focus but prevent activation.

## Requirements

### Functional Requirements

- **FR-001**: System MUST provide a Tab dataclass representing individual tabs with properties: label (required), content (Component or None), icon (optional), disabled (default False), is_active (default False), and custom class_.
- **FR-002**: System MUST provide HTMX attribute support on Tab including hx_get, hx_post, hx_trigger, hx_target, and hx_swap for dynamic content loading.
- **FR-003**: System MUST provide a Tabs container component that accepts a list of Tab objects and renders them with proper tab navigation UI.
- **FR-004**: System MUST support four tab variants: DEFAULT (bordered with background), UNDERLINE (minimal with bottom border indicator), PILLS (rounded background shapes), and FULL_WIDTH (tabs stretch to fill container width).
- **FR-005**: System MUST support color customization using the Color enum (BLUE, GREEN, RED, YELLOW, PURPLE, PINK, INDIGO, GRAY) for active tab indicators.
- **FR-006**: System MUST generate unique IDs for tab buttons and panels to associate them via aria-controls and id attributes, with support for custom tabs_id parameter.
- **FR-007**: System MUST implement full ARIA attributes including role="tablist" on container, role="tab" on buttons, role="tabpanel" on panels, aria-selected on active tabs, and aria-controls linking tabs to panels.
- **FR-008**: System MUST include Flowbite JavaScript data attributes (data-tabs-toggle, data-tabs-target) to enable Flowbite's tab switching and keyboard navigation.
- **FR-009**: System MUST support keyboard navigation via Flowbite JavaScript including arrow keys for tab navigation and Enter/Space for tab activation.
- **FR-010**: System MUST always include dark mode classes (dark:bg-*, dark:text-*, dark:border-*) regardless of theme context, following the project's dark mode pattern.
- **FR-011**: System MUST support icon positioning (left or right of label) using the existing icon system (get_icon() helper).
- **FR-012**: System MUST handle disabled tabs by preventing activation, applying disabled styling (opacity-50, cursor-not-allowed), and excluding from keyboard navigation.
- **FR-013**: System MUST activate the first tab by default if no tab has is_active=True explicitly set.
- **FR-014**: System MUST hide non-active tab panels using the "hidden" class and show only the active panel.
- **FR-015**: System MUST support custom classes on both individual tabs and the container via class_ parameter, merged using ClassBuilder.
- **FR-016**: System MUST use the class-based dataclass pattern with @dataclass(frozen=True, kw_only=True) and implement htmy(self, context: Context) -> Component method.
- **FR-017**: System MUST integrate with ThemeContext for dark mode support and ClassBuilder for class construction.
- **FR-018**: System MUST export Tab, Tabs, TabVariant enum, and IconPosition enum from components/__init__.py.

### Key Entities

- **Tab**: Represents an individual tab with label text, optional content panel, optional icon, disabled state, active state, HTMX attributes for lazy loading, and custom classes. Each tab has a unique ID that associates the button with its content panel.

- **Tabs**: Container component that manages a collection of Tab objects, determines which variant to render (default, underline, pills, full-width), sets the color scheme for active indicators, generates unique IDs for tab/panel associations, and provides ARIA structure for accessibility.

- **TabVariant**: Enumeration of visual styles (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH) that determine border styles, backgrounds, and indicator patterns.

- **IconPosition**: Enumeration of icon placement options (LEFT, RIGHT) relative to tab label text.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can switch between tabs using mouse clicks with visual feedback appearing within 100ms (perceived as instant).
- **SC-002**: Users can navigate all tabs and activate them using only keyboard (Tab, Arrow keys, Enter) without requiring a mouse, meeting WCAG 2.1 Level AA requirements.
- **SC-003**: All four tab variants (default, underline, pills, full-width) render with pixel-perfect alignment to Flowbite's reference implementation, verified by visual comparison.
- **SC-004**: HTMX lazy loading requests complete and render content within tab panels without JavaScript errors or conflicts with Flowbite tab switching.
- **SC-005**: Component achieves 90% or higher test coverage with all user stories independently testable via unit tests.
- **SC-006**: Screen readers correctly announce tab roles, active states, and panel associations using ARIA attributes, verified by accessibility testing tools.
- **SC-007**: Dark mode styling applies consistently across all variants without requiring theme context checks, using Tailwind's dark: prefix pattern.
- **SC-008**: Disabled tabs are visually distinguishable and cannot be activated via mouse or keyboard, preventing unintended navigation.

## Assumptions

- **Default Active Tab**: If no tab is explicitly marked as active (is_active=True), the first tab in the list will be activated automatically.
- **Icon System Integration**: The existing icon system (get_icon() helper) supports all necessary icons for tabs (no new icon registration required).
- **Flowbite JavaScript Availability**: Flowbite JavaScript is loaded on pages using the Tabs component, enabling keyboard navigation and tab switching logic.
- **HTMX Integration**: HTMX library is loaded on pages using lazy-loaded tabs, and HTMX events don't conflict with Flowbite's tab event handlers.
- **Python Version**: Python 3.11+ as per project requirements.
- **Testing Framework**: pytest with async support for htmy rendering tests.
- **Unique ID Strategy**: Using Python's id(self) for generating unique tab IDs is sufficient to avoid collisions within a single page render.

## Scope

### In Scope

- Tab and Tabs dataclasses with full ARIA support
- Four visual variants (default, underline, pills, full-width)
- Color customization for active tab indicators
- Icon support with left/right positioning
- Disabled tab state with visual and functional restrictions
- HTMX attribute support for lazy loading
- Flowbite JavaScript integration for tab switching
- Keyboard navigation (arrow keys, Enter/Space, Tab)
- Dark mode classes for all variants
- Unique ID generation for tab/panel associations
- Custom class merging via ClassBuilder
- Test suite with 90%+ coverage
- Showcase application (examples/tabs.py)
- Integration into consolidated showcase

### Out of Scope

- Vertical tabs orientation (future enhancement)
- Drag-and-drop tab reordering (future enhancement)
- Tab closing/removal functionality (future enhancement)
- Nested tabs (tabs within tab panels) (future enhancement)
- Tab overflow scrolling for many tabs (future enhancement)
- Custom tab templates beyond icon+label (future enhancement)
- Animation/transition effects beyond Flowbite defaults (future enhancement)
- Tab badge/counter indicators (future enhancement)

## Dependencies

- **htmy**: Component rendering framework (0.1.0+)
- **ClassBuilder**: Utility for constructing Tailwind class strings
- **ThemeContext**: Provides dark mode context to components
- **Icon System**: get_icon() helper for rendering SVG icons
- **Color Enum**: Flowbite color variants (types/color.py)
- **Flowbite CSS**: Version 2.5.1 for tab styling classes
- **Flowbite JavaScript**: For tab switching and keyboard navigation
- **HTMX**: Version 2.0.2 for lazy loading functionality (optional)
- **pytest**: Testing framework with async support
- **FastAPI + fasthx**: For showcase application
