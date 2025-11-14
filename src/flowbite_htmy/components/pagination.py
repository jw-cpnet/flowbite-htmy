"""Pagination component for Flowbite."""

from dataclasses import dataclass
from typing import Literal

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext

# Size variants
SizeVariant = Literal["sm", "md"]


@dataclass(frozen=True, kw_only=True)
class Pagination:
    """Pagination component for navigating through pages of content.

    Automatically calculates page ranges and generates navigation links.
    Supports showing info text like "Showing 1 to 10 of 100 Entries".

    Example:
        ```python
        # Basic pagination with page numbers
        Pagination(
            current_page=3,
            total_pages=10,
            base_url="/products?page={page}",
        )

        # Pagination from total items
        Pagination(
            current_page=2,
            total_items=100,
            items_per_page=10,
            base_url="/posts?page={page}",
            show_info=True,
        )

        # Pagination with icons
        Pagination(
            current_page=5,
            total_pages=20,
            base_url="/page={page}",
            show_icons=True,
            max_visible_pages=7,
        )
        ```
    """

    # Required props
    current_page: int
    """Current active page number (1-indexed)."""

    base_url: str
    """URL pattern with {page} placeholder (e.g., '/products?page={page}')."""

    # Optional props - specify either total_pages OR (total_items + items_per_page)
    total_pages: int | None = None
    """Total number of pages. If not provided, calculated from total_items."""

    total_items: int | None = None
    """Total number of items (used to calculate total_pages)."""

    items_per_page: int = 10
    """Items per page (used with total_items to calculate total_pages)."""

    # Display options
    show_info: bool = False
    """Whether to show 'Showing X to Y of Z Entries' text."""

    show_icons: bool = False
    """Whether to show icons in Previous/Next buttons."""

    max_visible_pages: int = 7
    """Maximum number of page links to show (prevents overflow)."""

    prev_label: str = "Previous"
    """Label for the Previous button."""

    next_label: str = "Next"
    """Label for the Next button."""

    size: SizeVariant = "sm"
    """Size variant: 'sm' or 'md'."""

    class_: str = ""
    """Additional CSS classes for the pagination wrapper."""

    def htmy(self, context: Context) -> Component:
        """Render the pagination component."""
        theme = ThemeContext.from_context(context)

        # Calculate total pages if needed
        total_pages = self._calculate_total_pages()

        # Build info text if requested
        info_text = None
        if self.show_info and self.total_items:
            info_text = self._render_info_text()

        # Build pagination navigation
        nav = self._render_navigation(total_pages, theme)

        # Wrap in container
        if info_text:
            return html.div(
                info_text,  # type: ignore[arg-type]
                nav,  # type: ignore[arg-type]
                class_=f"flex flex-col items-center {self.class_}",
            )
        else:
            return html.div(nav, class_=self.class_)  # type: ignore[arg-type]

    def _calculate_total_pages(self) -> int:
        """Calculate total pages from total_items or use provided total_pages."""
        if self.total_pages is not None:
            return self.total_pages

        if self.total_items is not None:
            # Calculate pages from total items
            return max(1, (self.total_items + self.items_per_page - 1) // self.items_per_page)

        # Default to 1 page if nothing specified
        return 1

    def _render_info_text(self) -> Component:
        """Render the 'Showing X to Y of Z Entries' text."""
        if not self.total_items:
            return html.span()

        # Calculate start and end items for current page
        start_item = (self.current_page - 1) * self.items_per_page + 1
        end_item = min(self.current_page * self.items_per_page, self.total_items)

        return html.span(
            "Showing ",
            html.span(str(start_item), class_="font-semibold text-gray-900 dark:text-white"),
            " to ",
            html.span(str(end_item), class_="font-semibold text-gray-900 dark:text-white"),
            " of ",
            html.span(str(self.total_items), class_="font-semibold text-gray-900 dark:text-white"),
            " Entries",
            class_="text-sm text-gray-700 dark:text-gray-400",
        )

    def _render_navigation(self, total_pages: int, theme: ThemeContext) -> Component:
        """Render the main pagination navigation."""
        # Size-specific classes
        height_class = "h-8" if self.size == "sm" else "h-10"
        text_class = "text-sm" if self.size == "sm" else "text-base"
        padding_class = "px-3" if self.size == "sm" else "px-4"

        # Build page items
        items: list[Component] = []

        # Previous button
        items.append(self._render_prev_button(height_class, text_class, padding_class))

        # Page number links
        page_numbers = self._calculate_visible_pages(total_pages)
        for page_num in page_numbers:
            items.append(self._render_page_link(page_num, height_class, text_class, padding_class))

        # Next button
        items.append(self._render_next_button(total_pages, height_class, text_class, padding_class))

        return html.nav(
            html.ul(
                *items,  # type: ignore[arg-type]
                class_=f"inline-flex -space-x-px {text_class}",
            ),
            **{"aria-label": "Page navigation"},
        )

    def _render_prev_button(
        self, height_class: str, text_class: str, padding_class: str
    ) -> Component:
        """Render the Previous button."""
        is_disabled = self.current_page <= 1

        # Build classes
        builder = ClassBuilder(
            f"flex items-center justify-center {padding_class} {height_class} ms-0"
        )
        builder.add("leading-tight rounded-s-lg")

        if is_disabled:
            builder.add("cursor-not-allowed opacity-50")
            builder.add("text-gray-400 bg-gray-200 border border-e-0 border-gray-300")
            builder.add("dark:bg-gray-700 dark:border-gray-600 dark:text-gray-500")
        else:
            builder.add("text-gray-500 bg-white border border-e-0 border-gray-300")
            builder.add("hover:bg-gray-100 hover:text-gray-700")
            builder.add("dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400")
            builder.add("dark:hover:bg-gray-700 dark:hover:text-white")

        # Build content
        content = self._render_prev_icon() if self.show_icons else self.prev_label

        if is_disabled:
            return html.span(content, class_=builder.build())  # type: ignore[arg-type]
        else:
            prev_page = self.current_page - 1
            url = self.base_url.format(page=prev_page)
            return html.li(
                html.a(content, href=url, class_=builder.build())  # type: ignore[arg-type]
            )

    def _render_next_button(
        self, total_pages: int, height_class: str, text_class: str, padding_class: str
    ) -> Component:
        """Render the Next button."""
        is_disabled = self.current_page >= total_pages

        # Build classes
        builder = ClassBuilder(f"flex items-center justify-center {padding_class} {height_class}")
        builder.add("leading-tight rounded-e-lg")

        if is_disabled:
            builder.add("cursor-not-allowed opacity-50")
            builder.add("text-gray-400 bg-gray-200 border border-gray-300")
            builder.add("dark:bg-gray-700 dark:border-gray-600 dark:text-gray-500")
        else:
            builder.add("text-gray-500 bg-white border border-gray-300")
            builder.add("hover:bg-gray-100 hover:text-gray-700")
            builder.add("dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400")
            builder.add("dark:hover:bg-gray-700 dark:hover:text-white")

        # Build content
        content = self._render_next_icon() if self.show_icons else self.next_label

        if is_disabled:
            return html.span(content, class_=builder.build())  # type: ignore[arg-type]
        else:
            next_page = self.current_page + 1
            url = self.base_url.format(page=next_page)
            return html.li(
                html.a(content, href=url, class_=builder.build())  # type: ignore[arg-type]
            )

    def _render_page_link(
        self, page_num: int, height_class: str, text_class: str, padding_class: str
    ) -> Component:
        """Render a single page number link."""
        is_current = page_num == self.current_page

        # Build classes
        builder = ClassBuilder(
            f"flex items-center justify-center {padding_class} {height_class} leading-tight"
        )

        if is_current:
            builder.add("text-blue-600 border border-gray-300 bg-blue-50")
            builder.add("hover:bg-blue-100 hover:text-blue-700")
            builder.add("dark:border-gray-700 dark:bg-gray-700 dark:text-white")
        else:
            builder.add("text-gray-500 bg-white border border-gray-300")
            builder.add("hover:bg-gray-100 hover:text-gray-700")
            builder.add("dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400")
            builder.add("dark:hover:bg-gray-700 dark:hover:text-white")

        url = self.base_url.format(page=page_num)

        if is_current:
            return html.li(
                html.a(
                    str(page_num),
                    href=url,
                    **{"aria-current": "page"},
                    class_=builder.build(),
                )
            )
        else:
            return html.li(html.a(str(page_num), href=url, class_=builder.build()))

    def _calculate_visible_pages(self, total_pages: int) -> list[int]:
        """Calculate which page numbers to show based on max_visible_pages."""
        if total_pages <= self.max_visible_pages:
            # Show all pages if total is less than max
            return list(range(1, total_pages + 1))

        # Calculate range around current page
        half_visible = self.max_visible_pages // 2

        # Start and end of visible range
        start = max(1, self.current_page - half_visible)
        end = min(total_pages, self.current_page + half_visible)

        # Adjust if we're near the beginning or end
        if end - start + 1 < self.max_visible_pages:
            if start == 1:
                end = min(total_pages, self.max_visible_pages)
            else:
                start = max(1, total_pages - self.max_visible_pages + 1)

        return list(range(start, end + 1))

    def _render_prev_icon(self) -> Component:
        """Render the Previous arrow icon with sr-only text."""
        icon_svg = SafeStr(
            '<svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" '
            'xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-width="2" d="M5 1 1 5l4 4"/></svg>'
        )
        return html.span(
            html.span(self.prev_label, class_="sr-only"),
            icon_svg,
        )

    def _render_next_icon(self) -> Component:
        """Render the Next arrow icon with sr-only text."""
        icon_svg = SafeStr(
            '<svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" '
            'xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">'
            '<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-width="2" d="m1 9 4-4-4-4"/></svg>'
        )
        return html.span(
            self.next_label,
            icon_svg,
            class_="sr-only" if self.show_icons else "",
        )
