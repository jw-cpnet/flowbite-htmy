"""Tests for Card component."""

import pytest
from htmy import Renderer, html

from flowbite_htmy.components.card import Card


@pytest.mark.asyncio
async def test_card_renders_default(renderer: Renderer) -> None:
    """Test card renders with default props."""
    card = Card(
        content=html.p("This is card content."),
    )
    html_output = await renderer.render(card)

    assert "This is card content." in html_output
    assert "div" in html_output
    # Base card classes
    assert "bg-white" in html_output
    assert "border" in html_output
    assert "border-gray-200" in html_output
    assert "rounded-lg" in html_output
    assert "shadow-sm" in html_output
    assert "p-6" in html_output


@pytest.mark.asyncio
async def test_card_with_title(renderer: Renderer) -> None:
    """Test card renders with title."""
    card = Card(
        title="Card Title",
        content=html.p("Card body text."),
    )
    html_output = await renderer.render(card)

    assert "Card Title" in html_output
    assert "Card body text." in html_output
    assert "text-2xl" in html_output
    assert "font-bold" in html_output


@pytest.mark.asyncio
async def test_card_with_image(renderer: Renderer) -> None:
    """Test card renders with image."""
    card = Card(
        image_src="/images/card.jpg",
        image_alt="Card image",
        content=html.p("Content below image."),
    )
    html_output = await renderer.render(card)

    assert "Content below image." in html_output
    assert "/images/card.jpg" in html_output
    assert "Card image" in html_output
    assert "rounded-t-lg" in html_output  # Image rounded top corners


@pytest.mark.asyncio
async def test_card_with_title_and_image(renderer: Renderer) -> None:
    """Test card with both title and image."""
    card = Card(
        title="Featured Post",
        image_src="/images/blog.jpg",
        content=html.p("Blog post excerpt."),
    )
    html_output = await renderer.render(card)

    assert "Featured Post" in html_output
    assert "/images/blog.jpg" in html_output
    assert "Blog post excerpt." in html_output


@pytest.mark.asyncio
async def test_card_with_multiple_children(renderer: Renderer) -> None:
    """Test card with multiple child components."""
    card = Card(
        title="Multi-content Card",
        content=(
            html.p("First paragraph.", class_="mb-2"),
            html.p("Second paragraph.", class_="mb-2"),
            html.a("Learn more", href="#", class_="text-blue-600"),
        ),
    )
    html_output = await renderer.render(card)

    assert "Multi-content Card" in html_output
    assert "First paragraph." in html_output
    assert "Second paragraph." in html_output
    assert "Learn more" in html_output


@pytest.mark.asyncio
async def test_card_custom_class(renderer: Renderer) -> None:
    """Test card with custom classes."""
    card = Card(
        content=html.p("Custom styled card."),
        class_="my-custom-card",
    )
    html_output = await renderer.render(card)

    assert "Custom styled card." in html_output
    assert "my-custom-card" in html_output


@pytest.mark.asyncio
async def test_card_with_href(renderer: Renderer) -> None:
    """Test card as clickable link."""
    card = Card(
        title="Clickable Card",
        content=html.p("Click anywhere on this card."),
        href="/details",
    )
    html_output = await renderer.render(card)

    assert "Clickable Card" in html_output
    assert 'href="/details"' in html_output
