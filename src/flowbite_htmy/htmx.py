"""HTMX helper functions for Flowbite component interactions.

Generates JavaScript snippets for common HTMX + Flowbite patterns such as
closing drawers or modals after a successful request.

Example:
    ```python
    from flowbite_htmy.htmx import drawer_close_handler

    Button(
        label="Save",
        hx_post="/api/save",
        hx_on={"after-request": drawer_close_handler("my-drawer")},
    )
    ```
"""


def drawer_close_handler(
    drawer_id: str,
    *,
    reset_form: bool = False,
    extra_js: str = "",
) -> str:
    """Generate ``hx-on::after-request`` JS to close a Flowbite drawer.

    Args:
        drawer_id: Flowbite drawer ID to close.
        reset_form: If ``True``, reset the submitting form after success.
        extra_js: Additional JavaScript to execute inside the success block.

    Returns:
        JavaScript string suitable for ``hx-on::after-request`` or
        ``Button(hx_on={"after-request": ...})``.
    """
    parts = [
        "if(event.detail.successful) {",
        f"    const drawer = FlowbiteInstances.getInstance('Drawer', '{drawer_id}');",
        "    if (drawer) { drawer.hide(); }",
    ]
    if reset_form:
        parts.append(
            "    if (event.target && typeof event.target.reset === 'function') "
            "{ event.target.reset(); }"
        )
    if extra_js:
        parts.append(f"    {extra_js}")
    parts.append("}")
    return "\n".join(parts)


def modal_close_handler(
    modal_id: str,
    *,
    extra_js: str = "",
) -> str:
    """Generate ``hx-on::after-request`` JS to close a Flowbite modal.

    Args:
        modal_id: Flowbite modal ID to close.
        extra_js: Additional JavaScript to execute inside the success block.

    Returns:
        JavaScript string suitable for ``hx-on::after-request`` or
        ``Button(hx_on={"after-request": ...})``.
    """
    parts = [
        "if(event.detail.successful) {",
        f"    const modal = FlowbiteInstances.getInstance('Modal', '{modal_id}');",
        "    if (modal) { modal.hide(); }",
    ]
    if extra_js:
        parts.append(f"    {extra_js}")
    parts.append("}")
    return "\n".join(parts)


__all__ = [
    "drawer_close_handler",
    "modal_close_handler",
]
