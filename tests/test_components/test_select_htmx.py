"""Tests for Select component - name attribute, bare mode, and HTMX attributes."""

import pytest

from flowbite_htmy.components import Select


@pytest.mark.asyncio
async def test_select_name_defaults_to_id(renderer):
    """Test that name defaults to id when not provided."""
    select = Select(id="country", options=["US", "CA"])
    html = await renderer.render(select)

    assert 'name="country"' in html


@pytest.mark.asyncio
async def test_select_custom_name(renderer):
    """Test that name can be set independently of id."""
    select = Select(id="country-field", name="country_code", options=["US", "CA"])
    html = await renderer.render(select)

    assert 'id="country-field"' in html
    assert 'name="country_code"' in html


@pytest.mark.asyncio
async def test_select_bare_mode(renderer):
    """Test select renders without label wrapper when label is None."""
    select = Select(id="bare-select", options=["A", "B"])
    html = await renderer.render(select)

    # Should have the select element
    assert 'id="bare-select"' in html
    assert "<option" in html
    # Should NOT have a label element
    assert "<label" not in html


@pytest.mark.asyncio
async def test_select_with_label(renderer):
    """Test select renders with label wrapper."""
    select = Select(id="country", label="Country", options=["US", "CA"])
    html = await renderer.render(select)

    assert "<label" in html
    assert "Country" in html
    assert 'for="country"' in html


@pytest.mark.asyncio
async def test_select_hx_get(renderer):
    """Test select with hx-get attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_get="/api/cities",
    )
    html = await renderer.render(select)

    assert 'hx-get="/api/cities"' in html


@pytest.mark.asyncio
async def test_select_hx_post(renderer):
    """Test select with hx-post attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_post="/api/filter",
    )
    html = await renderer.render(select)

    assert 'hx-post="/api/filter"' in html


@pytest.mark.asyncio
async def test_select_hx_target(renderer):
    """Test select with hx-target attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_get="/api/cities",
        hx_target="#cities-list",
    )
    html = await renderer.render(select)

    assert 'hx-target="#cities-list"' in html


@pytest.mark.asyncio
async def test_select_hx_swap(renderer):
    """Test select with hx-swap attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_get="/api/cities",
        hx_swap="outerHTML",
    )
    html = await renderer.render(select)

    assert 'hx-swap="outerHTML"' in html


@pytest.mark.asyncio
async def test_select_hx_trigger(renderer):
    """Test select with hx-trigger attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_get="/api/cities",
        hx_trigger="change",
    )
    html = await renderer.render(select)

    assert 'hx-trigger="change"' in html


@pytest.mark.asyncio
async def test_select_hx_include(renderer):
    """Test select with hx-include attribute."""
    select = Select(
        id="region",
        options=["US", "CA"],
        hx_get="/api/cities",
        hx_include="#filter-form",
    )
    html = await renderer.render(select)

    assert 'hx-include="#filter-form"' in html


@pytest.mark.asyncio
async def test_select_all_htmx_attrs(renderer):
    """Test select with all HTMX attributes combined."""
    select = Select(
        id="datasource",
        name="ds_id",
        options=[{"value": "1", "label": "DS 1"}, {"value": "2", "label": "DS 2"}],
        hx_get="/api/features",
        hx_target="#features-list",
        hx_swap="innerHTML",
        hx_trigger="change",
        hx_include="#filter-form",
    )
    html = await renderer.render(select)

    assert 'name="ds_id"' in html
    assert 'hx-get="/api/features"' in html
    assert 'hx-target="#features-list"' in html
    assert 'hx-swap="innerHTML"' in html
    assert 'hx-trigger="change"' in html
    assert 'hx-include="#filter-form"' in html
    assert "<label" not in html  # bare mode
