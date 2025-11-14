# Data Model: Toast Component

**Feature**: Toast notification component
**Branch**: 003-toast
**Date**: 2025-11-14

## Overview

This document defines the data structures for the Toast component following the established dataclass pattern used throughout the flowbite-htmy library.

## Core Entities

### ToastVariant Enum

**Purpose**: Type-safe enumeration of toast notification types

**Location**: `src/flowbite_htmy/types/toast.py`

**Definition**:
```python
from enum import Enum

class ToastVariant(str, Enum):
    """Toast notification variants matching Flowbite design system.

    Each variant has associated colors, icons, and styling.
    """
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
```

**Usage**:
```python
from flowbite_htmy.types import ToastVariant

toast = Toast(
    message="Operation successful",
    variant=ToastVariant.SUCCESS
)
```

**Relationships**:
- Maps to Icon enum values (SUCCESS → Icon.CHECK, etc.)
- Maps to Tailwind color classes (success → green-*, danger → red-*, etc.)
- Used by Toast component as required field

### ToastActionButton Dataclass

**Purpose**: Configuration for optional action button in interactive toasts

**Location**: `src/flowbite_htmy/components/toast.py` (nested in same file as Toast)

**Definition**:
```python
from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class ToastActionButton:
    """Action button configuration for interactive toasts.

    Supports HTMX integration for server-side interactions.
    """
    label: str

    # HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | bool | None = None
    hx_select: str | None = None

    # Standard button attributes
    type_: str = "button"
    class_: str = ""
```

**Usage**:
```python
action_button = ToastActionButton(
    label="Reply",
    hx_get="/reply",
    hx_target="#chat-window"
)

toast = Toast(
    message="New message from Alice",
    variant=ToastVariant.INFO,
    action_button=action_button
)
```

**Relationships**:
- Used by Toast component as optional field
- Rendered as Button-like element with HTMX attributes
- Independent lifecycle (not a separate component)

### Toast Component

**Purpose**: Main toast notification component for temporary messages

**Location**: `src/flowbite_htmy/components/toast.py`

**Definition**:
```python
from dataclasses import dataclass
from typing import Any
from htmy import Component, Context, html
from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import ToastVariant
from flowbite_htmy.icons import Icon, get_icon

@dataclass(frozen=True, kw_only=True)
class Toast:
    """Toast notification component for temporary messages.

    Supports four variants (success, danger, warning, info), optional
    action buttons, rich content with avatars, and Flowbite JavaScript
    dismiss functionality.

    Examples:
        Simple success toast:
        >>> Toast(message="Saved successfully", variant=ToastVariant.SUCCESS)

        Interactive toast with action:
        >>> Toast(
        ...     message="New message from Alice",
        ...     variant=ToastVariant.INFO,
        ...     action_button=ToastActionButton(label="Reply", hx_get="/reply")
        ... )

        Rich content toast:
        >>> Toast(
        ...     message="Alice: Thanks for sharing!",
        ...     variant=ToastVariant.INFO,
        ...     avatar_src="/users/alice.jpg"
        ... )
    """
    # Required fields
    message: str

    # Variant and styling
    variant: ToastVariant = ToastVariant.INFO
    icon: Icon | None = None  # None = use default for variant
    class_: str = ""

    # Dismissible functionality
    dismissible: bool = True
    id: str | None = None  # Auto-generated if None

    # Interactive features
    action_button: ToastActionButton | None = None

    # Rich content
    avatar_src: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render toast notification component."""
        theme = ThemeContext.from_context(context)
        toast_id = self.id or f"toast-{id(self)}"
        icon_component = self._get_icon()
        classes = self._build_classes(theme)

        return html.div(
            self._render_content(icon_component, toast_id),
            id=toast_id,
            class_=classes,
            role="alert"
        )

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build toast container classes."""
        builder = ClassBuilder(
            "flex items-center w-full max-w-xs p-4",
            "text-gray-500 bg-white rounded-lg shadow-sm",
            "dark:text-gray-400 dark:bg-gray-800"
        )
        return builder.merge(self.class_)

    def _get_icon(self) -> Icon:
        """Get icon for toast (custom or default for variant)."""
        if self.icon is not None:
            return self.icon

        # Default icons per variant
        return {
            ToastVariant.SUCCESS: Icon.CHECK,
            ToastVariant.DANGER: Icon.CLOSE,
            ToastVariant.WARNING: Icon.EXCLAMATION,
            ToastVariant.INFO: Icon.INFO
        }[self.variant]

    def _render_content(self, icon: Icon, toast_id: str) -> Component:
        """Render toast content (icon, message, button, close)."""
        # Implementation details in actual code
        ...
```

**Field Descriptions**:

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `message` | str | Yes | - | Toast message text to display |
| `variant` | ToastVariant | No | INFO | Color variant (SUCCESS, DANGER, WARNING, INFO) |
| `icon` | Icon \| None | No | None | Custom icon (None = use default for variant) |
| `class_` | str | No | "" | Additional CSS classes to merge |
| `dismissible` | bool | No | True | Whether toast can be dismissed with close button |
| `id` | str \| None | No | None | Toast HTML ID (auto-generated if None) |
| `action_button` | ToastActionButton \| None | No | None | Optional action button for interactions |
| `avatar_src` | str \| None | No | None | Optional avatar image URL for rich content |

**Relationships**:
- Uses `ToastVariant` enum for type-safe variants
- Uses `Icon` enum for icon selection
- Optionally contains `ToastActionButton` for interactions
- Uses `ClassBuilder` from base utilities
- Uses `ThemeContext` for dark mode support
- May use `get_icon()` helper from icons module
- May use `Avatar` component if avatar_src provided (future enhancement)

### Variant-to-Class Mappings

**Icon Container Classes**:
```python
VARIANT_ICON_CLASSES = {
    ToastVariant.SUCCESS: (
        "inline-flex items-center justify-center shrink-0 w-8 h-8 "
        "text-green-500 bg-green-100 rounded-lg "
        "dark:bg-green-800 dark:text-green-200"
    ),
    ToastVariant.DANGER: (
        "inline-flex items-center justify-center shrink-0 w-8 h-8 "
        "text-red-500 bg-red-100 rounded-lg "
        "dark:bg-red-800 dark:text-red-200"
    ),
    ToastVariant.WARNING: (
        "inline-flex items-center justify-center shrink-0 w-8 h-8 "
        "text-yellow-500 bg-yellow-100 rounded-lg "
        "dark:bg-yellow-800 dark:text-yellow-200"
    ),
    ToastVariant.INFO: (
        "inline-flex items-center justify-center shrink-0 w-8 h-8 "
        "text-blue-500 bg-blue-100 rounded-lg "
        "dark:bg-blue-800 dark:text-blue-200"
    ),
}
```

**Default Icons**:
```python
VARIANT_DEFAULT_ICONS = {
    ToastVariant.SUCCESS: Icon.CHECK,
    ToastVariant.DANGER: Icon.CLOSE,
    ToastVariant.WARNING: Icon.EXCLAMATION,
    ToastVariant.INFO: Icon.INFO,
}
```

## State Transitions

**Toast Lifecycle**:
1. **Created**: Toast component instantiated with props
2. **Rendered**: Component htmy() method called, HTML generated
3. **Displayed**: HTML inserted into DOM (via HTMX or initial render)
4. **Dismissed** (optional): User clicks close button, Flowbite JS removes element
5. **Destroyed**: Element removed from DOM

**State Diagram**:
```
Created → Rendered → Displayed → [Dismissed] → Destroyed
                                   ↑
                                   └─ (if dismissible=True)
```

**Notes**:
- Component is stateless (no internal state management)
- Dismiss functionality handled by Flowbite JavaScript (outside component scope)
- Auto-dismiss timers handled by application (outside component scope)
- Positioning/stacking handled by parent container (outside component scope)

## Validation Rules

**Message Validation**:
- MUST NOT be empty string (assertion or validation in constructor)
- CAN be long (component handles text wrapping with max-w-xs constraint)
- CAN contain HTML entities (htmy handles escaping)

**Variant Validation**:
- MUST be valid ToastVariant enum value (enforced by type system)
- Cannot be None (required field with default)

**Icon Validation**:
- CAN be None (uses default icon for variant)
- If provided, MUST be valid Icon enum value (enforced by type system)

**ID Validation**:
- CAN be None (auto-generated)
- If provided, SHOULD be unique across toasts on same page (developer responsibility)
- If provided, MUST be valid HTML ID (developer responsibility)

**Action Button Validation**:
- CAN be None (no action button rendered)
- If provided, label MUST NOT be empty
- At least one of hx_get, hx_post, hx_put, hx_delete, hx_patch SHOULD be provided (otherwise button does nothing)

**Avatar Validation**:
- CAN be None (no avatar rendered)
- If provided, MUST be valid image URL (developer responsibility)
- Image loading failures handled by browser (not component concern)

## Component Dependencies

**Internal Dependencies** (from flowbite-htmy):
- `ClassBuilder` - Class string construction
- `ThemeContext` - Dark mode support
- `Icon` enum - Icon type definitions
- `get_icon()` - Icon SVG retrieval
- `ToastVariant` enum - Variant types

**External Dependencies**:
- `htmy` - Component rendering framework
- `dataclasses` - Dataclass decorator
- Flowbite CSS 2.5.1 - Styling
- Flowbite JavaScript - Dismiss functionality (optional)

**Optional Component Dependencies**:
- `Avatar` component - Rich content support (future enhancement)

## Type Definitions

**Type Aliases** (if needed):
```python
ToastID = str  # HTML ID for toast element
AvatarURL = str  # Image URL for avatar
```

## Examples

### Example 1: Simple Success Toast
```python
toast = Toast(
    message="Item saved successfully",
    variant=ToastVariant.SUCCESS
)
# Renders: Green toast with checkmark icon and close button
```

### Example 2: Error Toast (Non-dismissible)
```python
toast = Toast(
    message="Connection failed. Please try again.",
    variant=ToastVariant.DANGER,
    dismissible=False
)
# Renders: Red toast with X icon, no close button
```

### Example 3: Interactive Toast with Action
```python
toast = Toast(
    message="File uploaded. Would you like to share it?",
    variant=ToastVariant.INFO,
    action_button=ToastActionButton(
        label="Share",
        hx_post="/share",
        hx_target="#share-modal"
    )
)
# Renders: Blue toast with info icon, Share button, and close button
```

### Example 4: Rich Content Toast with Avatar
```python
toast = Toast(
    message="Alice: Thanks for the feedback!",
    variant=ToastVariant.INFO,
    avatar_src="/static/avatars/alice.jpg",
    action_button=ToastActionButton(
        label="Reply",
        hx_get="/messages/reply/123"
    )
)
# Renders: Blue toast with avatar, message, Reply button, and close button
```

### Example 5: Custom Icon Toast
```python
toast = Toast(
    message="Payment processed",
    variant=ToastVariant.SUCCESS,
    icon=Icon.PAYMENT  # Custom icon instead of default checkmark
)
# Renders: Green toast with payment icon and close button
```

## Migration Notes

**Breaking Changes**: None (new component)

**Deprecations**: None (new component)

**Future Enhancements**:
- Consider supporting multiple action buttons (list of ToastActionButton)
- Consider adding title/heading field for structured content
- Consider adding timestamp field for temporal context
- Consider supporting custom dismiss callbacks (requires JavaScript bridge)
