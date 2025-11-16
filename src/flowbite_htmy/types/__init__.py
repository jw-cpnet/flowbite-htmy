"""Type definitions and enums."""

from enum import Enum

from flowbite_htmy.types.button import ButtonVariant
from flowbite_htmy.types.colors import Color
from flowbite_htmy.types.sizes import Size
from flowbite_htmy.types.toast import ToastVariant
from flowbite_htmy.types.validation import ValidationState


# T005: DropdownPlacement enum
class DropdownPlacement(str, Enum):
    """Dropdown menu positioning options."""

    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"


# T006: DropdownTriggerType enum
class DropdownTriggerType(str, Enum):
    """Dropdown trigger element types."""

    BUTTON = "button"
    AVATAR = "avatar"
    TEXT = "text"


# T007: DropdownTriggerMode enum
class DropdownTriggerMode(str, Enum):
    """Dropdown activation methods."""

    CLICK = "click"
    HOVER = "hover"


# T008: Update __all__ to export new enums
__all__ = [
    "ButtonVariant",
    "Color",
    "DropdownPlacement",
    "DropdownTriggerMode",
    "DropdownTriggerType",
    "Size",
    "ToastVariant",
    "ValidationState",
]
