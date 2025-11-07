"""Size type definitions for Flowbite components."""

from enum import Enum


class Size(str, Enum):
    """Flowbite size variants."""

    XS = "xs"
    SM = "sm"
    MD = "md"
    LG = "lg"
    XL = "xl"
    XXL = "2xl"

    def __str__(self) -> str:
        """Return the size value as a string."""
        return self.value
