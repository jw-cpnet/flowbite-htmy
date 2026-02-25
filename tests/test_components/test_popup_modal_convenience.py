"""Tests for PopupModal convenience props (auto-generated buttons)."""

import pytest

from flowbite_htmy.components import PopupModal


@pytest.mark.asyncio
async def test_popup_modal_convenience_default_buttons(renderer):
    """Test PopupModal with convenience props generates buttons."""
    modal = PopupModal(
        id="confirm-delete",
        message="Are you sure?",
    )
    html = await renderer.render(modal)

    assert "Are you sure?" in html
    assert "Yes, I&#x27;m sure" in html or "Yes, I'm sure" in html
    assert "No, cancel" in html


@pytest.mark.asyncio
async def test_popup_modal_convenience_with_url(renderer):
    """Test PopupModal with confirm_url generates HTMX button."""
    modal = PopupModal(
        id="confirm-delete",
        message="Delete this item?",
        confirm_url="/api/items/123",
        confirm_method="delete",
    )
    html = await renderer.render(modal)

    assert 'hx-delete="/api/items/123"' in html


@pytest.mark.asyncio
async def test_popup_modal_convenience_with_target(renderer):
    """Test PopupModal with confirm_target adds hx-target."""
    modal = PopupModal(
        id="confirm-delete",
        message="Delete?",
        confirm_url="/api/items/123",
        confirm_target="#items-container",
    )
    html = await renderer.render(modal)

    assert 'hx-target="#items-container"' in html


@pytest.mark.asyncio
async def test_popup_modal_convenience_post_method(renderer):
    """Test PopupModal with post method."""
    modal = PopupModal(
        id="confirm-action",
        message="Proceed?",
        confirm_url="/api/action",
        confirm_method="post",
    )
    html = await renderer.render(modal)

    assert 'hx-post="/api/action"' in html


@pytest.mark.asyncio
async def test_popup_modal_convenience_custom_labels(renderer):
    """Test PopupModal with custom button labels."""
    modal = PopupModal(
        id="confirm",
        message="Delete?",
        confirm_label="Delete it",
        cancel_label="Keep it",
    )
    html = await renderer.render(modal)

    assert "Delete it" in html
    assert "Keep it" in html


@pytest.mark.asyncio
async def test_popup_modal_danger_styling(renderer):
    """Test PopupModal danger=True uses red styling."""
    modal = PopupModal(
        id="danger",
        message="Delete?",
        danger=True,
    )
    html = await renderer.render(modal)

    assert "bg-red-600" in html


@pytest.mark.asyncio
async def test_popup_modal_non_danger_styling(renderer):
    """Test PopupModal danger=False uses primary styling."""
    modal = PopupModal(
        id="non-danger",
        message="Confirm?",
        danger=False,
    )
    html = await renderer.render(modal)

    assert "bg-primary-600" in html
    assert "bg-red-600" not in html


@pytest.mark.asyncio
async def test_popup_modal_cancel_button_hides_modal(renderer):
    """Test auto-generated cancel button has data-modal-hide."""
    modal = PopupModal(
        id="test-modal",
        message="Test?",
    )
    html = await renderer.render(modal)

    assert 'data-modal-hide="test-modal"' in html


@pytest.mark.asyncio
async def test_popup_modal_explicit_buttons_override(renderer):
    """Test explicit confirm_button overrides convenience props."""
    from htmy import html as h

    custom_btn = h.button("Custom Confirm", type="button", class_="custom-btn")
    modal = PopupModal(
        id="override",
        message="Test?",
        confirm_button=custom_btn,
        confirm_url="/api/should-be-ignored",  # Should not appear
    )
    html = await renderer.render(modal)

    assert "Custom Confirm" in html
    assert "custom-btn" in html
    # The confirm_url should NOT generate a button since confirm_button takes precedence
    assert 'hx-delete="/api/should-be-ignored"' not in html
