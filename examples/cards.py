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

from flowbite_htmy.components import Badge
from flowbite_htmy.icons import Icon, Payment, Social, get_icon, get_payment_icon, get_social_icon
from flowbite_htmy.types import Color

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
        # 8. Card with navigation tabs
        html.h2(
            "Card with navigation tabs",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Interactive tabbed cards with switchable content panels.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.ul(
                    html.li(
                        html.button(
                            "About",
                            id="about-tab",
                            type="button",
                            role="tab",
                            class_="inline-block p-4 text-blue-600 rounded-ss-lg hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-blue-500",
                            **{
                                "data-tabs-target": "#about",
                                "aria-controls": "about",
                                "aria-selected": "true",
                            },
                        ),
                        class_="me-2",
                    ),
                    html.li(
                        html.button(
                            "Services",
                            id="services-tab",
                            type="button",
                            role="tab",
                            class_="inline-block p-4 hover:text-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-gray-300",
                            **{
                                "data-tabs-target": "#services",
                                "aria-controls": "services",
                                "aria-selected": "false",
                            },
                        ),
                        class_="me-2",
                    ),
                    html.li(
                        html.button(
                            "Facts",
                            id="statistics-tab",
                            type="button",
                            role="tab",
                            class_="inline-block p-4 hover:text-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-gray-300",
                            **{
                                "data-tabs-target": "#statistics",
                                "aria-controls": "statistics",
                                "aria-selected": "false",
                            },
                        ),
                        class_="me-2",
                    ),
                    id="defaultTab",
                    role="tablist",
                    class_="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 rounded-t-lg bg-gray-50 dark:border-gray-700 dark:text-gray-400 dark:bg-gray-800",
                    **{"data-tabs-toggle": "#defaultTabContent"},
                ),
                html.div(
                    # About tab
                    html.div(
                        html.h2(
                            "Powering innovation & trust at 200,000+ companies worldwide",
                            class_="mb-3 text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white",
                        ),
                        html.p(
                            "Empower Developers, IT Ops, and business teams to collaborate at high velocity. Respond to changes and deliver great customer and employee service experiences fast.",
                            class_="mb-3 text-gray-500 dark:text-gray-400",
                        ),
                        html.a(
                            "Learn more",
                            get_icon(Icon.CHEVRON_RIGHT, class_="w-2.5 h-2.5 ms-2 rtl:rotate-180"),
                            href="#",
                            class_="inline-flex items-center font-medium text-blue-600 hover:text-blue-800 dark:text-blue-500 dark:hover:text-blue-700",
                        ),
                        id="about",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg md:p-8 dark:bg-gray-800",
                        **{"aria-labelledby": "about-tab"},
                    ),
                    # Services tab
                    html.div(
                        html.h2(
                            "We invest in the world's potential",
                            class_="mb-5 text-2xl font-extrabold tracking-tight text-gray-900 dark:text-white",
                        ),
                        html.ul(
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Dynamic reports and dashboards", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Templates for everyone", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Development workflow", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Limitless business automation", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            role="list",
                            class_="space-y-4 text-gray-500 dark:text-gray-400",
                        ),
                        id="services",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg md:p-8 dark:bg-gray-800",
                        **{"aria-labelledby": "services-tab"},
                    ),
                    # Statistics tab
                    html.div(
                        html.dl(
                            html.div(
                                html.dt("73M+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Developers", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col",
                            ),
                            html.div(
                                html.dt("100M+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Public repositories", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col",
                            ),
                            html.div(
                                html.dt("1000s", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Open source projects", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col",
                            ),
                            class_="grid max-w-screen-xl grid-cols-2 gap-8 p-4 mx-auto text-gray-900 sm:grid-cols-3 xl:grid-cols-6 dark:text-white sm:p-8",
                        ),
                        id="statistics",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg md:p-8 dark:bg-gray-800",
                        **{"aria-labelledby": "statistics-tab"},
                    ),
                    id="defaultTabContent",
                ),
                class_="w-full bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 9. Card full width with tabs
        html.h2(
            "Card full width with tabs",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Responsive tab selector (dropdown on mobile, button row on desktop).",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                # Mobile dropdown selector
                html.div(
                    html.label("Select tab", **{"for": "tabs", "class": "sr-only"}),
                    html.select(
                        html.option("Statistics"),
                        html.option("Services"),
                        html.option("FAQ"),
                        id="tabs",
                        class_="bg-gray-50 border-0 border-b border-gray-200 text-gray-900 text-sm rounded-t-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    ),
                    class_="sm:hidden",
                ),
                # Desktop tabs
                html.ul(
                    html.li(
                        html.button(
                            "Statistics",
                            id="stats-tab",
                            type="button",
                            role="tab",
                            class_="inline-block w-full p-4 rounded-ss-lg bg-gray-50 hover:bg-gray-100 focus:outline-none dark:bg-gray-700 dark:hover:bg-gray-600",
                            **{
                                "data-tabs-target": "#stats",
                                "aria-controls": "stats",
                                "aria-selected": "true",
                            },
                        ),
                        class_="w-full",
                    ),
                    html.li(
                        html.button(
                            "Services",
                            id="services-full-tab",
                            type="button",
                            role="tab",
                            class_="inline-block w-full p-4 bg-gray-50 hover:bg-gray-100 focus:outline-none dark:bg-gray-700 dark:hover:bg-gray-600",
                            **{
                                "data-tabs-target": "#services-full",
                                "aria-controls": "services-full",
                                "aria-selected": "false",
                            },
                        ),
                        class_="w-full",
                    ),
                    html.li(
                        html.button(
                            "FAQ",
                            id="faq-tab",
                            type="button",
                            role="tab",
                            class_="inline-block w-full p-4 rounded-se-lg bg-gray-50 hover:bg-gray-100 focus:outline-none dark:bg-gray-700 dark:hover:bg-gray-600",
                            **{
                                "data-tabs-target": "#faq",
                                "aria-controls": "faq",
                                "aria-selected": "false",
                            },
                        ),
                        class_="w-full",
                    ),
                    id="fullWidthTab",
                    role="tablist",
                    class_="hidden text-sm font-medium text-center text-gray-500 divide-x divide-gray-200 rounded-lg sm:flex dark:divide-gray-600 dark:text-gray-400 rtl:divide-x-reverse",
                    **{"data-tabs-toggle": "#fullWidthTabContent"},
                ),
                html.div(
                    # Statistics tab
                    html.div(
                        html.dl(
                            html.div(
                                html.dt("73M+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Developers", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            html.div(
                                html.dt("100M+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Public repositories", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            html.div(
                                html.dt("1000s", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Open source projects", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            html.div(
                                html.dt("1B+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Contributors", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            html.div(
                                html.dt("90+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Top Forbes companies", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            html.div(
                                html.dt("4M+", class_="mb-2 text-3xl font-extrabold"),
                                html.dd("Organizations", class_="text-gray-500 dark:text-gray-400"),
                                class_="flex flex-col items-center justify-center",
                            ),
                            class_="grid max-w-screen-xl grid-cols-2 gap-8 p-4 mx-auto text-gray-900 sm:grid-cols-3 xl:grid-cols-6 dark:text-white sm:p-8",
                        ),
                        id="stats",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg md:p-8 dark:bg-gray-800",
                        **{"aria-labelledby": "stats-tab"},
                    ),
                    # Services tab
                    html.div(
                        html.h2(
                            "We invest in the world's potential",
                            class_="mb-5 text-2xl font-extrabold tracking-tight text-gray-900 dark:text-white",
                        ),
                        html.ul(
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Dynamic reports and dashboards", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Templates for everyone", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Development workflow", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            html.li(
                                get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-3.5 h-3.5 text-blue-600 dark:text-blue-500"),
                                html.span("Limitless business automation", class_="leading-tight"),
                                class_="flex space-x-2 rtl:space-x-reverse items-center",
                            ),
                            role="list",
                            class_="space-y-4 text-gray-500 dark:text-gray-400",
                        ),
                        id="services-full",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg md:p-8 dark:bg-gray-800",
                        **{"aria-labelledby": "services-full-tab"},
                    ),
                    # FAQ tab with accordion
                    html.div(
                        html.div(
                            # FAQ 1
                            html.h2(
                                html.button(
                                    html.span("What is Flowbite?"),
                                    get_icon(Icon.CHEVRON_DOWN, class_="w-3 h-3 rotate-180 shrink-0"),
                                    type="button",
                                    class_="flex items-center justify-between w-full py-5 font-medium text-left rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400",
                                    **{
                                        "data-accordion-target": "#accordion-flush-body-1",
                                        "aria-expanded": "true",
                                        "aria-controls": "accordion-flush-body-1",
                                    },
                                ),
                                id="accordion-flush-heading-1",
                            ),
                            html.div(
                                html.div(
                                    html.p(
                                        "Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.",
                                        class_="mb-2 text-gray-500 dark:text-gray-400",
                                    ),
                                    html.p(
                                        "Check out this guide to learn how to ",
                                        html.a(
                                            "get started",
                                            href="/docs/getting-started/introduction/",
                                            class_="text-blue-600 dark:text-blue-500 hover:underline",
                                        ),
                                        " and start developing websites even faster with components on top of Tailwind CSS.",
                                        class_="text-gray-500 dark:text-gray-400",
                                    ),
                                    class_="py-5 border-b border-gray-200 dark:border-gray-700",
                                ),
                                id="accordion-flush-body-1",
                                class_="hidden",
                                **{"aria-labelledby": "accordion-flush-heading-1"},
                            ),
                            # FAQ 2
                            html.h2(
                                html.button(
                                    html.span("Is there a Figma file available?"),
                                    get_icon(Icon.CHEVRON_DOWN, class_="w-3 h-3 rotate-180 shrink-0"),
                                    type="button",
                                    class_="flex items-center justify-between w-full py-5 font-medium text-left rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400",
                                    **{
                                        "data-accordion-target": "#accordion-flush-body-2",
                                        "aria-expanded": "false",
                                        "aria-controls": "accordion-flush-body-2",
                                    },
                                ),
                                id="accordion-flush-heading-2",
                            ),
                            html.div(
                                html.div(
                                    html.p(
                                        "Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.",
                                        class_="mb-2 text-gray-500 dark:text-gray-400",
                                    ),
                                    html.p(
                                        "Check out the ",
                                        html.a(
                                            "Figma design system",
                                            href="https://flowbite.com/figma/",
                                            class_="text-blue-600 dark:text-blue-500 hover:underline",
                                        ),
                                        " based on the utility classes from Tailwind CSS and components from Flowbite.",
                                        class_="text-gray-500 dark:text-gray-400",
                                    ),
                                    class_="py-5 border-b border-gray-200 dark:border-gray-700",
                                ),
                                id="accordion-flush-body-2",
                                class_="hidden",
                                **{"aria-labelledby": "accordion-flush-heading-2"},
                            ),
                            # FAQ 3
                            html.h2(
                                html.button(
                                    html.span("What are the differences between Flowbite and Tailwind UI?"),
                                    get_icon(Icon.CHEVRON_DOWN, class_="w-3 h-3 rotate-180 shrink-0"),
                                    type="button",
                                    class_="flex items-center justify-between w-full py-5 font-medium text-left rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400",
                                    **{
                                        "data-accordion-target": "#accordion-flush-body-3",
                                        "aria-expanded": "false",
                                        "aria-controls": "accordion-flush-body-3",
                                    },
                                ),
                                id="accordion-flush-heading-3",
                            ),
                            html.div(
                                html.div(
                                    html.p(
                                        "The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.",
                                        class_="mb-2 text-gray-500 dark:text-gray-400",
                                    ),
                                    html.p(
                                        "However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.",
                                        class_="mb-2 text-gray-500 dark:text-gray-400",
                                    ),
                                    html.p(
                                        "Learn more about these technologies:",
                                        class_="mb-2 text-gray-500 dark:text-gray-400",
                                    ),
                                    html.ul(
                                        html.li(
                                            html.a(
                                                "Flowbite Pro",
                                                href="https://flowbite.com/pro/",
                                                class_="text-blue-600 dark:text-blue-500 hover:underline",
                                            )
                                        ),
                                        html.li(
                                            html.a(
                                                "Tailwind UI",
                                                href="https://tailwindui.com/",
                                                class_="text-blue-600 dark:text-blue-500 hover:underline",
                                                rel="nofollow",
                                            )
                                        ),
                                        class_="ps-5 text-gray-500 list-disc dark:text-gray-400",
                                    ),
                                    class_="py-5 border-b border-gray-200 dark:border-gray-700",
                                ),
                                id="accordion-flush-body-3",
                                class_="hidden",
                                **{"aria-labelledby": "accordion-flush-heading-3"},
                            ),
                            id="accordion-flush",
                            **{
                                "data-accordion": "collapse",
                                "data-active-classes": "bg-white dark:bg-gray-800 text-gray-900 dark:text-white",
                                "data-inactive-classes": "text-gray-500 dark:text-gray-400",
                            },
                        ),
                        id="faq",
                        role="tabpanel",
                        class_="hidden p-4 bg-white rounded-lg dark:bg-gray-800",
                        **{"aria-labelledby": "faq-tab"},
                    ),
                    id="fullWidthTabContent",
                    class_="border-t border-gray-200 dark:border-gray-600",
                ),
                class_="w-full bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 10. Card with list
        html.h2(
            "Card with list",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Display list items with avatars, names, and values.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.div(
                    html.h5(
                        "Latest Customers",
                        class_="text-xl font-bold leading-none text-gray-900 dark:text-white",
                    ),
                    html.a(
                        "View all",
                        href="#",
                        class_="text-sm font-medium text-blue-600 hover:underline dark:text-blue-500",
                    ),
                    class_="flex items-center justify-between mb-4",
                ),
                html.div(
                    html.ul(
                        # Customer 1
                        html.li(
                            html.div(
                                html.div(
                                    html.img(
                                        src="https://flowbite.com/docs/images/people/profile-picture-1.jpg",
                                        alt="Neil image",
                                        class_="w-8 h-8 rounded-full",
                                    ),
                                    class_="shrink-0",
                                ),
                                html.div(
                                    html.p(
                                        "Neil Sims",
                                        class_="text-sm font-medium text-gray-900 truncate dark:text-white",
                                    ),
                                    html.p(
                                        "email@windster.com",
                                        class_="text-sm text-gray-500 truncate dark:text-gray-400",
                                    ),
                                    class_="flex-1 min-w-0 ms-4",
                                ),
                                html.div(
                                    "$320",
                                    class_="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white",
                                ),
                                class_="flex items-center",
                            ),
                            class_="py-3 sm:py-4",
                        ),
                        # Customer 2
                        html.li(
                            html.div(
                                html.div(
                                    html.img(
                                        src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                                        alt="Bonnie image",
                                        class_="w-8 h-8 rounded-full",
                                    ),
                                    class_="shrink-0",
                                ),
                                html.div(
                                    html.p(
                                        "Bonnie Green",
                                        class_="text-sm font-medium text-gray-900 truncate dark:text-white",
                                    ),
                                    html.p(
                                        "email@windster.com",
                                        class_="text-sm text-gray-500 truncate dark:text-gray-400",
                                    ),
                                    class_="flex-1 min-w-0 ms-4",
                                ),
                                html.div(
                                    "$3467",
                                    class_="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white",
                                ),
                                class_="flex items-center",
                            ),
                            class_="py-3 sm:py-4",
                        ),
                        # Customer 3
                        html.li(
                            html.div(
                                html.div(
                                    html.img(
                                        src="https://flowbite.com/docs/images/people/profile-picture-2.jpg",
                                        alt="Michael image",
                                        class_="w-8 h-8 rounded-full",
                                    ),
                                    class_="shrink-0",
                                ),
                                html.div(
                                    html.p(
                                        "Michael Gough",
                                        class_="text-sm font-medium text-gray-900 truncate dark:text-white",
                                    ),
                                    html.p(
                                        "email@windster.com",
                                        class_="text-sm text-gray-500 truncate dark:text-gray-400",
                                    ),
                                    class_="flex-1 min-w-0 ms-4",
                                ),
                                html.div(
                                    "$67",
                                    class_="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white",
                                ),
                                class_="flex items-center",
                            ),
                            class_="py-3 sm:py-4",
                        ),
                        # Customer 4
                        html.li(
                            html.div(
                                html.div(
                                    html.img(
                                        src="https://flowbite.com/docs/images/people/profile-picture-4.jpg",
                                        alt="Lana image",
                                        class_="w-8 h-8 rounded-full",
                                    ),
                                    class_="shrink-0",
                                ),
                                html.div(
                                    html.p(
                                        "Lana Byrd",
                                        class_="text-sm font-medium text-gray-900 truncate dark:text-white",
                                    ),
                                    html.p(
                                        "email@windster.com",
                                        class_="text-sm text-gray-500 truncate dark:text-gray-400",
                                    ),
                                    class_="flex-1 min-w-0 ms-4",
                                ),
                                html.div(
                                    "$367",
                                    class_="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white",
                                ),
                                class_="flex items-center",
                            ),
                            class_="py-3 sm:py-4",
                        ),
                        # Customer 5
                        html.li(
                            html.div(
                                html.div(
                                    html.img(
                                        src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
                                        alt="Thomas image",
                                        class_="w-8 h-8 rounded-full",
                                    ),
                                    class_="shrink-0",
                                ),
                                html.div(
                                    html.p(
                                        "Thomes Lean",
                                        class_="text-sm font-medium text-gray-900 truncate dark:text-white",
                                    ),
                                    html.p(
                                        "email@windster.com",
                                        class_="text-sm text-gray-500 truncate dark:text-gray-400",
                                    ),
                                    class_="flex-1 min-w-0 ms-4",
                                ),
                                html.div(
                                    "$2367",
                                    class_="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white",
                                ),
                                class_="flex items-center",
                            ),
                            class_="pt-3 pb-0 sm:pt-4",
                        ),
                        role="list",
                        class_="divide-y divide-gray-200 dark:divide-gray-700",
                    ),
                    class_="flow-root",
                ),
                class_="w-full max-w-md p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-8 dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 11. Pricing card
        html.h2(
            "Pricing card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Display pricing plans with features and call-to-action.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.h5(
                    "Standard plan",
                    class_="mb-4 text-xl font-medium text-gray-500 dark:text-gray-400",
                ),
                html.div(
                    html.span("$", class_="text-3xl font-semibold"),
                    html.span("49", class_="text-5xl font-extrabold tracking-tight"),
                    html.span("/month", class_="ms-1 text-xl font-normal text-gray-500 dark:text-gray-400"),
                    class_="flex items-baseline text-gray-900 dark:text-white",
                ),
                html.ul(
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-blue-700 dark:text-blue-500"),
                        html.span("2 team members", class_="text-base font-normal leading-tight text-gray-500 dark:text-gray-400 ms-3"),
                        class_="flex items-center",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-blue-700 dark:text-blue-500"),
                        html.span("20GB Cloud storage", class_="text-base font-normal leading-tight text-gray-500 dark:text-gray-400 ms-3"),
                        class_="flex",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-blue-700 dark:text-blue-500"),
                        html.span("Integration help", class_="text-base font-normal leading-tight text-gray-500 dark:text-gray-400 ms-3"),
                        class_="flex",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-gray-400 dark:text-gray-500"),
                        html.span("Sketch Files", class_="text-base font-normal leading-tight text-gray-500 ms-3"),
                        class_="flex line-through decoration-gray-500",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-gray-400 dark:text-gray-500"),
                        html.span("API Access", class_="text-base font-normal leading-tight text-gray-500 ms-3"),
                        class_="flex line-through decoration-gray-500",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-gray-400 dark:text-gray-500"),
                        html.span("Complete documentation", class_="text-base font-normal leading-tight text-gray-500 ms-3"),
                        class_="flex line-through decoration-gray-500",
                    ),
                    html.li(
                        get_icon(Icon.CHECK_CIRCLE, class_="shrink-0 w-4 h-4 text-gray-400 dark:text-gray-500"),
                        html.span("24×7 phone & email support", class_="text-base font-normal leading-tight text-gray-500 ms-3"),
                        class_="flex line-through decoration-gray-500",
                    ),
                    role="list",
                    class_="space-y-5 my-7",
                ),
                html.button(
                    "Choose plan",
                    type="button",
                    class_="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-200 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-900 font-medium rounded-lg text-sm px-5 py-2.5 inline-flex justify-center w-full text-center",
                ),
                class_="w-full max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-8 dark:bg-gray-800 dark:border-gray-700",
            ),
            class_="mb-12",
        ),
        # 12. Testimonial card
        html.h2(
            "Testimonial card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Grid of testimonial cards with quotes and author information.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                # Testimonial 1
                html.figure(
                    html.blockquote(
                        html.h3(
                            "Very easy this was to integrate",
                            class_="text-lg font-semibold text-gray-900 dark:text-white",
                        ),
                        html.p(
                            "If you care for your time, I hands down would go with this.\"",
                            class_="my-4",
                        ),
                        class_="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400",
                    ),
                    html.figcaption(
                        html.img(
                            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/karen-nelson.png",
                            alt="profile picture",
                            class_="rounded-full w-9 h-9",
                        ),
                        html.div(
                            html.div("Bonnie Green"),
                            html.div(
                                "Developer at Open AI",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3",
                        ),
                        class_="flex items-center justify-center",
                    ),
                    class_="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 rounded-t-lg md:rounded-t-none md:rounded-ss-lg md:border-e dark:bg-gray-800 dark:border-gray-700",
                ),
                # Testimonial 2
                html.figure(
                    html.blockquote(
                        html.h3(
                            "Solid foundation for any project",
                            class_="text-lg font-semibold text-gray-900 dark:text-white",
                        ),
                        html.p(
                            "Designing with Figma components that can be easily translated to the utility classes of Tailwind CSS is a huge timesaver!\"",
                            class_="my-4",
                        ),
                        class_="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400",
                    ),
                    html.figcaption(
                        html.img(
                            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/roberta-casas.png",
                            alt="profile picture",
                            class_="rounded-full w-9 h-9",
                        ),
                        html.div(
                            html.div("Roberta Casas"),
                            html.div(
                                "Lead designer at Dropbox",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3",
                        ),
                        class_="flex items-center justify-center",
                    ),
                    class_="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 md:rounded-se-lg dark:bg-gray-800 dark:border-gray-700",
                ),
                # Testimonial 3
                html.figure(
                    html.blockquote(
                        html.h3(
                            "Mindblowing workflow",
                            class_="text-lg font-semibold text-gray-900 dark:text-white",
                        ),
                        html.p(
                            "Aesthetically, the well designed components are beautiful and will undoubtedly level up your next application.\"",
                            class_="my-4",
                        ),
                        class_="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400",
                    ),
                    html.figcaption(
                        html.img(
                            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png",
                            alt="profile picture",
                            class_="rounded-full w-9 h-9",
                        ),
                        html.div(
                            html.div("Jese Leos"),
                            html.div(
                                "Software Engineer at Facebook",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3",
                        ),
                        class_="flex items-center justify-center",
                    ),
                    class_="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 md:rounded-es-lg md:border-b-0 md:border-e dark:bg-gray-800 dark:border-gray-700",
                ),
                # Testimonial 4
                html.figure(
                    html.blockquote(
                        html.h3(
                            "Efficient Collaborating",
                            class_="text-lg font-semibold text-gray-900 dark:text-white",
                        ),
                        html.p(
                            "You have many examples that can be used to create a fast prototype for your team.\"",
                            class_="my-4",
                        ),
                        class_="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400",
                    ),
                    html.figcaption(
                        html.img(
                            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/joseph-mcfall.png",
                            alt="profile picture",
                            class_="rounded-full w-9 h-9",
                        ),
                        html.div(
                            html.div("Joseph McFall"),
                            html.div(
                                "CTO at Google",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3",
                        ),
                        class_="flex items-center justify-center",
                    ),
                    class_="flex flex-col items-center justify-center p-8 text-center bg-white border-gray-200 rounded-b-lg md:rounded-se-lg dark:bg-gray-800 dark:border-gray-700",
                ),
                class_="grid mb-8 border border-gray-200 rounded-lg shadow-xs dark:border-gray-700 md:mb-12 md:grid-cols-2 bg-white dark:bg-gray-800",
            ),
            class_="mb-12",
        ),
        # 13. Crypto wallet card
        html.h2(
            "Crypto wallet card",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Connect wallet card with popular crypto wallet providers.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                html.h5(
                    "Connect wallet",
                    class_="mb-3 text-base font-semibold text-gray-900 md:text-xl dark:text-white",
                ),
                html.p(
                    "Connect with one of our available wallet providers or create a new one.",
                    class_="text-sm font-normal text-gray-500 dark:text-gray-400",
                ),
                html.ul(
                    html.li(
                        html.a(
                            get_payment_icon(Payment.METAMASK, class_="h-4"),
                            html.span("MetaMask", class_="flex-1 ms-3 whitespace-nowrap"),
                            Badge(label="Popular", color=Color.GRAY, class_="ms-3"),
                            href="#",
                            class_="flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            get_payment_icon(Payment.COINBASE, class_="h-5"),
                            html.span("Coinbase Wallet", class_="flex-1 ms-3 whitespace-nowrap"),
                            href="#",
                            class_="flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            get_payment_icon(Payment.OPERA_WALLET, class_="w-5 h-5"),
                            html.span("Opera Wallet", class_="flex-1 ms-3 whitespace-nowrap"),
                            href="#",
                            class_="flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            get_payment_icon(Payment.WALLET_CONNECT, class_="h-5"),
                            html.span("WalletConnect", class_="flex-1 ms-3 whitespace-nowrap"),
                            href="#",
                            class_="flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white",
                        ),
                    ),
                    html.li(
                        html.a(
                            get_payment_icon(Payment.FORTMATIC, class_="h-4"),
                            html.span("Fortmatic", class_="flex-1 ms-3 whitespace-nowrap"),
                            href="#",
                            class_="flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white",
                        ),
                    ),
                    class_="my-4 space-y-3",
                ),
                html.div(
                    html.a(
                        get_icon(Icon.HELP_CIRCLE, class_="w-3 h-3 me-2"),
                        "Why do I need to connect with my wallet?",
                        href="#",
                        class_="inline-flex items-center text-xs font-normal text-gray-500 hover:underline dark:text-gray-400",
                    ),
                ),
                class_="w-full max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-6 dark:bg-gray-800 dark:border-gray-700",
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
