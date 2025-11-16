"""Accordion showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Accordion, AccordionMode, AccordionVariant, Panel
from flowbite_htmy.types import Color


def build_accordions_showcase():
    """Build comprehensive accordion showcase content."""
    return html.div(
        # Default collapse accordion
        html.h2(
            "Default accordion",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the default accordion to show and hide content with collapse behavior (only one panel open at a time).",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Accordion(
            panels=[
                Panel(
                    title="What is Flowbite?",
                    content=html.div(
                        html.p(
                            "Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.",
                            class_="mb-2 text-gray-500 dark:text-gray-400",
                        ),
                        html.p(
                            "Check out this guide to learn how to ",
                            html.a(
                                "get started",
                                href="/docs/getting-started/",
                                class_="text-blue-600 dark:text-blue-500 hover:underline",
                            ),
                            " and start developing websites even faster with components on top of Tailwind CSS.",
                            class_="text-gray-500 dark:text-gray-400",
                        ),
                    ),
                    is_open=True,
                ),
                Panel(
                    title="Is there a Figma file available?",
                    content=html.div(
                        html.p(
                            "Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.",
                            class_="mb-2 text-gray-500 dark:text-gray-400",
                        ),
                        html.p(
                            "Check out the ",
                            html.a(
                                "Figma design system",
                                href="https://flowbite.com/figma/",
                                class_="text-blue-600 dark:text-blue-500 hover:underline",
                            ),
                            " based on the utility classes from Tailwind CSS and components from Flowbite.",
                            class_="text-gray-500 dark:text-gray-400",
                        ),
                    ),
                ),
                Panel(
                    title="What are the differences between Flowbite and Tailwind UI?",
                    content=html.div(
                        html.p(
                            "The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product.",
                            class_="mb-2 text-gray-500 dark:text-gray-400",
                        ),
                        html.p(
                            "However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.",
                            class_="mb-2 text-gray-500 dark:text-gray-400",
                        ),
                        html.p(
                            "Learn more about these technologies:",
                            class_="mb-2 text-gray-500 dark:text-gray-400",
                        ),
                        html.ul(
                            html.li(
                                html.a(
                                    "Flowbite Pro",
                                    href="https://flowbite.com/pro/",
                                    class_="text-blue-600 dark:text-blue-500 hover:underline",
                                )
                            ),
                            html.li(
                                html.a(
                                    "Tailwind UI",
                                    href="https://tailwindui.com/",
                                    class_="text-blue-600 dark:text-blue-500 hover:underline",
                                )
                            ),
                            class_="ps-5 text-gray-500 list-disc dark:text-gray-400",
                        ),
                    ),
                ),
            ],
            mode=AccordionMode.COLLAPSE,
            variant=AccordionVariant.DEFAULT,
        ),
        html.div(class_="mb-12"),
        # Always open accordion
        html.h2(
            "Always open accordion",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the always-open mode to keep multiple panels open simultaneously.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Accordion(
            panels=[
                Panel(
                    title="What is Flowbite?",
                    content=html.p(
                        "Flowbite is an open-source library of interactive components built on top of Tailwind CSS.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    is_open=True,
                ),
                Panel(
                    title="Is there a Figma file available?",
                    content=html.p(
                        "Yes, Flowbite has a complete Figma design system available for designers.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    is_open=True,
                ),
                Panel(
                    title="What are the differences between Flowbite and Tailwind UI?",
                    content=html.p(
                        "Flowbite is open source under MIT license, while Tailwind UI is a paid product.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                ),
            ],
            mode=AccordionMode.ALWAYS_OPEN,
            variant=AccordionVariant.DEFAULT,
        ),
        html.div(class_="mb-12"),
        # Flush accordion
        html.h2(
            "Flush accordion",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the flush variant for a borderless accordion that integrates seamlessly with your content.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Accordion(
            panels=[
                Panel(
                    title="What is Flowbite?",
                    content=html.p(
                        "Flowbite is an open-source library of interactive components built on top of Tailwind CSS.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    is_open=True,
                ),
                Panel(
                    title="Is there a Figma file available?",
                    content=html.p(
                        "Yes, Flowbite provides complete Figma design files for all components.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                ),
                Panel(
                    title="What are the differences?",
                    content=html.p(
                        "Flowbite is MIT licensed and open source, while Tailwind UI is a commercial product.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                ),
            ],
            mode=AccordionMode.COLLAPSE,
            variant=AccordionVariant.FLUSH,
        ),
        html.div(class_="mb-12"),
        # Color options
        html.h2(
            "Color options",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Customize accordion header colors using the color prop.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        Accordion(
            panels=[
                Panel(
                    title="What is Flowbite?",
                    content=html.p(
                        "Flowbite is an open-source library built on Tailwind CSS.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                    is_open=True,
                ),
                Panel(
                    title="Is there a Figma file?",
                    content=html.p(
                        "Yes, complete Figma files are available.",
                        class_="text-gray-500 dark:text-gray-400",
                    ),
                ),
            ],
            mode=AccordionMode.COLLAPSE,
            color=Color.BLUE,
        ),
    )
