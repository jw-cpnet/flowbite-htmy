"""Tests for Alert component."""

import pytest
from htmy import Renderer

from flowbite_htmy.components.alert import Alert
from flowbite_htmy.types import Color


@pytest.mark.asyncio
async def test_alert_renders_default(renderer: Renderer) -> None:
    """Test alert renders with default props."""
    alert = Alert(message="Info alert! Change a few things up and try submitting again.")
    html = await renderer.render(alert)

    assert "Info alert!" in html
    assert "div" in html
    assert 'role="alert"' in html
    # Default alert classes (info/blue)
    assert "p-4" in html
    assert "mb-4" in html
    assert "text-sm" in html
    assert "text-blue-800" in html
    assert "rounded-lg" in html
    assert "bg-blue-50" in html


@pytest.mark.asyncio
async def test_alert_with_title(renderer: Renderer) -> None:
    """Test alert renders with title."""
    alert = Alert(
        title="Info alert!",
        message="Change a few things up and try submitting again.",
    )
    html = await renderer.render(alert)

    assert "Info alert!" in html
    assert "font-medium" in html
    assert "Change a few things up" in html


@pytest.mark.asyncio
async def test_alert_color_success(renderer: Renderer) -> None:
    """Test alert renders with success color."""
    alert = Alert(message="Success!", color=Color.SUCCESS)
    html = await renderer.render(alert)

    assert "Success!" in html
    assert "bg-green-50" in html
    assert "text-green-800" in html


@pytest.mark.asyncio
async def test_alert_color_danger(renderer: Renderer) -> None:
    """Test alert renders with danger color."""
    alert = Alert(message="Error occurred!", color=Color.DANGER)
    html = await renderer.render(alert)

    assert "Error occurred!" in html
    assert "bg-red-50" in html
    assert "text-red-800" in html


@pytest.mark.asyncio
async def test_alert_color_warning(renderer: Renderer) -> None:
    """Test alert renders with warning color."""
    alert = Alert(message="Warning!", color=Color.WARNING)
    html = await renderer.render(alert)

    assert "Warning!" in html
    assert "bg-yellow-50" in html
    assert "text-yellow-800" in html


@pytest.mark.asyncio
async def test_alert_with_border(renderer: Renderer) -> None:
    """Test alert renders with border."""
    alert = Alert(message="Bordered alert", bordered=True)
    html = await renderer.render(alert)

    assert "Bordered alert" in html
    assert "border" in html
    assert "border-blue-300" in html


@pytest.mark.asyncio
async def test_alert_custom_class(renderer: Renderer) -> None:
    """Test alert with custom classes."""
    alert = Alert(message="Custom", class_="my-alert")
    html = await renderer.render(alert)

    assert "Custom" in html
    assert "my-alert" in html
