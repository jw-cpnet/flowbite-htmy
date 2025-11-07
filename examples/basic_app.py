"""Basic example FastAPI application using flowbite-htmy.

This example will be expanded as components are implemented.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Components will be imported as they're implemented
# from flowbite_htmy.components import Button, Badge
# from flowbite_htmy.layouts import PageLayout

app = FastAPI(title="Flowbite-HTMY Example")


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    """Render the index page."""
    # This is a placeholder until we implement components
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flowbite-HTMY Example</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css" rel="stylesheet" />
        <script src="https://unpkg.com/htmx.org@2.0.2"></script>
    </head>
    <body class="bg-gray-50 dark:bg-gray-900">
        <div class="container mx-auto p-8">
            <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-4">
                Flowbite-HTMY Example
            </h1>
            <p class="text-gray-600 dark:text-gray-400">
                Components will be added here as they're implemented.
            </p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
