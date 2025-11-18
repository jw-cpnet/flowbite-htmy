"""Drawer type definitions for Flowbite components."""

from enum import Enum


class DrawerPlacement(str, Enum):
    """Drawer placement positions for edge positioning."""

    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"

    def __str__(self) -> str:
        """Return the placement value as a string."""
        return self.value
