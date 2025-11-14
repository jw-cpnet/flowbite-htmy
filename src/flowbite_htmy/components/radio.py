"""Radio button component with validation and HTMX support."""

from dataclasses import dataclass

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder
from flowbite_htmy.types import ValidationState

# Module-level counter for auto-generated IDs
_radio_counter = 0


def _generate_radio_id() -> str:
    """Generate unique radio button ID."""
    global _radio_counter
    _radio_counter += 1
    return f"radio-{_radio_counter}"


@dataclass(frozen=True, kw_only=True)
class Radio:
    """Radio button component with label, validation, and HTMX support."""

    # Core attributes
    label: str = ""
    name: str = ""
    value: str = ""
    checked: bool = False
    disabled: bool = False
    id: str | None = None

    # Validation & feedback
    validation_state: ValidationState = ValidationState.DEFAULT
    helper_text: str = ""

    # Accessibility
    aria_label: str = ""

    # Styling
    class_: str = ""

    # HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | None = None
    hx_select: str | None = None

    def __post_init__(self) -> None:
        """Validate component props."""
        if not self.label and not self.aria_label:
            raise ValueError("Either 'label' or 'aria_label' must be provided for accessibility")

    def htmy(self, context: Context) -> Component:
        """Render radio button component."""
        # Generate ID if not provided
        radio_id = self.id if self.id else _generate_radio_id()

        # Build classes
        input_classes = self._build_input_classes()
        label_classes = self._build_label_classes()
        helper_classes = self._build_helper_classes()

        # Build input element
        input_elem = html.input_(
            type="radio",
            id=radio_id,
            name=self.name or None,
            value=self.value or None,
            checked=self.checked or None,
            disabled=self.disabled or None,
            aria_label=self.aria_label or None,
            class_=input_classes,
            hx_get=self.hx_get,
            hx_post=self.hx_post,
            hx_put=self.hx_put,
            hx_delete=self.hx_delete,
            hx_patch=self.hx_patch,
            hx_target=self.hx_target,
            hx_swap=self.hx_swap,
            hx_trigger=self.hx_trigger,
            hx_push_url=self.hx_push_url,
            hx_select=self.hx_select,
        )

        # Container structure (Flowbite pattern)
        if self.label and self.helper_text:
            # Layout with label and helper text
            return html.div(
                html.div(
                    input_elem,
                    class_="flex items-center h-5",
                ),
                html.div(
                    html.label(
                        self.label,
                        for_=radio_id,
                        class_=label_classes,
                    ),
                    html.p(self.helper_text, class_=helper_classes),
                    class_="ms-2 text-sm",
                ),
                class_="flex items-start",
            )
        elif self.label:
            # Layout with label only
            return html.div(
                html.div(
                    input_elem,
                    class_="flex items-center h-5",
                ),
                html.div(
                    html.label(
                        self.label,
                        for_=radio_id,
                        class_=label_classes,
                    ),
                    class_="ms-2 text-sm",
                ),
                class_="flex items-start",
            )
        elif self.helper_text:
            # Layout with helper text only (no label, using aria-label)
            return html.div(
                html.div(
                    input_elem,
                    class_="flex items-center h-5",
                ),
                html.div(
                    html.p(self.helper_text, class_=helper_classes),
                    class_="ms-2 text-sm",
                ),
                class_="flex items-start",
            )
        else:
            # Just the input (no label or helper text, using aria-label)
            return html.div(
                html.div(
                    input_elem,
                    class_="flex items-center h-5",
                ),
                class_="flex items-start",
            )

    def _build_input_classes(self) -> str:
        """Build CSS classes for input element."""
        builder = ClassBuilder("w-4 h-4 bg-gray-100 border-gray-300")
        builder.add("focus:ring-2 dark:ring-offset-gray-800")
        builder.add("dark:bg-gray-700 dark:border-gray-600")

        # Validation state colors
        if self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 border-red-500 dark:border-red-600")
            builder.add("focus:ring-red-500 dark:focus:ring-red-600")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 border-green-500 dark:border-green-600")
            builder.add("focus:ring-green-500 dark:focus:ring-green-600")
        else:
            builder.add("text-blue-600")
            builder.add("focus:ring-blue-500 dark:focus:ring-blue-600")

        # Disabled state
        if self.disabled:
            builder.add("disabled:opacity-50 disabled:cursor-not-allowed")

        return builder.merge(self.class_)

    def _build_label_classes(self) -> str:
        """Build CSS classes for label text."""
        builder = ClassBuilder("font-medium")

        # Validation state text colors (disabled overrides)
        if self.disabled:
            builder.add("text-gray-400 dark:text-gray-500")
        elif self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 dark:text-red-500")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 dark:text-green-500")
        else:
            builder.add("text-gray-900 dark:text-gray-300")

        return builder.build()

    def _build_helper_classes(self) -> str:
        """Build CSS classes for helper text."""
        builder = ClassBuilder()

        # Validation state text colors
        if self.validation_state == ValidationState.ERROR:
            builder.add("text-red-600 dark:text-red-500")
        elif self.validation_state == ValidationState.SUCCESS:
            builder.add("text-green-600 dark:text-green-500")
        else:
            builder.add("text-gray-500 dark:text-gray-400")

        return builder.build()
