"""Pagination component for Flowbite."""

from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import urlencode

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


@dataclass(frozen=True, kw_only=True)
class HtmxPagination:
    """HTMX-enabled pagination component with filter preservation.

    Renders a pagination control bar with Previous/Next buttons, page info,
    page size selector, and HTMX attributes for SPA-like navigation.
    Preserves query parameters across page changes.

    Example:
        ```python
        HtmxPagination(
            current_page=2,
            total_pages=10,
            total_items=100,
            page_size=10,
            base_url="/api/v1/features",
            push_url="/features",
            hx_target="#features-container",
            query_params={"origin": "MACHINE"},
        )
        ```

    For search results mode:
        ```python
        HtmxPagination(
            current_page=1,
            total_pages=1,
            total_items=5,
            page_size=10,
            is_search=True,
            base_url="/api/v1/features",
            push_url="/features",
            hx_target="#features-container",
        )
        ```
    """

    # Required props
    current_page: int
    """Current page number (1-indexed)."""

    total_pages: int
    """Total number of pages."""

    total_items: int
    """Total number of items across all pages."""

    page_size: int
    """Number of items per page."""

    base_url: str
    """Base URL for API requests (e.g., '/api/v1/features')."""

    hx_target: str
    """HTMX target selector (e.g., '#features-container')."""

    # Optional configuration
    push_url: str | None = None
    """Base URL for browser history push (e.g., '/features'). If None, no push."""

    query_params: dict[str, Any] = field(default_factory=dict)
    """Additional query parameters to preserve across pages."""

    is_search: bool = False
    """Whether this is displaying search results (shows Clear Search button)."""

    on_after_request: str | None = None
    """JavaScript to run after HTMX request completes (hx-on::after-request)."""

    page_size_options: tuple[int, ...] = (10, 25, 50, 100)
    """Available page size options for the dropdown."""

    class_: str = ""
    """Additional CSS classes for the wrapper."""

    def htmy(self, context: Context) -> Component:
        """Render the pagination component."""
        if self.is_search:
            return self._render_search_footer()
        return self._render_pagination_footer()

    def _render_search_footer(self) -> Component:
        """Render search results footer with Clear Search button."""
        clear_url = self._build_api_url(1, exclude_filters=True)

        clear_attrs: dict[str, Any] = {
            "hx-get": clear_url,
            "hx-target": self.hx_target,
        }
        if self.push_url:
            clear_attrs["hx-push-url"] = self._build_push_url(1, exclude_filters=True)
        if self.on_after_request:
            clear_attrs["hx-on::after-request"] = self.on_after_request

        clear_icon = SafeStr(
            '<svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20" '
            'xmlns="http://www.w3.org/2000/svg">'
            '<path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293'
            "a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414"
            'l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" '
            'clip-rule="evenodd"></path></svg>'
        )

        clear_btn = html.button(
            clear_icon,
            "Clear Search",
            type="button",
            class_=(
                "inline-flex items-center text-white bg-gray-800 hover:bg-gray-900 "
                "focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm "
                "px-5 py-2.5 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800"
            ),
            **clear_attrs,
        )

        return html.div(
            # Left side: result count
            html.div(
                html.span(
                    "Found ",
                    html.span(
                        str(self.total_items),
                        class_="font-semibold text-gray-900 dark:text-white",
                    ),
                    " results",
                    class_="text-sm font-normal text-gray-500 dark:text-gray-400",
                ),
                class_="flex items-center mb-4 sm:mb-0",
            ),
            # Right side: Clear Search button
            html.div(clear_btn, class_="flex items-center space-x-3"),
            class_=self._wrapper_classes(),
        )

    def _render_pagination_footer(self) -> Component:
        """Render standard pagination footer with nav buttons and info."""
        return html.div(
            self._render_left_nav(),
            self._render_right_nav(),
            class_=self._wrapper_classes(),
        )

    def _wrapper_classes(self) -> str:
        """Build wrapper CSS classes."""
        base = (
            "sticky bottom-0 right-0 items-center w-full p-4 bg-white "
            "border-t border-gray-200 sm:flex sm:justify-between "
            "dark:bg-gray-800 dark:border-gray-700"
        )
        if self.class_:
            return f"{base} {self.class_}"
        return base

    def _render_left_nav(self) -> Component:
        """Render left navigation with icon buttons, page info, and size selector."""
        children: list[Component] = []

        if self.current_page > 1:
            children.append(self._render_nav_button("prev", icon_only=True))

        children.append(self._render_page_info())

        if self.current_page < self.total_pages:
            children.append(self._render_nav_button("next", icon_only=True))

        children.append(self._render_page_size_selector())

        return html.div(*children, class_="flex items-center mb-4 sm:mb-0 gap-4")

    def _render_right_nav(self) -> Component:
        """Render right navigation with text Previous/Next buttons."""
        children: list[Component] = []

        if self.current_page > 1:
            children.append(self._render_nav_button("prev", icon_only=False))

        if self.current_page < self.total_pages:
            children.append(self._render_nav_button("next", icon_only=False))

        return html.div(*children, class_="flex items-center space-x-3")

    def _render_page_info(self) -> Component:
        """Render 'Showing X-Y of Z' text."""
        start_item = (self.current_page - 1) * self.page_size + 1
        end_item = min(self.current_page * self.page_size, self.total_items)

        return html.span(
            "Showing ",
            html.span(
                f"{start_item}-{end_item}",
                class_="font-semibold text-gray-900 dark:text-white",
            ),
            " of ",
            html.span(
                str(self.total_items),
                class_="font-semibold text-gray-900 dark:text-white",
            ),
            class_="text-sm font-normal text-gray-500 dark:text-gray-400",
        )

    def _render_page_size_selector(self) -> Component:
        """Render a dropdown to change items per page."""
        filter_params = "&".join(
            f"{k}={v}" for k, v in self.query_params.items() if v is not None and v != ""
        )
        filter_suffix = f"&{filter_params}" if filter_params else ""

        push_js = ""
        if self.push_url:
            push_js = f", pushUrl:'{self.push_url}?page=1&size='+s+'{filter_suffix}'"

        onchange = (
            "var s=this.value;"
            f"htmx.ajax('GET', "
            f"'{self.base_url}?page=1&size='+s+'{filter_suffix}', "
            f"{{target:'{self.hx_target}'{push_js}}})"
        )

        options = [
            html.option(
                str(size),
                value=str(size),
                **({"selected": ""} if size == self.page_size else {}),
            )
            for size in self.page_size_options
        ]

        return html.div(
            html.select(
                *options,
                onchange=onchange,
                class_=(
                    "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                    "rounded-lg focus:ring-blue-500 focus:border-blue-500 "
                    "p-1.5 dark:bg-gray-700 dark:border-gray-600 "
                    "dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                ),
            ),
            html.span("/ page", class_="text-sm text-gray-500 dark:text-gray-400 ml-1"),
            class_="flex items-center",
        )

    def _render_nav_button(self, direction: str, *, icon_only: bool) -> Component:
        """Render a navigation button (icon-only or with text)."""
        is_prev = direction == "prev"
        target_page = self.current_page - 1 if is_prev else self.current_page + 1

        url = self._build_api_url(target_page)
        btn_attrs: dict[str, Any] = {
            "hx-get": url,
            "hx-target": self.hx_target,
        }
        if self.push_url:
            btn_attrs["hx-push-url"] = self._build_push_url(target_page)
        if self.on_after_request:
            btn_attrs["hx-on::after-request"] = self.on_after_request

        if icon_only:
            return self._render_icon_button(is_prev, btn_attrs)
        return self._render_text_button(is_prev, btn_attrs)

    def _render_icon_button(self, is_prev: bool, attrs: dict[str, Any]) -> Component:
        """Render an icon-only navigation button."""
        label = "Previous page" if is_prev else "Next page"

        if is_prev:
            icon = SafeStr(
                '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10'
                'l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" '
                'clip-rule="evenodd"></path></svg>'
            )
        else:
            icon = SafeStr(
                '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10'
                'L7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" '
                'clip-rule="evenodd"></path></svg>'
            )

        return html.button(
            icon,
            html.span(label, class_="sr-only"),
            type="button",
            class_=(
                "inline-flex items-center justify-center p-1 text-gray-500 "
                "rounded-lg hover:text-gray-900 hover:bg-gray-100 "
                "dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
            ),
            **attrs,
        )

    def _render_text_button(self, is_prev: bool, attrs: dict[str, Any]) -> Component:
        """Render a text navigation button with icon."""
        if is_prev:
            icon = SafeStr(
                '<svg class="w-5 h-5 mr-1 -ml-1" fill="currentColor" viewBox="0 0 20 20" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10'
                'l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" '
                'clip-rule="evenodd"></path></svg>'
            )
            label = "Previous"
        else:
            icon = SafeStr(
                '<svg class="w-5 h-5 ml-1 -mr-1" fill="currentColor" viewBox="0 0 20 20" '
                'xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10'
                'L7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" '
                'clip-rule="evenodd"></path></svg>'
            )
            label = "Next"

        btn_class = (
            "inline-flex items-center text-white bg-blue-700 hover:bg-blue-800 "
            "focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm "
            "px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        )

        if is_prev:
            return html.button(icon, label, type="button", class_=btn_class, **attrs)
        else:
            return html.button(label, icon, type="button", class_=btn_class, **attrs)

    def _build_api_url(self, page: int, exclude_filters: bool = False) -> str:
        """Build API URL with query parameters."""
        params: dict[str, Any] = {"page": page, "size": self.page_size}
        if not exclude_filters:
            for key, value in self.query_params.items():
                if value is not None and value != "":
                    params[key] = value
        return f"{self.base_url}?{urlencode(params)}"

    def _build_push_url(self, page: int, exclude_filters: bool = False) -> str:
        """Build browser history URL with query parameters."""
        base = self.push_url or self.base_url
        params: dict[str, Any] = {"page": page, "size": self.page_size}
        if not exclude_filters:
            for key, value in self.query_params.items():
                if value is not None and value != "":
                    params[key] = value
        return f"{base}?{urlencode(params)}"
