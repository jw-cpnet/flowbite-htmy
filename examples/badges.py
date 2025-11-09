"""Badge showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/badges.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components import Badge
from flowbite_htmy.types import Color

app = FastAPI(title="Flowbite-HTMY Badge Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the badge showcase page using Jinja layout + htmy components."""

    # Build comprehensive badge showcase
    badges_section = html.div(
        # Default badges
        html.h2(
            "Default badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the following badge elements to indicate counts or labels inside or outside components.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE),
            Badge(label="Dark", color=Color.GRAY),
            Badge(label="Red", color=Color.RED),
            Badge(label="Green", color=Color.GREEN),
            Badge(label="Yellow", color=Color.YELLOW),
            Badge(label="Indigo", color=Color.INDIGO),
            Badge(label="Purple", color=Color.PURPLE),
            Badge(label="Pink", color=Color.PINK),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Large badges
        html.h2(
            "Large badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the large prop for bigger badge variants.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, large=True),
            Badge(label="Dark", color=Color.GRAY, large=True),
            Badge(label="Red", color=Color.RED, large=True),
            Badge(label="Green", color=Color.GREEN, large=True),
            Badge(label="Yellow", color=Color.YELLOW, large=True),
            Badge(label="Indigo", color=Color.INDIGO, large=True),
            Badge(label="Purple", color=Color.PURPLE, large=True),
            Badge(label="Pink", color=Color.PINK, large=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Badge pills
        html.h2(
            "Badge pills",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the rounded prop for fully rounded, pill-shaped badges.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, rounded=True),
            Badge(label="Dark", color=Color.GRAY, rounded=True),
            Badge(label="Red", color=Color.RED, rounded=True),
            Badge(label="Green", color=Color.GREEN, rounded=True),
            Badge(label="Yellow", color=Color.YELLOW, rounded=True),
            Badge(label="Indigo", color=Color.INDIGO, rounded=True),
            Badge(label="Purple", color=Color.PURPLE, rounded=True),
            Badge(label="Pink", color=Color.PINK, rounded=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Bordered badges
        html.h2(
            "Bordered badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the border prop for outlined badge styles with transparent backgrounds in dark mode.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, border=True),
            Badge(label="Dark", color=Color.GRAY, border=True),
            Badge(label="Red", color=Color.RED, border=True),
            Badge(label="Green", color=Color.GREEN, border=True),
            Badge(label="Yellow", color=Color.YELLOW, border=True),
            Badge(label="Indigo", color=Color.INDIGO, border=True),
            Badge(label="Purple", color=Color.PURPLE, border=True),
            Badge(label="Pink", color=Color.PINK, border=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(badges_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Badge Showcase",
        "subtitle": "Comprehensive badge variants - all Flowbite styles supported",
        "content": content_html,
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Badge Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("badges:app", host="0.0.0.0", port=8000, reload=True)
