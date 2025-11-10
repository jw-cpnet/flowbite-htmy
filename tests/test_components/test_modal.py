"""Tests for Modal component."""

import pytest
from htmy import SafeStr

from flowbite_htmy.components import Modal
from flowbite_htmy.types import Size


@pytest.mark.asyncio
async def test_modal_renders_default(renderer):
    """Test default modal renders with minimal props."""
    modal = Modal(
        id="test-modal",
        title="Test Modal",
        children=SafeStr("<p>Modal content</p>"),
    )
    html = await renderer.render(modal)

    # Check container attributes
    assert 'id="test-modal"' in html
    assert 'tabindex="-1"' in html
    assert 'aria-hidden="true"' in html

    # Check container classes
    assert "hidden" in html
    assert "overflow-y-auto" in html
    assert "overflow-x-hidden" in html
    assert "fixed" in html
    assert "z-50" in html

    # Check title
    assert "Test Modal" in html

    # Check content
    assert "<p>Modal content</p>" in html

    # Check close button SVG exists
    assert "<svg" in html
    assert "Close modal" in html


@pytest.mark.asyncio
async def test_modal_renders_with_footer(renderer):
    """Test modal renders with footer content."""
    modal = Modal(
        id="footer-modal",
        title="Modal with Footer",
        children=SafeStr("<p>Body content</p>"),
        footer=SafeStr('<button type="button">Accept</button>'),
    )
    html = await renderer.render(modal)

    assert "Body content" in html
    assert '<button type="button">Accept</button>' in html
    assert "border-t" in html  # Footer should have top border


@pytest.mark.asyncio
async def test_modal_static_backdrop(renderer):
    """Test modal with static backdrop (prevents close on outside click)."""
    modal = Modal(
        id="static-modal",
        title="Static Modal",
        children=SafeStr("<p>Content</p>"),
        static_backdrop=True,
    )
    html = await renderer.render(modal)

    assert 'data-modal-backdrop="static"' in html


@pytest.mark.asyncio
async def test_modal_sizes(renderer):
    """Test modal size variants."""
    # Small
    small = Modal(
        id="small-modal",
        title="Small",
        children=SafeStr("<p>Content</p>"),
        size=Size.SM,
    )
    html_sm = await renderer.render(small)

    assert "max-w-md" in html_sm

    # Medium (default)
    medium = Modal(
        id="medium-modal",
        title="Medium",
        children=SafeStr("<p>Content</p>"),
        size=Size.MD,
    )
    html_md = await renderer.render(medium)

    assert "max-w-2xl" in html_md

    # Large
    large = Modal(
        id="large-modal",
        title="Large",
        children=SafeStr("<p>Content</p>"),
        size=Size.LG,
    )
    html_lg = await renderer.render(large)

    assert "max-w-4xl" in html_lg


@pytest.mark.asyncio
async def test_modal_custom_classes(renderer):
    """Test modal accepts custom classes."""
    modal = Modal(
        id="custom-modal",
        title="Custom",
        children=SafeStr("<p>Content</p>"),
        class_="custom-class",
    )
    html = await renderer.render(modal)

    assert "custom-class" in html


@pytest.mark.asyncio
async def test_modal_dark_mode_classes(renderer, dark_context):
    """Test modal includes dark mode classes."""
    modal = Modal(
        id="dark-modal",
        title="Dark Modal",
        children=SafeStr("<p>Content</p>"),
    )
    html = await renderer.render(modal, context=dark_context)

    # Content wrapper should have dark mode classes
    assert "dark:bg-gray-700" in html
    assert "dark:border-gray-600" in html
    assert "dark:text-white" in html


@pytest.mark.asyncio
async def test_modal_passthrough_attributes(renderer):
    """Test modal supports passthrough attributes."""
    modal = Modal(
        id="attrs-modal",
        title="Attrs Modal",
        children=SafeStr("<p>Content</p>"),
        attrs={"data-testid": "modal-test", "aria-labelledby": "modal-title"},
    )
    html = await renderer.render(modal)

    assert 'data-testid="modal-test"' in html
    assert 'aria-labelledby="modal-title"' in html


@pytest.mark.asyncio
async def test_modal_close_button_data_attribute(renderer):
    """Test modal close button has correct data-modal-hide attribute."""
    modal = Modal(
        id="close-modal",
        title="Close Test",
        children=SafeStr("<p>Content</p>"),
    )
    html = await renderer.render(modal)

    assert 'data-modal-hide="close-modal"' in html
