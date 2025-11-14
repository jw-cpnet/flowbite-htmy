"""Tests for Textarea component."""

import pytest
from htmy import Renderer

from flowbite_htmy.components import Textarea


@pytest.mark.asyncio
async def test_textarea_default_rendering(renderer: Renderer):
    """Test default textarea rendering with label and textarea structure."""
    textarea = Textarea(
        id="comment",
        label="Your comment",
    )

    html = await renderer.render(textarea)

    # Should have label
    assert '<label' in html
    assert 'Your comment' in html

    # Should have textarea
    assert '<textarea' in html
    assert 'id="comment"' in html


@pytest.mark.asyncio
async def test_textarea_label_for_id_association(renderer: Renderer):
    """Test textarea ID and label for attribute association."""
    textarea = Textarea(
        id="feedback",
        label="Feedback",
    )

    html = await renderer.render(textarea)

    # Label should have for attribute pointing to textarea id
    assert 'for="feedback"' in html
    assert 'id="feedback"' in html


@pytest.mark.asyncio
async def test_textarea_placeholder_rendering(renderer: Renderer):
    """Test placeholder attribute rendering."""
    textarea = Textarea(
        id="message",
        label="Message",
        placeholder="Write your thoughts here...",
    )

    html = await renderer.render(textarea)

    assert 'placeholder="Write your thoughts here..."' in html


@pytest.mark.asyncio
async def test_textarea_value_rendering(renderer: Renderer):
    """Test value (pre-filled content) rendering."""
    textarea = Textarea(
        id="bio",
        label="Biography",
        value="Existing bio content",
    )

    html = await renderer.render(textarea)

    # Value should be textarea content (with possible whitespace from htmy)
    assert 'Existing bio content' in html
    assert '</textarea>' in html


@pytest.mark.asyncio
async def test_textarea_default_rows(renderer: Renderer):
    """Test default rows=4 rendering."""
    textarea = Textarea(
        id="note",
        label="Note",
    )

    html = await renderer.render(textarea)

    assert 'rows="4"' in html


@pytest.mark.asyncio
async def test_textarea_dark_mode_classes(renderer: Renderer):
    """Test dark mode classes are always present."""
    textarea = Textarea(
        id="comment",
        label="Comment",
    )

    html = await renderer.render(textarea)

    # Dark mode classes should be present
    assert 'dark:' in html
    # Specific dark classes from Flowbite pattern
    assert 'dark:bg-gray-700' in html or 'dark:text-white' in html


@pytest.mark.asyncio
async def test_textarea_flowbite_base_classes(renderer: Renderer):
    """Test Flowbite CSS base classes."""
    textarea = Textarea(
        id="test",
        label="Test",
    )

    html = await renderer.render(textarea)

    # Base layout classes
    assert 'block' in html
    assert 'p-2.5' in html
    assert 'w-full' in html
    assert 'text-sm' in html
    assert 'rounded-lg' in html
    assert 'border' in html


@pytest.mark.asyncio
async def test_textarea_focus_ring_classes(renderer: Renderer):
    """Test focus ring classes."""
    textarea = Textarea(
        id="test",
        label="Test",
    )

    html = await renderer.render(textarea)

    # Focus ring classes
    assert 'focus:ring-blue-500' in html
    assert 'focus:border-blue-500' in html


# ============================================================================
# User Story 2 Tests: Validation Feedback
# ============================================================================


@pytest.mark.asyncio
async def test_textarea_validation_success(renderer: Renderer):
    """Test validation='success' with green border and text classes."""
    textarea = Textarea(
        id="review",
        label="Review",
        validation="success",
    )

    html = await renderer.render(textarea)

    # Success validation classes
    assert 'bg-green-50' in html
    assert 'border-green-500' in html
    assert 'text-green-900' in html or 'text-green-400' in html
    # Label should be green
    assert 'text-green-700' in html or 'text-green-500' in html


@pytest.mark.asyncio
async def test_textarea_validation_error(renderer: Renderer):
    """Test validation='error' with red border and text classes."""
    textarea = Textarea(
        id="message",
        label="Message",
        validation="error",
    )

    html = await renderer.render(textarea)

    # Error validation classes
    assert 'bg-red-50' in html
    assert 'border-red-500' in html
    assert 'text-red-900' in html or 'text-red-500' in html
    # Label should be red
    assert 'text-red-700' in html or 'text-red-500' in html


@pytest.mark.asyncio
async def test_textarea_validation_default(renderer: Renderer):
    """Test validation=None (default) with neutral colors."""
    textarea = Textarea(
        id="note",
        label="Note",
        validation=None,
    )

    html = await renderer.render(textarea)

    # Default colors (not success or error)
    assert 'bg-gray-50' in html
    assert 'border-gray-300' in html
    assert 'text-gray-900' in html


@pytest.mark.asyncio
async def test_textarea_helper_text_rendering(renderer: Renderer):
    """Test helper text rendering with id attribute."""
    textarea = Textarea(
        id="feedback",
        label="Feedback",
        helper_text="Please provide detailed feedback",
    )

    html = await renderer.render(textarea)

    # Helper text should be present
    assert 'Please provide detailed feedback' in html
    assert 'id="feedback-helper"' in html
    assert '<p' in html


@pytest.mark.asyncio
async def test_textarea_helper_text_success_color(renderer: Renderer):
    """Test helper text color matching success validation state."""
    textarea = Textarea(
        id="comment",
        label="Comment",
        validation="success",
        helper_text="Great comment!",
    )

    html = await renderer.render(textarea)

    # Helper text should be green for success
    assert 'Great comment!' in html
    assert 'text-green-600' in html or 'text-green-500' in html


@pytest.mark.asyncio
async def test_textarea_helper_text_error_color(renderer: Renderer):
    """Test helper text color matching error validation state."""
    textarea = Textarea(
        id="message",
        label="Message",
        validation="error",
        helper_text="Message is too short",
    )

    html = await renderer.render(textarea)

    # Helper text should be red for error
    assert 'Message is too short' in html
    assert 'text-red-600' in html or 'text-red-500' in html


# ============================================================================
# User Story 3 Tests: Size and Layout Control
# ============================================================================


@pytest.mark.asyncio
async def test_textarea_custom_rows_3(renderer: Renderer):
    """Test custom rows=3 rendering."""
    textarea = Textarea(
        id="short",
        label="Short Comment",
        rows=3,
    )

    html = await renderer.render(textarea)

    assert 'rows="3"' in html


@pytest.mark.asyncio
async def test_textarea_custom_rows_10(renderer: Renderer):
    """Test custom rows=10 rendering."""
    textarea = Textarea(
        id="long",
        label="Long Essay",
        rows=10,
    )

    html = await renderer.render(textarea)

    assert 'rows="10"' in html


@pytest.mark.asyncio
async def test_textarea_rows_clamping_zero(renderer: Renderer):
    """Test rows=0 clamping to rows=1."""
    textarea = Textarea(
        id="test",
        label="Test",
        rows=0,
    )

    html = await renderer.render(textarea)

    # Should be clamped to 1
    assert 'rows="1"' in html
    assert 'rows="0"' not in html


@pytest.mark.asyncio
async def test_textarea_rows_clamping_negative(renderer: Renderer):
    """Test rows=-5 clamping to rows=1."""
    textarea = Textarea(
        id="test",
        label="Test",
        rows=-5,
    )

    html = await renderer.render(textarea)

    # Should be clamped to 1
    assert 'rows="1"' in html


@pytest.mark.asyncio
async def test_textarea_custom_class(renderer: Renderer):
    """Test class_ parameter merging with component classes."""
    textarea = Textarea(
        id="test",
        label="Test",
        class_="w-1/2 custom-class",
    )

    html = await renderer.render(textarea)

    # Custom classes should be present on wrapper div
    assert 'w-1/2' in html
    assert 'custom-class' in html


# ============================================================================
# User Story 4 Tests: Accessibility and States
# ============================================================================


@pytest.mark.asyncio
async def test_textarea_required_attribute(renderer: Renderer):
    """Test required attribute rendering."""
    textarea = Textarea(
        id="description",
        label="Description",
        required=True,
    )

    html = await renderer.render(textarea)

    assert 'required' in html


@pytest.mark.asyncio
async def test_textarea_required_asterisk_in_label(renderer: Renderer):
    """Test required=True appending asterisk to label."""
    textarea = Textarea(
        id="comment",
        label="Comment",
        required=True,
    )

    html = await renderer.render(textarea)

    # Label should have asterisk
    assert 'Comment *' in html


@pytest.mark.asyncio
async def test_textarea_disabled_attribute(renderer: Renderer):
    """Test disabled attribute rendering with grayed styling."""
    textarea = Textarea(
        id="locked",
        label="Locked",
        disabled=True,
    )

    html = await renderer.render(textarea)

    assert 'disabled' in html


@pytest.mark.asyncio
async def test_textarea_disabled_cursor_not_allowed(renderer: Renderer):
    """Test disabled cursor-not-allowed class."""
    textarea = Textarea(
        id="test",
        label="Test",
        disabled=True,
    )

    html = await renderer.render(textarea)

    assert 'cursor-not-allowed' in html


@pytest.mark.asyncio
async def test_textarea_readonly_attribute(renderer: Renderer):
    """Test readonly attribute rendering."""
    textarea = Textarea(
        id="terms",
        label="Terms",
        readonly=True,
    )

    html = await renderer.render(textarea)

    assert 'readonly' in html


@pytest.mark.asyncio
async def test_textarea_disabled_takes_precedence_over_readonly(renderer: Renderer):
    """Test disabled=True with readonly=True (disabled wins, no readonly attribute)."""
    textarea = Textarea(
        id="test",
        label="Test",
        disabled=True,
        readonly=True,
    )

    html = await renderer.render(textarea)

    # Should have disabled
    assert 'disabled' in html
    # Should NOT have readonly (disabled takes precedence)
    assert 'readonly' not in html


@pytest.mark.asyncio
async def test_textarea_name_attribute(renderer: Renderer):
    """Test name attribute (optional, None by default)."""
    textarea = Textarea(
        id="feedback",
        label="Feedback",
        name="user_feedback",
    )

    html = await renderer.render(textarea)

    assert 'name="user_feedback"' in html


# ============================================================================
# Phase 7 Tests: HTMX Integration & Passthrough Attributes
# ============================================================================


@pytest.mark.asyncio
async def test_textarea_htmx_get(renderer: Renderer):
    """Test hx_get attribute rendering as hx-get."""
    textarea = Textarea(
        id="test",
        label="Test",
        hx_get="/api/validate",
    )

    html = await renderer.render(textarea)

    assert 'hx-get="/api/validate"' in html or 'hx_get="/api/validate"' in html


@pytest.mark.asyncio
async def test_textarea_htmx_post(renderer: Renderer):
    """Test hx_post attribute rendering as hx-post."""
    textarea = Textarea(
        id="test",
        label="Test",
        hx_post="/api/submit",
    )

    html = await renderer.render(textarea)

    assert 'hx-post="/api/submit"' in html or 'hx_post="/api/submit"' in html


@pytest.mark.asyncio
async def test_textarea_htmx_multiple_attributes(renderer: Renderer):
    """Test multiple HTMX attributes."""
    textarea = Textarea(
        id="test",
        label="Test",
        hx_post="/api/comment",
        hx_target="#comments",
        hx_swap="afterbegin",
    )

    html = await renderer.render(textarea)

    assert '/api/comment' in html
    assert '#comments' in html
    assert 'afterbegin' in html


@pytest.mark.asyncio
async def test_textarea_attrs_passthrough(renderer: Renderer):
    """Test attrs dict passthrough for custom attributes."""
    textarea = Textarea(
        id="code",
        label="Code",
        attrs={
            "spellcheck": "false",
            "maxlength": "1000",
        },
    )

    html = await renderer.render(textarea)

    assert 'spellcheck="false"' in html
    assert 'maxlength="1000"' in html
