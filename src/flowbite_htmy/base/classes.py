"""Utility for building Tailwind CSS class strings."""



class ClassBuilder:
    """Utility for building Tailwind CSS class strings.

    Provides a fluent API for conditionally adding CSS classes,
    useful for components with complex styling logic.

    Example:
        >>> builder = ClassBuilder("btn")
        >>> builder.add("text-white").add_if(True, "bg-blue-500")
        >>> builder.merge("custom-class")
        'btn text-white bg-blue-500 custom-class'
    """

    def __init__(self, base: str = "") -> None:
        """Initialize the ClassBuilder with optional base classes.

        Args:
            base: Initial base class string.
        """
        self.classes: list[str] = [base] if base else []

    def add(self, *classes: str) -> "ClassBuilder":
        """Add classes unconditionally.

        Args:
            *classes: One or more class strings to add.

        Returns:
            Self for method chaining.
        """
        self.classes.extend(classes)
        return self

    def add_if(self, condition: bool, *classes: str) -> "ClassBuilder":
        """Add classes conditionally.

        Args:
            condition: If True, add the classes.
            *classes: One or more class strings to add.

        Returns:
            Self for method chaining.
        """
        if condition:
            self.classes.extend(classes)
        return self

    def add_from_dict(self, class_map: dict[str, bool]) -> "ClassBuilder":
        """Add classes from a dictionary mapping class names to conditions.

        Args:
            class_map: Dictionary mapping class names to boolean conditions.

        Returns:
            Self for method chaining.

        Example:
            >>> builder = ClassBuilder()
            >>> builder.add_from_dict({
            ...     "active": is_active,
            ...     "disabled": is_disabled
            ... })
        """
        for class_name, condition in class_map.items():
            if condition:
                self.classes.append(class_name)
        return self

    def merge(self, custom: str = "") -> str:
        """Merge with custom classes and return final class string.

        Args:
            custom: Additional custom classes to append.

        Returns:
            Final space-separated class string.
        """
        if custom:
            self.classes.append(custom)
        return " ".join(filter(None, self.classes))

    def build(self) -> str:
        """Build and return the final class string.

        Alias for merge() without custom classes.

        Returns:
            Final space-separated class string.
        """
        return self.merge()

    @classmethod
    def from_dict(cls, class_map: dict[str, bool], base: str = "") -> str:
        """Create a ClassBuilder from a dictionary and immediately build.

        Convenience method for simple conditional class building.

        Args:
            class_map: Dictionary mapping class names to boolean conditions.
            base: Optional base classes.

        Returns:
            Final space-separated class string.

        Example:
            >>> classes = ClassBuilder.from_dict({
            ...     "btn-primary": is_primary,
            ...     "btn-lg": is_large
            ... }, base="btn")
        """
        return cls(base).add_from_dict(class_map).build()
