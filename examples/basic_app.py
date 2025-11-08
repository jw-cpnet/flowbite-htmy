"""Example FastAPI application showcasing flowbite-htmy components.

Run with: python examples/basic_app.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from htmy import Renderer, Tag, html

from flowbite_htmy.components import Alert, Avatar, Badge, Button, Card
from flowbite_htmy.layouts import PageLayout
from flowbite_htmy.types import Color, Size

app = FastAPI(title="Flowbite-HTMY Component Showcase")
renderer = Renderer()


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    """Render the component showcase page."""
    # Build all content in a single wrapper div
    content_wrapper = html.div(
            # Header with dark mode toggle
            html.div(
                html.div(
                    html.h1(
                        "Flowbite-HTMY Component Showcase",
                        class_="text-4xl font-bold text-gray-900 dark:text-white mb-2",
                    ),
                    html.p(
                        "All Phase 1 components built with htmy, FastAPI, and HTMX",
                        class_="text-lg text-gray-600 dark:text-gray-400 mb-4",
                    ),
                    # Dark mode info
                    Badge(
                        label="💡 Use browser/OS dark mode to test",
                        color=Color.DARK,
                        class_="text-xs",
                    ),
                    class_="flex justify-between items-start mb-8",
                ),
                class_="container mx-auto px-4 py-8",
            ),
            # Components Grid
            html.div(
                # Buttons Section
                html.div(
                    html.h2(
                        "Buttons",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    html.div(
                        Button(label="Primary", color=Color.PRIMARY),
                        Button(label="Success", color=Color.SUCCESS),
                        Button(label="Danger", color=Color.DANGER),
                        Button(label="Warning", color=Color.WARNING),
                        Button(label="Secondary", color=Color.SECONDARY),
                        class_="flex flex-wrap gap-2 mb-8",
                    ),
                    class_="mb-8",
                ),
                # HTMX Button Example
                html.div(
                    html.h2(
                        "Interactive Button (HTMX)",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    html.div(
                        Button(
                            label="Click Me!",
                            color=Color.INFO,
                            hx_get="/clicked",
                            hx_target="#click-result",
                            hx_swap="innerHTML",
                        ),
                        html.div(
                            html.p(
                                "Click the button above to see HTMX in action!",
                                class_="text-gray-600 dark:text-gray-400",
                            ),
                            id="click-result",
                            class_="mt-4",
                        ),
                        class_="mb-8",
                    ),
                ),
                # Badges Section
                html.div(
                    html.h2(
                        "Badges",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    html.div(
                        Badge(label="Default", color=Color.PRIMARY),
                        Badge(label="Success", color=Color.SUCCESS),
                        Badge(label="Danger", color=Color.DANGER),
                        Badge(label="Warning", color=Color.WARNING),
                        Badge(label="Info", color=Color.INFO),
                        Badge(label="Pill", color=Color.PURPLE, rounded=True),
                        Badge(label="Large", color=Color.PINK, large=True),
                        class_="flex flex-wrap gap-2 mb-8",
                    ),
                ),
                # Alerts Section
                html.div(
                    html.h2(
                        "Alerts",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    Alert(
                        title="Info alert!",
                        message="Change a few things up and try submitting again.",
                        color=Color.INFO,
                    ),
                    Alert(
                        title="Success!",
                        message="Your changes have been saved successfully.",
                        color=Color.SUCCESS,
                    ),
                    Alert(
                        title="Warning!",
                        message="Please review your input before continuing.",
                        color=Color.WARNING,
                    ),
                    Alert(
                        message="Bordered alert with accent.",
                        color=Color.DANGER,
                        bordered=True,
                    ),
                    class_="mb-8",
                ),
                # Avatars Section
                html.div(
                    html.h2(
                        "Avatars",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    html.div(
                        Avatar(
                            src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                            alt="User 1",
                            size=Size.XS,
                        ),
                        Avatar(
                            src="https://flowbite.com/docs/images/people/profile-picture-4.jpg",
                            alt="User 2",
                            size=Size.SM,
                        ),
                        Avatar(
                            src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                            alt="User 3",
                            size=Size.MD,
                        ),
                        Avatar(
                            src="https://flowbite.com/docs/images/people/profile-picture-2.jpg",
                            alt="User 4",
                            size=Size.LG,
                            bordered=True,
                        ),
                        Avatar(initials="JD", size=Size.MD),
                        Avatar(initials="AB", size=Size.LG),
                        Avatar(size=Size.MD),  # Placeholder icon
                        class_="flex flex-wrap items-center gap-4 mb-8",
                    ),
                ),
                # Cards Section
                html.div(
                    html.h2(
                        "Cards",
                        class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
                    ),
                    html.div(
                        Card(
                            title="Simple Card",
                            content=html.p(
                                "This is a basic card with just a title and content.",
                                class_="text-gray-700 dark:text-gray-400",
                            ),
                        ),
                        Card(
                            title="Card with Image",
                            image_src="https://flowbite.com/docs/images/blog/image-1.jpg",
                            image_alt="Blog image",
                            content=html.p(
                                "This card includes an image at the top.",
                                class_="text-gray-700 dark:text-gray-400",
                            ),
                        ),
                        Card(
                            title="Interactive Card",
                            content=(
                                html.p(
                                    "Cards can contain multiple elements and buttons.",
                                    class_="text-gray-700 dark:text-gray-400 mb-4",
                                ),
                                Button(
                                    label="Learn More",
                                    color=Color.PRIMARY,
                                    hx_get="/learn-more",
                                    hx_target="#learn-more-content",
                                ),
                                html.div(id="learn-more-content", class_="mt-4"),
                            ),
                        ),
                        class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8",
                    ),
                ),
                # Footer
                html.div(
                    html.hr(class_="my-8 border-gray-200 dark:border-gray-700"),
                    html.div(
                        html.p(
                            "Built with ",
                            html.a(
                                "flowbite-htmy",
                                href="https://github.com/yourusername/flowbite-htmy",
                                class_="text-blue-600 hover:underline",
                            ),
                            " - ",
                            Badge(label="Phase 1 Complete", color=Color.SUCCESS),
                            class_="text-center text-gray-600 dark:text-gray-400",
                        ),
                        class_="pb-8",
                    ),
                ),
                class_="container mx-auto px-4",
            ),
    )

    page = PageLayout(
        title="Flowbite-HTMY Component Showcase",
        body_class="bg-gray-50 dark:bg-gray-900 min-h-screen",
        content=content_wrapper,
    )

    return await renderer.render(page)


@app.get("/clicked", response_class=HTMLResponse)
async def clicked() -> str:
    """HTMX endpoint - button click response."""
    alert = Alert(
        title="Button Clicked!",
        message="You successfully clicked the HTMX button. This was rendered server-side!",
        color=Color.SUCCESS,
    )
    return await renderer.render(alert)


@app.get("/learn-more", response_class=HTMLResponse)
async def learn_more() -> str:
    """HTMX endpoint - learn more content."""
    content = html.div(
        html.p(
            "This content was loaded dynamically using HTMX!",
            class_="text-gray-700 dark:text-gray-400 mb-2",
        ),
        html.p(
            "flowbite-htmy makes it easy to build interactive UIs with server-side rendering.",
            class_="text-gray-600 dark:text-gray-400 text-sm",
        ),
        class_="p-4 bg-blue-50 dark:bg-blue-900 rounded-lg",
    )
    return await renderer.render(content)


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Component Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ All Phase 1 components + PageLayout included!")
    uvicorn.run("basic_app:app", host="0.0.0.0", port=8000, reload=True)
