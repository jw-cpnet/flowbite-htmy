"""Tests for HTMX helper functions."""

from flowbite_htmy.htmx import drawer_close_handler, modal_close_handler


def test_drawer_close_handler_basic():
    """Test basic drawer close handler."""
    js = drawer_close_handler("my-drawer")

    assert "event.detail.successful" in js
    assert "FlowbiteInstances.getInstance('Drawer', 'my-drawer')" in js
    assert "drawer.hide()" in js


def test_drawer_close_handler_with_reset_form():
    """Test drawer close handler with form reset."""
    js = drawer_close_handler("my-drawer", reset_form=True)

    assert "event.target.reset" in js
    assert "drawer.hide()" in js


def test_drawer_close_handler_with_extra_js():
    """Test drawer close handler with extra JavaScript."""
    js = drawer_close_handler("my-drawer", extra_js="location.reload();")

    assert "location.reload();" in js
    assert "drawer.hide()" in js


def test_drawer_close_handler_with_all_options():
    """Test drawer close handler with all options."""
    js = drawer_close_handler(
        "my-drawer",
        reset_form=True,
        extra_js="console.log('done');",
    )

    assert "drawer.hide()" in js
    assert "event.target.reset" in js
    assert "console.log('done');" in js


def test_modal_close_handler_basic():
    """Test basic modal close handler."""
    js = modal_close_handler("my-modal")

    assert "event.detail.successful" in js
    assert "FlowbiteInstances.getInstance('Modal', 'my-modal')" in js
    assert "modal.hide()" in js


def test_modal_close_handler_with_extra_js():
    """Test modal close handler with extra JavaScript."""
    js = modal_close_handler("my-modal", extra_js="location.reload();")

    assert "location.reload();" in js
    assert "modal.hide()" in js


def test_handlers_are_multiline():
    """Test that handlers produce multiline output for readability."""
    js = drawer_close_handler("test")
    assert "\n" in js

    js = modal_close_handler("test")
    assert "\n" in js
