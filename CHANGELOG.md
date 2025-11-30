# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2024-11-30

### Added

- **Button `indicator` prop**: New built-in HTMX loading indicator support
  - `indicator=True` adds a default spinner with `htmx-indicator` class
  - Custom icons supported via `indicator=SafeStr(...)`
  - Spinner automatically shows during HTMX requests and hides when complete
  - Much simpler than using `hx_on` for loading states

- **Button HTMX attributes**: Added missing HTMX attributes for better DX
  - `hx_include` - Include additional element values in requests
  - `hx_confirm` - Show confirmation dialog before request
  - `hx_vals` - Add values to request
  - `hx_encoding` - Set request encoding type
  - `hx_headers` - Add custom request headers
  - `hx_disabled_elt` - Disable elements during request
  - `hx_sync` - Synchronize requests

- **Button `hx_on` prop**: Dict-based HTMX event handlers
  - Solves the awkward `hx-on::event-name` syntax issue
  - Example: `hx_on={"after-request": "drawer.hide()"}`

- **Icon.SPINNER**: Added reusable spinner icon to icons module

- **Documentation**: Added Tailwind v4 upgrade guide (`docs/tailwind-v4-upgrade.md`)

### Changed

- **HTMX version**: Updated from 2.0.2 to 2.0.8
  - Fixes bug where `hx-disabled-elt` prevented `htmx-request` class removal
  - Indicators now properly hide after request completion

### Fixed

- Fixed `htmx-indicator` CSS conflicts with Tailwind's `inline` class
- Fixed indicator taking up space when hidden (use `display: none` instead of `opacity: 0`)

## [0.3.0] - 2024-11-XX

### Added

- **Drawer component**: Full implementation with Flowbite JS integration
  - Multiple placement options (left, right, top, bottom)
  - Backdrop support
  - Body scroll lock option
  - `trigger_variant` prop for trigger button styling

- **Hybrid distribution strategy**: Library packaging improvements

### Fixed

- Modal initialization in consolidated showcase
- Drawer initialization and placement issues

## [0.2.0] - 2024-11-XX

### Added

- **Accordion component**: Collapsible panels with ARIA support
- **Toast component**: Temporary notifications with actions
- **Textarea component**: Multi-line text inputs
- **Radio component**: Radio buttons with validation states
- **Checkbox component**: Checkboxes with labels and validation

## [0.1.0] - 2024-10-XX

### Added

- Initial release
- **Core components**: Button, Badge, Alert, Avatar
- **Form components**: Input, Select, Pagination
- **Interactive components**: Modal
- **Base utilities**: ClassBuilder, ThemeContext
- **Icon system**: Icon enum with SVG icons
- **HTMX integration**: Full support for HTMX attributes
- **Showcase app**: Consolidated example application

---

[0.4.0]: https://github.com/yourusername/flowbite-htmy/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/yourusername/flowbite-htmy/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/yourusername/flowbite-htmy/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/yourusername/flowbite-htmy/releases/tag/v0.1.0
