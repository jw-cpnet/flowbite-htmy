"""Card component for Flowbite."""

from dataclasses import dataclass

from htmy import Component, ComponentType, Context, html

from flowbite_htmy.base import ClassBuilder, ThemeContext


@dataclass(frozen=True, kw_only=True)
class Card:
    """Flowbite card component.

    A versatile container component for displaying content in a bordered,
    shadowed box. Supports titles, images, and arbitrary child content.

    Example:
        >>> Card(
        ...     title="Blog Post",
        ...     image_src="/images/post.jpg",
        ...     content=html.p("Post excerpt..."),
        ... )
    """

    content: ComponentType
    """Main card content (can be a single component or tuple of components)."""

    title: str | None = None
    """Optional card title."""

    image_src: str | None = None
    """Optional image URL (displayed at top of card)."""

    image_alt: str = ""
    """Alt text for the image."""

    href: str | None = None
    """Optional href to make the entire card clickable."""

    class_: str = ""
    """Additional custom classes."""

    def htmy(self, context: Context) -> Component:
        """Render the card component.

        Args:
            context: Rendering context.

        Returns:
            Card HTML component (div element).
        """
        theme = ThemeContext.from_context(context)
        classes = self._build_classes(theme)

        # Build card structure
        children: list[ComponentType] = []

        # Add image if provided
        if self.image_src:
            img = html.img(src=self.image_src, alt=self.image_alt, class_="rounded-t-lg")
            if self.href:
                children.append(html.a(img, href=self.href))
            else:
                children.append(img)

        # Content wrapper (with padding)
        content_children: list[ComponentType] = []

        # Add title if provided
        if self.title:
            title_elem = html.h5(
                self.title,
                class_="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white",
            )
            if self.href:
                content_children.append(html.a(title_elem, href=self.href))
            else:
                content_children.append(title_elem)

        # Add main content (handle both single component and tuple)
        if isinstance(self.content, (list, tuple)):
            content_children.extend(self.content)
        else:
            content_children.append(self.content)

        # Wrap content in div with padding (only if there's content besides image)
        if self.image_src:
            children.append(html.div(*content_children, class_="p-5"))
        else:
            # No image, so the card itself has padding
            children.extend(content_children)

        return html.div(*children, class_=classes)

    def _build_classes(self, theme: ThemeContext) -> str:
        """Build CSS classes for the card.

        Args:
            theme: Theme context for dark mode.

        Returns:
            Complete class string.
        """
        # Base card classes
        builder = ClassBuilder(
            "max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm"
        )

        # Padding only if no image (otherwise padding is on inner div)
        if not self.image_src:
            builder.add("p-6")

        # Dark mode classes
        if theme.dark_mode:
            builder.add("dark:bg-gray-800 dark:border-gray-700")

        return builder.merge(self.class_)
