"""Type definitions for consolidated showcase application."""

from typing import TypedDict


class ComponentRoute(TypedDict):
    """Metadata for a component showcase page route."""

    name: str
    path: str
    title: str
    description: str
    order: int


class NavigationItem(TypedDict):
    """Navigation menu item with active state."""

    label: str
    url: str
    is_active: bool


class PageContext(TypedDict):
    """Template context data for page rendering."""

    current_page: str
    title: str
    navigation: str
    content: str
