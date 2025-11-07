"""Page layout component for complete HTML pages."""

from dataclasses import dataclass

from htmy import Component, ComponentType, Context, html

from flowbite_htmy import FLOWBITE_VERSION, HTMX_VERSION


@dataclass(frozen=True, kw_only=True)
class PageLayout:
    """Complete HTML page layout with all necessary dependencies.

    Provides a full HTML document structure with Tailwind CSS, Flowbite CSS,
    HTMX, and optional Flowbite JavaScript.

    Example:
        >>> PageLayout(
        ...     title="My App",
        ...     content=html.div("Page content"),
        ...     include_flowbite_js=False,
        ... )
    """

    title: str
    """Page title (appears in browser tab)."""

    content: ComponentType
    """Main page content."""

    include_flowbite_js: bool = False
    """Include Flowbite JavaScript for interactive components."""

    body_class: str = ""
    """Custom CSS classes for the body element."""

    lang: str = "en"
    """HTML document language."""

    def htmy(self, context: Context) -> Component:
        """Render the complete page layout.

        Args:
            context: Rendering context.

        Returns:
            Complete HTML document.
        """
        return (
            html.DOCTYPE.html,
            html.html(
                self._render_head(),  # type: ignore[arg-type]
                self._render_body(),  # type: ignore[arg-type]
                lang=self.lang,
            ),
        )

    def _render_head(self) -> Component:
        """Render the head section.

        Returns:
            Head element with meta tags and dependencies.
        """
        head_children: list[ComponentType] = [
            html.title(self.title),
            html.meta(charset="UTF-8"),
            html.meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0",
            ),
            # Tailwind CSS
            html.script(src="https://cdn.tailwindcss.com"),
            # Flowbite CSS
            html.link(
                rel="stylesheet",
                href=f"https://cdn.jsdelivr.net/npm/flowbite@{FLOWBITE_VERSION}/dist/flowbite.min.css",
            ),
            # HTMX
            html.script(src=f"https://unpkg.com/htmx.org@{HTMX_VERSION}"),
        ]

        # Optional Flowbite JS
        if self.include_flowbite_js:
            head_children.append(
                html.script(
                    src=f"https://cdn.jsdelivr.net/npm/flowbite@{FLOWBITE_VERSION}/dist/flowbite.min.js"
                )
            )

        return html.head(*head_children)

    def _render_body(self) -> Component:
        """Render the body section.

        Returns:
            Body element with content.
        """
        return html.body(self.content, class_=self.body_class if self.body_class else None)
