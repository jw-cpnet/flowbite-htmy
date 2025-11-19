"""Drawers showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Button, Drawer, Input, Textarea
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color, DrawerPlacement


def build_drawers_showcase():
    """Build comprehensive drawers showcase content.

    Uses Drawer component following Flowbite examples.
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
        Drawer(
            trigger_label="Show navigation",
            placement=DrawerPlacement.LEFT,
            trigger_color=Color.PRIMARY,
            content=html.div(
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
            ),
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
            Drawer(
                trigger_label="Show left drawer",
                placement=DrawerPlacement.LEFT,
                trigger_color=Color.PRIMARY,
                content=html.p(
                    "This drawer slides in from the left side of the screen.",
                    class_="text-gray-500 dark:text-gray-400",
                ),
            ),
            Drawer(
                trigger_label="Show right drawer",
                placement=DrawerPlacement.RIGHT,
                trigger_color=Color.SECONDARY,
                content=html.p(
                    "This drawer slides in from the right side of the screen.",
                    class_="text-gray-500 dark:text-gray-400",
                ),
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
        Drawer(
            trigger_label="Show contact form",
            placement=DrawerPlacement.RIGHT,
            trigger_color=Color.BLUE,
            content=html.div(
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
            ),
        ),
        class_="space-y-8",
    )
