"""Tests for Modal shell mode, closable, body_class, and footer_class."""

import pytest
from htmy import SafeStr

from flowbite_htmy.components import Modal
from flowbite_htmy.types import Size


@pytest.mark.asyncio
async def test_modal_shell_mode_with_content_id(renderer):
    """Test modal in shell mode renders content div with loading spinner."""
    modal = Modal(
        id="dynamic-modal",
        title="Loading...",
        content_id="modal-content",
    )
    html = await renderer.render(modal)

    assert 'id="dynamic-modal"' in html
    assert 'id="modal-content"' in html
    assert "animate-spin" in html  # Loading spinner
    assert "Loading..." in html


@pytest.mark.asyncio
async def test_modal_shell_mode_no_children(renderer):
    """Test modal shell mode when children is None and content_id is set."""
    modal = Modal(
        id="shell-modal",
        title="Shell",
        content_id="shell-content",
    )
    html = await renderer.render(modal)

    # Should have the content div for HTMX loading
    assert 'id="shell-content"' in html
    # Should have loading spinner
    assert "border-primary-600" in html


@pytest.mark.asyncio
async def test_modal_empty_body_no_children_no_content_id(renderer):
    """Test modal with neither children nor content_id renders empty body."""
    modal = Modal(
        id="empty-modal",
        title="Empty",
    )
    html = await renderer.render(modal)

    assert 'id="empty-modal"' in html
    assert "Empty" in html


@pytest.mark.asyncio
async def test_modal_closable_true_shows_close_button(renderer):
    """Test modal with closable=True (default) shows close button."""
    modal = Modal(
        id="closable-modal",
        title="Closable",
        children=SafeStr("<p>Content</p>"),
        closable=True,
    )
    html = await renderer.render(modal)

    assert 'data-modal-hide="closable-modal"' in html
    assert "Close modal" in html


@pytest.mark.asyncio
async def test_modal_closable_false_hides_close_button(renderer):
    """Test modal with closable=False hides close button."""
    modal = Modal(
        id="no-close-modal",
        title="No Close",
        children=SafeStr("<p>Content</p>"),
        closable=False,
    )
    html = await renderer.render(modal)

    assert 'data-modal-hide="no-close-modal"' not in html
    assert "Close modal" not in html


@pytest.mark.asyncio
async def test_modal_body_class(renderer):
    """Test modal body_class is appended to body classes."""
    modal = Modal(
        id="body-class-modal",
        title="Body Class",
        children=SafeStr("<p>Content</p>"),
        body_class="max-h-96 overflow-y-auto",
    )
    html = await renderer.render(modal)

    assert "max-h-96" in html
    assert "overflow-y-auto" in html
    # Should still have base body classes
    assert "p-4" in html


@pytest.mark.asyncio
async def test_modal_footer_class(renderer):
    """Test modal footer_class is appended to footer classes."""
    modal = Modal(
        id="footer-class-modal",
        title="Footer Class",
        children=SafeStr("<p>Content</p>"),
        footer=SafeStr("<button>OK</button>"),
        footer_class="justify-center",
    )
    html = await renderer.render(modal)

    assert "justify-center" in html
    # Should still have base footer classes
    assert "border-t" in html


@pytest.mark.asyncio
async def test_modal_children_takes_precedence_over_content_id(renderer):
    """Test that when both children and content_id are set, children is rendered."""
    modal = Modal(
        id="precedence-modal",
        title="Test",
        children=SafeStr("<p>Static content</p>"),
        content_id="dynamic-content",
    )
    html = await renderer.render(modal)

    assert "Static content" in html
    # content_id div should NOT appear since children is not None
    assert 'id="dynamic-content"' not in html


@pytest.mark.asyncio
async def test_modal_shell_with_size(renderer):
    """Test modal shell with custom size."""
    modal = Modal(
        id="large-shell",
        title="Large Shell",
        content_id="large-content",
        size=Size.XL,
    )
    html = await renderer.render(modal)

    assert "max-w-5xl" in html
    assert 'id="large-content"' in html
