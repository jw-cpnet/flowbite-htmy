"""Tests for Avatar component."""

import pytest
from htmy import Renderer

from flowbite_htmy.components.avatar import Avatar
from flowbite_htmy.types import Size


@pytest.mark.asyncio
async def test_avatar_renders_default(renderer: Renderer) -> None:
    """Test avatar renders with image src."""
    avatar = Avatar(src="/images/user.jpg", alt="User avatar")
    html = await renderer.render(avatar)

    assert "/images/user.jpg" in html
    assert "User avatar" in html
    assert "img" in html
    assert "rounded-full" in html
    assert "w-10" in html
    assert "h-10" in html


@pytest.mark.asyncio
async def test_avatar_with_initials(renderer: Renderer) -> None:
    """Test avatar renders with initials placeholder."""
    avatar = Avatar(initials="JD")
    html = await renderer.render(avatar)

    assert "JD" in html
    assert "div" in html
    assert "bg-gray-100" in html
    assert "rounded-full" in html
    assert "inline-flex" in html
    assert "items-center" in html
    assert "justify-center" in html


@pytest.mark.asyncio
async def test_avatar_size_small(renderer: Renderer) -> None:
    """Test avatar renders with small size."""
    avatar = Avatar(src="/images/user.jpg", size=Size.SM)
    html = await renderer.render(avatar)

    assert "w-8" in html
    assert "h-8" in html


@pytest.mark.asyncio
async def test_avatar_size_large(renderer: Renderer) -> None:
    """Test avatar renders with large size."""
    avatar = Avatar(src="/images/user.jpg", size=Size.LG)
    html = await renderer.render(avatar)

    assert "w-20" in html
    assert "h-20" in html


@pytest.mark.asyncio
async def test_avatar_size_extra_large(renderer: Renderer) -> None:
    """Test avatar renders with extra large size."""
    avatar = Avatar(initials="AB", size=Size.XL)
    html = await renderer.render(avatar)

    assert "AB" in html
    assert "w-24" in html
    assert "h-24" in html


@pytest.mark.asyncio
async def test_avatar_bordered(renderer: Renderer) -> None:
    """Test avatar renders with border."""
    avatar = Avatar(src="/images/user.jpg", bordered=True)
    html = await renderer.render(avatar)

    assert "ring-2" in html
    assert "ring-gray-300" in html
    assert "p-1" in html


@pytest.mark.asyncio
async def test_avatar_rounded_square(renderer: Renderer) -> None:
    """Test avatar renders with rounded square (not circle)."""
    avatar = Avatar(src="/images/user.jpg", rounded=False)
    html = await renderer.render(avatar)

    assert "rounded-sm" in html
    assert "rounded-full" not in html


@pytest.mark.asyncio
async def test_avatar_custom_class(renderer: Renderer) -> None:
    """Test avatar with custom classes."""
    avatar = Avatar(src="/images/user.jpg", class_="custom-avatar")
    html = await renderer.render(avatar)

    assert "custom-avatar" in html


@pytest.mark.asyncio
async def test_avatar_placeholder_icon(renderer: Renderer) -> None:
    """Test avatar renders with default placeholder icon when no src or initials."""
    avatar = Avatar()
    html = await renderer.render(avatar)

    assert "svg" in html
    assert "path" in html
    assert "bg-gray-100" in html
    assert "text-gray-400" in html
    assert "rounded-full" in html
