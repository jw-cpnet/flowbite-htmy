"""PopupModal component for confirmations and alerts."""

from dataclasses import dataclass
from typing import Any

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext


@dataclass(frozen=True, kw_only=True)
class PopupModal:
    """Popup modal for confirmations, alerts, and destructive actions.

    Unlike the standard Modal component, PopupModal has:
    - Centered content layout (no header/footer borders)
    - Close button positioned absolutely at top-right
    - Icon support for warnings, success, errors
    - Inline action buttons (not in separate footer)

    Perfect for:
    - Confirmation dialogs ("Are you sure?")
    - Destructive actions (delete, remove, etc.)
    - Alerts and notifications
    - Simple yes/no decisions

    Example:
        ```python
        PopupModal(
            id="confirm-delete",
            message="Are you sure you want to delete this product?",
            icon=SafeStr('<svg>...</svg>'),  # Warning icon
            confirm_button=Button(label="Yes, I'm sure", color=Color.RED),
            cancel_button=Button(label="No, cancel"),
            static_backdrop=True,  # Prevent closing on backdrop click
        )
        ```

    Toggle button example:
        ```python
        Button(
            label="Delete",
            color=Color.RED,
            attrs={"data-modal-toggle": "confirm-delete"},
        )
        ```
    """

    # Required props
    id: str
    """Unique ID for the modal (used with data-modal-toggle/show/hide)."""

    message: str
    """Main message/question to display (centered)."""

    confirm_button: Component
    """Primary action button (usually Button component)."""

    # Optional props
    cancel_button: Component | None = None
    """Secondary/cancel button (usually Button component)."""

    icon: SafeStr | None = None
    """Optional icon to display above the message (warning, success, error, etc.)."""

    static_backdrop: bool = False
    """If True, prevents closing modal by clicking outside (backdrop click)."""

    class_: str = ""
    """Additional CSS classes for the modal container."""

    attrs: dict[str, Any] | None = None
    """Additional HTML attributes for the modal container."""

    def htmy(self, context: Context) -> Component:
        """Render the popup modal component."""
        theme = ThemeContext.from_context(context)
        container_classes = self._build_container_classes(theme)
        content_wrapper_classes = self._build_content_wrapper_classes(theme)
        close_button_classes = self._build_close_button_classes(theme)

        # Build attributes dict
        modal_attrs: dict[str, Any] = {
            "id": self.id,
            "tabindex": "-1",
            "aria-hidden": "true",
            "class": container_classes,
        }

        # Add static backdrop attribute if enabled
        if self.static_backdrop:
            modal_attrs["data-modal-backdrop"] = "static"

        # Merge passthrough attributes
        if self.attrs:
            modal_attrs.update(self.attrs)

        # Build buttons list
        buttons = [self.confirm_button]
        if self.cancel_button:
            buttons.append(self.cancel_button)

        # Build centered content items (filter out None)
        content_items: list[Component] = []
        if self.icon:
            content_items.append(self.icon)
        content_items.append(
            html.h3(
                self.message,
                class_="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400",
            )
        )
        content_items.append(
            html.div(
                *buttons,  # type: ignore[arg-type]
                class_="inline-flex items-center",
            )
        )

        # Build popup structure
        return html.div(
            html.div(
                html.div(
                    # Close button (absolutely positioned)
                    self._render_close_button(close_button_classes),  # type: ignore[arg-type]
                    # Centered content
                    html.div(
                        *content_items,  # type: ignore[arg-type]
                        class_="p-4 md:p-5 text-center",
                    ),
                    class_=content_wrapper_classes,
                ),
                class_="relative p-4 w-full max-w-md max-h-full",
            ),
            **modal_attrs,
        )

    def _render_close_button(self, classes: str) -> Component:
        """Render the close button with SVG icon."""
        # SVG close icon - using SafeStr for proper rendering
        svg_icon = SafeStr(
            '<svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" '
            'fill="none" viewBox="0 0 14 14">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>'
            '</svg>'
        )

        return html.button(
            svg_icon,
            html.span("Close modal", class_="sr-only"),
            type="button",
            class_=classes,
            **{"data-modal-hide": self.id},
        )

    def _build_container_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal container (outer fixed overlay)."""
        builder = ClassBuilder(
            "hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 "
            "justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
        )
        return builder.merge(self.class_)

    def _build_content_wrapper_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal content wrapper."""
        return "relative bg-white rounded-lg shadow-sm dark:bg-gray-700"

    def _build_close_button_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for close button (absolutely positioned)."""
        return (
            "absolute top-3 end-2.5 text-gray-400 bg-transparent "
            "hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 "
            "ms-auto inline-flex justify-center items-center "
            "dark:hover:bg-gray-600 dark:hover:text-white"
        )
