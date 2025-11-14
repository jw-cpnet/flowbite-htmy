"""Radio button component showcase application."""

from fasthx import Jinja
from fastapi import FastAPI
from htmy import html

from flowbite_htmy.components import Radio
from flowbite_htmy.types import ValidationState

app = FastAPI()
jinja = Jinja(app)


def build_radios_showcase():
    """Build comprehensive radio button showcase content."""
    return html.div(
        # Section 1: Basic Radio Groups
        html.h2(
            "Basic Radio Groups", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"
        ),
        html.p(
            "Simple radio button groups for single-selection forms.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            # Payment method example
            html.div(
                html.h3(
                    "Payment Method",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(label="Credit Card", name="payment", value="credit", checked=True),
                    Radio(label="PayPal", name="payment", value="paypal"),
                    Radio(label="Bank Transfer", name="payment", value="bank"),
                    Radio(label="Cryptocurrency", name="payment", value="crypto"),
                    class_="space-y-2",
                ),
                class_="mb-6",
            ),
            # Shipping method example
            html.div(
                html.h3(
                    "Shipping Method",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(
                        label="Standard Shipping (5-7 days)",
                        name="shipping",
                        value="standard",
                        checked=True,
                    ),
                    Radio(label="Express Shipping (2-3 days)", name="shipping", value="express"),
                    Radio(label="Overnight Shipping (1 day)", name="shipping", value="overnight"),
                    class_="space-y-2",
                ),
                class_="mb-6",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 2: Validation States
        html.h2(
            "Validation States", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"
        ),
        html.p(
            "Radio buttons with error, success, and default validation states.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                html.h3(
                    "Delivery Options with Validation",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(
                        label="Pickup in Store",
                        name="delivery",
                        value="pickup",
                        validation_state=ValidationState.SUCCESS,
                        helper_text="Free - Available at 15 locations near you",
                        checked=True,
                    ),
                    Radio(
                        label="Home Delivery",
                        name="delivery",
                        value="home",
                        validation_state=ValidationState.DEFAULT,
                        helper_text="$5.99 - Delivered to your doorstep",
                    ),
                    Radio(
                        label="Express Delivery",
                        name="delivery",
                        value="express",
                        validation_state=ValidationState.ERROR,
                        helper_text="Not available in your region",
                        disabled=True,
                    ),
                    class_="space-y-3",
                ),
                class_="mb-6",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 3: Disabled States
        html.h2("Disabled States", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"),
        html.p(
            "Radio buttons in disabled states with reduced opacity.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                html.h3(
                    "Subscription Plans",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(label="Free Plan", name="plan", value="free", checked=True),
                    Radio(label="Pro Plan - $9/month", name="plan", value="pro"),
                    Radio(
                        label="Enterprise Plan - Contact Sales",
                        name="plan",
                        value="enterprise",
                        disabled=True,
                        helper_text="Currently at capacity",
                    ),
                    Radio(
                        label="Legacy Plan (Discontinued)",
                        name="plan",
                        value="legacy",
                        disabled=True,
                        checked=False,
                    ),
                    class_="space-y-2",
                ),
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 4: HTMX Integration
        html.h2("HTMX Integration", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"),
        html.p(
            "Radio buttons that trigger dynamic server updates.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                html.h3(
                    "Color Theme Selection",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(
                        label="Light Theme",
                        name="theme",
                        value="light",
                        hx_get="/update-theme?theme=light",
                        hx_target="#theme-preview",
                        hx_swap="innerHTML",
                        checked=True,
                    ),
                    Radio(
                        label="Dark Theme",
                        name="theme",
                        value="dark",
                        hx_get="/update-theme?theme=dark",
                        hx_target="#theme-preview",
                        hx_swap="innerHTML",
                    ),
                    Radio(
                        label="Auto (System Preference)",
                        name="theme",
                        value="auto",
                        hx_get="/update-theme?theme=auto",
                        hx_target="#theme-preview",
                        hx_swap="innerHTML",
                    ),
                    class_="space-y-2 mb-4",
                ),
                html.div(
                    html.p(
                        "Selected: Light Theme", class_="text-sm text-gray-600 dark:text-gray-400"
                    ),
                    id="theme-preview",
                    class_="p-3 bg-gray-100 dark:bg-gray-700 rounded",
                ),
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 5: Helper Text Examples
        html.h2(
            "Helper Text Examples", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"
        ),
        html.p(
            "Radio buttons with informative helper text.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                html.h3(
                    "Newsletter Frequency",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.div(
                    Radio(
                        label="Daily Digest",
                        name="newsletter",
                        value="daily",
                        helper_text="Receive updates every morning at 8 AM",
                    ),
                    Radio(
                        label="Weekly Summary",
                        name="newsletter",
                        value="weekly",
                        helper_text="Get a comprehensive summary every Monday",
                        checked=True,
                    ),
                    Radio(
                        label="Monthly Roundup",
                        name="newsletter",
                        value="monthly",
                        helper_text="Monthly highlights and key updates",
                    ),
                    Radio(
                        label="No Newsletter",
                        name="newsletter",
                        value="never",
                        helper_text="You can change this anytime in settings",
                    ),
                    class_="space-y-3",
                ),
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 6: Accessibility (Empty Label with aria-label)
        html.h2(
            "Accessibility Examples", class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white"
        ),
        html.p(
            "Radio buttons with aria-label for accessibility (no visible label).",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                html.h3(
                    "Color Selection (Icon Only)",
                    class_="text-lg font-semibold mb-3 text-gray-800 dark:text-gray-200",
                ),
                html.p(
                    "Screen readers will announce the color name:",
                    class_="text-sm text-gray-600 dark:text-gray-400 mb-2",
                ),
                html.div(
                    Radio(
                        label="",
                        aria_label="Select red color",
                        name="color",
                        value="red",
                        helper_text="Red",
                        class_="accent-red-600",
                    ),
                    Radio(
                        label="",
                        aria_label="Select blue color",
                        name="color",
                        value="blue",
                        helper_text="Blue",
                        class_="accent-blue-600",
                        checked=True,
                    ),
                    Radio(
                        label="",
                        aria_label="Select green color",
                        name="color",
                        value="green",
                        helper_text="Green",
                        class_="accent-green-600",
                    ),
                    class_="space-y-2",
                ),
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        class_="space-y-8",
    )


@app.get("/")
async def index():
    """Render radio showcase."""
    section = build_radios_showcase()
    return await jinja.render_template(
        "radio-layout.html.jinja",
        {"content": await jinja.render(section)},
    )


@app.get("/update-theme")
async def update_theme(theme: str):
    """HTMX endpoint for theme selection demo."""
    theme_messages = {
        "light": "Selected: Light Theme ☀️",
        "dark": "Selected: Dark Theme 🌙",
        "auto": "Selected: Auto (System Preference) 🔄",
    }
    message = theme_messages.get(theme, f"Selected: {theme}")
    return html.p(message, class_="text-sm text-gray-600 dark:text-gray-400")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
