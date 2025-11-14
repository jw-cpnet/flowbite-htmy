"""Validation state enum for form components."""

from enum import Enum


class ValidationState(str, Enum):
    """Validation state for form components."""

    DEFAULT = "default"
    ERROR = "error"
    SUCCESS = "success"
