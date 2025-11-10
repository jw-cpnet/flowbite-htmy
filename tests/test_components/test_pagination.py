"""Tests for the Pagination component."""

import pytest

from flowbite_htmy.components import Pagination


@pytest.mark.asyncio
async def test_pagination_imports():
    """Test that Pagination can be imported."""
    assert Pagination is not None


@pytest.mark.asyncio
async def test_pagination_basic(renderer):
    """Test basic pagination with current page and total pages."""
    pagination = Pagination(
        current_page=3,
        total_pages=5,
        base_url="/products?page={page}",
    )
    html = await renderer.render(pagination)

    assert "Previous" in html
    assert "Next" in html
    assert "1" in html
    assert "2" in html
    assert "3" in html
    assert "4" in html
    assert "5" in html
    assert "aria-current=" in html  # Current page marker


@pytest.mark.asyncio
async def test_pagination_from_total_items(renderer):
    """Test pagination calculated from total items and items per page."""
    pagination = Pagination(
        current_page=2,
        total_items=100,
        items_per_page=10,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination)

    # Should have 10 pages (100 items / 10 per page)
    assert "1" in html
    assert "10" in html


@pytest.mark.asyncio
async def test_pagination_prev_disabled_on_first_page(renderer):
    """Test that Previous button is disabled on first page."""
    pagination = Pagination(
        current_page=1,
        total_pages=5,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination)

    # Previous should be disabled (check for cursor-not-allowed or similar)
    assert "cursor-not-allowed" in html or "opacity-50" in html


@pytest.mark.asyncio
async def test_pagination_next_disabled_on_last_page(renderer):
    """Test that Next button is disabled on last page."""
    pagination = Pagination(
        current_page=5,
        total_pages=5,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination)

    # Next should be disabled
    assert html.count("cursor-not-allowed") >= 1 or html.count("opacity-50") >= 1


@pytest.mark.asyncio
async def test_pagination_with_info_text(renderer):
    """Test pagination with info text showing item ranges."""
    pagination = Pagination(
        current_page=2,
        total_items=100,
        items_per_page=10,
        base_url="/page={page}",
        show_info=True,
    )
    html = await renderer.render(pagination)

    # Should show "Showing 11 to 20 of 100 Entries"
    assert "Showing" in html
    assert "11" in html  # Start item for page 2
    assert "20" in html  # End item for page 2
    assert "100" in html  # Total items
    assert "Entries" in html


@pytest.mark.asyncio
async def test_pagination_with_icons(renderer):
    """Test pagination with icons for prev/next buttons."""
    pagination = Pagination(
        current_page=3,
        total_pages=5,
        base_url="/page={page}",
        show_icons=True,
    )
    html = await renderer.render(pagination)

    # Should have SVG elements
    assert "<svg" in html
    assert "Previous" in html or "sr-only" in html
    assert "Next" in html or "sr-only" in html


@pytest.mark.asyncio
async def test_pagination_limited_page_numbers(renderer):
    """Test pagination with many pages shows limited numbers."""
    pagination = Pagination(
        current_page=10,
        total_pages=100,
        base_url="/page={page}",
        max_visible_pages=5,
    )
    html = await renderer.render(pagination)

    # Should show ellipsis or limited range
    assert "10" in html  # Current page always shown
    # Shouldn't show all 100 pages
    assert html.count('href="/page=') < 15  # Reasonable limit


@pytest.mark.asyncio
async def test_pagination_dark_mode(renderer, dark_context):
    """Test pagination includes dark mode classes."""
    pagination = Pagination(
        current_page=1,
        total_pages=5,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination, dark_context)

    assert "dark:bg-gray-800" in html or "dark:bg-gray-700" in html
    assert "dark:text-white" in html or "dark:text-gray-400" in html
    assert "dark:border-gray-700" in html


@pytest.mark.asyncio
async def test_pagination_custom_labels(renderer):
    """Test pagination with custom prev/next labels."""
    pagination = Pagination(
        current_page=3,
        total_pages=5,
        base_url="/page={page}",
        prev_label="← Anterior",
        next_label="Siguiente →",
    )
    html = await renderer.render(pagination)

    assert "Anterior" in html
    assert "Siguiente" in html


@pytest.mark.asyncio
async def test_pagination_aria_label(renderer):
    """Test pagination has proper ARIA label."""
    pagination = Pagination(
        current_page=3,
        total_pages=5,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination)

    assert "aria-label=" in html or "role=" in html


@pytest.mark.asyncio
async def test_pagination_single_page(renderer):
    """Test pagination with only one page."""
    pagination = Pagination(
        current_page=1,
        total_pages=1,
        base_url="/page={page}",
    )
    html = await renderer.render(pagination)

    # Should still render but with disabled prev/next
    assert "1" in html
    assert "cursor-not-allowed" in html or "opacity-50" in html


@pytest.mark.asyncio
async def test_pagination_url_formatting(renderer):
    """Test pagination URLs are formatted correctly."""
    pagination = Pagination(
        current_page=2,
        total_pages=5,
        base_url="/products?page={page}&sort=name",
    )
    html = await renderer.render(pagination)

    # Check URL contains the page parameter (& is HTML-escaped to &amp;)
    assert "/products?page=" in html
    assert "&amp;sort=name" in html or "&sort=name" in html


@pytest.mark.asyncio
async def test_pagination_size_variants(renderer):
    """Test different size variants."""
    # Small size
    pagination = Pagination(
        current_page=2,
        total_pages=5,
        base_url="/page={page}",
        size="sm",
    )
    html = await renderer.render(pagination)

    assert "h-8" in html or "text-sm" in html


@pytest.mark.asyncio
async def test_pagination_custom_class(renderer):
    """Test pagination with custom classes."""
    pagination = Pagination(
        current_page=2,
        total_pages=5,
        base_url="/page={page}",
        class_="my-custom-pagination",
    )
    html = await renderer.render(pagination)

    assert "my-custom-pagination" in html
