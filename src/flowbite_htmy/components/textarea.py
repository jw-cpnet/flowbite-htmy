"""Textarea component for Flowbite."""

from dataclasses import dataclass
from typing import Any, Literal

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext

# Validation state type (reuse from Input component pattern)
ValidationState = Literal["success", "error"] | None


@dataclass(frozen=True, kw_only=True)
class Textarea:
    """Multi-line text input component with Flowbite styling.

    Provides a textarea element with label, validation states, helper text,
    and dark mode support following the established Input component pattern.

    Example:
        Basic usage:
        ```python
        Textarea(
            id="comment",
            label="Your comment",
            placeholder="Write your thoughts here...",
        )
        ```

        With validation:
        ```python
        Textarea(
            id="feedback",
            label="Feedback",
            validation="error",
            helper_text="Feedback must be at least 10 characters",
        )
        ```

        Edit form with pre-filled value:
        ```python
        Textarea(
            id="bio",
            label="Biography",
            value="Previously saved bio text...",
            rows=6,
        )
        ```

        Required field:
        ```python
        Textarea(
            id="description",
            label="Description",  # Will display as "Description *"
            required=True,
        )
        ```
    """

    # Required props
    id: str
    """Unique ID for the textarea (used for label association)."""

    label: str
    """Label text displayed above the textarea."""

    # Optional props
    placeholder: str | None = None
    """Placeholder text shown when textarea is empty."""

    value: str | None = None
    """Initial value for the textarea (pre-filled content)."""

    rows: int = 4
    """Number of visible text lines (default: 4)."""

    validation: ValidationState = None
    """Validation state: 'success', 'error', or None."""

    helper_text: str | None = None
    """Helper text displayed below the textarea."""

    class_: str = ""
    """Additional CSS classes for the wrapper div."""

    name: str | None = None
    """Name attribute for form submission (optional)."""

    required: bool = False
    """Whether the textarea is required."""

    disabled: bool = False
    """Whether the textarea is disabled."""

    readonly: bool = False
    """Whether the textarea is readonly (disabled takes precedence)."""

    attrs: dict[str, Any] | None = None
    """Additional HTML attributes for the textarea element."""

    # HTMX attributes
    hx_get: str | None = None
    """HTMX GET request URL."""

    hx_post: str | None = None
    """HTMX POST request URL."""

    hx_put: str | None = None
    """HTMX PUT request URL."""

    hx_patch: str | None = None
    """HTMX PATCH request URL."""

    hx_delete: str | None = None
    """HTMX DELETE request URL."""

    hx_target: str | None = None
    """HTMX target element selector."""

    hx_swap: str | None = None
    """HTMX swap strategy."""

    hx_trigger: str | None = None
    """HTMX trigger event."""

    def htmy(self, context: Context) -> Component:
        """Render the textarea component.

        Returns:
            Component tree: div > label + textarea
        """
        theme = ThemeContext.from_context(context)

        # Build classes
        label_classes = self._build_label_classes()
        textarea_classes = self._build_textarea_classes(theme)

        # Build textarea attributes
        textarea_attrs = self._build_textarea_attrs()

        # Get label with required indicator
        display_label = self._get_display_label()

        # Build components
        content: list[Component] = [
            html.label(
                display_label,
                **{"for": self.id},
                class_=label_classes,
            ),
            html.textarea(
                self.value or "",  # Textarea content (empty string if None)
                **textarea_attrs,
                class_=textarea_classes,
            ),
        ]

        # Add helper text if provided
        if self.helper_text:
            content.append(self._render_helper_text())

        return html.div(*content, class_=self.class_)  # type: ignore[arg-type]

    def _get_display_label(self) -> str:
        """Get label text with asterisk if required.

        Returns:
            Label text with " *" appended if required=True.
        """
        if self.required:
            return f"{self.label} *"
        return self.label

    def _build_label_classes(self) -> str:
        """Build label CSS classes based on validation state.

        Returns:
            Space-separated CSS classes for the label element.
        """
        builder = ClassBuilder("block mb-2 text-sm font-medium")

        if self.validation == "success":
            builder.add("text-green-700 dark:text-green-500")
        elif self.validation == "error":
            builder.add("text-red-700 dark:text-red-500")
        else:
            builder.add("text-gray-900 dark:text-white")

        return builder.build()

    def _build_textarea_classes(self, theme: ThemeContext) -> str:
        """Build textarea CSS classes based on state and validation.

        Args:
            theme: ThemeContext for consistency with pattern.

        Returns:
            Space-separated CSS classes for the textarea element.
        """
        builder = ClassBuilder()

        # Base classes (layout, typography, shape)
        builder.add("block p-2.5 w-full text-sm rounded-lg border")

        # Focus ring (always blue)
        builder.add("focus:ring-blue-500 focus:border-blue-500")
        builder.add("dark:focus:ring-blue-500 dark:focus:border-blue-500")

        # Disabled state overrides everything
        if self.disabled:
            builder.add("cursor-not-allowed bg-gray-100 dark:bg-gray-700")
            builder.add("text-gray-500 dark:text-gray-400")
            # Skip validation styling for disabled fields
            return builder.build()

        # Validation-specific classes (only if not disabled)
        if self.validation == "success":
            builder.add("bg-green-50 border-green-500")
            builder.add("text-green-900 dark:text-green-400")
            builder.add("placeholder-green-700 dark:placeholder-green-500")
            builder.add("dark:border-green-500")
        elif self.validation == "error":
            builder.add("bg-red-50 border-red-500")
            builder.add("text-red-900 placeholder-red-700")
            builder.add("dark:text-red-500 dark:placeholder-red-500")
            builder.add("dark:border-red-500")
        else:
            # Default state colors
            builder.add("bg-gray-50 text-gray-900 border-gray-300")
            builder.add("dark:bg-gray-700 dark:border-gray-600")
            builder.add("dark:placeholder-gray-400 dark:text-white")

        return builder.build()

    def _build_textarea_attrs(self) -> dict[str, Any]:
        """Build textarea element HTML attributes.

        Returns:
            Dictionary of HTML attributes for the textarea element.
        """
        # Clamp rows to minimum of 1
        effective_rows = max(1, self.rows)

        attrs: dict[str, Any] = {
            "id": self.id,
            "rows": effective_rows,
        }

        # Optional standard attributes
        if self.name:
            attrs["name"] = self.name

        if self.placeholder:
            attrs["placeholder"] = self.placeholder

        if self.required:
            attrs["required"] = ""

        # Disabled takes precedence over readonly
        if self.disabled:
            attrs["disabled"] = ""
        elif self.readonly:
            attrs["readonly"] = ""

        # ARIA for helper text
        if self.helper_text:
            attrs["aria_describedby"] = f"{self.id}-helper"

        # HTMX attributes
        if self.hx_get:
            attrs["hx_get"] = self.hx_get
        if self.hx_post:
            attrs["hx_post"] = self.hx_post
        if self.hx_put:
            attrs["hx_put"] = self.hx_put
        if self.hx_patch:
            attrs["hx_patch"] = self.hx_patch
        if self.hx_delete:
            attrs["hx_delete"] = self.hx_delete
        if self.hx_target:
            attrs["hx_target"] = self.hx_target
        if self.hx_swap:
            attrs["hx_swap"] = self.hx_swap
        if self.hx_trigger:
            attrs["hx_trigger"] = self.hx_trigger

        # Merge passthrough attributes (last, so they can override)
        if self.attrs:
            attrs.update(self.attrs)

        return attrs

    def _render_helper_text(self) -> Component:
        """Render helper text with validation-appropriate styling.

        Returns:
            HTML paragraph element with helper text.
        """
        text_classes = "mt-2 text-sm"

        if self.validation == "success":
            text_classes += " text-green-600 dark:text-green-500"
        elif self.validation == "error":
            text_classes += " text-red-600 dark:text-red-500"
        else:
            text_classes += " text-gray-500 dark:text-gray-400"

        return html.p(
            self.helper_text,  # type: ignore[arg-type]
            id=f"{self.id}-helper",
            class_=text_classes,
        )
