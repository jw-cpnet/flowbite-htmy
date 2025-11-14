"""Toast notification component."""

from dataclasses import dataclass

from htmy import Component, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import ToastVariant


@dataclass(frozen=True, kw_only=True)
class ToastActionButton:
    """Action button configuration for interactive toasts.

    Supports HTMX integration for server-side interactions.
    """

    label: str

    # HTMX attributes
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_target: str | None = None
    hx_swap: str | None = None
    hx_trigger: str | None = None
    hx_push_url: str | bool | None = None
    hx_select: str | None = None

    # Standard button attributes
    type_: str = "button"
    class_: str = ""


@dataclass(frozen=True, kw_only=True)
class Toast:
    """Toast notification component for temporary messages.

    Supports four variants (success, danger, warning, info), optional
    action buttons, rich content with avatars, and Flowbite JavaScript
    dismiss functionality.

    Examples:
        Simple success toast:
        >>> Toast(message="Saved successfully", variant=ToastVariant.SUCCESS)

        Interactive toast with action:
        >>> Toast(
        ...     message="New message from Alice",
        ...     variant=ToastVariant.INFO,
        ...     action_button=ToastActionButton(label="Reply", hx_get="/reply")
        ... )

        Rich content toast:
        >>> Toast(
        ...     message="Alice: Thanks for sharing!",
        ...     variant=ToastVariant.INFO,
        ...     avatar_src="/users/alice.jpg"
        ... )
    """

    # Required fields
    message: str

    # Variant and styling
    variant: ToastVariant = ToastVariant.INFO
    icon: Icon | None = None  # Custom icon (None = use default for variant)
    class_: str = ""

    # Dismissible functionality
    dismissible: bool = True
    id: str | None = None  # Auto-generated if None

    # Interactive features
    action_button: ToastActionButton | None = None

    # Rich content
    avatar_src: str | None = None

    def htmy(self, context: Context) -> Component:
        """Render toast notification component."""
        theme = ThemeContext.from_context(context)
        toast_id = self.id or f"toast-{id(self)}"
        icon = self._get_icon()
        classes = self._build_classes(theme)

        # Build children list
        children = []

        # Add avatar if provided (rich content layout)
        if self.avatar_src:
            children.append(self._render_avatar())

        # Add icon container (always present)
        children.append(self._render_icon_container(icon))

        # Add message content (with optional action button)
        children.append(self._render_message_content())

        # Add close button if dismissible
        if self.dismissible:
            children.append(self._render_close_button(toast_id))

        return html.div(
            *children,  # type: ignore[arg-type]
            id=toast_id,
            class_=classes,
            role="alert",
        )

    def _get_icon(self) -> Icon:
        """Get icon for toast (custom or default for variant).

        T020: Implement Toast._get_icon() method.
        """
        if self.icon is not None:
            return self.icon

        # Default icons per variant
        return {
            ToastVariant.SUCCESS: Icon.CHECK,
            ToastVariant.DANGER: Icon.CLOSE,
            ToastVariant.WARNING: Icon.EXCLAMATION_CIRCLE,
            ToastVariant.INFO: Icon.INFO,
        }[self.variant]

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build toast container classes.

        T022: Implement Toast._build_classes() method.
        """
        builder = ClassBuilder(
            "flex items-center w-full max-w-xs p-4 "
            "text-gray-500 bg-white rounded-lg shadow-sm "
            "dark:text-gray-400 dark:bg-gray-800"
        )
        return builder.merge(self.class_)

    def _render_icon_container(self, icon: Icon) -> Component:
        """Render icon container with variant colors.

        T023: Implement Toast._render_icon_container() method.
        T021: Uses VARIANT_ICON_CLASSES dictionary.
        """
        icon_classes = {
            ToastVariant.SUCCESS: (
                "inline-flex items-center justify-center shrink-0 w-8 h-8 "
                "text-green-500 bg-green-100 rounded-lg "
                "dark:bg-green-800 dark:text-green-200"
            ),
            ToastVariant.DANGER: (
                "inline-flex items-center justify-center shrink-0 w-8 h-8 "
                "text-red-500 bg-red-100 rounded-lg "
                "dark:bg-red-800 dark:text-red-200"
            ),
            ToastVariant.WARNING: (
                "inline-flex items-center justify-center shrink-0 w-8 h-8 "
                "text-yellow-500 bg-yellow-100 rounded-lg "
                "dark:bg-yellow-800 dark:text-yellow-200"
            ),
            ToastVariant.INFO: (
                "inline-flex items-center justify-center shrink-0 w-8 h-8 "
                "text-blue-500 bg-blue-100 rounded-lg "
                "dark:bg-blue-800 dark:text-blue-200"
            ),
        }[self.variant]

        icon_component = get_icon(icon, class_="w-4 h-4")

        return html.div(icon_component, class_=icon_classes)

    def _render_message_content(self) -> Component:
        """Render message content with optional action button.

        T040-T041: Update content structure for rich content layout.
        """
        # Render with or without action button
        if self.action_button:
            return html.div(
                self.message,
                html.div(
                    self._render_action_button(),  # type: ignore[arg-type]
                    class_="mt-2",
                ),
                class_="ms-3 text-sm font-normal",
            )
        else:
            return html.div(
                self.message,
                class_="ms-3 text-sm font-normal",
            )

    def _render_action_button(self) -> Component:
        """Render action button with HTMX attributes.

        T038: Implement Toast._render_action_button() method.
        """
        if not self.action_button:
            return html.div()  # Empty component

        button = self.action_button

        # Build HTMX attributes
        attrs: dict[str, str | bool] = {
            "type": button.type_,
            "class_": (
                "inline-flex px-2.5 py-1.5 text-xs font-medium text-center "
                "text-white bg-blue-600 rounded-lg hover:bg-blue-700 "
                "focus:ring-4 focus:outline-none focus:ring-blue-300 "
                "dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800"
            ),
        }

        # Add HTMX attributes
        if button.hx_get:
            attrs["hx_get"] = button.hx_get
        if button.hx_post:
            attrs["hx_post"] = button.hx_post
        if button.hx_put:
            attrs["hx_put"] = button.hx_put
        if button.hx_delete:
            attrs["hx_delete"] = button.hx_delete
        if button.hx_patch:
            attrs["hx_patch"] = button.hx_patch
        if button.hx_target:
            attrs["hx_target"] = button.hx_target
        if button.hx_swap:
            attrs["hx_swap"] = button.hx_swap
        if button.hx_trigger:
            attrs["hx_trigger"] = button.hx_trigger
        if button.hx_push_url is not None:
            attrs["hx_push_url"] = button.hx_push_url
        if button.hx_select:
            attrs["hx_select"] = button.hx_select

        # Merge custom classes
        if button.class_:
            attrs["class_"] = f"{attrs['class_']} {button.class_}"

        return html.button(button.label, **attrs)

    def _render_avatar(self) -> Component:
        """Render circular avatar image.

        T039: Implement Toast._render_avatar() method.
        """
        if not self.avatar_src:
            return html.div()  # Empty component

        return html.img(
            src=self.avatar_src,
            alt="Avatar",
            class_="w-8 h-8 rounded-full",
        )

    def _render_close_button(self, toast_id: str) -> Component:
        """Render dismissible close button.

        T024: Implement Toast._render_close_button() method.
        """
        return html.button(
            html.span("Close", class_="sr-only"),
            get_icon(Icon.CLOSE, class_="w-3 h-3"),
            type="button",
            class_=(
                "ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 "
                "rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 "
                "inline-flex items-center justify-center h-8 w-8 "
                "dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
            ),
            data_dismiss_target=f"#{toast_id}",
            aria_label="Close",
        )
