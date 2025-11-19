"""Tabs component showcase application.

Demonstrates all Tabs features:
- 4 visual variants (DEFAULT, UNDERLINE, PILLS, FULL_WIDTH)
- Color customization
- HTMX lazy loading
- Icon support (left/right positioning)
- Disabled tabs

Run: python examples/tabs.py
Visit: http://localhost:8000
"""

from htmy import Component, html

from flowbite_htmy.components import IconPosition, Tab, Tabs, TabVariant
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import Color


def build_tabs_showcase() -> Component:
    """Build tabs showcase content for consolidated showcase integration."""
    sections = []

    # Section 1: DEFAULT Variant
    sections.append(
        html.section(
            html.h2(
                "1. Default Tabs", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Border + background styling (default variant)",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Profile",
                        content=html.div(
                            html.p(
                                "This is the Profile tab content using the DEFAULT variant.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Dashboard",
                        content=html.div(
                            html.p(
                                "This is the Dashboard tab with border and background styling.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Settings",
                        content=html.div(
                            html.p(
                                "Settings panel - the default variant shows active tabs with gray background.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                ],
                variant=TabVariant.DEFAULT,
            ),
            class_="mb-12",
        )
    )

    # Section 2: UNDERLINE Variant
    sections.append(
        html.section(
            html.h2(
                "2. Underline Tabs", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Minimal design with bottom border indicator",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Overview",
                        content=html.div(
                            html.p(
                                "Overview content with UNDERLINE variant - minimal design with bottom border indicator.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Analytics",
                        content=html.div(
                            html.p(
                                "Analytics data - underline tabs are great for minimal, clean interfaces.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Reports",
                        content=html.div(
                            html.p(
                                "Reports section - the active tab shows a colored border underneath.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                ],
                variant=TabVariant.UNDERLINE,
            ),
            class_="mb-12",
        )
    )

    # Section 3: PILLS Variant
    sections.append(
        html.section(
            html.h2(
                "3. Pills Tabs", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Rounded pill-shaped buttons with solid background",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Tab 1",
                        content=html.div(
                            html.p(
                                "First tab with PILLS variant - rounded backgrounds for modern UI.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Tab 2",
                        content=html.div(
                            html.p(
                                "Second tab - pills have solid color backgrounds when active.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Tab 3",
                        content=html.div(
                            html.p(
                                "Third tab - great for segmented controls and app-like interfaces.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                ],
                variant=TabVariant.PILLS,
            ),
            class_="mb-12",
        )
    )

    # Section 4: FULL-WIDTH Variant
    sections.append(
        html.section(
            html.h2(
                "4. Full-Width Tabs", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Tabs stretch to fill container width equally",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Profile",
                        content=html.div(
                            html.p(
                                "Profile section - full-width tabs stretch equally across the container.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Dashboard",
                        content=html.div(
                            html.p(
                                "Dashboard - perfect for mobile-first designs and equal emphasis on all tabs.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Settings",
                        content=html.div(
                            html.p(
                                "Settings - notice the rounded corners and shadow effect.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Invoice",
                        content=html.div(
                            html.p(
                                "Invoice section - full-width tabs provide visual balance.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                ],
                variant=TabVariant.FULL_WIDTH,
            ),
            class_="mb-12",
        )
    )

    # Section 5: Color Customization
    sections.append(
        html.section(
            html.h2(
                "5. Color Options", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Underline tabs with purple color (Color.PURPLE)",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Overview",
                        content=html.div(
                            html.p(
                                "Purple-colored tabs demonstrate color customization.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                    ),
                    Tab(
                        label="Details",
                        content=html.div(
                            html.p(
                                "Color.PURPLE applies to active tab indicator (text, background, or border).",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                ],
                variant=TabVariant.UNDERLINE,
                color=Color.PURPLE,
            ),
            class_="mb-12",
        )
    )

    # Section 6: HTMX Lazy Loading
    sections.append(
        html.section(
            html.h2(
                "6. HTMX Lazy Loading",
                class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
            ),
            html.p(
                "Tabs that load content dynamically when activated",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Static Content",
                        content=html.div(
                            html.p(
                                "This content is static (pre-rendered).",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Dynamic Dashboard",
                        hx_get="/api/dashboard",
                        hx_trigger="revealed once",  # Load only once on first reveal
                    ),
                    Tab(
                        label="Live Data",
                        hx_get="/api/live-data",
                        hx_trigger="revealed",  # Reload every time tab is activated
                    ),
                ],
                variant=TabVariant.DEFAULT,
                tabs_id="htmx-demo-tabs",
            ),
            class_="mb-12",
        )
    )

    # Section 7: Icons
    sections.append(
        html.section(
            html.h2(
                "7. Tabs with Icons", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Icons positioned left (default) and right",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Profile",
                        content=html.div(
                            html.p(
                                "Icon on the left (default position).",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        icon=Icon.USER,
                        is_active=True,
                    ),
                    Tab(
                        label="Shopping Cart",
                        content=html.div(
                            html.p(
                                "Icon on the right side of the label.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        icon=Icon.SHOPPING_CART,
                        icon_position=IconPosition.RIGHT,
                    ),
                    Tab(
                        label="Messages",
                        content=html.div(
                            html.p(
                                "Icons improve visual recognition and scannability.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        icon=Icon.ENVELOPE,
                    ),
                ],
                variant=TabVariant.UNDERLINE,
                color=Color.GREEN,
            ),
            class_="mb-12",
        )
    )

    # Section 8: Disabled Tabs
    sections.append(
        html.section(
            html.h2(
                "8. Disabled Tabs", class_="text-2xl font-bold text-gray-900 dark:text-white mb-4"
            ),
            html.p(
                "Tabs with disabled state (non-interactive)",
                class_="text-gray-600 dark:text-gray-400 mb-4",
            ),
            Tabs(
                tabs=[
                    Tab(
                        label="Free Features",
                        content=html.div(
                            html.p(
                                "These features are available to all users.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        is_active=True,
                    ),
                    Tab(
                        label="Premium Features",
                        content=html.div(
                            html.p(
                                "Upgrade to access premium features.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        disabled=True,
                    ),
                    Tab(
                        label="Enterprise",
                        content=html.div(
                            html.p(
                                "Enterprise features require a custom plan.",
                                class_="text-sm text-gray-500 dark:text-gray-400",
                            ),
                            class_="p-4 rounded-lg bg-gray-50 dark:bg-gray-800",
                        ),
                        disabled=True,
                    ),
                ],
                variant=TabVariant.DEFAULT,
            ),
            class_="mb-12",
        )
    )

    return html.div(*sections)
