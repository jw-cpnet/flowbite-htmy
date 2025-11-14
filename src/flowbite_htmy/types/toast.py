"""Toast component types."""

from enum import Enum


class ToastVariant(str, Enum):
    """Toast notification variants matching Flowbite design system.

    Each variant has associated colors, icons, and styling.
    """

    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
