"""Tests for the Input component."""

import pytest

from flowbite_htmy.components import Input


@pytest.mark.asyncio
async def test_input_imports():
    """Test that Input can be imported."""
    assert Input is not None


@pytest.mark.asyncio
async def test_input_renders_basic(renderer):
    """Test basic input rendering with label and input field."""
    input_field = Input(
        id="email",
        label="Email address",
        type="email",
    )
    html = await renderer.render(input_field)

    assert 'id="email"' in html
    assert "Email address" in html
    assert 'type="email"' in html
    assert "bg-gray-50" in html  # Default background
    assert "border-gray-300" in html  # Default border


@pytest.mark.asyncio
async def test_input_with_placeholder(renderer):
    """Test input with placeholder text."""
    input_field = Input(
        id="name",
        label="Your name",
        placeholder="John Doe",
    )
    html = await renderer.render(input_field)

    assert 'placeholder="John Doe"' in html


@pytest.mark.asyncio
async def test_input_required(renderer):
    """Test required input field."""
    input_field = Input(
        id="email",
        label="Email",
        required=True,
    )
    html = await renderer.render(input_field)

    assert "required" in html


@pytest.mark.asyncio
async def test_input_with_helper_text(renderer):
    """Test input with helper text below field."""
    input_field = Input(
        id="password",
        label="Password",
        helper_text="Must be at least 8 characters",
    )
    html = await renderer.render(input_field)

    assert "Must be at least 8 characters" in html
    assert "text-sm" in html  # Helper text styling


@pytest.mark.asyncio
async def test_input_validation_success(renderer):
    """Test input with success validation state."""
    input_field = Input(
        id="username",
        label="Username",
        validation="success",
        helper_text="Username is available!",
    )
    html = await renderer.render(input_field)

    assert "border-green-500" in html  # Success border
    assert "text-green-" in html  # Success text color
    assert "Username is available!" in html


@pytest.mark.asyncio
async def test_input_validation_error(renderer):
    """Test input with error validation state."""
    input_field = Input(
        id="username",
        label="Username",
        validation="error",
        helper_text="Username is already taken",
    )
    html = await renderer.render(input_field)

    assert "border-red-500" in html  # Error border
    assert "text-red-" in html  # Error text color
    assert "Username is already taken" in html


@pytest.mark.asyncio
async def test_input_disabled(renderer):
    """Test disabled input field."""
    input_field = Input(
        id="disabled",
        label="Disabled field",
        disabled=True,
        value="Cannot edit",
    )
    html = await renderer.render(input_field)

    assert "disabled" in html
    assert "cursor-not-allowed" in html
    assert "Cannot edit" in html


@pytest.mark.asyncio
async def test_input_with_value(renderer):
    """Test input with initial value."""
    input_field = Input(
        id="city",
        label="City",
        value="San Francisco",
    )
    html = await renderer.render(input_field)

    assert 'value="San Francisco"' in html


@pytest.mark.asyncio
async def test_input_dark_mode(renderer, dark_context):
    """Test input includes dark mode classes."""
    input_field = Input(
        id="email",
        label="Email",
    )
    html = await renderer.render(input_field, dark_context)

    assert "dark:bg-gray-700" in html
    assert "dark:border-gray-600" in html
    assert "dark:text-white" in html


@pytest.mark.asyncio
async def test_input_custom_class(renderer):
    """Test input with custom classes."""
    input_field = Input(
        id="custom",
        label="Custom",
        class_="my-custom-class",
    )
    html = await renderer.render(input_field)

    assert "my-custom-class" in html


@pytest.mark.asyncio
async def test_input_passthrough_attrs(renderer):
    """Test input with passthrough attributes."""
    input_field = Input(
        id="phone",
        label="Phone",
        attrs={"data-testid": "phone-input", "autocomplete": "tel"},
    )
    html = await renderer.render(input_field)

    assert 'data-testid="phone-input"' in html
    assert 'autocomplete="tel"' in html


@pytest.mark.asyncio
async def test_input_various_types(renderer):
    """Test different input types."""
    types_to_test = ["text", "email", "password", "number", "tel", "url"]

    for input_type in types_to_test:
        input_field = Input(
            id=f"test-{input_type}",
            label=f"Test {input_type}",
            type=input_type,
        )
        html = await renderer.render(input_field)
        assert f'type="{input_type}"' in html
