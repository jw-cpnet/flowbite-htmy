"""Toast component showcase."""

from htmy import html

from flowbite_htmy.components import Toast, ToastActionButton
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import ToastVariant


def build_toasts_showcase():
    """Build comprehensive toast showcase content."""
    return html.div(
        html.h1(
            "Toast Notifications",
            class_="text-4xl font-bold mb-8 text-gray-900 dark:text-white",
        ),
        html.p(
            "Toast notifications for temporary messages with icons, colors, and actions.",
            class_="text-lg text-gray-600 dark:text-gray-400 mb-8",
        ),
        _section_basic_variants(),
        _section_custom_icons(),
        _section_dismissible(),
        _section_interactive(),
        _section_rich_content(),
        _section_custom_styling(),
        class_="space-y-12",
    )


def _section_basic_variants():
    """T072: Showcase all 4 toast variants."""
    return html.div(
        html.h2(
            "Basic Variants",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Toast notifications in four variants: success, danger, warning, and info.",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            Toast(
                message="Item saved successfully",
                variant=ToastVariant.SUCCESS,
                id="toast-success",
            ),
            Toast(
                message="Connection failed. Please try again.",
                variant=ToastVariant.DANGER,
                id="toast-danger",
            ),
            Toast(
                message="Please review your settings before continuing.",
                variant=ToastVariant.WARNING,
                id="toast-warning",
            ),
            Toast(
                message="New updates are available for download.",
                variant=ToastVariant.INFO,
                id="toast-info",
            ),
            class_="space-y-4",
        ),
    )


def _section_custom_icons():
    """T073: Showcase custom icon override."""
    return html.div(
        html.h2(
            "Custom Icons",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Override default variant icons with custom icons from the Icon library.",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            Toast(
                message="Payment processed successfully",
                variant=ToastVariant.SUCCESS,
                icon=Icon.CHECK_CIRCLE,  # Override default CHECK with CHECK_CIRCLE
                id="toast-custom-icon-1",
            ),
            Toast(
                message="File uploaded to cloud storage",
                variant=ToastVariant.INFO,
                icon=Icon.ARROW_RIGHT,  # Custom icon for upload
                id="toast-custom-icon-2",
            ),
            class_="space-y-4",
        ),
    )


def _section_dismissible():
    """T074: Showcase dismissible=True and False."""
    return html.div(
        html.h2(
            "Dismissible Control",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Control whether toasts show a close button with dismissible parameter.",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            html.div(
                html.h3(
                    "Dismissible (with close button)",
                    class_="text-lg font-semibold mb-2 text-gray-900 dark:text-white",
                ),
                Toast(
                    message="You can close this notification",
                    variant=ToastVariant.INFO,
                    dismissible=True,
                    id="toast-dismissible-true",
                ),
            ),
            html.div(
                html.h3(
                    "Non-dismissible (no close button)",
                    class_="text-lg font-semibold mb-2 mt-4 text-gray-900 dark:text-white",
                ),
                Toast(
                    message="Critical: Action required. This cannot be dismissed.",
                    variant=ToastVariant.DANGER,
                    dismissible=False,
                    id="toast-dismissible-false",
                ),
            ),
            class_="space-y-2",
        ),
    )


def _section_interactive():
    """T075: Showcase action buttons with HTMX."""
    return html.div(
        html.h2(
            "Interactive Toasts",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Toasts with action buttons for user interactions (Reply, Undo, View).",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            Toast(
                message="File uploaded successfully. Share with your team?",
                variant=ToastVariant.SUCCESS,
                action_button=ToastActionButton(
                    label="Share",
                    hx_post="/share",
                    hx_target="#share-modal",
                ),
                id="toast-interactive-1",
            ),
            Toast(
                message="Item deleted from your cart.",
                variant=ToastVariant.WARNING,
                action_button=ToastActionButton(
                    label="Undo",
                    hx_post="/cart/undo",
                    hx_target="#cart-items",
                ),
                id="toast-interactive-2",
            ),
            Toast(
                message="New comment on your post from @alice",
                variant=ToastVariant.INFO,
                action_button=ToastActionButton(
                    label="View",
                    hx_get="/comments/view/123",
                    hx_target="#comment-viewer",
                ),
                id="toast-interactive-3",
            ),
            class_="space-y-4",
        ),
    )


def _section_rich_content():
    """T076: Showcase avatars and formatted content."""
    return html.div(
        html.h2(
            "Rich Content",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Toasts with avatars for chat messages, user notifications, and social interactions.",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            Toast(
                message="Alice: Thanks for the quick response!",
                variant=ToastVariant.INFO,
                avatar_src="https://flowbite.com/docs/images/people/profile-picture-1.jpg",
                action_button=ToastActionButton(
                    label="Reply",
                    hx_get="/messages/reply/alice",
                    hx_target="#chat-window",
                ),
                id="toast-rich-1",
            ),
            Toast(
                message="Bob commented on your photo",
                variant=ToastVariant.SUCCESS,
                avatar_src="https://flowbite.com/docs/images/people/profile-picture-3.jpg",
                action_button=ToastActionButton(
                    label="View Photo",
                    hx_get="/photos/123",
                ),
                id="toast-rich-2",
            ),
            class_="space-y-4",
        ),
    )


def _section_custom_styling():
    """T077: Showcase class_ parameter customization."""
    return html.div(
        html.h2(
            "Custom Styling",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Apply custom CSS classes to toasts for application-specific styling.",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        html.div(
            Toast(
                message="Custom border and shadow",
                variant=ToastVariant.INFO,
                class_="border-2 border-blue-600 shadow-lg",
                id="toast-custom-1",
            ),
            Toast(
                message="Custom background with opacity",
                variant=ToastVariant.WARNING,
                class_="bg-opacity-90 backdrop-blur-sm",
                id="toast-custom-2",
            ),
            Toast(
                message="Extra large with custom padding",
                variant=ToastVariant.SUCCESS,
                class_="p-6 max-w-md",
                id="toast-custom-3",
            ),
            class_="space-y-4",
        ),
    )
