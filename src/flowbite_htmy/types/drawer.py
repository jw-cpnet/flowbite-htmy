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


class DrawerWidth(str, Enum):
    """Max-width options for drawer shell components."""

    XS = "max-w-xs"  # 320px
    SM = "max-w-sm"  # 384px
    MD = "max-w-md"  # 448px
    LG = "max-w-lg"  # 512px
    XL = "max-w-xl"  # 576px
    XXL = "max-w-2xl"  # 672px (default)
    XXXL = "max-w-3xl"  # 768px
    XXXXL = "max-w-4xl"  # 896px

    def __str__(self) -> str:
        """Return the width value as a string."""
        return self.value
