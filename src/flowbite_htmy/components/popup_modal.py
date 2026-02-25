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

    Example with explicit buttons:
        ```python
        PopupModal(
            id="confirm-delete",
            message="Are you sure you want to delete this product?",
            icon=SafeStr('<svg>...</svg>'),  # Warning icon
            confirm_button=Button(label="Yes, I'm sure", color=Color.RED),
            cancel_button=Button(label="No, cancel"),
            static_backdrop=True,
        )
        ```

    Example with convenience props (auto-generated buttons):
        ```python
        PopupModal(
            id="confirm-delete",
            message="Are you sure you want to delete this item?",
            confirm_url="/api/v1/items/123",
            confirm_method="delete",
            confirm_target="#items-container",
            danger=True,
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

    # Explicit button props (takes precedence over convenience props)
    confirm_button: Component | None = None
    """Primary action button (usually Button component). Overrides convenience props."""

    cancel_button: Component | None = None
    """Secondary/cancel button (usually Button component)."""

    # Convenience props for auto-generated buttons
    confirm_url: str | None = None
    """HTMX action URL for confirm button (used with confirm_method)."""

    confirm_method: str = "delete"
    """HTTP method for confirm action (delete, post, put)."""

    confirm_target: str | None = None
    """HTMX target for confirm action response."""

    confirm_label: str = "Yes, I'm sure"
    """Label for the auto-generated confirm button."""

    cancel_label: str = "No, cancel"
    """Label for the auto-generated cancel button."""

    danger: bool = True
    """Whether to style the confirm button as danger (red). Only for auto-generated buttons."""

    # Optional props
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

        # Resolve buttons (explicit props take precedence)
        confirm_btn = self.confirm_button or self._build_confirm_button()
        cancel_btn = self.cancel_button or self._build_cancel_button()

        # Build buttons list
        buttons: list[Component] = [confirm_btn]
        if cancel_btn:
            buttons.append(cancel_btn)

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

    def _build_confirm_button(self) -> Component:
        """Build auto-generated confirm button from convenience props."""
        if self.danger:
            btn_class = (
                "text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none "
                "focus:ring-red-300 font-medium rounded-lg text-sm inline-flex items-center "
                "px-5 py-2.5 text-center dark:focus:ring-red-800"
            )
        else:
            btn_class = (
                "text-white bg-primary-600 hover:bg-primary-800 focus:ring-4 focus:outline-none "
                "focus:ring-primary-300 font-medium rounded-lg text-sm inline-flex items-center "
                "px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 "
                "dark:focus:ring-primary-800"
            )

        btn_attrs: dict[str, Any] = {}
        if self.confirm_url:
            hx_attr = f"hx-{self.confirm_method}"
            btn_attrs[hx_attr] = self.confirm_url
            if self.confirm_target:
                btn_attrs["hx-target"] = self.confirm_target

        return html.button(
            self.confirm_label,
            type="button",
            class_=btn_class,
            **btn_attrs,
        )

    def _build_cancel_button(self) -> Component:
        """Build auto-generated cancel button."""
        return html.button(
            self.cancel_label,
            type="button",
            class_=(
                "py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none "
                "bg-white rounded-lg border border-gray-200 hover:bg-gray-100 "
                "hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 "
                "dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 "
                "dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
            ),
            **{"data-modal-hide": self.id},
        )

    def _render_close_button(self, classes: str) -> Component:
        """Render the close button with SVG icon."""
        # SVG close icon - using SafeStr for proper rendering
        svg_icon = SafeStr(
            '<svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" '
            'fill="none" viewBox="0 0 14 14">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>'
            "</svg>"
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
