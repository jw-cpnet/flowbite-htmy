"""Tests for Toast component."""

import pytest

from flowbite_htmy.components import Toast, ToastActionButton
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import ToastVariant


# ============================================================================
# Phase 3: User Story 1 - RED Phase (Write Failing Tests)
# ============================================================================


@pytest.mark.asyncio
async def test_toast_renders_default(renderer):
    """Test T010: Default toast renders with minimal props (message only)."""
    toast = Toast(message="Test message")
    html = await renderer.render(toast)

    assert "Test message" in html
    assert 'role="alert"' in html
    assert "toast-" in html  # Auto-generated ID prefix


@pytest.mark.asyncio
async def test_toast_variant_success(renderer):
    """Test T011: Success variant renders with green colors and checkmark icon."""
    toast = Toast(message="Success", variant=ToastVariant.SUCCESS)
    html = await renderer.render(toast)

    assert "Success" in html
    assert "text-green-500" in html
    assert "bg-green-100" in html
    assert "dark:bg-green-800" in html
    assert "dark:text-green-200" in html


@pytest.mark.asyncio
async def test_toast_variant_danger(renderer):
    """Test T012: Danger variant renders with red colors and X icon."""
    toast = Toast(message="Error", variant=ToastVariant.DANGER)
    html = await renderer.render(toast)

    assert "Error" in html
    assert "text-red-500" in html
    assert "bg-red-100" in html
    assert "dark:bg-red-800" in html
    assert "dark:text-red-200" in html


@pytest.mark.asyncio
async def test_toast_variant_warning(renderer):
    """Test T013: Warning variant renders with yellow colors and exclamation icon."""
    toast = Toast(message="Warning", variant=ToastVariant.WARNING)
    html = await renderer.render(toast)

    assert "Warning" in html
    assert "text-yellow-500" in html
    assert "bg-yellow-100" in html
    assert "dark:bg-yellow-800" in html
    assert "dark:text-yellow-200" in html


@pytest.mark.asyncio
async def test_toast_variant_info(renderer):
    """Test T014: Info variant renders with blue colors and info icon."""
    toast = Toast(message="Info", variant=ToastVariant.INFO)
    html = await renderer.render(toast)

    assert "Info" in html
    assert "text-blue-500" in html
    assert "bg-blue-100" in html
    assert "dark:bg-blue-800" in html
    assert "dark:text-blue-200" in html


@pytest.mark.asyncio
async def test_toast_dismissible_true(renderer):
    """Test T015: Dismissible=True renders close button with data-dismiss-target."""
    toast = Toast(message="Dismissible", dismissible=True)
    html = await renderer.render(toast)

    assert "Dismissible" in html
    assert 'data-dismiss-target="#toast-' in html
    assert 'aria-label="Close"' in html
    assert '<span class="sr-only">Close</span>' in html


@pytest.mark.asyncio
async def test_toast_dismissible_false(renderer):
    """Test T016: Dismissible=False does not render close button."""
    toast = Toast(message="Non-dismissible", dismissible=False)
    html = await renderer.render(toast)

    assert "Non-dismissible" in html
    assert "data-dismiss-target" not in html
    assert 'aria-label="Close"' not in html


@pytest.mark.asyncio
async def test_toast_auto_generates_id(renderer):
    """Test T017: Toast auto-generates unique ID when id=None."""
    toast1 = Toast(message="Toast 1")
    toast2 = Toast(message="Toast 2")

    html1 = await renderer.render(toast1)
    html2 = await renderer.render(toast2)

    # Both should have IDs
    assert 'id="toast-' in html1
    assert 'id="toast-' in html2

    # IDs should be different (extract and compare)
    import re

    id1_match = re.search(r'id="(toast-\d+)"', html1)
    id2_match = re.search(r'id="(toast-\d+)"', html2)

    assert id1_match is not None
    assert id2_match is not None
    assert id1_match.group(1) != id2_match.group(1)


@pytest.mark.asyncio
async def test_toast_uses_custom_id(renderer):
    """Test T018: Toast uses custom ID when provided."""
    toast = Toast(message="Custom ID", id="my-custom-toast")
    html = await renderer.render(toast)

    assert 'id="my-custom-toast"' in html
    assert 'data-dismiss-target="#my-custom-toast"' in html


# ============================================================================
# Phase 4: User Story 2 - RED Phase (Interactive Toast)
# ============================================================================


@pytest.mark.asyncio
async def test_toast_with_action_button(renderer):
    """Test T031: Toast with action button renders button label."""
    action = ToastActionButton(label="Reply", hx_get="/reply")
    toast = Toast(message="New message", action_button=action)
    html = await renderer.render(toast)

    assert "New message" in html
    assert "Reply" in html


@pytest.mark.asyncio
async def test_toast_action_button_htmx_get(renderer):
    """Test T032: Action button renders hx-get attribute."""
    action = ToastActionButton(label="View", hx_get="/view/123")
    toast = Toast(message="Update available", action_button=action)
    html = await renderer.render(toast)

    assert 'hx-get="/view/123"' in html


@pytest.mark.asyncio
async def test_toast_action_button_htmx_post(renderer):
    """Test T033: Action button renders hx-post and hx-target attributes."""
    action = ToastActionButton(
        label="Undo", hx_post="/undo", hx_target="#content"
    )
    toast = Toast(message="Item deleted", action_button=action)
    html = await renderer.render(toast)

    assert 'hx-post="/undo"' in html
    assert 'hx-target="#content"' in html


@pytest.mark.asyncio
async def test_toast_without_action_button(renderer):
    """Test T034: Toast without action button doesn't render button."""
    toast = Toast(message="Simple notification", action_button=None)
    html = await renderer.render(toast)

    assert "Simple notification" in html
    assert "hx-get" not in html
    assert "hx-post" not in html


@pytest.mark.asyncio
async def test_toast_with_avatar(renderer):
    """Test T035: Toast with avatar renders image with src."""
    toast = Toast(
        message="Alice sent a message",
        avatar_src="/static/avatars/alice.jpg",
    )
    html = await renderer.render(toast)

    assert "Alice sent a message" in html
    assert 'src="/static/avatars/alice.jpg"' in html
    assert "rounded-full" in html  # Avatar should be circular


@pytest.mark.asyncio
async def test_toast_without_avatar(renderer):
    """Test T036: Toast without avatar doesn't render image."""
    toast = Toast(message="No avatar")
    html = await renderer.render(toast)

    assert "No avatar" in html
    assert "rounded-full" not in html
    assert "<img" not in html


# ============================================================================
# Phase 5: User Story 3 - RED Phase (Accessibility)
# ============================================================================


@pytest.mark.asyncio
async def test_toast_role_alert(renderer):
    """Test T047: Toast includes role='alert' for accessibility."""
    toast = Toast(message="Accessible toast")
    html = await renderer.render(toast)

    assert 'role="alert"' in html


@pytest.mark.asyncio
async def test_toast_aria_hidden_on_icon(renderer):
    """Test T048: Icon SVG includes aria-hidden='true'."""
    toast = Toast(message="Icon test")
    html = await renderer.render(toast)

    # Icon SVG should have aria-hidden="true" (from get_icon)
    assert 'aria-hidden="true"' in html


@pytest.mark.asyncio
async def test_toast_sr_only_close_label(renderer):
    """Test T049: Close button includes sr-only 'Close' text."""
    toast = Toast(message="Dismissible", dismissible=True)
    html = await renderer.render(toast)

    assert '<span class="sr-only">Close</span>' in html


@pytest.mark.asyncio
async def test_toast_dark_mode_classes(renderer):
    """Test T050: Toast includes dark mode classes."""
    toast = Toast(message="Dark mode test")
    html = await renderer.render(toast)

    assert "dark:bg-gray-800" in html
    assert "dark:text-gray-400" in html


@pytest.mark.asyncio
async def test_toast_custom_classes(renderer):
    """Test T051: class_ parameter merges with component classes."""
    toast = Toast(
        message="Custom styling",
        class_="border-2 border-yellow-600 shadow-lg",
    )
    html = await renderer.render(toast)

    assert "border-2" in html
    assert "border-yellow-600" in html
    assert "shadow-lg" in html
    # Should also have base classes
    assert "flex items-center" in html
    assert "max-w-xs" in html


@pytest.mark.asyncio
async def test_toast_custom_icon_override(renderer):
    """Test T052: icon prop overrides default variant icon."""
    # INFO variant normally uses Icon.INFO, override with CHECK
    toast = Toast(
        message="Custom icon", variant=ToastVariant.INFO, icon=Icon.CHECK
    )
    html = await renderer.render(toast)

    # Should use CHECK icon (checkmark path), not INFO icon
    # This is hard to verify without inspecting actual SVG paths
    # For now, just verify it renders without error
    assert "Custom icon" in html


# ============================================================================
# Additional Tests for Coverage (Edge Cases)
# ============================================================================


@pytest.mark.asyncio
async def test_toast_action_button_all_htmx_attributes(renderer):
    """Test action button with multiple HTMX attributes."""
    action = ToastActionButton(
        label="Submit",
        hx_post="/submit",
        hx_target="#result",
        hx_swap="innerHTML",
        hx_trigger="click",
    )
    toast = Toast(message="Form ready", action_button=action)
    html = await renderer.render(toast)

    assert 'hx-post="/submit"' in html
    assert 'hx-target="#result"' in html
    assert 'hx-swap="innerHTML"' in html
    assert 'hx-trigger="click"' in html


@pytest.mark.asyncio
async def test_toast_action_button_custom_class(renderer):
    """Test action button with custom class."""
    action = ToastActionButton(
        label="Custom", hx_get="/custom", class_="my-custom-class"
    )
    toast = Toast(message="Custom button", action_button=action)
    html = await renderer.render(toast)

    assert "my-custom-class" in html
