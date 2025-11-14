"""Checkbox component for Flowbite."""

from dataclasses import dataclass
from typing import Any, Literal

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext


@dataclass(frozen=True, kw_only=True)
class Checkbox:
    """A Flowbite checkbox component.

    Supports validation states, helper text, checked/disabled states,
    and dark mode.

    Args:
        id: Unique identifier for the checkbox (required)
        label: Label text or HTML component for the checkbox
        value: Value attribute for the checkbox (default: "")
        name: Name attribute for grouped checkboxes
        checked: Whether the checkbox is checked (default: False)
        disabled: Whether the checkbox is disabled (default: False)
        required: Whether the checkbox is required (default: False)
        validation: Validation state ("success" or "error")
        helper_text: Helper text displayed below the checkbox
        class_: Additional CSS classes for the wrapper
        attrs: Additional HTML attributes to pass to the input element

    Example:
        >>> Checkbox(
        ...     id="terms",
        ...     label="I agree to the terms and conditions",
        ...     required=True
        ... )

        >>> Checkbox(
        ...     id="promo",
        ...     label="Get promotional offers",
        ...     helper_text="We'll send you weekly updates",
        ...     checked=True
        ... )

        >>> Checkbox(
        ...     id="color",
        ...     name="colors",
        ...     value="blue",
        ...     label="Blue"
        ... )
    """

    id: str
    label: str | SafeStr | Component
    value: str = ""
    name: str | None = None
    checked: bool = False
    disabled: bool = False
    required: bool = False
    validation: Literal["success", "error"] | None = None
    helper_text: str | None = None
    class_: str = ""
    attrs: dict[str, Any] | None = None

    def htmy(self, context: Context) -> Component:
        """Render the checkbox component."""
        theme = ThemeContext.from_context(context)
        input_classes = self._build_input_classes(theme)
        label_classes = self._build_label_classes()
        helper_classes = self._build_helper_classes()

        # Build input attributes
        input_attrs: dict[str, Any] = {
            "id": self.id,
            "type": "checkbox",
            "class_": input_classes,
            "value": self.value,
        }

        if self.name:
            input_attrs["name"] = self.name

        if self.checked:
            input_attrs["checked"] = ""

        if self.disabled:
            input_attrs["disabled"] = ""

        if self.required:
            input_attrs["required"] = ""

        if self.helper_text:
            input_attrs["aria_describedby"] = f"{self.id}-helper"

        # Add custom attributes
        if self.attrs:
            input_attrs.update(self.attrs)

        # Build wrapper classes
        wrapper_classes = ClassBuilder("flex")
        if not self.helper_text:
            wrapper_classes.add("items-center")
        if self.helper_text:
            wrapper_classes.add("mb-4")
        wrapper_classes.merge(self.class_)

        # Build structure
        if self.helper_text:
            # Complex layout with helper text
            return html.div(
                html.div(
                    html.input_(**input_attrs),
                    class_="flex items-center h-5",
                ),
                html.div(
                    html.label(
                        self.label,  # type: ignore[arg-type]
                        for_=self.id,
                        class_=label_classes,
                    ),
                    html.p(
                        self.helper_text,
                        id=f"{self.id}-helper",
                        class_=helper_classes,
                    ),
                    class_="ms-2 text-sm",
                ),
                class_=wrapper_classes.build(),
            )
        else:
            # Simple layout
            return html.div(
                html.input_(**input_attrs),
                html.label(
                    self.label,  # type: ignore[arg-type]
                    for_=self.id,
                    class_=label_classes,
                ),
                class_=wrapper_classes.build(),
            )

    def _build_input_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the checkbox input."""
        builder = ClassBuilder("w-4 h-4 rounded-sm")

        # Validation-specific styles
        if self.validation == "success":
            builder.add(
                "text-green-600 bg-green-50 border-green-300 "
                "focus:ring-green-500 dark:focus:ring-green-600 "
                "dark:bg-green-900 dark:border-green-600"
            )
        elif self.validation == "error":
            builder.add(
                "text-red-600 bg-red-50 border-red-300 "
                "focus:ring-red-500 dark:focus:ring-red-600 "
                "dark:bg-red-900 dark:border-red-600"
            )
        else:
            # Default styles
            builder.add(
                "text-blue-600 bg-gray-100 border-gray-300 "
                "focus:ring-blue-500 dark:focus:ring-blue-600 "
                "dark:bg-gray-700 dark:border-gray-600"
            )

        # Focus ring
        builder.add("dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2")

        # Disabled state
        if self.disabled:
            builder.add("bg-gray-50 dark:bg-gray-700")

        return builder.build()

    def _build_label_classes(self) -> str:
        """Build CSS classes for the label."""
        builder = ClassBuilder("ms-2 text-sm font-medium")

        if self.disabled:
            builder.add("text-gray-400 dark:text-gray-500")
        else:
            builder.add("text-gray-900 dark:text-gray-300")

        return builder.build()

    def _build_helper_classes(self) -> str:
        """Build CSS classes for helper text."""
        builder = ClassBuilder("text-xs font-normal")

        if self.validation == "success":
            builder.add("text-green-600 dark:text-green-400")
        elif self.validation == "error":
            builder.add("text-red-600 dark:text-red-400")
        else:
            builder.add("text-gray-500 dark:text-gray-400")

        return builder.build()
