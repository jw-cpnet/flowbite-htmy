"""Tests for PageLayout component."""

import pytest
from htmy import Renderer, html

from flowbite_htmy.layouts.page import PageLayout


@pytest.mark.asyncio
async def test_page_layout_renders_default(renderer: Renderer) -> None:
    """Test page layout renders with default props."""
    page = PageLayout(
        title="Test Page",
        content=html.div("Hello World"),
    )
    html_output = await renderer.render(page)

    assert "<!DOCTYPE html>" in html_output
    assert "<html" in html_output
    assert "<head" in html_output
    assert "<title" in html_output
    assert "Test Page" in html_output
    assert "<body" in html_output
    assert "Hello World" in html_output
    # Meta tags
    assert 'charset="UTF-8"' in html_output
    assert 'name="viewport"' in html_output


@pytest.mark.asyncio
async def test_page_layout_includes_tailwind(renderer: Renderer) -> None:
    """Test page layout includes Tailwind CSS."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
    )
    html_output = await renderer.render(page)

    assert "cdn.tailwindcss.com" in html_output


@pytest.mark.asyncio
async def test_page_layout_includes_flowbite_css(renderer: Renderer) -> None:
    """Test page layout includes Flowbite CSS."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
    )
    html_output = await renderer.render(page)

    assert "flowbite" in html_output
    assert ".css" in html_output


@pytest.mark.asyncio
async def test_page_layout_includes_htmx(renderer: Renderer) -> None:
    """Test page layout includes HTMX."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
    )
    html_output = await renderer.render(page)

    assert "htmx.org" in html_output


@pytest.mark.asyncio
async def test_page_layout_with_flowbite_js(renderer: Renderer) -> None:
    """Test page layout optionally includes Flowbite JS."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
        include_flowbite_js=True,
    )
    html_output = await renderer.render(page)

    assert "flowbite.min.js" in html_output


@pytest.mark.asyncio
async def test_page_layout_without_flowbite_js(renderer: Renderer) -> None:
    """Test page layout excludes Flowbite JS by default."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
    )
    html_output = await renderer.render(page)

    assert "flowbite.min.js" not in html_output


@pytest.mark.asyncio
async def test_page_layout_body_class(renderer: Renderer) -> None:
    """Test page layout with custom body class."""
    page = PageLayout(
        title="Test",
        content=html.p("Content"),
        body_class="bg-gray-50 dark:bg-gray-900",
    )
    html_output = await renderer.render(page)

    assert "bg-gray-50" in html_output
    assert "dark:bg-gray-900" in html_output
