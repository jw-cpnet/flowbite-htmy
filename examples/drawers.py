"""Drawers showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Button, Input, Textarea
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color


def build_drawers_showcase():
    """Build comprehensive drawers showcase content.

    Each section demonstrates a single drawer variant with a dedicated button.
    Drawers are closed by default and open when their button is clicked.

    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Default drawer (left)
        html.h2(
            "Default drawer",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "The default drawer slides in from the left side of the screen with a backdrop overlay. Click the button to open the navigation drawer.",
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
            # Drawer panel
            html.div(
                # Header
                html.div(
                    html.h5(
                        "Menu",
                        id="drawer-navigation-label",
                        class_="text-base font-semibold text-gray-500 uppercase dark:text-gray-400",
                    ),
                    html.button(
                        get_icon(Icon.CLOSE, class_="w-3 h-3"),
                        type="button",
                        class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                        **{"data-drawer-hide": "drawer-navigation"},
                    ),
                    class_="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700",
                ),
                # Body
                html.div(
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
                    class_="p-4 overflow-y-auto",
                ),
                id="drawer-navigation",
                class_="fixed left-0 top-0 z-40 h-screen w-80 -translate-x-full transition-transform bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700",
                **{
                    "aria-labelledby": "drawer-navigation-label",
                    "tabindex": "-1",
                    "aria-hidden": "true",
                },
            ),
            # Backdrop
            html.div(
                class_="fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80",
                **{
                    "data-drawer-backdrop": "drawer-navigation",
                    "data-drawer-hide": "drawer-navigation",
                    "aria-hidden": "true",
                },
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
            # Left placement
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
                    html.div(
                        html.h5(
                            "Left Drawer",
                            class_="text-base font-semibold text-gray-500 uppercase dark:text-gray-400",
                        ),
                        html.button(
                            get_icon(Icon.CLOSE, class_="w-3 h-3"),
                            type="button",
                            class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                            **{"data-drawer-hide": "drawer-left"},
                        ),
                        class_="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700",
                    ),
                    html.div(
                        html.p(
                            "This drawer slides in from the left side of the screen.",
                            class_="text-gray-500 dark:text-gray-400",
                        ),
                        class_="p-4",
                    ),
                    id="drawer-left",
                    class_="fixed left-0 top-0 z-40 h-screen w-80 -translate-x-full transition-transform bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700",
                    tabindex="-1",
                    aria_hidden="true",
                ),
                html.div(
                    class_="fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80",
                    **{
                        "data-drawer-backdrop": "drawer-left",
                        "data-drawer-hide": "drawer-left",
                        "aria-hidden": "true",
                    },
                ),
                class_="mb-4",
            ),
            # Right placement
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
                    html.div(
                        html.h5(
                            "Right Drawer",
                            class_="text-base font-semibold text-gray-500 uppercase dark:text-gray-400",
                        ),
                        html.button(
                            get_icon(Icon.CLOSE, class_="w-3 h-3"),
                            type="button",
                            class_="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white",
                            **{"data-drawer-hide": "drawer-right"},
                        ),
                        class_="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700",
                    ),
                    html.div(
                        html.p(
                            "This drawer slides in from the right side of the screen.",
                            class_="text-gray-500 dark:text-gray-400",
                        ),
                        class_="p-4",
                    ),
                    id="drawer-right",
                    class_="fixed right-0 top-0 z-40 h-screen w-80 translate-x-full transition-transform bg-white dark:bg-gray-800 border-l border-gray-200 dark:border-gray-700",
                    tabindex="-1",
                    aria_hidden="true",
                ),
                html.div(
                    class_="fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80",
                    **{
                        "data-drawer-backdrop": "drawer-right",
                        "data-drawer-hide": "drawer-right",
                        "aria-hidden": "true",
                    },
                ),
                class_="mb-4",
            ),
            class_="flex flex-wrap gap-3",
        ),
        class_="space-y-8",
    )
