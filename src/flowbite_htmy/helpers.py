"""Helper functions for including Flowbite assets in templates.

This module provides utility functions to generate HTML tags for including
Flowbite CSS, Flowbite JS, and flowbite-htmy initialization code in your
templates.

Example usage in a Jinja2 template:
    ```jinja2
    <head>
        {{ flowbite_css() | safe }}
        {{ htmx_script() | safe }}
    </head>
    <body>
        ...
        {{ flowbite_js() | safe }}
        {{ flowbite_init_js() | safe }}
    </body>
    ```

For production deployments, you may want to self-host these assets and
skip these helpers in favor of your own <link> and <script> tags.
"""

from flowbite_htmy import FLOWBITE_VERSION, HTMX_VERSION

# Default router prefix for the flowbite-htmy.js endpoint
DEFAULT_ROUTER_PREFIX = "/_flowbite_htmy"


def flowbite_css(version: str = FLOWBITE_VERSION) -> str:
    """Generate <link> tag for Flowbite CSS from CDN.

    Args:
        version: Flowbite version to use. Defaults to the library's version.

    Returns:
        HTML <link> tag as a string.

    Example:
        >>> flowbite_css()
        '<link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/..." rel="stylesheet" />'

        >>> flowbite_css("3.1.2")
        '<link href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/..." rel="stylesheet" />'
    """
    url = f"https://cdn.jsdelivr.net/npm/flowbite@{version}/dist/flowbite.min.css"
    return f'<link href="{url}" rel="stylesheet" />'


def flowbite_js(version: str = FLOWBITE_VERSION) -> str:
    """Generate <script> tag for Flowbite JavaScript from CDN.

    Args:
        version: Flowbite version to use. Defaults to the library's version.

    Returns:
        HTML <script> tag as a string.

    Example:
        >>> flowbite_js()
        '<script src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/..." defer></script>'
    """
    url = f"https://cdn.jsdelivr.net/npm/flowbite@{version}/dist/flowbite.min.js"
    return f'<script src="{url}" defer></script>'


def htmx_script(version: str = HTMX_VERSION) -> str:
    """Generate <script> tag for HTMX from CDN.

    Args:
        version: HTMX version to use. Defaults to the library's version.

    Returns:
        HTML <script> tag as a string.

    Example:
        >>> htmx_script()
        '<script src="https://unpkg.com/htmx.org@2.0.2"></script>'
    """
    url = f"https://unpkg.com/htmx.org@{version}"
    return f'<script src="{url}"></script>'


def flowbite_init_js(prefix: str = DEFAULT_ROUTER_PREFIX) -> str:
    """Generate <script> tag for flowbite-htmy initialization code.

    This script must be included AFTER the Flowbite JS library.
    It initializes Flowbite components (modals, toasts, drawers, etc.)
    used by flowbite-htmy components.

    The script is served from the FastAPI router that you must include
    in your application:

        ```python
        from flowbite_htmy.router import router as flowbite_router

        app.include_router(flowbite_router, prefix="/_flowbite_htmy")
        ```

    Args:
        prefix: URL prefix where the flowbite-htmy router is mounted.
                Defaults to "/_flowbite_htmy".

    Returns:
        HTML <script> tag as a string.

    Example:
        >>> flowbite_init_js()
        '<script src="/_flowbite_htmy/flowbite-htmy.js" defer></script>'

        >>> flowbite_init_js(prefix="/assets/flowbite")
        '<script src="/assets/flowbite/flowbite-htmy.js" defer></script>'
    """
    return f'<script src="{prefix}/flowbite-htmy.js" defer></script>'


def all_scripts(
    flowbite_version: str = FLOWBITE_VERSION,
    htmx_version: str = HTMX_VERSION,
    router_prefix: str = DEFAULT_ROUTER_PREFIX,
) -> str:
    """Generate all required script tags in the correct order.

    This is a convenience function that generates all necessary script tags
    for using flowbite-htmy components. The scripts are returned in the
    correct loading order.

    Args:
        flowbite_version: Flowbite version to use.
        htmx_version: HTMX version to use.
        router_prefix: URL prefix for the flowbite-htmy router.

    Returns:
        All <script> tags as a single string, separated by newlines.

    Example:
        In your Jinja2 template:
        ```jinja2
        <body>
            {{ content }}
            {{ all_scripts() | safe }}
        </body>
        ```
    """
    scripts = [
        htmx_script(htmx_version),
        flowbite_js(flowbite_version),
        flowbite_init_js(router_prefix),
    ]
    return "\n".join(scripts)


__all__ = [
    "flowbite_css",
    "flowbite_js",
    "htmx_script",
    "flowbite_init_js",
    "all_scripts",
]
