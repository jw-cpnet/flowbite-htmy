"""Tests for Input component - name attribute, bare mode, and HTMX attributes."""

import pytest

from flowbite_htmy.components import Input


@pytest.mark.asyncio
async def test_input_name_defaults_to_id(renderer):
    """Test that name defaults to id when not provided."""
    input_field = Input(id="email", label="Email")
    html = await renderer.render(input_field)

    assert 'name="email"' in html


@pytest.mark.asyncio
async def test_input_custom_name(renderer):
    """Test that name can be set independently of id."""
    input_field = Input(id="email-field", name="user_email", label="Email")
    html = await renderer.render(input_field)

    assert 'id="email-field"' in html
    assert 'name="user_email"' in html


@pytest.mark.asyncio
async def test_input_bare_mode(renderer):
    """Test input renders without label wrapper when label is None."""
    input_field = Input(id="bare-input")
    html = await renderer.render(input_field)

    # Should have the input element
    assert 'id="bare-input"' in html
    # Should NOT have a label element
    assert "<label" not in html
    # Should NOT have a wrapping div with 'for' attribute
    assert 'for="bare-input"' not in html


@pytest.mark.asyncio
async def test_input_bare_mode_with_name(renderer):
    """Test bare input has name attribute."""
    input_field = Input(id="search", name="q")
    html = await renderer.render(input_field)

    assert 'name="q"' in html
    assert "<label" not in html


@pytest.mark.asyncio
async def test_input_hx_get(renderer):
    """Test input with hx-get attribute."""
    input_field = Input(
        id="search",
        label="Search",
        hx_get="/api/search",
    )
    html = await renderer.render(input_field)

    assert 'hx-get="/api/search"' in html


@pytest.mark.asyncio
async def test_input_hx_post(renderer):
    """Test input with hx-post attribute."""
    input_field = Input(
        id="email",
        label="Email",
        hx_post="/api/validate",
    )
    html = await renderer.render(input_field)

    assert 'hx-post="/api/validate"' in html


@pytest.mark.asyncio
async def test_input_hx_target(renderer):
    """Test input with hx-target attribute."""
    input_field = Input(
        id="search",
        label="Search",
        hx_get="/api/search",
        hx_target="#results",
    )
    html = await renderer.render(input_field)

    assert 'hx-target="#results"' in html


@pytest.mark.asyncio
async def test_input_hx_swap(renderer):
    """Test input with hx-swap attribute."""
    input_field = Input(
        id="search",
        label="Search",
        hx_get="/api/search",
        hx_swap="outerHTML",
    )
    html = await renderer.render(input_field)

    assert 'hx-swap="outerHTML"' in html


@pytest.mark.asyncio
async def test_input_hx_trigger(renderer):
    """Test input with hx-trigger attribute."""
    input_field = Input(
        id="search",
        label="Search",
        hx_get="/api/search",
        hx_trigger="keyup changed delay:300ms",
    )
    html = await renderer.render(input_field)

    assert 'hx-trigger="keyup changed delay:300ms"' in html


@pytest.mark.asyncio
async def test_input_all_htmx_attrs(renderer):
    """Test input with all HTMX attributes."""
    input_field = Input(
        id="search",
        name="q",
        hx_get="/api/search",
        hx_target="#results",
        hx_swap="innerHTML",
        hx_trigger="keyup changed delay:500ms",
    )
    html = await renderer.render(input_field)

    assert 'name="q"' in html
    assert 'hx-get="/api/search"' in html
    assert 'hx-target="#results"' in html
    assert 'hx-swap="innerHTML"' in html
    assert 'hx-trigger="keyup changed delay:500ms"' in html
    assert "<label" not in html  # bare mode
