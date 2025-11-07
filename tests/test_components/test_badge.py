"""Tests for Badge component."""

import pytest
from htmy import Renderer

from flowbite_htmy.components.badge import Badge
from flowbite_htmy.types import Color


@pytest.mark.asyncio
async def test_badge_renders_default(renderer: Renderer) -> None:
    """Test badge renders with default props."""
    result = Badge(label="Default")
    html = await renderer.render(result)

    assert "Default" in html
    assert "span" in html
    # Default badge classes (blue)
    assert "bg-blue-100" in html
    assert "text-blue-800" in html
    assert "text-xs" in html
    assert "font-medium" in html
    assert "px-2.5" in html
    assert "py-0.5" in html
    assert "rounded-sm" in html


@pytest.mark.asyncio
async def test_badge_color_success(renderer: Renderer) -> None:
    """Test badge renders with success color."""
    result = Badge(label="Success", color=Color.SUCCESS)
    html = await renderer.render(result)

    assert "Success" in html
    assert "bg-green-100" in html
    assert "text-green-800" in html


@pytest.mark.asyncio
async def test_badge_color_danger(renderer: Renderer) -> None:
    """Test badge renders with danger color."""
    result = Badge(label="Error", color=Color.DANGER)
    html = await renderer.render(result)

    assert "Error" in html
    assert "bg-red-100" in html
    assert "text-red-800" in html


@pytest.mark.asyncio
async def test_badge_rounded(renderer: Renderer) -> None:
    """Test badge renders with rounded (pill) style."""
    result = Badge(label="New", rounded=True)
    html = await renderer.render(result)

    assert "New" in html
    assert "rounded-full" in html
    assert "rounded-sm" not in html


@pytest.mark.asyncio
async def test_badge_large_size(renderer: Renderer) -> None:
    """Test badge renders with large size."""
    result = Badge(label="Large", large=True)
    html = await renderer.render(result)

    assert "Large" in html
    assert "text-sm" in html
    assert "text-xs" not in html


@pytest.mark.asyncio
async def test_badge_custom_class(renderer: Renderer) -> None:
    """Test badge with custom classes."""
    result = Badge(label="Custom", class_="my-badge")
    html = await renderer.render(result)

    assert "Custom" in html
    assert "my-badge" in html
