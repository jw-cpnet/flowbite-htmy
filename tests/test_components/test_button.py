"""Tests for Button component."""

import pytest
from htmy import Renderer

from flowbite_htmy.components.button import Button
from flowbite_htmy.types import Color


@pytest.mark.asyncio
async def test_button_renders_default(renderer: Renderer) -> None:
    """Test button renders with default props."""
    button = Button(label="Click Me")
    html = await renderer.render(button)

    assert "Click Me" in html
    assert "button" in html
    assert 'type="button"' in html
    # Base Flowbite button classes
    assert "text-white" in html
    assert "bg-blue-700" in html
    assert "hover:bg-blue-800" in html
    assert "focus:ring-4" in html
    assert "focus:ring-blue-300" in html
    assert "font-medium" in html
    assert "rounded-lg" in html
    assert "text-sm" in html
    assert "px-5" in html
    assert "py-2.5" in html


@pytest.mark.asyncio
async def test_button_color_success(renderer: Renderer) -> None:
    """Test button renders with success color."""
    button = Button(label="Submit", color=Color.SUCCESS)
    html = await renderer.render(button)

    assert "Submit" in html
    assert "bg-green-700" in html
    assert "hover:bg-green-800" in html
    assert "focus:ring-green-300" in html


@pytest.mark.asyncio
async def test_button_color_danger(renderer: Renderer) -> None:
    """Test button renders with danger color."""
    button = Button(label="Delete", color=Color.DANGER)
    html = await renderer.render(button)

    assert "Delete" in html
    assert "bg-red-700" in html
    assert "hover:bg-red-800" in html
    assert "focus:ring-red-300" in html


@pytest.mark.asyncio
async def test_button_color_secondary(renderer: Renderer) -> None:
    """Test button renders with secondary color."""
    button = Button(label="Cancel", color=Color.SECONDARY)
    html = await renderer.render(button)

    assert "Cancel" in html
    assert "bg-white" in html
    assert "border" in html
    assert "border-gray-200" in html
    assert "hover:text-blue-700" in html
    assert "focus:z-10" in html


@pytest.mark.asyncio
async def test_button_htmx_attributes(renderer: Renderer) -> None:
    """Test button renders with HTMX attributes."""
    button = Button(
        label="Load More",
        hx_get="/api/items",
        hx_target="#items",
        hx_swap="beforeend",
    )
    html = await renderer.render(button)

    assert "Load More" in html
    assert 'hx-get="/api/items"' in html
    assert 'hx-target="#items"' in html
    assert 'hx-swap="beforeend"' in html


@pytest.mark.asyncio
async def test_button_disabled(renderer: Renderer) -> None:
    """Test button renders in disabled state."""
    button = Button(label="Disabled", disabled=True)
    html = await renderer.render(button)

    assert "Disabled" in html
    assert "disabled" in html


@pytest.mark.asyncio
async def test_button_custom_class(renderer: Renderer) -> None:
    """Test button with custom classes."""
    button = Button(label="Custom", class_="my-custom-class")
    html = await renderer.render(button)

    assert "Custom" in html
    assert "my-custom-class" in html
