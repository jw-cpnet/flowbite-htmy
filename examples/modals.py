"""Modal showcase FastAPI application using hybrid Jinja + htmy approach.

This demonstrates the recommended pattern:
- Jinja templates for page layouts and JavaScript (including Flowbite JS for modal functionality)
- htmy components for UI elements (type-safe, composable)
- fasthx for integration between FastAPI and both systems

Run with: python examples/modals.py
Then visit: http://localhost:8000
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fasthx.jinja import Jinja
from htmy import Renderer, SafeStr, html

from flowbite_htmy.components import Button, Modal, PopupModal
from flowbite_htmy.types import Color, Size

app = FastAPI(title="Flowbite-HTMY Modal Showcase")
templates = Jinja2Templates(directory="examples/templates")
jinja = Jinja(templates)
renderer = Renderer()


@app.get("/")
@jinja.page("base.html.jinja")
async def index() -> dict:
    """Render the modal showcase page using Jinja layout + htmy components."""

    # Build comprehensive modal showcase
    modals_section = html.div(
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
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
                </p>
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    The European Union's General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.
                </p>
                """
            ),
            footer=SafeStr(
                """
                <button data-modal-hide="default-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                <button data-modal-hide="default-modal" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Decline</button>
                """
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
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
                </p>
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    The European Union's General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.
                </p>
                """
            ),
            footer=SafeStr(
                """
                <button data-modal-hide="static-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                <button data-modal-hide="static-modal" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Decline</button>
                """
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
            icon=SafeStr(
                """
                <svg class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
                </svg>
                """
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
            children=SafeStr(
                """
                <form>
                    <div class="grid gap-4 mb-4 grid-cols-2">
                        <div class="col-span-2">
                            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                            <input type="text" name="name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Type product name" required="">
                        </div>
                        <div class="col-span-2 sm:col-span-1">
                            <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                            <input type="number" name="price" id="price" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="$2999" required="">
                        </div>
                        <div class="col-span-2 sm:col-span-1">
                            <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Category</label>
                            <select id="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                                <option selected="">Select category</option>
                                <option value="TV">TV/Monitors</option>
                                <option value="PC">PC</option>
                                <option value="GA">Gaming/Console</option>
                                <option value="PH">Phones</option>
                            </select>
                        </div>
                        <div class="col-span-2">
                            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Product Description</label>
                            <textarea id="description" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write product description here"></textarea>
                        </div>
                    </div>
                    <button type="submit" class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd"></path></svg>
                        Add new product
                    </button>
                </form>
                """
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
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    This is a small modal with max-width of 28rem (max-w-md).
                </p>
                """
            ),
        ),
        # Medium modal (default)
        Modal(
            id="medium-modal",
            title="Medium modal (default)",
            size=Size.MD,
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    This is the default medium modal with max-width of 42rem (max-w-2xl).
                </p>
                """
            ),
        ),
        # Large modal
        Modal(
            id="large-modal",
            title="Large modal",
            size=Size.LG,
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    This is a large modal with max-width of 56rem (max-w-4xl). Perfect for detailed content.
                </p>
                """
            ),
        ),
        # Extra large modal
        Modal(
            id="xl-modal",
            title="Extra large modal",
            size=Size.XL,
            children=SafeStr(
                """
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    This is an extra large modal with max-width of 64rem (max-w-5xl). Great for dashboards or complex forms.
                </p>
                """
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
            children=SafeStr(
                """
                <div class="text-center">
                    <svg class="mx-auto mb-4 text-green-500 w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <p class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
                        Your changes have been saved successfully!
                    </p>
                </div>
                """
            ),
        ),
        class_="space-y-8",
    )

    # Render the section to HTML
    rendered_modals = await renderer.render(modals_section)

    return {
        "title": "Modal Showcase - Flowbite HTMY",
        "heading": "Modal Component",
        "description": "Interactive dialog overlays powered by Flowbite JS. Modals require Flowbite JavaScript to function.",
        "content": rendered_modals,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
