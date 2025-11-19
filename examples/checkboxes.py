"""Checkboxes showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Checkbox


def build_checkboxes_showcase():
    """Build comprehensive checkboxes showcase content.

    Extracted for reuse in consolidated showcase application.
    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Section 1: Basic Checkbox
        html.div(
            html.h3(
                "1. Basic Checkbox",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Simple checkbox with label",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(id="terms", label="I agree to the terms and conditions"),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 2: Checked Checkbox
        html.div(
            html.h3(
                "2. Checked Checkbox",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Pre-checked checkbox",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="promo",
                label="I want to get promotional offers",
                checked=True,
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 3: Required Checkbox
        html.div(
            html.h3(
                "3. Required Checkbox",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Required field",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="age",
                label="I am 18 years or older",
                required=True,
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 4: Disabled Checkbox
        html.div(
            html.h3(
                "4. Disabled Checkbox",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Disabled state (grayed out)",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="shipping",
                label="Eligible for international shipping (disabled)",
                disabled=True,
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 5: With Helper Text
        html.div(
            html.h3(
                "5. With Helper Text",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Checkbox with additional context below label",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="free-shipping",
                label="Free shipping via Flowbite",
                helper_text="For orders shipped from $25 in books or $29 in other categories",
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 6: With HTML Label
        html.div(
            html.h3(
                "6. With HTML Label",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Label can contain links and formatting",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="privacy",
                label=html.span(
                    "I agree to the ",
                    html.a(
                        "privacy policy",
                        href="#",
                        class_="text-blue-600 hover:underline dark:text-blue-500",
                    ),
                    " and ",
                    html.a(
                        "terms of service",
                        href="#",
                        class_="text-blue-600 hover:underline dark:text-blue-500",
                    ),
                ),
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 7: Success Validation
        html.div(
            html.h3(
                "7. Success Validation",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Checkbox with success state (green)",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="newsletter",
                label="Subscribe to newsletter",
                validation="success",
                helper_text="You'll receive weekly updates about new products",
                checked=True,
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 8: Error Validation
        html.div(
            html.h3(
                "8. Error Validation",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Checkbox with error state (red)",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            Checkbox(
                id="consent",
                label="I agree to data processing",
                validation="error",
                helper_text="You must accept to continue with the registration",
                required=True,
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 9: Checkbox Group
        html.div(
            html.h3(
                "9. Checkbox Group (Colors)",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Multiple checkboxes with same name for multi-select",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            html.fieldset(
                html.legend(
                    "Select colors:",
                    class_="mb-4 font-semibold text-gray-900 dark:text-white",
                ),
                Checkbox(id="color-red", name="colors", value="red", label="Red"),
                Checkbox(
                    id="color-blue",
                    name="colors",
                    value="blue",
                    label="Blue",
                    checked=True,
                ),
                Checkbox(
                    id="color-green",
                    name="colors",
                    value="green",
                    label="Green",
                    checked=True,
                ),
                Checkbox(id="color-yellow", name="colors", value="yellow", label="Yellow"),
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 10: Subscription Preferences
        html.div(
            html.h3(
                "10. Subscription Preferences",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Practical example with helper text on each option",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            html.fieldset(
                html.legend(
                    "Email Preferences:",
                    class_="mb-4 font-semibold text-gray-900 dark:text-white",
                ),
                Checkbox(
                    id="pref-news",
                    label="Product news and updates",
                    helper_text="Get notified about new features and releases",
                    checked=True,
                ),
                Checkbox(
                    id="pref-tips",
                    label="Tips and tutorials",
                    helper_text="Learn how to get the most out of our platform",
                    checked=True,
                ),
                Checkbox(
                    id="pref-offers",
                    label="Special offers and promotions",
                    helper_text="Exclusive deals for subscribers",
                ),
                class_="space-y-4",
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 11: Terms Agreement
        html.div(
            html.h3(
                "11. Terms Agreement",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Common pattern for registration forms",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            html.div(
                Checkbox(
                    id="accept-terms",
                    label=html.span(
                        "I accept the ",
                        html.a(
                            "Terms and Conditions",
                            href="#",
                            class_="font-medium text-blue-600 hover:underline dark:text-blue-500",
                        ),
                    ),
                    required=True,
                ),
                Checkbox(
                    id="accept-privacy",
                    label=html.span(
                        "I accept the ",
                        html.a(
                            "Privacy Policy",
                            href="#",
                            class_="font-medium text-blue-600 hover:underline dark:text-blue-500",
                        ),
                    ),
                    required=True,
                ),
                Checkbox(
                    id="accept-marketing",
                    label="I want to receive marketing communications",
                ),
                class_="space-y-4",
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 12: Feature Toggles
        html.div(
            html.h3(
                "12. Feature Toggles",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Settings panel example",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            html.div(
                html.h4(
                    "Notification Settings",
                    class_="mb-4 text-lg font-semibold text-gray-900 dark:text-white",
                ),
                Checkbox(
                    id="notify-email",
                    label="Email notifications",
                    helper_text="Receive notifications via email",
                    checked=True,
                ),
                Checkbox(
                    id="notify-push",
                    label="Push notifications",
                    helper_text="Get instant alerts on your device",
                    checked=True,
                ),
                Checkbox(
                    id="notify-sms",
                    label="SMS notifications",
                    helper_text="Receive text message alerts (carrier rates may apply)",
                ),
                Checkbox(
                    id="notify-digest",
                    label="Daily digest",
                    helper_text="Get a summary of activity once per day",
                    checked=True,
                ),
                class_="space-y-4",
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        # Section 13: Table Selection
        html.div(
            html.h3(
                "13. Table Selection",
                class_="text-xl font-semibold text-gray-900 dark:text-white mb-2",
            ),
            html.p(
                "Checkbox in table rows for bulk actions",
                class_="text-sm text-gray-600 dark:text-gray-400 mb-4",
            ),
            html.div(
                html.table(
                    html.thead(
                        html.tr(
                            html.th(
                                Checkbox(
                                    id="select-all",
                                    label="",
                                    attrs={"aria-label": "Select all"},
                                ),
                                scope="col",
                                class_="p-4 w-4",
                            ),
                            html.th("Product name", scope="col", class_="px-6 py-3"),
                            html.th("Category", scope="col", class_="px-6 py-3"),
                            html.th("Price", scope="col", class_="px-6 py-3"),
                            class_="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400",
                        ),
                    ),
                    html.tbody(
                        html.tr(
                            html.td(
                                Checkbox(
                                    id="select-1",
                                    label="",
                                    attrs={"aria-label": "Select row"},
                                ),
                                class_="p-4 w-4",
                            ),
                            html.td(
                                'Apple MacBook Pro 17"',
                                class_="px-6 py-4 font-medium text-gray-900 dark:text-white",
                            ),
                            html.td("Laptop", class_="px-6 py-4"),
                            html.td("$2999", class_="px-6 py-4"),
                            class_="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600",
                        ),
                        html.tr(
                            html.td(
                                Checkbox(
                                    id="select-2",
                                    label="",
                                    attrs={"aria-label": "Select row"},
                                ),
                                class_="p-4 w-4",
                            ),
                            html.td(
                                "Microsoft Surface Pro",
                                class_="px-6 py-4 font-medium text-gray-900 dark:text-white",
                            ),
                            html.td("Laptop PC", class_="px-6 py-4"),
                            html.td("$1999", class_="px-6 py-4"),
                            class_="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600",
                        ),
                        html.tr(
                            html.td(
                                Checkbox(
                                    id="select-3",
                                    label="",
                                    attrs={"aria-label": "Select row"},
                                ),
                                class_="p-4 w-4",
                            ),
                            html.td(
                                "Magic Mouse 2",
                                class_="px-6 py-4 font-medium text-gray-900 dark:text-white",
                            ),
                            html.td("Accessories", class_="px-6 py-4"),
                            html.td("$99", class_="px-6 py-4"),
                            class_="bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600",
                        ),
                    ),
                    class_="w-full text-sm text-left text-gray-500 dark:text-gray-400",
                ),
                class_="relative overflow-x-auto shadow-md sm:rounded-lg",
            ),
            class_="mb-8 p-6 bg-white dark:bg-gray-800 rounded-lg shadow",
        ),
        class_="space-y-8",
    )
