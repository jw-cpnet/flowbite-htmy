"""Tests for PopupModal component."""

import pytest
from htmy import SafeStr

from flowbite_htmy.components import Button, PopupModal
from flowbite_htmy.types import Color


@pytest.mark.asyncio
async def test_popup_modal_renders_minimal(renderer):
    """Test PopupModal renders with minimal required props."""
    popup = PopupModal(
        id="test-popup",
        message="Are you sure?",
        confirm_button=Button(label="Yes", color=Color.RED),
    )
    html = await renderer.render(popup)

    # Check container attributes
    assert 'id="test-popup"' in html
    assert 'tabindex="-1"' in html
    assert 'aria-hidden="true"' in html

    # Check container classes
    assert "hidden" in html
    assert "fixed" in html
    assert "z-50" in html

    # Check message
    assert "Are you sure?" in html

    # Check close button exists and is positioned absolutely
    assert "Close modal" in html
    assert "absolute" in html

    # Check confirm button rendered
    assert "Yes" in html


@pytest.mark.asyncio
async def test_popup_modal_with_cancel_button(renderer):
    """Test PopupModal renders with both confirm and cancel buttons."""
    popup = PopupModal(
        id="confirm-popup",
        message="Delete this item?",
        confirm_button=Button(label="Yes, delete", color=Color.RED),
        cancel_button=Button(label="Cancel"),
    )
    html = await renderer.render(popup)

    assert "Delete this item?" in html
    assert "Yes, delete" in html
    assert "Cancel" in html


@pytest.mark.asyncio
async def test_popup_modal_with_icon(renderer):
    """Test PopupModal renders with custom icon."""
    icon_svg = SafeStr(
        '<svg class="test-icon"><path d="M10 10"/></svg>'
    )
    popup = PopupModal(
        id="icon-popup",
        message="Warning message",
        icon=icon_svg,
        confirm_button=Button(label="OK"),
    )
    html = await renderer.render(popup)

    assert "Warning message" in html
    assert "test-icon" in html
    assert '<svg class="test-icon">' in html


@pytest.mark.asyncio
async def test_popup_modal_static_backdrop(renderer):
    """Test PopupModal with static backdrop."""
    popup = PopupModal(
        id="static-popup",
        message="Important decision",
        confirm_button=Button(label="Confirm"),
        static_backdrop=True,
    )
    html = await renderer.render(popup)

    assert 'data-modal-backdrop="static"' in html


@pytest.mark.asyncio
async def test_popup_modal_custom_classes(renderer):
    """Test PopupModal accepts custom classes."""
    popup = PopupModal(
        id="custom-popup",
        message="Custom styled",
        confirm_button=Button(label="OK"),
        class_="my-custom-class",
    )
    html = await renderer.render(popup)

    assert "my-custom-class" in html


@pytest.mark.asyncio
async def test_popup_modal_passthrough_attributes(renderer):
    """Test PopupModal supports passthrough attributes."""
    popup = PopupModal(
        id="attrs-popup",
        message="Test attributes",
        confirm_button=Button(label="OK"),
        attrs={"data-testid": "popup-test", "aria-labelledby": "popup-label"},
    )
    html = await renderer.render(popup)

    assert 'data-testid="popup-test"' in html
    assert 'aria-labelledby="popup-label"' in html


@pytest.mark.asyncio
async def test_popup_modal_close_button_data_attribute(renderer):
    """Test PopupModal close button has correct data-modal-hide attribute."""
    popup = PopupModal(
        id="close-popup",
        message="Test close",
        confirm_button=Button(label="OK"),
    )
    html = await renderer.render(popup)

    assert 'data-modal-hide="close-popup"' in html


@pytest.mark.asyncio
async def test_popup_modal_centered_content(renderer):
    """Test PopupModal has centered text layout."""
    popup = PopupModal(
        id="centered-popup",
        message="Centered message",
        confirm_button=Button(label="OK"),
    )
    html = await renderer.render(popup)

    # Should have text-center class for centered layout
    assert "text-center" in html


@pytest.mark.asyncio
async def test_popup_modal_dark_mode_classes(renderer, dark_context):
    """Test PopupModal includes dark mode classes."""
    popup = PopupModal(
        id="dark-popup",
        message="Dark mode test",
        confirm_button=Button(label="OK"),
    )
    html = await renderer.render(popup, context=dark_context)

    # Content wrapper should have dark mode classes
    assert "dark:bg-gray-700" in html
    assert "dark:hover:bg-gray-600" in html
    assert "dark:hover:text-white" in html
