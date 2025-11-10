"""Tests for the Select component."""

import pytest

from flowbite_htmy.components import Select


@pytest.mark.asyncio
async def test_select_imports():
    """Test that Select can be imported."""
    assert Select is not None


@pytest.mark.asyncio
async def test_select_renders_basic(renderer):
    """Test basic select rendering with label and options."""
    select = Select(
        id="countries",
        label="Select your country",
        options=["United States", "Canada", "France", "Germany"],
    )
    html = await renderer.render(select)

    assert 'id="countries"' in html
    assert "Select your country" in html
    assert "<select" in html
    assert "United States" in html
    assert "Canada" in html
    assert "France" in html
    assert "Germany" in html


@pytest.mark.asyncio
async def test_select_with_dict_options(renderer):
    """Test select with dict options (value and label)."""
    select = Select(
        id="countries",
        label="Select a country",
        options=[
            {"value": "US", "label": "United States"},
            {"value": "CA", "label": "Canada"},
            {"value": "FR", "label": "France"},
        ],
    )
    html = await renderer.render(select)

    assert 'value="US"' in html
    assert 'value="CA"' in html
    assert 'value="FR"' in html
    assert "United States" in html
    assert "Canada" in html
    assert "France" in html


@pytest.mark.asyncio
async def test_select_with_placeholder(renderer):
    """Test select with placeholder option."""
    select = Select(
        id="countries",
        label="Select a country",
        placeholder="Choose a country",
        options=["United States", "Canada"],
    )
    html = await renderer.render(select)

    assert "Choose a country" in html
    assert "selected" in html


@pytest.mark.asyncio
async def test_select_with_selected_value(renderer):
    """Test select with pre-selected value."""
    select = Select(
        id="countries",
        label="Select a country",
        options=[
            {"value": "US", "label": "United States"},
            {"value": "CA", "label": "Canada"},
            {"value": "FR", "label": "France"},
        ],
        value="CA",
    )
    html = await renderer.render(select)

    assert 'value="CA"' in html
    assert "selected" in html
    assert "Canada" in html


@pytest.mark.asyncio
async def test_select_multiple(renderer):
    """Test select with multiple attribute."""
    select = Select(
        id="countries",
        label="Select countries",
        options=["United States", "Canada", "France"],
        multiple=True,
    )
    html = await renderer.render(select)

    assert "multiple" in html


@pytest.mark.asyncio
async def test_select_with_size(renderer):
    """Test select with size attribute."""
    select = Select(
        id="years",
        label="Select a year",
        options=["2020", "2021", "2022", "2023", "2024"],
        size=5,
    )
    html = await renderer.render(select)

    assert 'size="5"' in html


@pytest.mark.asyncio
async def test_select_disabled(renderer):
    """Test disabled select field."""
    select = Select(
        id="disabled",
        label="Disabled field",
        options=["Option 1", "Option 2"],
        disabled=True,
    )
    html = await renderer.render(select)

    assert "disabled" in html
    assert "cursor-not-allowed" in html


@pytest.mark.asyncio
async def test_select_required(renderer):
    """Test required select field."""
    select = Select(
        id="country",
        label="Country",
        options=["United States", "Canada"],
        required=True,
    )
    html = await renderer.render(select)

    assert "required" in html


@pytest.mark.asyncio
async def test_select_with_helper_text(renderer):
    """Test select with helper text below field."""
    select = Select(
        id="country",
        label="Country",
        options=["United States", "Canada"],
        helper_text="Choose your primary residence",
    )
    html = await renderer.render(select)

    assert "Choose your primary residence" in html
    assert "text-sm" in html  # Helper text styling


@pytest.mark.asyncio
async def test_select_validation_success(renderer):
    """Test select with success validation state."""
    select = Select(
        id="country",
        label="Country",
        options=["United States", "Canada"],
        validation="success",
        helper_text="Valid selection",
    )
    html = await renderer.render(select)

    assert "border-green-500" in html  # Success border
    assert "text-green-" in html  # Success text color


@pytest.mark.asyncio
async def test_select_validation_error(renderer):
    """Test select with error validation state."""
    select = Select(
        id="country",
        label="Country",
        options=["United States", "Canada"],
        validation="error",
        helper_text="Please select a valid country",
    )
    html = await renderer.render(select)

    assert "border-red-500" in html  # Error border
    assert "text-red-" in html  # Error text color


@pytest.mark.asyncio
async def test_select_dark_mode(renderer, dark_context):
    """Test select includes dark mode classes."""
    select = Select(
        id="country",
        label="Country",
        options=["United States", "Canada"],
    )
    html = await renderer.render(select, dark_context)

    assert "dark:bg-gray-700" in html
    assert "dark:border-gray-600" in html
    assert "dark:text-white" in html


@pytest.mark.asyncio
async def test_select_custom_class(renderer):
    """Test select with custom classes."""
    select = Select(
        id="custom",
        label="Custom",
        options=["Option 1"],
        class_="my-custom-class",
    )
    html = await renderer.render(select)

    assert "my-custom-class" in html


@pytest.mark.asyncio
async def test_select_passthrough_attrs(renderer):
    """Test select with passthrough attributes."""
    select = Select(
        id="country",
        label="Country",
        options=["United States"],
        attrs={"data-testid": "country-select", "autocomplete": "country"},
    )
    html = await renderer.render(select)

    assert 'data-testid="country-select"' in html
    assert 'autocomplete="country"' in html
