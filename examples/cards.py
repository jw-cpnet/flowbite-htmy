"""Card showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/cards.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.icons import Icon, Social, get_icon, get_social_icon

app = FastAPI(title="Flowbite-HTMY Card Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the card showcase page using Jinja layout + htmy components."""

    # Build comprehensive card showcase
    cards_section = html.div(
        # 1. Default card
        html.h2(
            "Default card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use this simple card component with a title and description.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.a(
                html.h5(
                    "Noteworthy technology acquisitions 2021",
                    class_="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
                ),
                html.p(
                    "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.",
                    class_="font-normal text-gray-700 dark:text-gray-400",
                ),
                href="#",
                class_="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700",
            ),
            class_="mb-12",
        ),
        # 2. Card with action button
        html.h2(
            "Card with action button",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Add action buttons to cards with CTA functionality.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.a(
                    html.h5(
                        "Noteworthy technology acquisitions 2021",
                        class_="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
                    ),
                    href="#",
                ),
                html.p(
                    "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.",
                    class_="mb-3 font-normal text-gray-700 dark:text-gray-400",
                ),
                html.a(
                    "Read more",
                    get_icon(Icon.ARROW_RIGHT, class_="rtl:rotate-180 w-3.5 h-3.5 ms-2"),
                    href="#",
                    class_="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                ),
                class_="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 3. Card with link
        html.h2(
            "Card with link",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Add icons and inline links within cards.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                get_icon(Icon.GIFT, class_="w-7 h-7 text-gray-500 dark:text-gray-400 mb-3"),
                html.a(
                    html.h5(
                        "Need a help in Claim?",
                        class_="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white",
                    ),
                    href="#",
                ),
                html.p(
                    "Go to this step by step guideline process on how to certify for your weekly benefits:",
                    class_="mb-3 font-normal text-gray-500 dark:text-gray-400",
                ),
                html.a(
                    "See our guideline",
                    get_icon(Icon.EXTERNAL_LINK, class_="w-3 h-3 ms-2.5 rtl:rotate-[270deg]"),
                    href="#",
                    class_="inline-flex font-medium items-center text-blue-600 hover:underline",
                ),
                class_="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 4. Card with image
        html.h2(
            "Card with image",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Cards can include images at the top with rounded corners.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.a(
                    html.img(
                        src="https://flowbite.com/docs/images/blog/image-1.jpg",
                        alt="",
                        class_="rounded-t-lg",
                    ),
                    href="#",
                ),
                html.div(
                    html.a(
                        html.h5(
                            "Noteworthy technology acquisitions 2021",
                            class_="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
                        ),
                        href="#",
                    ),
                    html.p(
                        "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.",
                        class_="mb-3 font-normal text-gray-700 dark:text-gray-400",
                    ),
                    html.a(
                        "Read more",
                        get_icon(Icon.ARROW_RIGHT, class_="rtl:rotate-180 w-3.5 h-3.5 ms-2"),
                        href="#",
                        class_="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                    ),
                    class_="p-5",
                ),
                class_="max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 5. Horizontal card
        html.h2(
            "Horizontal card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Layout cards horizontally with image on the left.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.a(
                html.img(
                    src="https://flowbite.com/docs/images/blog/image-4.jpg",
                    alt="",
                    class_="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg",
                ),
                html.div(
                    html.h5(
                        "Noteworthy technology acquisitions 2021",
                        class_="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
                    ),
                    html.p(
                        "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.",
                        class_="mb-3 font-normal text-gray-700 dark:text-gray-400",
                    ),
                    class_="flex flex-col justify-between p-4 leading-normal",
                ),
                href="#",
                class_="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow-sm md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700",
            ),
            class_="mb-12",
        ),
        # 6. E-commerce card
        html.h2(
            "E-commerce card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Product cards with ratings, pricing, and add-to-cart functionality.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.a(
                    html.img(
                        src="https://flowbite.com/docs/images/products/apple-watch.png",
                        alt="product image",
                        class_="p-8 rounded-t-lg",
                    ),
                    href="#",
                ),
                html.div(
                    html.a(
                        html.h5(
                            "Apple Watch Series 7 GPS, Aluminium Case, Starlight Sport",
                            class_="text-xl font-semibold tracking-tight text-gray-900 dark:text-white",
                        ),
                        href="#",
                    ),
                    html.div(
                        html.div(
                            get_icon(Icon.STAR, class_="w-4 h-4 text-yellow-300"),
                            get_icon(Icon.STAR, class_="w-4 h-4 text-yellow-300"),
                            get_icon(Icon.STAR, class_="w-4 h-4 text-yellow-300"),
                            get_icon(Icon.STAR, class_="w-4 h-4 text-yellow-300"),
                            get_icon(Icon.STAR, class_="w-4 h-4 text-gray-200 dark:text-gray-600"),
                            class_="flex items-center space-x-1 rtl:space-x-reverse",
                        ),
                        html.span(
                            "5.0",
                            class_="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded-sm dark:bg-blue-200 dark:text-blue-800 ms-3",
                        ),
                        class_="flex items-center mt-2.5 mb-5",
                    ),
                    html.div(
                        html.span(
                            "$599",
                            class_="text-3xl font-bold text-gray-900 dark:text-white",
                        ),
                        html.a(
                            "Add to cart",
                            href="#",
                            class_="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                        ),
                        class_="flex items-center justify-between",
                    ),
                    class_="px-5 pb-5",
                ),
                class_="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 7. Call to action card
        html.h2(
            "Call to action card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Centered content with download buttons for multiple platforms.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.h5(
                    "Work fast from anywhere",
                    class_="mb-2 text-3xl font-bold text-gray-900 dark:text-white",
                ),
                html.p(
                    "Stay up to date and move work forward with Flowbite on iOS & Android. Download the app today.",
                    class_="mb-5 text-base text-gray-500 sm:text-lg dark:text-gray-400",
                ),
                html.div(
                    html.a(
                        get_social_icon(Social.APPLE, class_="me-3 w-7 h-7"),
                        html.div(
                            html.div("Download on the", class_="mb-1 text-xs"),
                            html.div("Mac App Store", class_="-mt-1 font-sans text-sm font-semibold"),
                            class_="text-left rtl:text-right",
                        ),
                        href="#",
                        class_="w-full sm:w-auto bg-gray-800 hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-300 text-white rounded-lg inline-flex items-center justify-center px-4 py-2.5 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700",
                    ),
                    html.a(
                        get_social_icon(Social.GOOGLE_PLAY, class_="me-3 w-7 h-7"),
                        html.div(
                            html.div("Get in on", class_="mb-1 text-xs"),
                            html.div("Google Play", class_="-mt-1 font-sans text-sm font-semibold"),
                            class_="text-left rtl:text-right",
                        ),
                        href="#",
                        class_="w-full sm:w-auto bg-gray-800 hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-300 text-white rounded-lg inline-flex items-center justify-center px-4 py-2.5 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700",
                    ),
                    class_="items-center justify-center space-y-4 sm:flex sm:space-y-0 sm:space-x-4 rtl:space-x-reverse",
                ),
                class_="w-full p-4 text-center bg-white border border-gray-200 rounded-lg shadow-sm sm:p-8 dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(cards_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Card Showcase",
        "subtitle": "Versatile card components - all Flowbite styles supported",
        "content": content_html,
    }


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Card Showcase")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("cards:app", host="0.0.0.0", port=8000, reload=True)
