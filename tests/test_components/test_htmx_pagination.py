"""Tests for HtmxPagination component."""

import pytest

from flowbite_htmy.components.pagination import HtmxPagination


@pytest.mark.asyncio
async def test_htmx_pagination_renders_page_info(renderer):
    """Test HtmxPagination renders page info text."""
    pagination = HtmxPagination(
        current_page=2,
        total_pages=10,
        total_items=100,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items-container",
    )
    html = await renderer.render(pagination)

    assert "Showing" in html
    assert "11-20" in html
    assert "100" in html


@pytest.mark.asyncio
async def test_htmx_pagination_first_page(renderer):
    """Test HtmxPagination on first page hides previous button."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
    )
    html = await renderer.render(pagination)

    assert "Showing" in html
    assert "1-10" in html
    assert "Next" in html
    # Previous text button should not appear
    assert "Previous" not in html or html.count("Previous") == html.count("Previous page")


@pytest.mark.asyncio
async def test_htmx_pagination_last_page(renderer):
    """Test HtmxPagination on last page hides next button."""
    pagination = HtmxPagination(
        current_page=5,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
    )
    html = await renderer.render(pagination)

    assert "41-50" in html
    # Next text button should not appear in right nav
    # Only "Next page" sr-only text might remain from icon button


@pytest.mark.asyncio
async def test_htmx_pagination_hx_attributes(renderer):
    """Test HtmxPagination generates correct HTMX attributes."""
    pagination = HtmxPagination(
        current_page=2,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items-container",
    )
    html = await renderer.render(pagination)

    assert 'hx-get="/api/v1/items?' in html
    assert 'hx-target="#items-container"' in html


@pytest.mark.asyncio
async def test_htmx_pagination_push_url(renderer):
    """Test HtmxPagination generates push URL."""
    pagination = HtmxPagination(
        current_page=2,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        push_url="/items",
        hx_target="#items",
    )
    html = await renderer.render(pagination)

    assert 'hx-push-url="/items?' in html


@pytest.mark.asyncio
async def test_htmx_pagination_query_params(renderer):
    """Test HtmxPagination preserves query parameters."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
        query_params={"origin": "MACHINE", "group_id": "123"},
    )
    html = await renderer.render(pagination)

    assert "origin=MACHINE" in html
    assert "group_id=123" in html


@pytest.mark.asyncio
async def test_htmx_pagination_search_mode(renderer):
    """Test HtmxPagination in search mode shows Clear Search button."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=1,
        total_items=5,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
        is_search=True,
    )
    html = await renderer.render(pagination)

    assert "Clear Search" in html
    assert "Found" in html
    assert "5" in html
    assert "results" in html


@pytest.mark.asyncio
async def test_htmx_pagination_page_size_selector(renderer):
    """Test HtmxPagination renders page size selector."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
    )
    html = await renderer.render(pagination)

    assert "<select" in html
    assert "/ page" in html
    # Should have default options
    assert 'value="10"' in html
    assert 'value="25"' in html
    assert 'value="50"' in html
    assert 'value="100"' in html


@pytest.mark.asyncio
async def test_htmx_pagination_on_after_request(renderer):
    """Test HtmxPagination on_after_request attribute."""
    pagination = HtmxPagination(
        current_page=2,
        total_pages=5,
        total_items=50,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
        on_after_request="initDrawers()",
    )
    html = await renderer.render(pagination)

    assert "initDrawers()" in html


@pytest.mark.asyncio
async def test_htmx_pagination_custom_class(renderer):
    """Test HtmxPagination custom wrapper class."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=3,
        total_items=30,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
        class_="my-custom-class",
    )
    html = await renderer.render(pagination)

    assert "my-custom-class" in html


@pytest.mark.asyncio
async def test_htmx_pagination_single_page(renderer):
    """Test HtmxPagination with only one page doesn't show nav buttons."""
    pagination = HtmxPagination(
        current_page=1,
        total_pages=1,
        total_items=5,
        page_size=10,
        base_url="/api/v1/items",
        hx_target="#items",
    )
    html = await renderer.render(pagination)

    assert "Showing" in html
    assert "1-5" in html
    # Should not have Previous or Next text buttons
    assert "Previous" not in html
    assert "Next" not in html
