"""Example FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/basic_app.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components import Button
from flowbite_htmy.types import Color

app = FastAPI(title="Flowbite-HTMY Button Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the button showcase page using Jinja layout + htmy components."""

    # Build button components using htmy (type-safe!)
    buttons_section = html.div(
        html.h2(
            "Default buttons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use these default button styles with multiple colors to indicate an action or link within your website.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),

        # Default button color variants (matching Flowbite order)
        html.div(
            Button(label="Default", color=Color.PRIMARY),
            Button(label="Alternative", color=Color.SECONDARY),
            Button(label="Dark", color=Color.DARK),
            Button(label="Light", color=Color.LIGHT),
            Button(label="Green", color=Color.GREEN),
            Button(label="Red", color=Color.RED),
            Button(label="Yellow", color=Color.YELLOW),
            Button(label="Purple", color=Color.PURPLE),
            class_="flex flex-wrap gap-2 mb-8",
        ),

        # HTMX example
        html.div(
            html.h3(
                "Interactive HTMX Button",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-3",
            ),
            html.p(
                "Click the button below to see server-side rendering with HTMX:",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Button(
                label="Click Me!",
                color=Color.INFO,
                hx_get="/clicked",
                hx_target="#result",
                hx_swap="innerHTML",
            ),
            html.div(
                html.p(
                    "Waiting for button click...",
                    class_="text-gray-500 dark:text-gray-400 italic",
                ),
                id="result",
                class_="mt-4 p-4 rounded-lg bg-gray-100 dark:bg-gray-800",
            ),
        ),

        class_="mb-8",
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(buttons_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Button Showcase",
        "subtitle": "Hybrid approach: Jinja layouts + htmy components",
        "content": content_html,
    }


@app.get("/clicked")
async def clicked() -> str:
    """HTMX endpoint - returns rendered htmy component."""
    from flowbite_htmy.components import Alert

    alert = Alert(
        title="Success!",
        message="Button clicked! This Alert component was rendered server-side with htmy and returned via HTMX.",
        color=Color.SUCCESS,
    )

    # Return raw HTML (fasthx handles HTMLResponse automatically for HTMX requests)
    return await renderer.render(alert)


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Hybrid Example")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("basic_app:app", host="0.0.0.0", port=8000, reload=True)
