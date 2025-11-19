"""Dropdown showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Dropdown, DropdownDivider, DropdownHeader, DropdownItem
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import (
    Color,
    DropdownPlacement,
    DropdownTriggerMode,
    DropdownTriggerType,
    Size,
)


def build_dropdowns_showcase():
    """Build comprehensive dropdown showcase content."""
    return html.div(
        # Section 1: Basic dropdown
        html.h2(
            "Default dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "The default dropdown allows you to show a list of menu items when clicking on a trigger element.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Dropdown button",
            items=[
                DropdownItem(label="Dashboard", href="/dashboard"),
                DropdownItem(label="Settings", href="/settings"),
                DropdownItem(label="Earnings", href="/earnings"),
                DropdownItem(label="Sign out", href="/signout"),
            ],
        ),
        # Section 2: Dropdown with header and dividers (Flowbite-inspired using component)
        html.h2(
            "Dropdown with header and dividers",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Approximating Flowbite's user profile dropdown using Dropdown component with headers, icons, and dividers.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Dropdown button",
            items=[
                DropdownHeader(label="Bonnie Green", class_="font-semibold"),
                DropdownHeader(
                    label="name@flowbite.com",
                    class_="text-xs text-gray-500 dark:text-gray-400 font-normal",
                ),
                DropdownDivider(),
                DropdownItem(label="Account", icon=Icon.USER, href="#"),
                DropdownItem(label="Settings", icon=Icon.USER, href="#"),
                DropdownItem(label="Privacy", icon=Icon.USER, href="#"),
                DropdownItem(label="Notifications", icon=Icon.INFO, href="#"),
                DropdownItem(label="Help center", icon=Icon.INFO, href="#"),
                DropdownDivider(),
                DropdownItem(
                    label="Sign out",
                    icon=Icon.ARROW_RIGHT,
                    href="#",
                    class_="text-red-600 dark:text-red-500 hover:bg-gray-100 dark:hover:bg-gray-600",
                ),
            ],
            menu_class="w-72",  # Wider menu like Flowbite example
        ),
        # Section 3: Color variants
        html.h2(
            "Color variants",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Customize the dropdown trigger button with different color variants.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Dropdown(
                trigger_label="Blue",
                color=Color.BLUE,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="Green",
                color=Color.GREEN,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="Red",
                color=Color.RED,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="Purple",
                color=Color.PURPLE,
                items=[DropdownItem(label="Action")],
            ),
            class_="flex flex-wrap gap-4",
        ),
        # Section 4: Size variants
        html.h2(
            "Size variants",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Choose from different sizes for the dropdown trigger button.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Dropdown(
                trigger_label="XS",
                size=Size.XS,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="SM",
                size=Size.SM,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="MD",
                size=Size.MD,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="LG",
                size=Size.LG,
                items=[DropdownItem(label="Action")],
            ),
            Dropdown(
                trigger_label="XL",
                size=Size.XL,
                items=[DropdownItem(label="Action")],
            ),
            class_="flex flex-wrap items-center gap-4",
        ),
        # Section 5: Placement options
        html.h2(
            "Placement options",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Control where the dropdown menu appears relative to the trigger.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Dropdown(
                trigger_label="Dropdown top",
                placement=DropdownPlacement.TOP,
                items=[
                    DropdownItem(label="Dashboard", href="/dashboard"),
                    DropdownItem(label="Settings", href="/settings"),
                ],
            ),
            Dropdown(
                trigger_label="Dropdown bottom",
                placement=DropdownPlacement.BOTTOM,
                items=[
                    DropdownItem(label="Dashboard", href="/dashboard"),
                    DropdownItem(label="Settings", href="/settings"),
                ],
            ),
            Dropdown(
                trigger_label="Dropdown left",
                placement=DropdownPlacement.LEFT,
                items=[
                    DropdownItem(label="Dashboard", href="/dashboard"),
                    DropdownItem(label="Settings", href="/settings"),
                ],
            ),
            Dropdown(
                trigger_label="Dropdown right",
                placement=DropdownPlacement.RIGHT,
                items=[
                    DropdownItem(label="Dashboard", href="/dashboard"),
                    DropdownItem(label="Settings", href="/settings"),
                ],
            ),
            class_="flex flex-wrap gap-4",
        ),
        # Section 6: Avatar trigger (user menu)
        html.h2(
            "Avatar dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use an avatar image as the dropdown trigger for user profile menus.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="User menu",
            trigger_type=DropdownTriggerType.AVATAR,
            avatar_src="https://flowbite.com/docs/images/people/profile-picture-5.jpg",
            avatar_alt="User profile",
            items=[
                DropdownHeader(label="Bonnie Green"),
                DropdownHeader(label="bonnie@flowbite.com"),
                DropdownDivider(),
                DropdownItem(label="Dashboard", href="/dashboard"),
                DropdownItem(label="Settings", href="/settings"),
                DropdownItem(label="Earnings", href="/earnings"),
                DropdownDivider(),
                DropdownItem(label="Sign out", href="/signout"),
            ],
        ),
        # Section 7: Text trigger
        html.h2(
            "Text dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use a text link style trigger for minimal dropdown appearance.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Click to open",
            trigger_type=DropdownTriggerType.TEXT,
            items=[
                DropdownItem(label="Profile", href="/profile"),
                DropdownItem(label="Settings", href="/settings"),
                DropdownItem(label="Messages", href="/messages"),
            ],
        ),
        # Section 8: Hover trigger
        html.h2(
            "Hover dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Open dropdown on hover instead of click for navigation menus.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Hover me",
            trigger_mode=DropdownTriggerMode.HOVER,
            items=[
                DropdownItem(label="Quick action 1", href="#"),
                DropdownItem(label="Quick action 2", href="#"),
                DropdownItem(label="Quick action 3", href="#"),
            ],
        ),
        # Section 9: Dropdowns with icons
        html.h2(
            "Dropdown with icons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Add icons to menu items for better visual clarity and user experience.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Actions",
            items=[
                DropdownItem(label="Profile", icon=Icon.USER, href="/profile"),
                DropdownItem(label="Messages", icon=Icon.ENVELOPE, href="/messages"),
                DropdownItem(label="Cart", icon=Icon.SHOPPING_CART, href="/cart"),
                DropdownDivider(),
                DropdownItem(label="Sign out", icon=Icon.ARROW_RIGHT, href="/signout"),
            ],
        ),
        # Section 10: Multi-level dropdown (Flowbite official design)
        html.h2(
            "Multi-level dropdown",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Matching Flowbite's official multi-level design: nested submenu opens to the right.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Dropdown(
            trigger_label="Dropdown button",
            items=[
                DropdownItem(label="Dashboard", href="#"),
                DropdownItem(
                    label="Dropdown",
                    dropdown=Dropdown(
                        trigger_label="Dropdown submenu",
                        placement=DropdownPlacement.RIGHT,  # Opens to the right
                        offset_distance=2,  # Tiny gap between parent and nested menu
                        items=[
                            DropdownItem(label="Overview", href="#"),
                            DropdownItem(label="My downloads", href="#"),
                            DropdownItem(label="Billing", href="#"),
                            DropdownItem(label="Rewards", href="#"),
                        ],
                    ),
                ),
                DropdownItem(label="Earnings", href="#"),
                DropdownItem(label="Sign out", href="#"),
            ],
        ),
        class_="p-8 bg-white dark:bg-gray-900 min-h-screen",
    )
