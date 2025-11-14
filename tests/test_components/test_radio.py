"""Tests for Radio component."""

import pytest

from flowbite_htmy.types import ValidationState


# ============================================================================
# User Story 1: Basic Radio Button Selection (Priority: P1)
# ============================================================================


@pytest.mark.asyncio
async def test_radio_default_rendering(renderer):
    """Test default radio button renders with minimal props."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Accept Terms")
    html = await renderer.render(radio)

    assert "Accept Terms" in html
    assert 'type="radio"' in html
    assert 'class="' in html


@pytest.mark.asyncio
async def test_radio_with_name_and_value(renderer):
    """Test radio with name and value attributes."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Option 1", name="choice", value="opt1")
    html = await renderer.render(radio)

    assert 'name="choice"' in html
    assert 'value="opt1"' in html


@pytest.mark.asyncio
async def test_radio_checked_state(renderer):
    """Test radio button renders as checked."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Selected Option", checked=True)
    html = await renderer.render(radio)

    assert "checked" in html


@pytest.mark.asyncio
async def test_radio_auto_generated_id(renderer):
    """Test radio button auto-generates ID when not provided."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test")
    html = await renderer.render(radio)

    # Should have an id attribute
    assert 'id="radio-' in html


@pytest.mark.asyncio
async def test_radio_custom_id(renderer):
    """Test radio button uses custom ID when provided."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test", id="custom-id")
    html = await renderer.render(radio)

    assert 'id="custom-id"' in html


@pytest.mark.asyncio
async def test_radio_label_for_attribute(renderer):
    """Test label for= attribute matches input id=."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test Label", id="test-id")
    html = await renderer.render(radio)

    assert 'for="test-id"' in html
    assert 'id="test-id"' in html


# ============================================================================
# User Story 2: Validation States and Helper Text (Priority: P2)
# ============================================================================


@pytest.mark.asyncio
async def test_radio_validation_default_state(renderer):
    """Test radio with default validation state has blue colors."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Default Option", validation_state=ValidationState.DEFAULT)
    html = await renderer.render(radio)

    assert "text-blue-600" in html


@pytest.mark.asyncio
async def test_radio_validation_error_state(renderer):
    """Test radio with error validation state has red colors."""
    from flowbite_htmy.components import Radio

    radio = Radio(
        label="Invalid Option",
        validation_state=ValidationState.ERROR,
        helper_text="This option is not available",
    )
    html = await renderer.render(radio)

    assert "Invalid Option" in html
    assert "text-red-600" in html
    assert "This option is not available" in html


@pytest.mark.asyncio
async def test_radio_validation_success_state(renderer):
    """Test radio with success validation state has green colors."""
    from flowbite_htmy.components import Radio

    radio = Radio(
        label="Valid Option",
        validation_state=ValidationState.SUCCESS,
        helper_text="Recommended choice",
    )
    html = await renderer.render(radio)

    assert "text-green-600" in html
    assert "Recommended choice" in html


@pytest.mark.asyncio
async def test_radio_helper_text_rendering(renderer):
    """Test helper text appears below radio button."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test", helper_text="This is helper text")
    html = await renderer.render(radio)

    assert "This is helper text" in html


@pytest.mark.asyncio
async def test_radio_helper_text_error_color(renderer):
    """Test helper text is red when validation state is error."""
    from flowbite_htmy.components import Radio

    radio = Radio(
        label="Test",
        validation_state=ValidationState.ERROR,
        helper_text="Error message",
    )
    html = await renderer.render(radio)

    assert "Error message" in html
    assert "text-red-600" in html


@pytest.mark.asyncio
async def test_radio_helper_text_success_color(renderer):
    """Test helper text is green when validation state is success."""
    from flowbite_htmy.components import Radio

    radio = Radio(
        label="Test",
        validation_state=ValidationState.SUCCESS,
        helper_text="Success message",
    )
    html = await renderer.render(radio)

    assert "Success message" in html
    assert "text-green-600" in html


# ============================================================================
# User Story 3: Disabled State and Dark Mode (Priority: P3)
# ============================================================================


@pytest.mark.asyncio
async def test_radio_disabled_state(renderer):
    """Test disabled radio button has disabled attribute and opacity."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Disabled Option", disabled=True)
    html = await renderer.render(radio)

    assert "disabled" in html
    assert "disabled:opacity-50" in html
    assert "disabled:cursor-not-allowed" in html


@pytest.mark.asyncio
async def test_radio_disabled_checked_state(renderer):
    """Test disabled radio can be checked but not changed."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Disabled Checked", disabled=True, checked=True)
    html = await renderer.render(radio)

    assert "disabled" in html
    assert "checked" in html


@pytest.mark.asyncio
async def test_radio_disabled_label_color(renderer):
    """Test disabled radio has gray label color."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Disabled", disabled=True)
    html = await renderer.render(radio)

    assert "text-gray-400" in html or "text-gray-500" in html


@pytest.mark.asyncio
async def test_radio_dark_mode_classes_always_present(renderer):
    """Test dark mode classes are always present in output."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test")
    html = await renderer.render(radio)

    # Check for dark: classes
    assert "dark:bg-gray-700" in html
    assert "dark:border-gray-600" in html
    assert "dark:text-gray-300" in html


@pytest.mark.asyncio
async def test_radio_custom_classes_merge(renderer):
    """Test custom classes merge correctly."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Test", class_="my-custom-class")
    html = await renderer.render(radio)

    assert "my-custom-class" in html


# ============================================================================
# HTMX Integration & Edge Cases
# ============================================================================


@pytest.mark.asyncio
async def test_radio_htmx_get_attribute(renderer):
    """Test HTMX hx-get attribute renders correctly."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="Dynamic Option", hx_get="/endpoint")
    html = await renderer.render(radio)

    assert 'hx-get="/endpoint"' in html


@pytest.mark.asyncio
async def test_radio_htmx_multiple_attributes(renderer):
    """Test multiple HTMX attributes render correctly."""
    from flowbite_htmy.components import Radio

    radio = Radio(
        label="HTMX Radio",
        hx_get="/update",
        hx_target="#result",
        hx_swap="innerHTML",
    )
    html = await renderer.render(radio)

    assert 'hx-get="/update"' in html
    assert 'hx-target="#result"' in html
    assert 'hx-swap="innerHTML"' in html


@pytest.mark.asyncio
async def test_radio_empty_label_with_aria_label(renderer):
    """Test radio with empty label but aria-label provided is valid."""
    from flowbite_htmy.components import Radio

    radio = Radio(label="", aria_label="Select option", name="test", value="1")
    html = await renderer.render(radio)

    assert 'aria-label="Select option"' in html
    assert 'name="test"' in html


def test_radio_empty_label_without_aria_label_raises_error():
    """Test that empty label without aria-label raises ValueError."""
    from flowbite_htmy.components import Radio

    with pytest.raises(ValueError, match="Either 'label' or 'aria_label'"):
        Radio(label="", aria_label="")


@pytest.mark.asyncio
async def test_radio_long_label_text(renderer):
    """Test radio handles long label text gracefully."""
    from flowbite_htmy.components import Radio

    long_text = "This is a very long label text that should wrap gracefully across multiple lines when displayed in the browser without breaking the layout or causing overflow issues"
    radio = Radio(label=long_text)
    html = await renderer.render(radio)

    assert long_text in html
    assert 'type="radio"' in html
