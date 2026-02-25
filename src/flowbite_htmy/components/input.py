"""Input component for Flowbite."""

from dataclasses import dataclass
from typing import Any, Literal

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext

# Validation state type
ValidationState = Literal["success", "error"] | None


@dataclass(frozen=True, kw_only=True)
class Input:
    """Input field component with label and validation support.

    Wraps a label and input field together with consistent styling, validation
    states, helper text, and dark mode support.

    Example:
        ```python
        Input(
            id="email",
            label="Email address",
            type="email",
            placeholder="you@example.com",
            required=True,
            helper_text="We'll never share your email",
        )
        ```

    Validation example:
        ```python
        Input(
            id="username",
            label="Username",
            validation="error",
            helper_text="Username is already taken",
        )
        ```
    """

    # Required props
    id: str
    """Unique ID for the input field (used for label association)."""

    label: str | None = None
    """Label text displayed above the input field. If None, renders bare input."""

    # Optional props
    type: str = "text"
    """Input type (text, email, password, number, tel, url, etc.)."""

    name: str | None = None
    """HTML name attribute for form submission. Defaults to id if not provided."""

    placeholder: str | None = None
    """Placeholder text shown when input is empty."""

    value: str | None = None
    """Initial value for the input field."""

    required: bool = False
    """Whether the input field is required."""

    disabled: bool = False
    """Whether the input field is disabled."""

    validation: ValidationState = None
    """Validation state: 'success' or 'error'."""

    helper_text: str | None = None
    """Helper text displayed below the input field."""

    class_: str = ""
    """Additional CSS classes for the input wrapper."""

    attrs: dict[str, Any] | None = None
    """Additional HTML attributes for the input element."""

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

    def htmy(self, context: Context) -> Component:
        """Render the input component."""
        theme = ThemeContext.from_context(context)

        # Build input classes
        input_classes = self._build_input_classes(theme)

        # Build input attributes
        input_attrs = self._build_input_attrs()

        input_el = html.input_(**input_attrs, class_=input_classes)

        # Bare mode: no label wrapping
        if self.label is None:
            return input_el

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
            input_el,
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

    def _build_input_classes(self, theme: ThemeContext) -> str:
        """Build input CSS classes based on state and validation."""
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

    def _build_input_attrs(self) -> dict[str, Any]:
        """Build input element attributes."""
        attrs: dict[str, Any] = {
            "type": self.type,
            "id": self.id,
            "name": self.name or self.id,
        }

        if self.placeholder:
            attrs["placeholder"] = self.placeholder

        if self.value:
            attrs["value"] = self.value

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

        # Merge passthrough attributes
        if self.attrs:
            attrs.update(self.attrs)

        return attrs

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
