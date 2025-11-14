"""Badge showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Badge
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color


def build_badges_showcase():
    """Build comprehensive badge showcase content."""
    return html.div(
        # Default badges
        html.h2(
            "Default badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the following badge elements to indicate counts or labels inside or outside components.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE),
            Badge(label="Dark", color=Color.GRAY),
            Badge(label="Red", color=Color.RED),
            Badge(label="Green", color=Color.GREEN),
            Badge(label="Yellow", color=Color.YELLOW),
            Badge(label="Indigo", color=Color.INDIGO),
            Badge(label="Purple", color=Color.PURPLE),
            Badge(label="Pink", color=Color.PINK),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Large badges
        html.h2(
            "Large badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the large prop for bigger badge variants.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, large=True),
            Badge(label="Dark", color=Color.GRAY, large=True),
            Badge(label="Red", color=Color.RED, large=True),
            Badge(label="Green", color=Color.GREEN, large=True),
            Badge(label="Yellow", color=Color.YELLOW, large=True),
            Badge(label="Indigo", color=Color.INDIGO, large=True),
            Badge(label="Purple", color=Color.PURPLE, large=True),
            Badge(label="Pink", color=Color.PINK, large=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Badge pills
        html.h2(
            "Badge pills",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the rounded prop for fully rounded, pill-shaped badges.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, rounded=True),
            Badge(label="Dark", color=Color.GRAY, rounded=True),
            Badge(label="Red", color=Color.RED, rounded=True),
            Badge(label="Green", color=Color.GREEN, rounded=True),
            Badge(label="Yellow", color=Color.YELLOW, rounded=True),
            Badge(label="Indigo", color=Color.INDIGO, rounded=True),
            Badge(label="Purple", color=Color.PURPLE, rounded=True),
            Badge(label="Pink", color=Color.PINK, rounded=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Bordered badges
        html.h2(
            "Bordered badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the border prop for outlined badge styles with transparent backgrounds in dark mode.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, border=True),
            Badge(label="Dark", color=Color.GRAY, border=True),
            Badge(label="Red", color=Color.RED, border=True),
            Badge(label="Green", color=Color.GREEN, border=True),
            Badge(label="Yellow", color=Color.YELLOW, border=True),
            Badge(label="Indigo", color=Color.INDIGO, border=True),
            Badge(label="Purple", color=Color.PURPLE, border=True),
            Badge(label="Pink", color=Color.PINK, border=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Badges as links
        html.h2(
            "Badges as links",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the href prop to make badges clickable links with hover states.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Badge link", color=Color.BLUE, border=True, href="#"),
            Badge(label="Badge link", color=Color.BLUE, border=True, large=True, href="#"),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Badges with icon
        html.h2(
            "Badges with icon",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the icon prop to add SVG icons before the badge text.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(
                label="3 days ago",
                icon=get_icon(Icon.CLOCK, class_="w-2.5 h-2.5 me-1.5"),
                color=Color.GRAY,
                border=True,
            ),
            Badge(
                label="2 minutes ago",
                icon=get_icon(Icon.CLOCK, class_="w-2.5 h-2.5 me-1.5"),
                color=Color.BLUE,
                border=True,
            ),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Notification badge
        html.h2(
            "Notification badge",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Position a badge absolutely on a button to show notification counts.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            # Button with notification badge positioned absolutely
            html.button(
                get_icon(Icon.ENVELOPE, class_="w-5 h-5"),
                html.span("Notifications", class_="sr-only"),
                # Notification badge
                html.div(
                    "20",
                    class_="absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900",
                ),
                type="button",
                class_="relative inline-flex items-center p-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            ),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Badges with icon only
        html.h2(
            "Badges with icon only",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Circular badges containing only icons with screen-reader labels.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(
                label="Icon description",
                icon=get_icon(Icon.CHECK, class_="w-2.5 h-2.5"),
                icon_only=True,
                color=Color.GRAY,
            ),
            Badge(
                label="Icon description",
                icon=get_icon(Icon.BADGE_CHECK, class_="w-3 h-3"),
                icon_only=True,
                color=Color.BLUE,
            ),
            Badge(
                label="Icon description",
                icon=get_icon(Icon.USER, class_="w-3 h-3"),
                icon_only=True,
                color=Color.GRAY,
            ),
            Badge(
                label="Icon description",
                icon=get_icon(Icon.INFO, class_="w-3 h-3"),
                icon_only=True,
                color=Color.BLUE,
            ),
            class_="flex flex-wrap gap-2 mb-12",
        ),
        # Dismissible badges (chips)
        html.h2(
            "Dismissible badges",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Badges with close buttons that can be dismissed using data-dismiss-target.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Badge(label="Default", color=Color.BLUE, dismissible=True, id="badge-dismiss-default"),
            Badge(label="Dark", color=Color.GRAY, dismissible=True, id="badge-dismiss-dark"),
            Badge(label="Red", color=Color.RED, dismissible=True, id="badge-dismiss-red"),
            Badge(label="Green", color=Color.GREEN, dismissible=True, id="badge-dismiss-green"),
            Badge(label="Yellow", color=Color.YELLOW, dismissible=True, id="badge-dismiss-yellow"),
            Badge(label="Indigo", color=Color.INDIGO, dismissible=True, id="badge-dismiss-indigo"),
            Badge(label="Purple", color=Color.PURPLE, dismissible=True, id="badge-dismiss-purple"),
            Badge(label="Pink", color=Color.PINK, dismissible=True, id="badge-dismiss-pink"),
            class_="flex flex-wrap gap-2 mb-12",
        ),
    )
