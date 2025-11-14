"""Modal component for Flowbite."""

from dataclasses import dataclass
from typing import Any

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import Size

# Size to max-width mapping
SIZE_CLASSES = {
    Size.SM: "max-w-md",
    Size.MD: "max-w-2xl",
    Size.LG: "max-w-4xl",
    Size.XL: "max-w-5xl",
    Size.XXL: "max-w-7xl",
}


@dataclass(frozen=True, kw_only=True)
class Modal:
    """Modal dialog component.

    A modal component for displaying content in a dialog overlay. Requires Flowbite JS
    for interactive functionality (toggle, show, hide).

    Example:
        ```python
        Modal(
            id="my-modal",
            title="Confirm Action",
            children=SafeStr("<p>Are you sure?</p>"),
            footer=SafeStr('<button data-modal-hide="my-modal">Cancel</button>'),
            static_backdrop=True,
        )
        ```

    Toggle button example:
        ```python
        Button(
            label="Open Modal",
            attrs={"data-modal-toggle": "my-modal"},
        )
        ```
    """

    # Required props
    id: str
    """Unique ID for the modal (used with data-modal-toggle/show/hide)."""

    title: str
    """Modal header title."""

    children: SafeStr | Component
    """Modal body content."""

    # Optional props
    footer: SafeStr | Component | None = None
    """Optional footer content (buttons, actions, etc.)."""

    size: Size = Size.MD
    """Modal width size variant."""

    static_backdrop: bool = False
    """If True, prevents closing modal by clicking outside (backdrop click)."""

    class_: str = ""
    """Additional CSS classes for the modal container."""

    attrs: dict[str, Any] | None = None
    """Additional HTML attributes for the modal container."""

    def htmy(self, context: Context) -> Component:
        """Render the modal component."""
        theme = ThemeContext.from_context(context)
        container_classes = self._build_container_classes(theme)
        content_classes = self._build_content_classes(theme)
        header_classes = self._build_header_classes(theme)
        body_classes = self._build_body_classes(theme)
        footer_classes = self._build_footer_classes(theme)

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

        # Build content sections
        content_sections: list[Component] = [
            # Header
            html.div(
                html.h3(self.title),
                self._render_close_button(),  # type: ignore[arg-type]
                class_=header_classes,
            ),
            # Body with wrapper div for padding and spacing
            html.div(self.children, class_=body_classes),  # type: ignore[arg-type]
        ]

        # Add footer if provided
        if self.footer:
            content_sections.append(html.div(self.footer, class_=footer_classes))  # type: ignore[arg-type]

        # Build modal structure
        return html.div(
            html.div(
                html.div(
                    *content_sections,  # type: ignore[arg-type]
                    class_=content_classes,
                ),
                class_=f"relative p-4 w-full {SIZE_CLASSES[self.size]} max-h-full",
            ),
            **modal_attrs,
        )

    def _render_close_button(self) -> Component:
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
            class_=(
                "text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 "
                "rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center "
                "dark:hover:bg-gray-600 dark:hover:text-white"
            ),
            **{"data-modal-hide": self.id},
        )

    def _build_container_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal container (outer fixed overlay)."""
        builder = ClassBuilder(
            "hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 "
            "justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
        )
        return builder.merge(self.class_)

    def _build_content_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal content wrapper."""
        return "relative bg-white rounded-lg shadow-sm dark:bg-gray-700"

    def _build_header_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal header."""
        return (
            "flex items-center justify-between p-4 md:p-5 border-b rounded-t "
            "dark:border-gray-600 border-gray-200 text-xl font-semibold "
            "text-gray-900 dark:text-white"
        )

    def _build_body_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal body."""
        return "p-4 md:p-5 space-y-4"

    def _build_footer_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for modal footer."""
        return (
            "flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600"
        )
