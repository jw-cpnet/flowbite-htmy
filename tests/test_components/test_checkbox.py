"""Tests for Checkbox component."""

import pytest
from htmy import html

from flowbite_htmy.components import Checkbox


@pytest.mark.asyncio
class TestCheckbox:
    """Test Checkbox component."""

    async def test_checkbox_basic(self, renderer):
        """Test basic checkbox renders correctly."""
        checkbox = Checkbox(id="terms", label="I agree to the terms and conditions")
        result = await renderer.render(checkbox)

        assert 'type="checkbox"' in result
        assert 'id="terms"' in result
        assert "I agree to the terms and conditions" in result
        assert "w-4 h-4" in result
        assert "text-blue-600" in result
        assert "bg-gray-100" in result
        assert "border-gray-300" in result
        assert "rounded-sm" in result

    async def test_checkbox_checked(self, renderer):
        """Test checked checkbox."""
        checkbox = Checkbox(id="promo", label="Get promotional offers", checked=True)
        result = await renderer.render(checkbox)

        assert 'checked=""' in result or "checked" in result

    async def test_checkbox_disabled(self, renderer):
        """Test disabled checkbox."""
        checkbox = Checkbox(
            id="shipping", label="International shipping", disabled=True
        )
        result = await renderer.render(checkbox)

        assert 'disabled=""' in result or "disabled" in result
        assert "text-gray-400 dark:text-gray-500" in result

    async def test_checkbox_required(self, renderer):
        """Test required checkbox."""
        checkbox = Checkbox(id="age", label="I am 18 years or older", required=True)
        result = await renderer.render(checkbox)

        assert 'required=""' in result or "required" in result

    async def test_checkbox_with_helper_text(self, renderer):
        """Test checkbox with helper text."""
        checkbox = Checkbox(
            id="free-shipping",
            label="Free shipping via Flowbite",
            helper_text="For orders shipped from $25 in books or $29 in other categories",
        )
        result = await renderer.render(checkbox)

        assert "Free shipping via Flowbite" in result
        assert "For orders shipped from $25 in books" in result
        assert "text-xs font-normal text-gray-500 dark:text-gray-400" in result

    async def test_checkbox_with_html_label(self, renderer):
        """Test checkbox with HTML content in label."""
        checkbox = Checkbox(
            id="terms",
            label=html.span(
                "I agree to the ",
                html.a(
                    "terms and conditions",
                    href="#",
                    class_="text-blue-600 hover:underline dark:text-blue-500",
                ),
            ),
        )
        result = await renderer.render(checkbox)

        assert "I agree to the" in result
        assert "terms and conditions" in result
        assert 'href="#"' in result
        assert "text-blue-600 hover:underline" in result

    async def test_checkbox_validation_success(self, renderer):
        """Test checkbox with success validation state."""
        checkbox = Checkbox(
            id="email",
            label="Subscribe to newsletter",
            validation="success",
            helper_text="You'll receive weekly updates",
        )
        result = await renderer.render(checkbox)

        assert "text-green-600" in result
        assert "bg-green-50" in result
        assert "border-green-300" in result
        assert "text-green-600 dark:text-green-400" in result

    async def test_checkbox_validation_error(self, renderer):
        """Test checkbox with error validation state."""
        checkbox = Checkbox(
            id="consent",
            label="I agree to data processing",
            validation="error",
            helper_text="You must accept to continue",
        )
        result = await renderer.render(checkbox)

        assert "text-red-600" in result
        assert "bg-red-50" in result
        assert "border-red-300" in result
        assert "text-red-600 dark:text-red-400" in result

    async def test_checkbox_custom_class(self, renderer):
        """Test checkbox with custom classes."""
        checkbox = Checkbox(id="custom", label="Custom checkbox", class_="my-custom-class")
        result = await renderer.render(checkbox)

        assert "my-custom-class" in result

    async def test_checkbox_custom_value(self, renderer):
        """Test checkbox with custom value."""
        checkbox = Checkbox(id="color", label="Blue", value="blue")
        result = await renderer.render(checkbox)

        assert 'value="blue"' in result

    async def test_checkbox_with_name(self, renderer):
        """Test checkbox with name attribute."""
        checkbox = Checkbox(id="color-1", label="Red", name="colors", value="red")
        result = await renderer.render(checkbox)

        assert 'name="colors"' in result
        assert 'value="red"' in result

    async def test_checkbox_dark_mode(self, renderer, dark_context):
        """Test checkbox renders with dark mode classes."""
        checkbox = Checkbox(id="dark", label="Dark mode checkbox")
        result = await renderer.render(checkbox, dark_context)

        assert "dark:bg-gray-700" in result
        assert "dark:border-gray-600" in result
        assert "dark:text-gray-300" in result

    async def test_checkbox_with_attrs(self, renderer):
        """Test checkbox with additional attributes."""
        checkbox = Checkbox(
            id="data",
            label="Custom data",
            attrs={"data-testid": "my-checkbox", "aria-label": "Custom checkbox"},
        )
        result = await renderer.render(checkbox)

        assert 'data-testid="my-checkbox"' in result
        assert 'aria-label="Custom checkbox"' in result

    async def test_checkbox_aria_describedby_with_helper(self, renderer):
        """Test checkbox has aria-describedby when helper text is present."""
        checkbox = Checkbox(
            id="shipping", label="Free shipping", helper_text="Orders over $25"
        )
        result = await renderer.render(checkbox)

        assert 'aria-describedby="shipping-helper"' in result
        assert 'id="shipping-helper"' in result

    async def test_checkbox_structure(self, renderer):
        """Test checkbox HTML structure matches Flowbite pattern."""
        checkbox = Checkbox(id="test", label="Test label")
        result = await renderer.render(checkbox)

        # Should have wrapper div with flex items-center
        assert "flex items-center" in result
        # Should have input first, then label
        assert result.index("type=\"checkbox\"") < result.index("Test label")
