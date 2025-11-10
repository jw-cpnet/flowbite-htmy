"""Pagination showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/paginations.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components import Pagination

app = FastAPI(title="Flowbite-HTMY Pagination Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the pagination showcase page using Jinja layout + htmy components."""

    # Build comprehensive pagination showcase
    paginations_section = html.div(
        # Default pagination
        html.h2(
            "Default pagination",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use default pagination to navigate through multiple pages with Previous/Next buttons and page numbers.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=3,
                total_pages=5,
                base_url="/?page={page}",
            ),
            class_="mb-8",
        ),
        # Small size
        html.h2(
            "Small size",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the small size variant for compact pagination.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=2,
                total_pages=5,
                base_url="/?page={page}",
                size="sm",
            ),
            class_="mb-8",
        ),
        # Medium size
        html.h2(
            "Medium size",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the medium size variant for larger, more prominent pagination.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=2,
                total_pages=5,
                base_url="/?page={page}",
                size="md",
            ),
            class_="mb-8",
        ),
        # With icons
        html.h2(
            "With icons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Show arrow icons instead of text for Previous/Next buttons using the show_icons parameter.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=3,
                total_pages=5,
                base_url="/?page={page}",
                show_icons=True,
            ),
            class_="mb-8",
        ),
        # First page (Previous disabled)
        html.h2(
            "First page",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "On the first page, the Previous button is automatically disabled.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=1,
                total_pages=5,
                base_url="/?page={page}",
            ),
            class_="mb-8",
        ),
        # Last page (Next disabled)
        html.h2(
            "Last page",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "On the last page, the Next button is automatically disabled.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=5,
                total_pages=5,
                base_url="/?page={page}",
            ),
            class_="mb-8",
        ),
        # From total items
        html.h2(
            "Calculated from total items",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Automatically calculate total pages from total items and items per page.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=2,
                total_items=100,
                items_per_page=10,
                base_url="/products?page={page}",
            ),
            class_="mb-8",
        ),
        # With info text
        html.h2(
            "With info text",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Show information about the current range of items being displayed.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=3,
                total_items=100,
                items_per_page=10,
                base_url="/items?page={page}",
                show_info=True,
            ),
            class_="mb-8",
        ),
        # Many pages (limited display)
        html.h2(
            "Many pages",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "When there are many pages, only a limited range around the current page is shown.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=25,
                total_pages=100,
                base_url="/page={page}",
                max_visible_pages=7,
            ),
            class_="mb-8",
        ),
        # Near beginning with many pages
        html.h2(
            "Near beginning (many pages)",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Shows page 5 of 50, demonstrating how pagination adjusts when near the start.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=5,
                total_pages=50,
                base_url="/page={page}",
                max_visible_pages=7,
            ),
            class_="mb-8",
        ),
        # Near end with many pages
        html.h2(
            "Near end (many pages)",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Shows page 46 of 50, demonstrating how pagination adjusts when near the end.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=46,
                total_pages=50,
                base_url="/page={page}",
                max_visible_pages=7,
            ),
            class_="mb-8",
        ),
        # Custom labels
        html.h2(
            "Custom labels",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Customize the Previous and Next button labels for internationalization or different terminology.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=2,
                total_pages=5,
                base_url="/pagina={page}",
                prev_label="← Anterior",
                next_label="Siguiente →",
            ),
            class_="mb-8",
        ),
        # Table pagination with info
        html.h2(
            "Table pagination",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Common pattern for table data showing item range and navigation.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=1,
                total_items=100,
                items_per_page=10,
                base_url="/users?page={page}",
                show_info=True,
            ),
            class_="mb-8",
        ),
        # Single page
        html.h2(
            "Single page",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "When there's only one page, both Previous and Next are disabled.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=1,
                total_pages=1,
                base_url="/page={page}",
            ),
            class_="mb-8",
        ),
        # Complex URL
        html.h2(
            "Complex URL with query parameters",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Pagination works with complex URLs that include multiple query parameters.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Pagination(
                current_page=2,
                total_pages=10,
                base_url="/search?query=python&category=tutorials&page={page}&sort=date",
            ),
            class_="mb-8",
        ),
        class_="max-w-4xl mx-auto p-8",
    )

    return {
        "title": "Pagination Component Showcase - Flowbite HTMY",
        "content": await renderer.render(paginations_section),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
