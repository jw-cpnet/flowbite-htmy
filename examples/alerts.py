"""Alert showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/alerts.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components import Alert
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color

app = FastAPI(title="Flowbite-HTMY Alert Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the alert showcase page using Jinja layout + htmy components."""

    # Helper to get info icon with proper sizing
    def info_icon() -> str:
        return get_icon(Icon.INFO, class_="w-4 h-4")

    # Build comprehensive alert showcase
    alerts_section = html.div(
        # 1. Default alerts
        html.h2(
            "Default alerts",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the following alert elements to indicate informational messages, warnings, errors, and success notifications.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                title="Info alert!",
                message="Change a few things up and try submitting again.",
                color=Color.INFO,
            ),
            Alert(
                title="Danger alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DANGER,
            ),
            Alert(
                title="Success alert!",
                message="Change a few things up and try submitting again.",
                color=Color.SUCCESS,
            ),
            Alert(
                title="Warning alert!",
                message="Change a few things up and try submitting again.",
                color=Color.WARNING,
            ),
            Alert(
                title="Dark alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DARK,
            ),
            class_="space-y-4 mb-12",
        ),
        # 2. Alerts with icon
        html.h2(
            "Alerts with icon",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the icon prop to add an SVG icon alongside the alert message.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                title="Info alert!",
                message="Change a few things up and try submitting again.",
                color=Color.INFO,
                icon=info_icon(),
            ),
            Alert(
                title="Danger alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DANGER,
                icon=info_icon(),
            ),
            Alert(
                title="Success alert!",
                message="Change a few things up and try submitting again.",
                color=Color.SUCCESS,
                icon=info_icon(),
            ),
            Alert(
                title="Warning alert!",
                message="Change a few things up and try submitting again.",
                color=Color.WARNING,
                icon=info_icon(),
            ),
            Alert(
                title="Dark alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DARK,
                icon=info_icon(),
            ),
            class_="space-y-4 mb-12",
        ),
        # 3. Bordered alerts
        html.h2(
            "Bordered alerts",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the bordered prop to add a border accent around the alert.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                title="Info alert!",
                message="Change a few things up and try submitting again.",
                color=Color.INFO,
                icon=info_icon(),
                bordered=True,
            ),
            Alert(
                title="Danger alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DANGER,
                icon=info_icon(),
                bordered=True,
            ),
            Alert(
                title="Success alert!",
                message="Change a few things up and try submitting again.",
                color=Color.SUCCESS,
                icon=info_icon(),
                bordered=True,
            ),
            Alert(
                title="Warning alert!",
                message="Change a few things up and try submitting again.",
                color=Color.WARNING,
                icon=info_icon(),
                bordered=True,
            ),
            Alert(
                title="Dark alert!",
                message="Change a few things up and try submitting again.",
                color=Color.DARK,
                icon=info_icon(),
                bordered=True,
            ),
            class_="space-y-4 mb-12",
        ),
        # 4. Alerts with list
        html.h2(
            "Alerts with list",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Pass complex content using htmy components for lists and formatted text.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Info alert with list - using custom flex layout
            html.div(
                html.div(
                    info_icon(),
                    html.span("Info", class_="sr-only"),
                    class_="flex-shrink-0",
                ),
                html.div(
                    html.span("Ensure that these requirements are met:", class_="font-medium"),
                    html.ul(
                        html.li("At least 10 characters (and up to 100 characters)"),
                        html.li("At least one lowercase character"),
                        html.li("Inclusion of at least one special character, e.g., ! @ # ?"),
                        class_="mt-1.5 list-disc list-inside",
                    ),
                    class_="ms-3 text-sm font-medium",
                ),
                role="alert",
                class_="flex p-4 mb-4 text-sm text-blue-800 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400",
            ),
            # Danger alert with list - using custom flex layout
            html.div(
                html.div(
                    info_icon(),
                    html.span("Info", class_="sr-only"),
                    class_="flex-shrink-0",
                ),
                html.div(
                    html.span("Alert with list", class_="font-medium"),
                    html.ul(
                        html.li("Fix the error in line 42"),
                        html.li("Update the API endpoint"),
                        html.li("Test the changes"),
                        class_="mt-1.5 list-disc list-inside",
                    ),
                    class_="ms-3 text-sm font-medium",
                ),
                role="alert",
                class_="flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400",
            ),
            class_="mb-12",
        ),
        # 5. Dismissible alerts
        html.h2(
            "Dismissible alerts",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the dismissible prop to add a close button with data-dismiss-target functionality.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                message=html.span(
                    "A simple info alert with an ",
                    html.a("example link", href="#", class_="font-medium underline hover:no-underline"),
                    ". Give it a click if you like.",
                ),
                color=Color.INFO,
                icon=info_icon(),
                dismissible=True,
                id="alert-1",
            ),
            Alert(
                message=html.span(
                    "A simple danger alert with an ",
                    html.a("example link", href="#", class_="font-medium underline hover:no-underline"),
                    ". Give it a click if you like.",
                ),
                color=Color.DANGER,
                icon=info_icon(),
                dismissible=True,
                id="alert-2",
            ),
            Alert(
                message=html.span(
                    "A simple success alert with an ",
                    html.a("example link", href="#", class_="font-medium underline hover:no-underline"),
                    ". Give it a click if you like.",
                ),
                color=Color.SUCCESS,
                icon=info_icon(),
                dismissible=True,
                id="alert-3",
            ),
            Alert(
                message=html.span(
                    "A simple warning alert with an ",
                    html.a("example link", href="#", class_="font-medium underline hover:no-underline"),
                    ". Give it a click if you like.",
                ),
                color=Color.WARNING,
                icon=info_icon(),
                dismissible=True,
                id="alert-4",
            ),
            Alert(
                message=html.span(
                    "A simple dark alert with an ",
                    html.a("example link", href="#", class_="font-medium underline hover:no-underline"),
                    ". Give it a click if you like.",
                ),
                color=Color.DARK,
                icon=info_icon(),
                dismissible=True,
                id="alert-5",
            ),
            class_="space-y-4 mb-12",
        ),
        # 6. Border accent
        html.h2(
            "Border accent",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the border_accent prop to add a 4px top border for visual distinction.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                message=html.span(
                    "Info alert! Change a few things up and ",
                    html.a("try submitting again", href="#", class_="font-medium underline hover:no-underline"),
                    ".",
                ),
                color=Color.INFO,
                border_accent=True,
                dismissible=True,
                id="alert-border-1",
            ),
            Alert(
                message=html.span(
                    "Danger alert! Change a few things up and ",
                    html.a("try submitting again", href="#", class_="font-medium underline hover:no-underline"),
                    ".",
                ),
                color=Color.DANGER,
                border_accent=True,
                dismissible=True,
                id="alert-border-2",
            ),
            Alert(
                message=html.span(
                    "Success alert! Change a few things up and ",
                    html.a("try submitting again", href="#", class_="font-medium underline hover:no-underline"),
                    ".",
                ),
                color=Color.SUCCESS,
                border_accent=True,
                dismissible=True,
                id="alert-border-3",
            ),
            Alert(
                message=html.span(
                    "Warning alert! Change a few things up and ",
                    html.a("try submitting again", href="#", class_="font-medium underline hover:no-underline"),
                    ".",
                ),
                color=Color.WARNING,
                border_accent=True,
                dismissible=True,
                id="alert-border-4",
            ),
            Alert(
                message=html.span(
                    "Dark alert! Change a few things up and ",
                    html.a("try submitting again", href="#", class_="font-medium underline hover:no-underline"),
                    ".",
                ),
                color=Color.DARK,
                border_accent=True,
                dismissible=True,
                id="alert-border-5",
            ),
            class_="space-y-4 mb-12",
        ),
        # 7. Additional content
        html.h2(
            "Additional content",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Alerts with extended content including heading, paragraph, and action buttons.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Alert(
                message=html.div(
                    html.div(
                        info_icon(),
                        html.h3("This is a info alert", class_="text-lg font-medium"),
                        class_="flex items-center",
                    ),
                    html.div(
                        "More info about this info alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.",
                        class_="mt-2 mb-4 text-sm",
                    ),
                    html.div(
                        html.button(
                            get_icon(Icon.BADGE_CHECK, class_="w-4 h-4 me-2"),
                            "View more",
                            type="button",
                            class_="text-white bg-blue-800 hover:bg-blue-900 focus:ring-4 focus:outline-none focus:ring-blue-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                        ),
                        html.button(
                            "Dismiss",
                            type="button",
                            class_="text-blue-800 bg-transparent border border-blue-800 hover:bg-blue-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-blue-600 dark:border-blue-600 dark:text-blue-400 dark:hover:text-white dark:focus:ring-blue-800",
                            **{"data-dismiss-target": "#alert-additional-content-1", "aria-label": "Close"},
                        ),
                        class_="flex",
                    ),
                ),
                color=Color.INFO,
                id="alert-additional-content-1",
                class_="",
            ),
            Alert(
                message=html.div(
                    html.div(
                        info_icon(),
                        html.h3("This is a danger alert", class_="text-lg font-medium"),
                        class_="flex items-center",
                    ),
                    html.div(
                        "More info about this danger alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.",
                        class_="mt-2 mb-4 text-sm",
                    ),
                    html.div(
                        html.button(
                            get_icon(Icon.BADGE_CHECK, class_="w-4 h-4 me-2"),
                            "View more",
                            type="button",
                            class_="text-white bg-red-800 hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800",
                        ),
                        html.button(
                            "Dismiss",
                            type="button",
                            class_="text-red-800 bg-transparent border border-red-800 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-red-600 dark:border-red-600 dark:text-red-400 dark:hover:text-white dark:focus:ring-red-800",
                            **{"data-dismiss-target": "#alert-additional-content-2", "aria-label": "Close"},
                        ),
                        class_="flex",
                    ),
                ),
                color=Color.DANGER,
                id="alert-additional-content-2",
                class_="",
            ),
            Alert(
                message=html.div(
                    html.div(
                        info_icon(),
                        html.h3("This is a success alert", class_="text-lg font-medium"),
                        class_="flex items-center",
                    ),
                    html.div(
                        "More info about this success alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.",
                        class_="mt-2 mb-4 text-sm",
                    ),
                    html.div(
                        html.button(
                            get_icon(Icon.BADGE_CHECK, class_="w-4 h-4 me-2"),
                            "View more",
                            type="button",
                            class_="text-white bg-green-800 hover:bg-green-900 focus:ring-4 focus:outline-none focus:ring-green-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
                        ),
                        html.button(
                            "Dismiss",
                            type="button",
                            class_="text-green-800 bg-transparent border border-green-800 hover:bg-green-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-green-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-green-600 dark:border-green-600 dark:text-green-400 dark:hover:text-white dark:focus:ring-green-800",
                            **{"data-dismiss-target": "#alert-additional-content-3", "aria-label": "Close"},
                        ),
                        class_="flex",
                    ),
                ),
                color=Color.SUCCESS,
                id="alert-additional-content-3",
                class_="",
            ),
            Alert(
                message=html.div(
                    html.div(
                        info_icon(),
                        html.h3("This is a warning alert", class_="text-lg font-medium"),
                        class_="flex items-center",
                    ),
                    html.div(
                        "More info about this warning alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.",
                        class_="mt-2 mb-4 text-sm",
                    ),
                    html.div(
                        html.button(
                            get_icon(Icon.BADGE_CHECK, class_="w-4 h-4 me-2"),
                            "View more",
                            type="button",
                            class_="text-white bg-yellow-800 hover:bg-yellow-900 focus:ring-4 focus:outline-none focus:ring-yellow-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-yellow-300 dark:hover:bg-yellow-400 dark:focus:ring-yellow-800",
                        ),
                        html.button(
                            "Dismiss",
                            type="button",
                            class_="text-yellow-800 bg-transparent border border-yellow-800 hover:bg-yellow-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-yellow-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-yellow-300 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-gray-800 dark:focus:ring-yellow-800",
                            **{"data-dismiss-target": "#alert-additional-content-4", "aria-label": "Close"},
                        ),
                        class_="flex",
                    ),
                ),
                color=Color.WARNING,
                id="alert-additional-content-4",
                class_="",
            ),
            Alert(
                message=html.div(
                    html.div(
                        info_icon(),
                        html.h3("This is a dark alert", class_="text-lg font-medium"),
                        class_="flex items-center",
                    ),
                    html.div(
                        "More info about this dark alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.",
                        class_="mt-2 mb-4 text-sm",
                    ),
                    html.div(
                        html.button(
                            get_icon(Icon.BADGE_CHECK, class_="w-4 h-4 me-2"),
                            "View more",
                            type="button",
                            class_="text-white bg-gray-800 hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-gray-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800",
                        ),
                        html.button(
                            "Dismiss",
                            type="button",
                            class_="text-gray-800 bg-transparent border border-gray-800 hover:bg-gray-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-gray-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-gray-600 dark:border-gray-600 dark:text-gray-300 dark:hover:text-white dark:focus:ring-gray-800",
                            **{"data-dismiss-target": "#alert-additional-content-5", "aria-label": "Close"},
                        ),
                        class_="flex",
                    ),
                ),
                color=Color.DARK,
                id="alert-additional-content-5",
                class_="",
            ),
            class_="space-y-4 mb-12",
        ),
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(alerts_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Alert Showcase",
        "subtitle": "Comprehensive alert variants - all Flowbite styles supported",
        "content": content_html,
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Alert Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("alerts:app", host="0.0.0.0", port=8000, reload=True)
