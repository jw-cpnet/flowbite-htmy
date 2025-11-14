"""Consolidated component showcase FastAPI application.

This application consolidates all 10 standalone component showcases into a single
multi-page application with persistent sidebar navigation.

Architecture:
- Jinja templates for page layout with sidebar navigation
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems
- Existing showcase functions imported from standalone apps

Run with: python examples/showcase.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Component, Renderer, html

# Import showcase functions from standalone apps
from alerts import build_alerts_showcase
from avatars import build_avatars_showcase
from badges import build_badges_showcase
from buttons import build_buttons_showcase
from cards import build_cards_showcase
from checkboxes import build_checkboxes_showcase
from inputs import build_inputs_showcase
from modals import build_modals_showcase
from paginations import build_paginations_showcase
from radios import build_radios_showcase
from selects import build_selects_showcase
from textareas import build_textareas_showcase
from showcase_types import ComponentRoute, PageContext
from flowbite_htmy.components import Button
from flowbite_htmy.types import ButtonVariant, Color

app = FastAPI(title="Flowbite-HTMY Component Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()

# Component routes configuration
COMPONENT_ROUTES: list[ComponentRoute] = [
    {
        "name": "buttons",
        "path": "/buttons",
        "title": "Buttons",
        "description": "Interactive buttons with colors, sizes, variants, and icons",
        "order": 1,
    },
    {
        "name": "badges",
        "path": "/badges",
        "title": "Badges",
        "description": "Labels and indicators with color variants",
        "order": 2,
    },
    {
        "name": "alerts",
        "path": "/alerts",
        "title": "Alerts",
        "description": "Notification messages with dismissible option",
        "order": 3,
    },
    {
        "name": "avatars",
        "path": "/avatars",
        "title": "Avatars",
        "description": "User profile pictures with placeholders",
        "order": 4,
    },
    {
        "name": "cards",
        "path": "/cards",
        "title": "Cards",
        "description": "Content containers with images and titles",
        "order": 5,
    },
    {
        "name": "checkboxes",
        "path": "/checkboxes",
        "title": "Checkboxes",
        "description": "Checkboxes with labels and validation states",
        "order": 6,
    },
    {
        "name": "inputs",
        "path": "/inputs",
        "title": "Inputs",
        "description": "Text input fields with validation",
        "order": 7,
    },
    {
        "name": "modals",
        "path": "/modals",
        "title": "Modals",
        "description": "Dialog boxes and popups",
        "order": 8,
    },
    {
        "name": "radios",
        "path": "/radios",
        "title": "Radio Buttons",
        "description": "Radio buttons with validation states",
        "order": 9,
    },
    {
        "name": "paginations",
        "path": "/paginations",
        "title": "Paginations",
        "description": "Page navigation with info text",
        "order": 10,
    },
    {
        "name": "selects",
        "path": "/selects",
        "title": "Selects",
        "description": "Dropdown selection fields",
        "order": 11,
    },
    {
        "name": "textareas",
        "path": "/textareas",
        "title": "Textareas",
        "description": "Multi-line text input fields",
        "order": 12,
    },
]


def build_navigation(current_page: str = "home") -> Component:
    """Build sidebar navigation menu using Button components.

    Args:
        current_page: Name of the current page for active state indication.
                     Use "home" for homepage, component name for component pages.

    Returns:
        htmy Component with navigation buttons.
    """
    nav_buttons = []

    for route in COMPONENT_ROUTES:
        is_active = route["name"] == current_page

        # Active page: PRIMARY/DEFAULT (filled), Others: SECONDARY/OUTLINE
        button = html.a(
            Button(
                label=route["title"],
                color=Color.PRIMARY if is_active else Color.SECONDARY,
                variant=ButtonVariant.DEFAULT if is_active else ButtonVariant.OUTLINE,
                class_="w-full justify-start text-left",
            ),
            href=route["path"],
            class_="block mb-2",
        )
        nav_buttons.append(button)

    return html.div(*nav_buttons, class_="space-y-1")


def build_homepage_content() -> Component:
    """Build homepage content with component gallery.

    Returns:
        htmy Component with welcome message and component grid.
    """
    return html.div(
        # Welcome header
        html.h1(
            "Flowbite-HTMY Component Showcase",
            class_="text-4xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Explore all available Flowbite components built with htmy for type-safe, "
            "composable server-side rendering with FastAPI and HTMX.",
            class_="text-xl text-gray-600 dark:text-gray-400 mb-8",
        ),
        html.p(
            "Click any component in the sidebar navigation to view comprehensive examples.",
            class_="text-lg text-gray-600 dark:text-gray-400 mb-12",
        ),
        # Component grid
        html.h2(
            "Available Components",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-6",
        ),
        html.div(
            *[
                html.a(
                    html.div(
                        html.h3(
                            route["title"],
                            class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
                        ),
                        html.p(
                            route["description"],
                            class_="text-gray-600 dark:text-gray-400",
                        ),
                        class_="p-6 bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 transition-colors",
                    ),
                    href=route["path"],
                    class_="block",
                )
                for route in COMPONENT_ROUTES
            ],
            class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
        ),
    )


@app.get("/")
@jinja.page("showcase-layout.html.jinja")
async def homepage() -> PageContext:
    """Render homepage with component gallery and navigation."""
    navigation_html = await renderer.render(build_navigation("home"))
    content_html = await renderer.render(build_homepage_content())

    return {
        "current_page": "home",
        "title": "Flowbite-HTMY Component Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/buttons")
@jinja.page("showcase-layout.html.jinja")
async def buttons_page() -> PageContext:
    """Render button component showcase page."""
    navigation_html = await renderer.render(build_navigation("buttons"))
    content_html = await renderer.render(build_buttons_showcase())

    return {
        "current_page": "buttons",
        "title": "Buttons - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/badges")
@jinja.page("showcase-layout.html.jinja")
async def badges_page() -> PageContext:
    """Render badge component showcase page."""
    navigation_html = await renderer.render(build_navigation("badges"))
    content_html = await renderer.render(build_badges_showcase())

    return {
        "current_page": "badges",
        "title": "Badges - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/alerts")
@jinja.page("showcase-layout.html.jinja")
async def alerts_page() -> PageContext:
    """Render alert component showcase page."""
    navigation_html = await renderer.render(build_navigation("alerts"))
    content_html = await renderer.render(build_alerts_showcase())

    return {
        "current_page": "alerts",
        "title": "Alerts - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/avatars")
@jinja.page("showcase-layout.html.jinja")
async def avatars_page() -> PageContext:
    """Render avatar component showcase page."""
    navigation_html = await renderer.render(build_navigation("avatars"))
    content_html = await renderer.render(build_avatars_showcase())

    return {
        "current_page": "avatars",
        "title": "Avatars - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/cards")
@jinja.page("showcase-layout.html.jinja")
async def cards_page() -> PageContext:
    """Render card component showcase page."""
    navigation_html = await renderer.render(build_navigation("cards"))
    content_html = await renderer.render(build_cards_showcase())

    return {
        "current_page": "cards",
        "title": "Cards - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/checkboxes")
@jinja.page("showcase-layout.html.jinja")
async def checkboxes_page() -> PageContext:
    """Render checkbox component showcase page."""
    navigation_html = await renderer.render(build_navigation("checkboxes"))
    content_html = await renderer.render(build_checkboxes_showcase())

    return {
        "current_page": "checkboxes",
        "title": "Checkboxes - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/inputs")
@jinja.page("showcase-layout.html.jinja")
async def inputs_page() -> PageContext:
    """Render input component showcase page."""
    navigation_html = await renderer.render(build_navigation("inputs"))
    content_html = await renderer.render(build_inputs_showcase())

    return {
        "current_page": "inputs",
        "title": "Inputs - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/modals")
@jinja.page("showcase-layout.html.jinja")
async def modals_page() -> PageContext:
    """Render modal component showcase page."""
    navigation_html = await renderer.render(build_navigation("modals"))
    content_html = await renderer.render(build_modals_showcase())

    return {
        "title": "Modals - Flowbite HTMY Showcase",
        "active_page": "modals",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/radios")
@jinja.page("showcase-layout.html.jinja")
async def radios_page() -> PageContext:
    """Render radio button component showcase page."""
    navigation_html = await renderer.render(build_navigation("radios"))
    content_html = await renderer.render(build_radios_showcase())

    return {
        "title": "Radio Buttons - Flowbite HTMY Showcase",
        "active_page": "radios",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/paginations")
@jinja.page("showcase-layout.html.jinja")
async def paginations_page() -> PageContext:
    """Render pagination component showcase page."""
    navigation_html = await renderer.render(build_navigation("paginations"))
    content_html = await renderer.render(build_paginations_showcase())

    return {
        "current_page": "paginations",
        "title": "Paginations - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/selects")
@jinja.page("showcase-layout.html.jinja")
async def selects_page() -> PageContext:
    """Render select component showcase page."""
    navigation_html = await renderer.render(build_navigation("selects"))
    content_html = await renderer.render(build_selects_showcase())

    return {
        "current_page": "selects",
        "title": "Selects - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/textareas")
@jinja.page("showcase-layout.html.jinja")
async def textareas_page() -> PageContext:
    """Render textarea component showcase page."""
    navigation_html = await renderer.render(build_navigation("textareas"))
    content_html = await renderer.render(build_textareas_showcase())

    return {
        "current_page": "textareas",
        "title": "Textareas - Flowbite-HTMY Showcase",
        "navigation": navigation_html,
        "content": content_html,
    }


@app.get("/clicked", response_class=HTMLResponse)
async def clicked() -> str:
    """HTMX endpoint - returns rendered htmy Alert component."""
    from flowbite_htmy.components import Alert

    alert = Alert(
        title="Success!",
        message="Button clicked! This Alert component was rendered server-side with htmy and returned via HTMX.",
        color=Color.SUCCESS,
    )

    # Return raw HTML with HTMLResponse
    return await renderer.render(alert)


@app.exception_handler(404)
async def not_found_handler(request: Request, exc: Exception) -> HTMLResponse:
    """Custom 404 error page with links to all available routes."""
    available_routes = (
        "<ul>"
        + "".join(
            [
                f'<li><a href="{route["path"]}" class="text-blue-600 hover:underline">{route["title"]}</a></li>'
                for route in COMPONENT_ROUTES
            ]
        )
        + "</ul>"
    )

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Page Not Found</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 dark:bg-gray-900">
        <div class="container mx-auto px-4 py-16">
            <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-4">404 - Page Not Found</h1>
            <p class="text-lg text-gray-600 dark:text-gray-400 mb-8">
                The requested page does not exist.
            </p>
            <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Available Pages:</h2>
            <ul class="space-y-2 mb-6">
                <li><a href="/" class="text-blue-600 hover:underline">Home</a></li>
                {available_routes}
            </ul>
            <a href="/" class="text-blue-600 hover:underline">← Back to Home</a>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=404)


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Consolidated Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ All 10 components in one app with navigation!")
    print("🌙 Dark mode toggle in sidebar")
    print()
    print("Available routes:")
    print("  / - Homepage with component gallery")
    for route in COMPONENT_ROUTES:
        print(f"  {route['path']} - {route['title']}")

    uvicorn.run("showcase:app", host="0.0.0.0", port=8000, reload=True)
