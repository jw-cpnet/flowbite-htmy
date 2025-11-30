"""Tests for Button HTMX functionality."""

import pytest
from htmy import HTMY

from flowbite_htmy.components import Button


@pytest.fixture
def htmy():
    return HTMY()


class TestButtonHtmxInclude:
    """Test hx_include attribute."""

    @pytest.mark.asyncio
    async def test_hx_include_renders(self, htmy):
        button = Button(
            label="Delete",
            hx_delete="/api/items/1",
            hx_include="[name='page'], [name='size']",
        )
        html = await htmy.render(button)
        assert "hx-include=\"[name='page'], [name='size']\"" in html

    @pytest.mark.asyncio
    async def test_hx_include_with_closest_selector(self, htmy):
        button = Button(
            label="Submit",
            hx_post="/api/form",
            hx_include="closest form",
        )
        html = await htmy.render(button)
        assert 'hx-include="closest form"' in html


class TestButtonHtmxConfirm:
    """Test hx_confirm attribute."""

    @pytest.mark.asyncio
    async def test_hx_confirm_renders(self, htmy):
        button = Button(
            label="Delete",
            hx_delete="/api/items/1",
            hx_confirm="Are you sure?",
        )
        html = await htmy.render(button)
        assert 'hx-confirm="Are you sure?"' in html


class TestButtonHtmxVals:
    """Test hx_vals attribute."""

    @pytest.mark.asyncio
    async def test_hx_vals_renders(self, htmy):
        button = Button(
            label="Load More",
            hx_get="/api/items",
            hx_vals='{"page": 2, "size": 10}',
        )
        html = await htmy.render(button)
        # htmy uses single quotes for attributes containing double quotes
        assert "hx-vals=" in html
        assert '"page": 2' in html


class TestButtonHtmxIndicator:
    """Test hx_indicator attribute."""

    @pytest.mark.asyncio
    async def test_hx_indicator_renders(self, htmy):
        button = Button(
            label="Submit",
            hx_post="/api/submit",
            hx_indicator="#spinner",
        )
        html = await htmy.render(button)
        assert 'hx-indicator="#spinner"' in html


class TestButtonHtmxEncoding:
    """Test hx_encoding attribute."""

    @pytest.mark.asyncio
    async def test_hx_encoding_multipart(self, htmy):
        button = Button(
            label="Upload",
            hx_post="/api/upload",
            hx_encoding="multipart/form-data",
        )
        html = await htmy.render(button)
        assert 'hx-encoding="multipart/form-data"' in html


class TestButtonHtmxHeaders:
    """Test hx_headers attribute."""

    @pytest.mark.asyncio
    async def test_hx_headers_renders(self, htmy):
        button = Button(
            label="Submit",
            hx_post="/api/submit",
            hx_headers='{"X-Custom-Header": "value"}',
        )
        html = await htmy.render(button)
        assert "hx-headers" in html


class TestButtonHtmxDisabledElt:
    """Test hx_disabled_elt attribute."""

    @pytest.mark.asyncio
    async def test_hx_disabled_elt_renders(self, htmy):
        button = Button(
            label="Submit",
            hx_post="/api/submit",
            hx_disabled_elt="this",
        )
        html = await htmy.render(button)
        assert 'hx-disabled-elt="this"' in html

    @pytest.mark.asyncio
    async def test_hx_disabled_elt_with_selector(self, htmy):
        button = Button(
            label="Submit",
            hx_post="/api/submit",
            hx_disabled_elt="closest form",
        )
        html = await htmy.render(button)
        assert 'hx-disabled-elt="closest form"' in html


class TestButtonHtmxSync:
    """Test hx_sync attribute."""

    @pytest.mark.asyncio
    async def test_hx_sync_renders(self, htmy):
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_sync="closest form:abort",
        )
        html = await htmy.render(button)
        assert 'hx-sync="closest form:abort"' in html


class TestButtonHxOn:
    """Test hx_on event handlers."""

    @pytest.mark.asyncio
    async def test_single_event_handler(self, htmy):
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={"after-request": "drawer.hide()"},
        )
        html = await htmy.render(button)
        assert 'hx-on::after-request="drawer.hide()"' in html

    @pytest.mark.asyncio
    async def test_multiple_event_handlers(self, htmy):
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={
                "before-request": "showLoading()",
                "after-request": "hideLoading()",
            },
        )
        html = await htmy.render(button)
        assert 'hx-on::before-request="showLoading()"' in html
        assert 'hx-on::after-request="hideLoading()"' in html

    @pytest.mark.asyncio
    async def test_complex_handler_with_condition(self, htmy):
        handler = "if(event.detail.successful) { drawer.hide(); }"
        button = Button(
            label="Save",
            hx_post="/api/save",
            hx_on={"after-request": handler},
        )
        html = await htmy.render(button)
        # The handler will be HTML escaped
        assert "hx-on::after-request=" in html
        assert "event.detail.successful" in html

    @pytest.mark.asyncio
    async def test_htmx_response_events(self, htmy):
        """Test HTMX response-related events."""
        button = Button(
            label="Fetch",
            hx_get="/api/data",
            hx_on={
                "htmx:before-send": "console.log('sending')",
                "htmx:after-settle": "console.log('settled')",
            },
        )
        html = await htmy.render(button)
        assert "hx-on::htmx:before-send=" in html
        assert "hx-on::htmx:after-settle=" in html

    @pytest.mark.asyncio
    async def test_hx_on_empty_dict(self, htmy):
        """Test that empty hx_on dict doesn't add attributes."""
        button = Button(
            label="Click",
            hx_on={},
        )
        html = await htmy.render(button)
        assert "hx-on::" not in html

    @pytest.mark.asyncio
    async def test_hx_on_none(self, htmy):
        """Test that None hx_on doesn't add attributes."""
        button = Button(
            label="Click",
            hx_on=None,
        )
        html = await htmy.render(button)
        assert "hx-on::" not in html


class TestButtonHtmxCombined:
    """Test combinations of HTMX attributes."""

    @pytest.mark.asyncio
    async def test_delete_with_confirm_and_include(self, htmy):
        """Test a realistic delete button with confirmation."""
        button = Button(
            label="Delete Item",
            hx_delete="/api/items/123",
            hx_confirm="Are you sure you want to delete this item?",
            hx_include="[name='csrf_token']",
            hx_target="#item-123",
            hx_swap="outerHTML",
        )
        html = await htmy.render(button)
        assert 'hx-delete="/api/items/123"' in html
        assert "hx-confirm=" in html
        assert "hx-include=" in html
        assert 'hx-target="#item-123"' in html
        assert 'hx-swap="outerHTML"' in html

    @pytest.mark.asyncio
    async def test_form_submit_with_all_features(self, htmy):
        """Test a form submit button with comprehensive HTMX setup."""
        button = Button(
            label="Submit Form",
            hx_post="/api/form",
            hx_include="closest form",
            hx_indicator="#loading",
            hx_disabled_elt="this",
            hx_sync="closest form:abort",
            hx_on={
                "after-request": "if(event.detail.successful) showSuccess()",
            },
        )
        html = await htmy.render(button)
        assert 'hx-post="/api/form"' in html
        assert 'hx-include="closest form"' in html
        assert 'hx-indicator="#loading"' in html
        assert 'hx-disabled-elt="this"' in html
        assert 'hx-sync="closest form:abort"' in html
        assert "hx-on::after-request=" in html
