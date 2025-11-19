"""Drawers showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Button, Input, Textarea
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color


def build_drawers_showcase():
    """Build comprehensive drawers showcase content.

    Each section demonstrates a single drawer variant with a dedicated button.
    Drawers are closed by default and open when their button is clicked.
    Follows Flowbite's exact HTML structure for drawer components.

    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Default drawer (left)
        html.h2(
            "Default drawer",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "The default drawer slides in from the left side of the screen. Click the button to open the navigation drawer.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Trigger button
            Button(
                label="Show navigation",
                color=Color.PRIMARY,
                attrs={
                    "data-drawer-target": "drawer-navigation",
                    "data-drawer-show": "drawer-navigation",
                    "aria-controls": "drawer-navigation",
                },
            ),
            # Drawer component (NO separate header/body divs, NO backdrop element)
            html.div(
                html.h5(
                    "Menu",
                    id="drawer-navigation-label",
                    class_="inline-flex items-center mb-4 text-base font-semibold text-gray-500 dark:text-gray-400",
                ),
                html.button(
                    get_icon(Icon.CLOSE, class_="w-3 h-3"),
                    html.span("Close menu", class_="sr-only"),
                    type="button",
                    class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                    **{
                        "data-drawer-hide": "drawer-navigation",
                        "aria-controls": "drawer-navigation",
                    },
                ),
                html.p(
                    "Sometimes you need extra actions placed at the top of the app.",
                    class_="mb-6 text-sm text-gray-500 dark:text-gray-400",
                ),
                html.ul(
                    html.li(
                        html.a(
                            get_icon(Icon.STAR, class_="w-5 h-5 me-2.5"),
                            html.span("Dashboard", class_="ms-3"),
                            href="#",
                            class_="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.SHOPPING_CART, class_="w-5 h-5 me-2.5"),
                            html.span("Products", class_="ms-3"),
                            href="#",
                            class_="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.USER, class_="w-5 h-5 me-2.5"),
                            html.span("Users", class_="ms-3"),
                            href="#",
                            class_="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.ENVELOPE, class_="w-5 h-5 me-2.5"),
                            html.span("Inbox", class_="ms-3"),
                            href="#",
                            class_="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.HELP_CIRCLE, class_="w-5 h-5 me-2.5"),
                            html.span("Settings", class_="ms-3"),
                            href="#",
                            class_="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    class_="space-y-2 font-medium",
                ),
                id="drawer-navigation",
                class_="fixed top-0 left-0 z-40 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-white w-80 dark:bg-gray-800",
                tabindex="-1",
                aria_labelledby="drawer-navigation-label",
            ),
            class_="mb-4",
        ),
        # Placement variants
        html.h2(
            "Drawer placement",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Control the position from which the drawer slides in: left, right, top, or bottom.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Left placement example
            html.div(
                Button(
                    label="Show left drawer",
                    color=Color.PRIMARY,
                    attrs={
                        "data-drawer-target": "drawer-left",
                        "data-drawer-show": "drawer-left",
                        "aria-controls": "drawer-left",
                    },
                ),
                html.div(
                    html.h5(
                        "Left Drawer",
                        id="drawer-left-label",
                        class_="inline-flex items-center mb-4 text-base font-semibold text-gray-500 dark:text-gray-400",
                    ),
                    html.button(
                        get_icon(Icon.CLOSE, class_="w-3 h-3"),
                        html.span("Close", class_="sr-only"),
                        type="button",
                        class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                        **{
                            "data-drawer-hide": "drawer-left",
                            "aria-controls": "drawer-left",
                        },
                    ),
                    html.p(
                        "This drawer slides in from the left side of the screen.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    id="drawer-left",
                    class_="fixed top-0 left-0 z-40 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-white w-80 dark:bg-gray-800",
                    tabindex="-1",
                    aria_labelledby="drawer-left-label",
                ),
                class_="mb-4",
            ),
            # Right placement example
            html.div(
                Button(
                    label="Show right drawer",
                    color=Color.SECONDARY,
                    attrs={
                        "data-drawer-target": "drawer-right",
                        "data-drawer-show": "drawer-right",
                        "aria-controls": "drawer-right",
                    },
                ),
                html.div(
                    html.h5(
                        "Right Drawer",
                        id="drawer-right-label",
                        class_="inline-flex items-center mb-4 text-base font-semibold text-gray-500 dark:text-gray-400",
                    ),
                    html.button(
                        get_icon(Icon.CLOSE, class_="w-3 h-3"),
                        html.span("Close", class_="sr-only"),
                        type="button",
                        class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                        **{
                            "data-drawer-hide": "drawer-right",
                            "aria-controls": "drawer-right",
                        },
                    ),
                    html.p(
                        "This drawer slides in from the right side of the screen.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    id="drawer-right",
                    class_="fixed top-0 right-0 z-40 h-screen p-4 overflow-y-auto transition-transform translate-x-full bg-white w-80 dark:bg-gray-800",
                    tabindex="-1",
                    aria_labelledby="drawer-right-label",
                ),
                class_="mb-4",
            ),
            class_="flex flex-wrap gap-3",
        ),
        # Contact form drawer
        html.h2(
            "Contact form",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use a drawer for contact forms, settings panels, or any form-based interface.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Show contact form",
                color=Color.BLUE,
                attrs={
                    "data-drawer-target": "drawer-contact",
                    "data-drawer-show": "drawer-contact",
                    "aria-controls": "drawer-contact",
                },
            ),
            html.div(
                html.h5(
                    "Contact Us",
                    id="drawer-contact-label",
                    class_="mb-6 text-sm font-semibold text-gray-500 uppercase dark:text-gray-400",
                ),
                html.button(
                    get_icon(Icon.CLOSE, class_="w-3 h-3"),
                    html.span("Close", class_="sr-only"),
                    type="button",
                    class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                    **{
                        "data-drawer-hide": "drawer-contact",
                        "aria-controls": "drawer-contact",
                    },
                ),
                html.form(
                    Input(
                        id="email-contact",
                        label="Your email",
                        type="email",
                        placeholder="name@company.com",
                        required=True,
                        attrs={"name": "email"},
                        class_="mb-6",
                    ),
                    Input(
                        id="subject-contact",
                        label="Subject",
                        type="text",
                        placeholder="Let us know how we can help you",
                        required=True,
                        attrs={"name": "subject"},
                        class_="mb-6",
                    ),
                    Textarea(
                        id="message-contact",
                        label="Your message",
                        rows=4,
                        placeholder="Your message...",
                        attrs={"name": "message"},
                        class_="mb-6",
                    ),
                    Button(
                        label="Send message",
                        color=Color.PRIMARY,
                        attrs={"type": "submit"},
                        class_="w-full mb-6",
                    ),
                    class_="mb-6",
                ),
                html.p(
                    "Get in touch",
                    class_="mb-2 text-sm text-gray-500 dark:text-gray-400",
                ),
                html.p(
                    html.a(
                        "info@company.com",
                        href="mailto:info@company.com",
                        class_="hover:underline",
                    ),
                    class_="mb-2 text-sm text-gray-500 dark:text-gray-400",
                ),
                html.p(
                    html.a(
                        "212-456-7890",
                        href="tel:2124567890",
                        class_="hover:underline",
                    ),
                    class_="text-sm text-gray-500 dark:text-gray-400",
                ),
                id="drawer-contact",
                class_="fixed top-0 right-0 z-40 h-screen p-4 overflow-y-auto transition-transform translate-x-full bg-white w-80 dark:bg-gray-800",
                tabindex="-1",
                aria_labelledby="drawer-contact-label",
                **{"data-drawer-placement": "right"},
            ),
        ),
        class_="space-y-8",
    )
