"""Modals showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Button, Modal, PopupModal
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color, Size


def build_modals_showcase():
    """Build comprehensive modals showcase content.

    Extracted for reuse in consolidated showcase application.
    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Default modal
        html.h2(
            "Default modal",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the default modal to show information or gather user input within a dialog overlay.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Toggle modal",
                color=Color.PRIMARY,
                attrs={"data-modal-toggle": "default-modal"},
            ),
            class_="flex gap-3",
        ),
        # Default modal component
        Modal(
            id="default-modal",
            title="Terms of Service",
            children=html.div(
                html.p(
                    "With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.",
                    class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
                ),
                html.p(
                    "The European Union's General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.",
                    class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
                ),
            ),
            footer=html.div(
                Button(
                    label="I accept",
                    color=Color.PRIMARY,
                    attrs={"data-modal-hide": "default-modal"},
                ),
                Button(
                    label="Decline",
                    color=Color.SECONDARY,
                    class_="ms-3",
                    attrs={"data-modal-hide": "default-modal"},
                ),
            ),
        ),
        # Static backdrop modal
        html.h2(
            "Static modal",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Prevent the modal from closing when clicking outside by using a static backdrop. Useful for critical decisions.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Toggle modal",
                color=Color.PRIMARY,
                attrs={"data-modal-toggle": "static-modal"},
            ),
            class_="flex gap-3",
        ),
        Modal(
            id="static-modal",
            title="Static modal",
            static_backdrop=True,
            children=html.div(
                html.p(
                    "With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.",
                    class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
                ),
                html.p(
                    "The European Union's General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.",
                    class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
                ),
            ),
            footer=html.div(
                Button(
                    label="I accept",
                    color=Color.PRIMARY,
                    attrs={"data-modal-hide": "static-modal"},
                ),
                Button(
                    label="Decline",
                    color=Color.SECONDARY,
                    class_="ms-3",
                    attrs={"data-modal-hide": "static-modal"},
                ),
            ),
        ),
        # Popup modal (confirmation/delete) - Uses PopupModal component
        html.h2(
            "Popup modal",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use a popup modal for confirmation dialogs, destructive actions, or important warnings.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Delete product",
                color=Color.RED,
                attrs={"data-modal-toggle": "popup-modal"},
            ),
            class_="flex gap-3",
        ),
        # PopupModal component - separate from Modal for centered confirmation layout
        PopupModal(
            id="popup-modal",
            message="Are you sure you want to delete this product?",
            icon=get_icon(
                Icon.EXCLAMATION_CIRCLE,
                class_="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200",
            ),
            confirm_button=Button(
                label="Yes, I'm sure",
                color=Color.RED,
                attrs={"data-modal-hide": "popup-modal"},
            ),
            cancel_button=Button(
                label="No, cancel",
                color=Color.SECONDARY,
                attrs={"data-modal-hide": "popup-modal"},
                class_="ms-3",
            ),
        ),
        # Form modal (CRUD)
        html.h2(
            "Form modal",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use a modal to collect form data without navigating away from the current page. Perfect for CRUD operations.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Create new product",
                color=Color.PRIMARY,
                attrs={"data-modal-toggle": "crud-modal"},
            ),
            class_="flex gap-3",
        ),
        Modal(
            id="crud-modal",
            title="Create New Product",
            size=Size.SM,
            children=html.form(
                html.div(
                    # Name field
                    html.div(
                        html.label(
                            "Name",
                            **{"for": "name"},
                            class_="block mb-2 text-sm font-medium text-gray-900 dark:text-white",
                        ),
                        html.input_(
                            type="text",
                            name="name",
                            id="name",
                            class_="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                            placeholder="Type product name",
                            required=True,
                        ),
                        class_="col-span-2",
                    ),
                    # Price field
                    html.div(
                        html.label(
                            "Price",
                            **{"for": "price"},
                            class_="block mb-2 text-sm font-medium text-gray-900 dark:text-white",
                        ),
                        html.input_(
                            type="number",
                            name="price",
                            id="price",
                            class_="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                            placeholder="$2999",
                            required=True,
                        ),
                        class_="col-span-2 sm:col-span-1",
                    ),
                    # Category field
                    html.div(
                        html.label(
                            "Category",
                            **{"for": "category"},
                            class_="block mb-2 text-sm font-medium text-gray-900 dark:text-white",
                        ),
                        html.select(
                            html.option("Select category", selected=True),
                            html.option("TV/Monitors", value="TV"),
                            html.option("PC", value="PC"),
                            html.option("Gaming/Console", value="GA"),
                            html.option("Phones", value="PH"),
                            id="category",
                            class_="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                        ),
                        class_="col-span-2 sm:col-span-1",
                    ),
                    # Description field
                    html.div(
                        html.label(
                            "Product Description",
                            **{"for": "description"},
                            class_="block mb-2 text-sm font-medium text-gray-900 dark:text-white",
                        ),
                        html.textarea(
                            id="description",
                            rows=4,
                            class_="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                            placeholder="Write product description here",
                        ),
                        class_="col-span-2",
                    ),
                    class_="grid gap-4 mb-4 grid-cols-2",
                ),
            ),
            footer=Button(
                label="Add new product",
                color=Color.PRIMARY,
                icon=get_icon(Icon.PLUS, class_="me-1 -ms-1 w-5 h-5"),
                attrs={"type": "submit"},
            ),
        ),
        # Size variants
        html.h2(
            "Size variants",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Choose from small, medium, large, or extra large modal sizes to fit your content.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Small modal",
                color=Color.PRIMARY,
                attrs={"data-modal-toggle": "small-modal"},
            ),
            Button(
                label="Medium modal",
                color=Color.SECONDARY,
                attrs={"data-modal-toggle": "medium-modal"},
            ),
            Button(
                label="Large modal",
                color=Color.DARK,
                attrs={"data-modal-toggle": "large-modal"},
            ),
            Button(
                label="Extra large modal",
                color=Color.GREEN,
                attrs={"data-modal-toggle": "xl-modal"},
            ),
            class_="flex gap-3",
        ),
        # Small modal
        Modal(
            id="small-modal",
            title="Small modal",
            size=Size.SM,
            children=html.p(
                "This is a small modal with max-width of 28rem (max-w-md).",
                class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
            ),
        ),
        # Medium modal (default)
        Modal(
            id="medium-modal",
            title="Medium modal (default)",
            size=Size.MD,
            children=html.p(
                "This is the default medium modal with max-width of 42rem (max-w-2xl).",
                class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
            ),
        ),
        # Large modal
        Modal(
            id="large-modal",
            title="Large modal",
            size=Size.LG,
            children=html.p(
                "This is a large modal with max-width of 56rem (max-w-4xl). Perfect for detailed content.",
                class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
            ),
        ),
        # Extra large modal
        Modal(
            id="xl-modal",
            title="Extra large modal",
            size=Size.XL,
            children=html.p(
                "This is an extra large modal with max-width of 64rem (max-w-5xl). Great for dashboards or complex forms.",
                class_="text-base leading-relaxed text-gray-500 dark:text-gray-400",
            ),
        ),
        # Confirmation modal (simple, no footer)
        html.h2(
            "Confirmation modal",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Simple confirmation modal without a footer. Use for notifications or quick alerts.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Show notification",
                color=Color.PRIMARY,
                attrs={"data-modal-toggle": "notification-modal"},
            ),
            class_="flex gap-3",
        ),
        Modal(
            id="notification-modal",
            title="Success!",
            size=Size.SM,
            children=html.div(
                get_icon(Icon.CHECK, class_="mx-auto mb-4 text-green-500 w-12 h-12"),
                html.p(
                    "Your changes have been saved successfully!",
                    class_="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400",
                ),
                class_="text-center",
            ),
        ),
        class_="space-y-8",
    )
