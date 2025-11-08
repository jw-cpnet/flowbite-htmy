"""Button component for Flowbite."""

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar, cast

from htmy import Component, Context, SafeStr, html

from flowbite_htmy.base import ClassBuilder, ThemeContext
from flowbite_htmy.types import ButtonVariant, Color, Size


def _spinner_svg() -> SafeStr:
    """Return the SVG spinner for the button's loading state."""
    return SafeStr(
        """<svg aria-hidden="true" role="status" class="inline w-4 h-4 me-3 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor" fill-opacity="0.2"/>
<path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
</svg>"""
    )


@dataclass(frozen=True, kw_only=True)
class Button:
    """Flowbite button component.

    A versatile button component with support for different colors, sizes,
    variants, and HTMX attributes for interactive behavior.

    Example:
        >>> Button(label="Click Me", color=Color.PRIMARY, size=Size.MD)
    """

    label: str
    """Button text label."""

    color: Color | str = Color.PRIMARY
    """Button color variant. Can be a `Color` enum or a string for duotone gradients (e.g., 'purple-blue')."""

    size: Size = Size.MD
    """Button size."""

    variant: ButtonVariant = ButtonVariant.DEFAULT
    """Button style variant (solid, outline, gradient, etc.)."""

    pill: bool = False
    """If True, applies a full rounded style, making the button a 'pill' shape."""

    loading: bool = False
    """If True, shows a spinner and disables the button."""

    shadow: bool = False
    """If True, applies a colored shadow. Only effective for gradient variants."""

    disabled: bool = False
    """Whether the button is disabled."""

    type: str = "button"
    """Button type attribute (button, submit, reset)."""

    # HTMX attributes
    hx_get: str | None = None
    """HTMX hx-get attribute."""

    hx_post: str | None = None
    """HTMX hx-post attribute."""

    hx_target: str | None = None
    """HTMX hx-target attribute."""

    hx_swap: str | None = None
    """HTMX hx-swap attribute."""

    hx_trigger: str | None = None
    """HTMX hx-trigger attribute."""

    # Custom styling
    class_: str = ""
    """Additional custom classes."""

    # Class variables for color mappings
    _DEFAULT_COLORS: ClassVar[Mapping[Color, str]] = {
        Color.PRIMARY: "text-white bg-blue-700 hover:bg-blue-800 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
        Color.SECONDARY: "text-gray-900 bg-white border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700",
        Color.SUCCESS: "text-white bg-green-700 hover:bg-green-800 focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
        Color.DANGER: "text-white bg-red-700 hover:bg-red-800 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900",
        Color.WARNING: "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300 dark:focus:ring-yellow-900",
        Color.INFO: "text-white bg-cyan-700 hover:bg-cyan-800 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800",
        Color.DARK: "text-white bg-gray-800 hover:bg-gray-900 focus:ring-gray-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700",
        Color.LIGHT: "text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-gray-100 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700",
        Color.BLUE: "text-white bg-blue-700 hover:bg-blue-800 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
        Color.GREEN: "text-white bg-green-700 hover:bg-green-800 focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
        Color.RED: "text-white bg-red-700 hover:bg-red-800 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900",
        Color.YELLOW: "text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300 dark:focus:ring-yellow-900",
        Color.PURPLE: "text-white bg-purple-700 hover:bg-purple-800 focus:ring-purple-300 dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-900",
    }
    _OUTLINE_COLORS: ClassVar[Mapping[Color, str]] = {
        Color.PRIMARY: "text-blue-700 hover:text-white border border-blue-700 hover:bg-blue-800 focus:ring-blue-300 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:hover:bg-blue-500 dark:focus:ring-blue-800",
        Color.SUCCESS: "text-green-700 hover:text-white border border-green-700 hover:bg-green-800 focus:ring-green-300 dark:border-green-500 dark:text-green-500 dark:hover:text-white dark:hover:bg-green-600 dark:focus:ring-green-800",
        Color.DANGER: "text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-red-300 dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900",
        Color.WARNING: "text-yellow-400 hover:text-white border border-yellow-400 hover:bg-yellow-500 focus:ring-yellow-300 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-white dark:hover:bg-yellow-400 dark:focus:ring-yellow-900",
        Color.PURPLE: "text-purple-700 hover:text-white border border-purple-700 hover:bg-purple-800 focus:ring-purple-300 dark:border-purple-400 dark:text-purple-400 dark:hover:text-white dark:hover:bg-purple-500 dark:focus:ring-purple-900",
        Color.DARK: "text-gray-900 hover:text-white border border-gray-800 hover:bg-gray-900 focus:ring-gray-300 dark:border-gray-600 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-800",
    }
    _GRADIENT_MONO_COLORS: ClassVar[Mapping[Color, str]] = {
        Color.BLUE: "text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-blue-300 dark:focus:ring-blue-800",
        Color.GREEN: "text-white bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-green-300 dark:focus:ring-green-800",
        Color.CYAN: "text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-cyan-300 dark:focus:ring-cyan-800",
        Color.INFO: "text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-cyan-300 dark:focus:ring-cyan-800",
        Color.TEAL: "text-white bg-gradient-to-r from-teal-400 via-teal-500 to-teal-600 hover:bg-gradient-to-br focus:ring-teal-300 dark:focus:ring-teal-800",
        Color.LIME: "text-gray-900 bg-gradient-to-r from-lime-200 via-lime-400 to-lime-500 hover:bg-gradient-to-br focus:ring-lime-300 dark:focus:ring-lime-800",
        Color.RED: "text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-red-300 dark:focus:ring-red-800",
        Color.PINK: "text-white bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 hover:bg-gradient-to-br focus:ring-pink-300 dark:focus:ring-pink-800",
        Color.PURPLE: "text-white bg-gradient-to-r from-purple-500 via-purple-600 to-purple-700 hover:bg-gradient-to-br focus:ring-purple-300 dark:focus:ring-purple-800",
    }
    _GRADIENT_DUOTONE_COLORS: ClassVar[Mapping[str, str]] = {
        "purple-blue": "text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-blue-300 dark:focus:ring-blue-800",
        "cyan-blue": "text-white bg-gradient-to-r from-cyan-500 to-blue-500 hover:bg-gradient-to-bl focus:ring-cyan-300 dark:focus:ring-cyan-800",
        "green-blue": "text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-green-200 dark:focus:ring-green-800",
        "purple-pink": "text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-purple-200 dark:focus:ring-purple-800",
        "pink-orange": "text-white bg-gradient-to-br from-pink-500 to-orange-400 hover:bg-gradient-to-bl focus:ring-pink-200 dark:focus:ring-pink-800",
        "red-yellow": "text-gray-900 bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 hover:bg-gradient-to-bl focus:ring-red-100 dark:focus:ring-red-400",
    }
    _SHADOW_COLORS: ClassVar[Mapping[Any, str]] = {
        Color.BLUE: "shadow-blue-500/50 dark:shadow-blue-800/80",
        Color.GREEN: "shadow-green-500/50 dark:shadow-green-800/80",
        Color.CYAN: "shadow-cyan-500/50 dark:shadow-cyan-800/80",
        Color.INFO: "shadow-cyan-500/50 dark:shadow-cyan-800/80",
        Color.TEAL: "shadow-teal-500/50 dark:shadow-teal-800/80",
        Color.LIME: "shadow-lime-500/50 dark:shadow-lime-800/80",
        Color.RED: "shadow-red-500/50 dark:shadow-red-800/80",
        Color.PINK: "shadow-pink-500/50 dark:shadow-pink-800/80",
        Color.PURPLE: "shadow-purple-500/50 dark:shadow-purple-800/80",
        "purple-blue": "shadow-blue-500/50 dark:shadow-blue-800/80",
        "cyan-blue": "shadow-cyan-500/50 dark:shadow-cyan-800/80",
        "green-blue": "shadow-green-500/50 dark:shadow-green-800/80",
        "purple-pink": "shadow-purple-500/50 dark:shadow-purple-800/80",
        "pink-orange": "shadow-pink-500/50 dark:shadow-pink-800/80",
        "red-yellow": "shadow-red-500/50 dark:shadow-red-800/80",
    }

    def htmy(self, context: Context) -> Component:
        """Render the button component."""
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)
        is_disabled = self.disabled or self.loading

        # Build button content with optional loading spinner
        button_content: Any = (
            [_spinner_svg(), self.label] if self.loading else self.label
        )

        # For gradient outline, wrap content in a span
        if self.variant == ButtonVariant.GRADIENT_OUTLINE:
            inner_span_classes = (
                "relative transition-all ease-in duration-75 bg-white dark:bg-gray-900 group-hover:bg-opacity-0"
            )
            inner_span_classes += " " + self._get_size_classes(is_inner=True)
            inner_span_classes += " " + self._get_shape_classes()

            if self.loading:
                # Already a list with spinner + span - wrap the list
                button_content = [html.span(cast("Any", button_content), class_=inner_span_classes)]
            else:
                # Wrap the label text in inner span
                button_content = html.span(self.label, class_=inner_span_classes)

        # Render button
        if isinstance(button_content, list):
            return html.button(
                *button_content,
                type=self.type,
                disabled=is_disabled or None,
                class_=classes,
                hx_get=self.hx_get,
                hx_post=self.hx_post,
                hx_target=self.hx_target,
                hx_swap=self.hx_swap,
                hx_trigger=self.hx_trigger,
            )
        else:
            return html.button(
                button_content,
                type=self.type,
                disabled=is_disabled or None,
                class_=classes,
                hx_get=self.hx_get,
                hx_post=self.hx_post,
                hx_target=self.hx_target,
                hx_swap=self.hx_swap,
                hx_trigger=self.hx_trigger,
            )

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the button."""
        builder = ClassBuilder(
            "font-medium focus:ring-4 focus:outline-none text-center inline-flex items-center justify-center me-2 mb-2"
        )

        if self.variant != ButtonVariant.GRADIENT_OUTLINE:
            builder.add(self._get_size_classes())
            builder.add(self._get_shape_classes())

        variant_classes = {
            ButtonVariant.DEFAULT: self._get_default_variant_classes,
            ButtonVariant.OUTLINE: self._get_outline_variant_classes,
            ButtonVariant.GRADIENT: self._get_gradient_variant_classes,
            ButtonVariant.GRADIENT_OUTLINE: self._get_gradient_outline_variant_classes,
        }
        builder.add(variant_classes[self.variant]())

        if self.shadow and self.variant in (
            ButtonVariant.GRADIENT,
            ButtonVariant.GRADIENT_OUTLINE,
        ):
            builder.add(self._get_shadow_classes())

        if self.disabled or self.loading:
            builder.add("cursor-not-allowed")
            if self.variant == ButtonVariant.DEFAULT:
                builder.add("opacity-50")

        return builder.merge(self.class_)

    def _get_size_classes(self, is_inner: bool = False) -> str:
        size_map = {
            Size.XS: "text-xs px-3 py-2",
            Size.SM: "text-sm px-3 py-2",
            Size.MD: "text-sm px-5 py-2.5",
            Size.LG: "text-base px-5 py-3",
            Size.XL: "text-base px-6 py-3.5",
        }
        if is_inner:
            # For gradient outline, padding is on the inner span
            size_map = {
                Size.XS: "px-3 py-2",
                Size.SM: "px-3 py-2",
                Size.MD: "px-5 py-2.5",
                Size.LG: "px-5 py-3",
                Size.XL: "px-6 py-3.5",
            }
        return size_map.get(self.size, size_map[Size.MD])

    def _get_shape_classes(self) -> str:
        return "rounded-full" if self.pill else "rounded-lg"

    def _get_default_variant_classes(self) -> str:
        return self._DEFAULT_COLORS.get(self.color, self._DEFAULT_COLORS[Color.PRIMARY])  # type: ignore[call-overload, no-any-return]

    def _get_outline_variant_classes(self) -> str:
        return self._OUTLINE_COLORS.get(self.color, self._OUTLINE_COLORS[Color.PRIMARY])  # type: ignore[call-overload, no-any-return]

    def _get_gradient_variant_classes(self) -> str:
        # Check if it's a Color enum or a duotone string like "purple-blue"
        if isinstance(self.color, Color):
            # Monochrome gradient (Color enum)
            return self._GRADIENT_MONO_COLORS.get(
                self.color, self._GRADIENT_MONO_COLORS[Color.BLUE]
            )
        else:
            # Duotone gradient (string like "purple-blue")
            return self._GRADIENT_DUOTONE_COLORS.get(
                self.color, self._GRADIENT_MONO_COLORS[Color.BLUE]
            )

    def _get_gradient_outline_variant_classes(self) -> str:
        base_classes = "relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm font-medium text-gray-900 group dark:text-white"
        shape = self._get_shape_classes()
        gradient_classes = self._get_gradient_variant_classes().replace("text-white ", "")
        return f"{base_classes} {shape} {gradient_classes}"

    def _get_shadow_classes(self) -> str:
        return f"shadow-lg {self._SHADOW_COLORS.get(self.color, '')}"
