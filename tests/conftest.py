"""Pytest configuration and shared fixtures."""

import pytest
from htmy import Context, Renderer


@pytest.fixture
def renderer() -> Renderer:
    """Create a basic htmy Renderer instance."""
    return Renderer()


@pytest.fixture
def context() -> Context:
    """Create a basic rendering context."""
    return {}


@pytest.fixture
def dark_context() -> Context:
    """Create a context with dark mode enabled."""
    from flowbite_htmy.base import ThemeContext

    return ThemeContext(dark_mode=True).htmy_context()
