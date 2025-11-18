"""Drawers showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Button, Drawer, Input, Textarea
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color, DrawerPlacement, Size


def build_drawers_showcase():
    """Build comprehensive drawers showcase content.

    Extracted for reuse in consolidated showcase application.
    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Default drawer (left)
        html.h2(
            "Default drawer",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "The default drawer slides in from the left side of the screen with a backdrop overlay.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Drawer(
            trigger_label="Show navigation",
            placement=DrawerPlacement.LEFT,
            content=html.div(
                html.p(
                    "Sometimes you need extra actions placed at the top of the app.",
                    class_="mb-6 text-sm text-gray-500 dark:text-gray-400",
                ),
                html.ul(
                    html.li(
                        html.a(
                            get_icon(Icon.STAR, class_="w-5 h-5 me-2.5"),
                            "Dashboard",
                            href="#",
                            class_="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.SHOPPING_CART, class_="w-5 h-5 me-2.5"),
                            "Products",
                            href="#",
                            class_="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.USER, class_="w-5 h-5 me-2.5"),
                            "Users",
                            href="#",
                            class_="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.ENVELOPE, class_="w-5 h-5 me-2.5"),
                            "Inbox",
                            href="#",
                            class_="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    html.li(
                        html.a(
                            get_icon(Icon.HELP_CIRCLE, class_="w-5 h-5 me-2.5"),
                            "Settings",
                            href="#",
                            class_="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group",
                        )
                    ),
                    class_="space-y-2",
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
            Drawer(
                trigger_label="Show top drawer",
                placement=DrawerPlacement.TOP,
                trigger_color=Color.GREEN,
                content=html.p(
                    "This drawer slides in from the top of the screen.",
                    class_="text-gray-500 dark:text-gray-400",
                ),
            ),
            Drawer(
                trigger_label="Show bottom drawer",
                placement=DrawerPlacement.BOTTOM,
                trigger_color=Color.PURPLE,
                content=html.p(
                    "This drawer slides in from the bottom of the screen.",
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
            content=html.div(
                html.form(
                    html.div(
                        Input(
                            id="email-drawer",
                            label="Your email",
                            type="email",
                            placeholder="name@company.com",
                            required=True,
                            attrs={"name": "email"},
                        ),
                        class_="mb-6",
                    ),
                    html.div(
                        Input(
                            id="subject-drawer",
                            label="Subject",
                            type="text",
                            placeholder="Let us know how we can help you",
                            required=True,
                            attrs={"name": "subject"},
                        ),
                        class_="mb-6",
                    ),
                    html.div(
                        Textarea(
                            id="message-drawer",
                            label="Your message",
                            rows=4,
                            placeholder="Your message...",
                            attrs={"name": "message"},
                        ),
                        class_="mb-6",
                    ),
                    Button(
                        label="Send message",
                        color=Color.PRIMARY,
                        attrs={"type": "submit"},
                        class_="w-full",
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
                    class_="mb-2 text-sm text-gray-500 dark:text-gray-400",
                ),
            ),
        ),
        # Backdrop options
        html.h2(
            "Backdrop",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Control whether to show a dimming backdrop overlay behind the drawer.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Drawer(
                trigger_label="With backdrop",
                placement=DrawerPlacement.LEFT,
                backdrop=True,
                trigger_color=Color.PRIMARY,
                content=html.p(
                    "This drawer has a backdrop overlay that dims the page behind it.",
                    class_="text-gray-500 dark:text-gray-400",
                ),
            ),
            Drawer(
                trigger_label="No backdrop",
                placement=DrawerPlacement.LEFT,
                backdrop=False,
                trigger_color=Color.SECONDARY,
                content=html.p(
                    "This drawer has no backdrop, so you can see the page behind it clearly.",
                    class_="text-gray-500 dark:text-gray-400",
                ),
            ),
            class_="flex gap-3",
        ),
        # Swipeable edge
        html.h2(
            "Swipeable edge",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Show a visible tab at the edge when the drawer is closed, making it discoverable and swipeable.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Drawer(
                trigger_label="Show bottom drawer with edge",
                placement=DrawerPlacement.BOTTOM,
                edge=True,
                height="h-96",
                content=html.div(
                    html.p(
                        "This drawer has a visible tab at the bottom edge when closed. Click the tab to open the drawer.",
                        class_="mb-4 text-sm text-gray-500 dark:text-gray-400",
                    ),
                    html.div(
                        html.div(
                            get_icon(Icon.STAR, class_="w-6 h-6 mb-2 text-gray-500"),
                            html.span(
                                "Widgets",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="flex flex-col items-center justify-center p-4 rounded-lg bg-gray-50 dark:bg-gray-700",
                        ),
                        html.div(
                            get_icon(Icon.SHOPPING_CART, class_="w-6 h-6 mb-2 text-gray-500"),
                            html.span(
                                "Shop",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="flex flex-col items-center justify-center p-4 rounded-lg bg-gray-50 dark:bg-gray-700",
                        ),
                        html.div(
                            get_icon(Icon.USER, class_="w-6 h-6 mb-2 text-gray-500"),
                            html.span(
                                "Profile",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="flex flex-col items-center justify-center p-4 rounded-lg bg-gray-50 dark:bg-gray-700",
                        ),
                        html.div(
                            get_icon(Icon.HELP_CIRCLE, class_="w-6 h-6 mb-2 text-gray-500"),
                            html.span(
                                "Settings",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="flex flex-col items-center justify-center p-4 rounded-lg bg-gray-50 dark:bg-gray-700",
                        ),
                        class_="grid grid-cols-4 gap-4",
                    ),
                ),
            ),
            class_="flex gap-3",
        ),
        class_="space-y-8",
    )
