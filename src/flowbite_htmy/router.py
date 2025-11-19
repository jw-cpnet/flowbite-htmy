"""FastAPI router for serving flowbite-htmy static assets.

This module provides a pre-configured FastAPI router that serves the
flowbite-htmy.js initialization file. Include this router in your
FastAPI application to make the initialization script available.

Example usage:
    ```python
    from fastapi import FastAPI
    from flowbite_htmy.router import router as flowbite_router

    app = FastAPI()
    app.include_router(flowbite_router, prefix="/_flowbite_htmy")
    ```

The router serves:
- GET /_flowbite_htmy/flowbite-htmy.js - Initialization script for Flowbite components
"""

import importlib.resources

from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(tags=["flowbite-htmy"])


@router.get("/flowbite-htmy.js")
def get_flowbite_htmy_js() -> Response:
    """Serve the flowbite-htmy.js initialization script.

    This endpoint serves the bundled JavaScript file that initializes
    Flowbite components (modals, toasts, drawers, etc.) used by
    flowbite-htmy components.

    The script should be included in your HTML after the Flowbite JS library:
        ```html
        <script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"></script>
        <script src="/_flowbite_htmy/flowbite-htmy.js" defer></script>
        ```

    Returns:
        JavaScript file with appropriate content-type header.
        Returns 404 if the file cannot be found.

    Response Headers:
        Content-Type: application/javascript
        Cache-Control: public, max-age=3600 (1 hour)
    """
    try:
        # Read the JavaScript file from the package
        js_content = importlib.resources.read_text("flowbite_htmy", "flowbite-htmy.js")

        return Response(
            content=js_content,
            media_type="application/javascript",
            headers={
                # Cache for 1 hour - adjust based on your deployment strategy
                "Cache-Control": "public, max-age=3600"
            },
        )
    except FileNotFoundError:
        return Response(
            content="/* flowbite-htmy.js not found */",
            media_type="application/javascript",
            status_code=404,
        )


@router.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint for the flowbite-htmy router.

    Returns:
        Simple JSON response indicating the router is working.
    """
    return {"status": "ok", "service": "flowbite-htmy"}


__all__ = ["router"]
