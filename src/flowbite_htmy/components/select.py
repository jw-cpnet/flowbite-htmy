"""Select component for Flowbite."""

from dataclasses import dataclass
from typing import Any, Literal

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext

# Validation state type
ValidationState = Literal["success", "error"] | None

# Option type - either a string or a dict with value and label
OptionType = str | dict[str, str]


@dataclass(frozen=True, kw_only=True)
class Select:
    """Select dropdown component with label and validation support.

    Wraps a label and select field together with consistent styling, validation
    states, helper text, and dark mode support. Automatically generates option
    elements from Python list or dict data.

    Example:
        ```python
        # Simple string options
        Select(
            id="country",
            label="Select your country",
            options=["United States", "Canada", "France", "Germany"],
        )

        # Dict options with values and labels
        Select(
            id="country",
            label="Select your country",
            options=[
                {"value": "US", "label": "United States"},
                {"value": "CA", "label": "Canada"},
            ],
        )
        ```

    With placeholder and validation:
        ```python
        Select(
            id="country",
            label="Country",
            placeholder="Choose a country",
            options=["United States", "Canada"],
            validation="error",
            helper_text="Please select a valid country",
        )
        ```
    """

    # Required props
    id: str
    """Unique ID for the select field (used for label association)."""

    options: list[OptionType]
    """List of options - either strings or dicts with 'value' and 'label' keys."""

    # Optional props
    label: str | None = None
    """Label text displayed above the select field. If None, renders bare select."""

    name: str | None = None
    """HTML name attribute for form submission. Defaults to id if not provided."""

    placeholder: str | None = None
    """Placeholder option shown first with 'selected' attribute."""

    value: str | None = None
    """Pre-selected value (matches option value attribute)."""

    multiple: bool = False
    """Whether multiple selections are allowed."""

    size: int | None = None
    """Number of visible options in the list (for scrollable select)."""

    required: bool = False
    """Whether the select field is required."""

    disabled: bool = False
    """Whether the select field is disabled."""

    validation: ValidationState = None
    """Validation state: 'success' or 'error'."""

    helper_text: str | None = None
    """Helper text displayed below the select field."""

    class_: str = ""
    """Additional CSS classes for the select wrapper."""

    attrs: dict[str, Any] | None = None
    """Additional HTML attributes for the select element."""

    # HTMX attributes
    hx_get: str | None = None
    """HTMX hx-get attribute."""

    hx_post: str | None = None
    """HTMX hx-post attribute."""

    hx_target: str | None = None
    """HTMX hx-target attribute."""

    hx_swap: str | None = None
    """HTMX hx-swap attribute."""

    hx_trigger: str | None = None
    """HTMX hx-trigger attribute."""

    hx_include: str | None = None
    """HTMX hx-include attribute for including additional element values."""

    def htmy(self, context: Context) -> Component:
        """Render the select component."""
        theme = ThemeContext.from_context(context)

        # Build select classes
        select_classes = self._build_select_classes(theme)

        # Build select attributes
        select_attrs = self._build_select_attrs()

        # Build option elements
        option_elements = self._build_options()

        select_el = html.select(
            *option_elements,  # type: ignore[arg-type]
            **select_attrs,
            class_=select_classes,
        )

        # Bare mode: no label wrapping
        if self.label is None:
            return select_el

        # Build label classes
        label_classes = self._build_label_classes()

        # Build helper text if provided
        helper = self._render_helper_text() if self.helper_text else None

        # Build wrapper content
        content: list[Component] = [
            html.label(
                self.label,
                **{"for": self.id},
                class_=label_classes,
            ),
            select_el,
        ]

        if helper:
            content.append(helper)

        return html.div(*content, class_=self.class_)  # type: ignore[arg-type]

    def _build_label_classes(self) -> str:
        """Build label CSS classes based on validation state."""
        builder = ClassBuilder("block mb-2 text-sm font-medium")

        if self.validation == "success":
            builder.add("text-green-700 dark:text-green-500")
        elif self.validation == "error":
            builder.add("text-red-700 dark:text-red-500")
        else:
            builder.add("text-gray-900 dark:text-white")

        return builder.build()

    def _build_select_classes(self, theme: ThemeContext) -> str:
        """Build select CSS classes based on state and validation."""
        builder = ClassBuilder()

        # Base classes
        builder.add("text-sm rounded-lg block w-full p-2.5")
        builder.add("focus:ring-blue-500 focus:border-blue-500")

        # Disabled state
        if self.disabled:
            builder.add("cursor-not-allowed bg-gray-100")
            builder.add("dark:bg-gray-700")
        else:
            # Normal background
            builder.add("bg-gray-50 dark:bg-gray-700")

        # Validation-specific classes
        if self.validation == "success":
            builder.add("bg-green-50 border border-green-500")
            builder.add("text-green-900 dark:text-green-400")
            builder.add("placeholder-green-700 dark:placeholder-green-500")
            builder.add("dark:border-green-500")
        elif self.validation == "error":
            builder.add("bg-red-50 border border-red-500")
            builder.add("text-red-900 placeholder-red-700")
            builder.add("dark:text-red-500 dark:placeholder-red-500")
            builder.add("dark:border-red-500")
        else:
            # Default border and text
            builder.add("border border-gray-300 text-gray-900")
            builder.add("dark:border-gray-600 dark:placeholder-gray-400 dark:text-white")

        return builder.build()

    def _build_select_attrs(self) -> dict[str, Any]:
        """Build select element attributes."""
        attrs: dict[str, Any] = {
            "id": self.id,
            "name": self.name or self.id,
        }

        if self.multiple:
            attrs["multiple"] = True

        if self.size is not None:
            attrs["size"] = str(self.size)

        if self.required:
            attrs["required"] = True

        if self.disabled:
            attrs["disabled"] = True

        # HTMX attributes
        if self.hx_get:
            attrs["hx-get"] = self.hx_get
        if self.hx_post:
            attrs["hx-post"] = self.hx_post
        if self.hx_target:
            attrs["hx-target"] = self.hx_target
        if self.hx_swap:
            attrs["hx-swap"] = self.hx_swap
        if self.hx_trigger:
            attrs["hx-trigger"] = self.hx_trigger
        if self.hx_include:
            attrs["hx-include"] = self.hx_include

        # Merge passthrough attributes
        if self.attrs:
            attrs.update(self.attrs)

        return attrs

    def _build_options(self) -> list[Component]:
        """Build option elements from options list."""
        option_elements: list[Component] = []

        # Add placeholder option if provided
        if self.placeholder:
            option_elements.append(html.option(self.placeholder, selected=True))

        # Add regular options
        for option in self.options:
            if isinstance(option, str):
                # Simple string option
                is_selected = self.value == option if self.value else False
                attrs: dict[str, Any] = {}
                if is_selected:
                    attrs["selected"] = True
                option_elements.append(html.option(option, **attrs))
            else:
                # Dict option with value and label
                option_value = option.get("value", "")
                option_label = option.get("label", "")
                is_selected = self.value == option_value if self.value else False
                attrs = {"value": option_value}
                if is_selected:
                    attrs["selected"] = True
                option_elements.append(html.option(option_label, **attrs))

        return option_elements

    def _render_helper_text(self) -> Component:
        """Render helper text with appropriate styling."""
        text_classes = "mt-2 text-sm"

        if self.validation == "success":
            text_classes += " text-green-600 dark:text-green-500"
        elif self.validation == "error":
            text_classes += " text-red-600 dark:text-red-500"
        else:
            text_classes += " text-gray-500 dark:text-gray-400"

        # helper_text is guaranteed to be str when this method is called
        return html.p(self.helper_text, class_=text_classes)  # type: ignore[arg-type]
