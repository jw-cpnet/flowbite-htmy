"""Avatar showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/avatars.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components.avatar import Avatar
from flowbite_htmy.types import Size

app = FastAPI(title="Flowbite-HTMY Avatar Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the avatar showcase page using Jinja layout + htmy components."""

    # Build comprehensive avatar showcase
    avatars_section = html.div(
        # 1. Default avatar
        html.h2(
            "Default avatar",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use circular or rounded avatars with image elements.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Rounded avatar",
                    rounded=True,
                ),
                class_="me-4",
            ),
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Default avatar",
                    rounded=False,
                ),
            ),
            class_="flex mb-12",
        ),
        # 2. Bordered
        html.h2(
            "Bordered",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Apply a border around the avatar using the bordered prop.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Avatar(
                src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                alt="Bordered avatar",
                bordered=True,
            ),
            class_="mb-12",
        ),
        # 3. Placeholder icon
        html.h2(
            "Placeholder icon",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use a placeholder icon when no custom image is available.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Avatar(alt="User placeholder"),
            class_="mb-12",
        ),
        # 4. Placeholder initials
        html.h2(
            "Placeholder initials",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Display user initials as a placeholder when no profile picture is available.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Avatar(initials="JL", alt="Jese Leos"),
            class_="mb-12",
        ),
        # 5. Avatar tooltip
        html.h2(
            "Avatar tooltip",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Show a tooltip when hovering over the avatar (requires Flowbite JS).",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Avatar 1 with tooltip
            html.div(
                html.div(
                    "Jese Leos",
                    html.div(class_="tooltip-arrow", **{"data-popper-arrow": ""}),
                    id="tooltip-jese",
                    role="tooltip",
                    class_="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Jese Leos avatar",
                    class_="w-10 h-10 rounded-full",
                    **{"data-tooltip-target": "tooltip-jese"},
                ),
                class_="me-4",
            ),
            # Avatar 2 with tooltip
            html.div(
                html.div(
                    "Roberta Casas",
                    html.div(class_="tooltip-arrow", **{"data-popper-arrow": ""}),
                    id="tooltip-roberta",
                    role="tooltip",
                    class_="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-4.jpg",
                    alt="Roberta Casas avatar",
                    class_="w-10 h-10 rounded-full",
                    **{"data-tooltip-target": "tooltip-roberta"},
                ),
                class_="me-4",
            ),
            # Avatar 3 with tooltip
            html.div(
                html.div(
                    "Bonnie Green",
                    html.div(class_="tooltip-arrow", **{"data-popper-arrow": ""}),
                    id="tooltip-bonnie",
                    role="tooltip",
                    class_="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                    alt="Bonnie Green avatar",
                    class_="w-10 h-10 rounded-full",
                    **{"data-tooltip-target": "tooltip-bonnie"},
                ),
            ),
            class_="flex mb-12",
        ),
        # 6. Dot indicator
        html.h2(
            "Dot indicator",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Add a status indicator dot to show online/offline status.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Rounded avatar with top green dot
            html.div(
                html.div(
                    html.img(
                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                        alt="",
                        class_="w-10 h-10 rounded-full",
                    ),
                    html.span(
                        class_="top-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full"
                    ),
                    class_="relative",
                ),
                class_="me-4",
            ),
            # Square avatar with top red dot (with transform)
            html.div(
                html.div(
                    html.img(
                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                        alt="",
                        class_="w-10 h-10 rounded-sm",
                    ),
                    html.span(
                        class_="absolute top-0 left-8 transform -translate-y-1/2 w-3.5 h-3.5 bg-red-400 border-2 border-white dark:border-gray-800 rounded-full"
                    ),
                    class_="relative",
                ),
                class_="me-4",
            ),
            # Rounded avatar with bottom green dot
            html.div(
                html.div(
                    html.img(
                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                        alt="",
                        class_="w-10 h-10 rounded-full",
                    ),
                    html.span(
                        class_="bottom-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full"
                    ),
                    class_="relative",
                ),
                class_="me-4",
            ),
            # Square avatar with bottom green dot (with transform)
            html.div(
                html.div(
                    html.img(
                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                        alt="",
                        class_="w-10 h-10 rounded-sm",
                    ),
                    html.span(
                        class_="absolute bottom-0 left-8 transform translate-y-1/4 w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full"
                    ),
                    class_="relative",
                ),
            ),
            class_="flex mb-12",
        ),
        # 7. Stacked
        html.h2(
            "Stacked",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Stack avatars by overlapping them with negative margin spacing.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # First stacked group - 4 avatars
            html.div(
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-2.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-4.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                class_="flex -space-x-4 rtl:space-x-reverse",
            ),
            # Second stacked group - 3 avatars + counter
            html.div(
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-2.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.img(
                    src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                    alt="",
                    class_="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800",
                ),
                html.a(
                    "+99",
                    href="#",
                    class_="flex items-center justify-center w-10 h-10 text-xs font-medium text-white bg-gray-700 border-2 border-white rounded-full hover:bg-gray-600 dark:border-gray-800",
                ),
                class_="flex -space-x-4 rtl:space-x-reverse",
            ),
            class_="flex mb-12",
        ),
        # 8. Avatar with text
        html.h2(
            "Avatar with text",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Show additional user information alongside the avatar.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.div(
                    Avatar(
                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                        alt="Jese Leos",
                    ),
                    class_="shrink-0",
                ),
                html.div(
                    html.div(
                        "Jese Leos",
                        class_="text-sm font-medium text-gray-900 dark:text-white",
                    ),
                    html.div(
                        "Joined in August 2014",
                        class_="text-sm text-gray-500 dark:text-gray-400",
                    ),
                    class_="flex-1 min-w-0 ms-4",
                ),
                class_="flex items-center space-x-4 rtl:space-x-reverse",
            ),
            class_="mb-12",
        ),
        # 9. User dropdown
        # Note: This requires Flowbite JS for dropdown functionality - using raw HTML
        html.h2(
            "User dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Show a dropdown menu when clicking on the avatar.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.img(
                src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                alt="User dropdown",
                id="avatarButton",
                type="button",
                class_="w-10 h-10 rounded-full cursor-pointer",
                **{
                    "data-dropdown-toggle": "userDropdown",
                    "data-dropdown-placement": "bottom-start",
                },
            ),
            # Dropdown menu
            html.div(
                html.div(
                    html.div("Bonnie Green"),
                    html.div(
                        "name@flowbite.com",
                        class_="font-medium truncate",
                    ),
                    class_="px-4 py-3 text-sm text-gray-900 dark:text-white",
                ),
                html.ul(
                    html.li(
                        html.a(
                            "Dashboard",
                            href="#",
                            class_="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            "Settings",
                            href="#",
                            class_="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            "Earnings",
                            href="#",
                            class_="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white",
                        ),
                    ),
                    class_="py-2 text-sm text-gray-700 dark:text-gray-200",
                    **{"aria-labelledby": "avatarButton"},
                ),
                html.div(
                    html.a(
                        "Sign out",
                        href="#",
                        class_="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white",
                    ),
                    class_="py-1",
                ),
                id="userDropdown",
                class_="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600",
            ),
            class_="mb-12",
        ),
        # 10. Sizes
        html.h2(
            "Sizes",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Choose from multiple sizing options for avatars.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Extra small avatar",
                    size=Size.XS,
                ),
                class_="me-4",
            ),
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Small avatar",
                    size=Size.SM,
                ),
                class_="me-4",
            ),
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Medium avatar",
                    size=Size.MD,
                ),
                class_="me-4",
            ),
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Large avatar",
                    size=Size.LG,
                ),
                class_="me-4",
            ),
            html.div(
                Avatar(
                    src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                    alt="Extra large avatar",
                    size=Size.XL,
                ),
            ),
            class_="flex items-center mb-12",
        ),
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(avatars_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Avatar Showcase",
        "subtitle": "User profile pictures and placeholders - all Flowbite styles supported",
        "content": content_html,
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Avatar Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("avatars:app", host="0.0.0.0", port=8000, reload=True)
