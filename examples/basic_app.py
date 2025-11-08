"""Example FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/basic_app.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, html

from flowbite_htmy.components import Button
from flowbite_htmy.icons import Payment, Social, get_payment_icon, get_social_icon
from flowbite_htmy.types import ButtonVariant, Color, Size

app = FastAPI(title="Flowbite-HTMY Button Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the button showcase page using Jinja layout + htmy components."""

    # Build comprehensive button showcase
    buttons_section = html.div(
        # Default buttons
        html.h2(
            "Default buttons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use these default button styles with multiple colors to indicate an action or link within your website.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Default", color=Color.PRIMARY),
            Button(label="Alternative", color=Color.SECONDARY),
            Button(label="Dark", color=Color.DARK),
            Button(label="Light", color=Color.LIGHT),
            Button(label="Green", color=Color.GREEN),
            Button(label="Red", color=Color.RED),
            Button(label="Yellow", color=Color.YELLOW),
            Button(label="Purple", color=Color.PURPLE),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Button pills
        html.h2(
            "Button pills",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Use the pill prop for fully rounded buttons.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Default", color=Color.PRIMARY, pill=True),
            Button(label="Alternative", color=Color.SECONDARY, pill=True),
            Button(label="Dark", color=Color.DARK, pill=True),
            Button(label="Light", color=Color.LIGHT, pill=True),
            Button(label="Green", color=Color.GREEN, pill=True),
            Button(label="Red", color=Color.RED, pill=True),
            Button(label="Yellow", color=Color.YELLOW, pill=True),
            Button(label="Purple", color=Color.PURPLE, pill=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Gradient monochrome
        html.h2(
            "Gradient monochrome",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Gradient buttons with a single color.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Blue", color=Color.BLUE, variant=ButtonVariant.GRADIENT),
            Button(label="Green", color=Color.GREEN, variant=ButtonVariant.GRADIENT),
            Button(label="Cyan", color=Color.CYAN, variant=ButtonVariant.GRADIENT),
            Button(label="Teal", color=Color.TEAL, variant=ButtonVariant.GRADIENT),
            Button(label="Lime", color=Color.LIME, variant=ButtonVariant.GRADIENT),
            Button(label="Red", color=Color.RED, variant=ButtonVariant.GRADIENT),
            Button(label="Pink", color=Color.PINK, variant=ButtonVariant.GRADIENT),
            Button(label="Purple", color=Color.PURPLE, variant=ButtonVariant.GRADIENT),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Gradient duotone
        html.h2(
            "Gradient duotone",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Gradient buttons with two colors.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Purple to Blue", color="purple-blue", variant=ButtonVariant.GRADIENT),
            Button(label="Cyan to Blue", color="cyan-blue", variant=ButtonVariant.GRADIENT),
            Button(label="Green to Blue", color="green-blue", variant=ButtonVariant.GRADIENT),
            Button(label="Purple to Pink", color="purple-pink", variant=ButtonVariant.GRADIENT),
            Button(label="Pink to Orange", color="pink-orange", variant=ButtonVariant.GRADIENT),
            Button(label="Teal to Lime", color="teal-lime", variant=ButtonVariant.GRADIENT),
            Button(label="Red to Yellow", color="red-yellow", variant=ButtonVariant.GRADIENT),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Gradient outline
        html.h2(
            "Outlined gradient",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Gradient buttons with outlined style and transparent background.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Purple to blue", color="purple-blue", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Cyan to blue", color="cyan-blue", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Green to blue", color="green-blue", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Purple to pink", color="purple-pink", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Pink to orange", color="pink-orange", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Teal to Lime", color="teal-lime", variant=ButtonVariant.GRADIENT_OUTLINE),
            Button(label="Red to Yellow", color="red-yellow", variant=ButtonVariant.GRADIENT_OUTLINE),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Outline buttons
        html.h2(
            "Outline buttons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Outlined buttons with transparent backgrounds.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Default", color=Color.PRIMARY, variant=ButtonVariant.OUTLINE),
            Button(label="Dark", color=Color.DARK, variant=ButtonVariant.OUTLINE),
            Button(label="Green", color=Color.SUCCESS, variant=ButtonVariant.OUTLINE),
            Button(label="Red", color=Color.DANGER, variant=ButtonVariant.OUTLINE),
            Button(label="Yellow", color=Color.WARNING, variant=ButtonVariant.OUTLINE),
            Button(label="Purple", color=Color.PURPLE, variant=ButtonVariant.OUTLINE),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Button sizes
        html.h2(
            "Button sizes",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Buttons in different sizes from extra small to extra large.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Extra small", color=Color.PRIMARY, size=Size.XS),
            Button(label="Small", color=Color.PRIMARY, size=Size.SM),
            Button(label="Base", color=Color.PRIMARY, size=Size.MD),
            Button(label="Large", color=Color.PRIMARY, size=Size.LG),
            Button(label="Extra large", color=Color.PRIMARY, size=Size.XL),
            class_="flex flex-wrap items-center gap-2 mb-12",
        ),

        # Colored shadows
        html.h2(
            "Colored shadows",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Add colored shadows to gradient buttons.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Blue", color=Color.BLUE, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Green", color=Color.GREEN, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Cyan", color=Color.CYAN, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Teal", color=Color.TEAL, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Lime", color=Color.LIME, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Red", color=Color.RED, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Pink", color=Color.PINK, variant=ButtonVariant.GRADIENT, shadow=True),
            Button(label="Purple", color=Color.PURPLE, variant=ButtonVariant.GRADIENT, shadow=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Loading state
        html.h2(
            "Loading state",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Buttons with loading spinners.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(label="Loading", color=Color.PRIMARY, loading=True),
            Button(label="Loading", color=Color.SUCCESS, loading=True),
            Button(label="Loading", color=Color.DANGER, loading=True),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Social login buttons
        html.h2(
            "Social login buttons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Brand-specific buttons with SVG icons.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Sign in with Facebook",
                icon=get_social_icon(Social.FACEBOOK),
                color=Color.NONE,
                class_="text-white bg-[#3b5998] hover:bg-[#3b5998]/90 focus:ring-[#3b5998]/50 dark:focus:ring-[#3b5998]/55",
            ),
            Button(
                label="Sign in with Twitter",
                icon=get_social_icon(Social.TWITTER),
                color=Color.NONE,
                class_="text-white bg-[#1da1f2] hover:bg-[#1da1f2]/90 focus:ring-[#1da1f2]/50 dark:focus:ring-[#1da1f2]/55",
            ),
            Button(
                label="Sign in with Github",
                icon=get_social_icon(Social.GITHUB),
                color=Color.NONE,
                class_="text-white bg-[#24292F] hover:bg-[#24292F]/90 focus:ring-[#24292F]/50 dark:focus:ring-gray-500 dark:hover:bg-[#050708]/30",
            ),
            Button(
                label="Sign in with Google",
                icon=get_social_icon(Social.GOOGLE),
                color=Color.NONE,
                class_="text-white bg-[#4285F4] hover:bg-[#4285F4]/90 focus:ring-[#4285F4]/50 dark:focus:ring-[#4285F4]/55",
            ),
            Button(
                label="Sign in with Apple",
                icon=get_social_icon(Social.APPLE),
                color=Color.NONE,
                class_="text-white bg-[#050708] hover:bg-[#050708]/90 focus:ring-[#050708]/50 dark:focus:ring-[#050708]/50 dark:hover:bg-[#050708]/30",
            ),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # Payment buttons
        html.h2(
            "Payment buttons",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Payment provider buttons with brand logos and colors.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Button(
                label="Connect with MetaMask",
                icon=get_payment_icon(Payment.METAMASK),
                color=Color.NONE,
                class_="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-gray-100 dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700",
            ),
            Button(
                label="Connect with Opera Wallet",
                icon=get_payment_icon(Payment.OPERA_WALLET),
                color=Color.NONE,
                class_="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-gray-100 dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700",
            ),
            Button(
                label="Pay with Bitcoin",
                icon=get_payment_icon(Payment.BITCOIN),
                color=Color.NONE,
                class_="text-white bg-[#FF9119] hover:bg-[#FF9119]/80 focus:ring-[#FF9119]/50 dark:hover:bg-[#FF9119]/80 dark:focus:ring-[#FF9119]/40",
            ),
            Button(
                label="Check out with PayPal",
                icon=get_payment_icon(Payment.PAYPAL),
                color=Color.NONE,
                class_="text-gray-900 bg-[#F7BE38] hover:bg-[#F7BE38]/90 focus:ring-[#F7BE38]/50 dark:focus:ring-[#F7BE38]/50",
            ),
            Button(
                label="Check out with Apple Pay",
                icon=get_payment_icon(Payment.APPLE_PAY),
                color=Color.NONE,
                class_="text-white bg-[#050708] hover:bg-[#050708]/80 focus:ring-[#050708]/50 dark:hover:bg-[#050708]/40 dark:focus:ring-gray-600",
            ),
            Button(
                label="Pay with American Express",
                icon=get_payment_icon(Payment.AMEX),
                color=Color.NONE,
                class_="text-white bg-[#2557D6] hover:bg-[#2557D6]/90 focus:ring-[#2557D6]/50 dark:focus:ring-[#2557D6]/50",
            ),
            Button(
                label="Pay with Visa",
                icon=get_payment_icon(Payment.VISA),
                color=Color.NONE,
                class_="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-gray-100 dark:focus:ring-gray-800 dark:bg-white dark:border-gray-700 dark:text-gray-900 dark:hover:bg-gray-200",
            ),
            Button(
                label="Pay with MasterCard",
                icon=get_payment_icon(Payment.MASTERCARD),
                color=Color.NONE,
                class_="text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-gray-100 dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700",
            ),
            Button(
                label="Pay with Ethereum",
                icon=get_payment_icon(Payment.ETHEREUM),
                color=Color.NONE,
                class_="text-gray-900 bg-gray-100 hover:bg-gray-200 focus:ring-gray-100 dark:focus:ring-gray-500",
            ),
            class_="flex flex-wrap gap-2 mb-12",
        ),

        # HTMX interactive example
        html.h2(
            "Interactive HTMX Button",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4",
        ),
        html.p(
            "Click the button below to see server-side rendering with HTMX:",
            class_="text-gray-600 dark:text-gray-400 mb-4",
        ),
        Button(
            label="Click Me!",
            color=Color.INFO,
            hx_get="/clicked",
            hx_target="#result",
            hx_swap="innerHTML",
        ),
        html.div(
            html.p(
                "Waiting for button click...",
                class_="text-gray-500 dark:text-gray-400 italic",
            ),
            id="result",
            class_="mt-4 p-4 rounded-lg bg-gray-100 dark:bg-gray-800",
        ),
    )

    # Render htmy components to HTML string
    content_html = await renderer.render(buttons_section)

    # Return context for Jinja template
    return {
        "title": "Flowbite-HTMY Button Showcase",
        "subtitle": "Comprehensive button variants - all Flowbite styles supported",
        "content": content_html,
    }


@app.get("/clicked")
async def clicked() -> str:
    """HTMX endpoint - returns rendered htmy component."""
    from flowbite_htmy.components import Alert

    alert = Alert(
        title="Success!",
        message="Button clicked! This Alert component was rendered server-side with htmy and returned via HTMX.",
        color=Color.SUCCESS,
    )

    # Return raw HTML (fasthx handles HTMLResponse automatically for HTMX requests)
    return await renderer.render(alert)


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Flowbite-HTMY Hybrid Example")
    print("📍 Visit: http://localhost:8000")
    print("✨ Jinja for layouts + htmy for components!")
    print("🌙 Dark mode toggle in top-right corner")
    uvicorn.run("basic_app:app", host="0.0.0.0", port=8000, reload=True)
