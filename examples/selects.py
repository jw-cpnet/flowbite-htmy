"""Selects showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Select


def build_selects_showcase():
    """Build comprehensive selects showcase content.

    Extracted for reuse in consolidated showcase application.
    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Default select
        html.h2(
            "Default select",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the following example to show a simple select dropdown with a label, options, and helper text.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="countries",
                label="Select your country",
                placeholder="Choose a country",
                options=[
                    {"value": "US", "label": "United States"},
                    {"value": "CA", "label": "Canada"},
                    {"value": "FR", "label": "France"},
                    {"value": "DE", "label": "Germany"},
                    {"value": "IT", "label": "Italy"},
                    {"value": "ES", "label": "Spain"},
                ],
            ),
            class_="max-w-sm mb-8",
        ),
        # Simple string options
        html.h2(
            "Simple options",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "You can pass a simple list of strings for options when you don't need separate values and labels.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="colors",
                label="Choose your favorite color",
                options=["Red", "Blue", "Green", "Yellow", "Purple", "Orange"],
            ),
            class_="max-w-sm mb-8",
        ),
        # With helper text
        html.h2(
            "With helper text",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Add helper text below the select field to provide additional context or instructions.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="shipping",
                label="Shipping region",
                placeholder="Select shipping region",
                options=[
                    {"value": "NA", "label": "North America"},
                    {"value": "EU", "label": "Europe"},
                    {"value": "AS", "label": "Asia"},
                    {"value": "SA", "label": "South America"},
                    {"value": "AF", "label": "Africa"},
                    {"value": "AU", "label": "Australia & Oceania"},
                ],
                helper_text="Choose the region for shipping cost calculation",
            ),
            class_="max-w-sm mb-8",
        ),
        # Validation states
        html.h2(
            "Validation states",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Show validation feedback with success and error states.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Select(
                    id="country_success",
                    label="Country",
                    options=[
                        {"value": "US", "label": "United States"},
                        {"value": "CA", "label": "Canada"},
                        {"value": "MX", "label": "Mexico"},
                    ],
                    value="US",
                    validation="success",
                    helper_text="Valid country selected!",
                ),
                class_="mb-6",
            ),
            html.div(
                Select(
                    id="country_error",
                    label="Country",
                    options=[
                        {"value": "US", "label": "United States"},
                        {"value": "CA", "label": "Canada"},
                        {"value": "MX", "label": "Mexico"},
                    ],
                    validation="error",
                    helper_text="Please select a valid country from the list",
                ),
            ),
            class_="max-w-sm mb-8",
        ),
        # Required field
        html.h2(
            "Required field",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the required attribute to make the select field mandatory.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="terms",
                label="Terms & Conditions",
                options=[
                    {"value": "accept", "label": "I accept"},
                    {"value": "decline", "label": "I decline"},
                ],
                required=True,
                helper_text="You must accept the terms to continue",
            ),
            class_="max-w-sm mb-8",
        ),
        # Disabled field
        html.h2(
            "Disabled state",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Disable the select field when user input is not allowed.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="disabled_select",
                label="Disabled select",
                options=[
                    "Option 1",
                    "Option 2",
                    "Option 3",
                ],
                value="Option 1",
                disabled=True,
                helper_text="This field is currently disabled",
            ),
            class_="max-w-sm mb-8",
        ),
        # Multiple selection
        html.h2(
            "Multiple selection",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Allow users to select multiple options by adding the multiple attribute.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="languages",
                label="Programming languages",
                options=[
                    "Python",
                    "JavaScript",
                    "TypeScript",
                    "Java",
                    "C++",
                    "Go",
                    "Rust",
                    "Ruby",
                ],
                multiple=True,
                helper_text="Hold Ctrl (Cmd on Mac) to select multiple languages",
            ),
            class_="max-w-sm mb-8",
        ),
        # Size attribute
        html.h2(
            "Visible options (size)",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use the size attribute to specify how many options are visible at once in a scrollable list.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="years",
                label="Select year",
                options=[
                    "2024",
                    "2023",
                    "2022",
                    "2021",
                    "2020",
                    "2019",
                    "2018",
                    "2017",
                    "2016",
                    "2015",
                ],
                size=5,
                helper_text="Shows 5 years at a time",
            ),
            class_="max-w-sm mb-8",
        ),
        # Pre-selected value
        html.h2(
            "Pre-selected value",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Set a default selected value using the value prop.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="timezone",
                label="Time zone",
                options=[
                    {"value": "UTC-8", "label": "Pacific Time (UTC-8)"},
                    {"value": "UTC-7", "label": "Mountain Time (UTC-7)"},
                    {"value": "UTC-6", "label": "Central Time (UTC-6)"},
                    {"value": "UTC-5", "label": "Eastern Time (UTC-5)"},
                    {"value": "UTC", "label": "Coordinated Universal Time (UTC)"},
                ],
                value="UTC-5",
                helper_text="Your current time zone",
            ),
            class_="max-w-sm mb-8",
        ),
        # Categories with options
        html.h2(
            "Product categories",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "A practical example showing product categories in an e-commerce context.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Select(
                id="category",
                label="Product category",
                placeholder="Select category",
                options=[
                    {"value": "electronics", "label": "Electronics"},
                    {"value": "clothing", "label": "Clothing & Fashion"},
                    {"value": "books", "label": "Books & Media"},
                    {"value": "home", "label": "Home & Garden"},
                    {"value": "sports", "label": "Sports & Outdoors"},
                    {"value": "toys", "label": "Toys & Games"},
                    {"value": "automotive", "label": "Automotive"},
                    {"value": "health", "label": "Health & Beauty"},
                ],
                required=True,
                helper_text="Choose the main category for your product listing",
            ),
            class_="max-w-sm mb-8",
        ),
        class_="max-w-4xl mx-auto p-8",
    )
