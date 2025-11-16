"""Tests for Accordion component following strict TDD approach."""

import pytest
from htmy import SafeStr

from flowbite_htmy.components import Accordion, AccordionMode, AccordionVariant, Panel
from flowbite_htmy.icons import Icon, get_icon
from flowbite_htmy.types import Color

# ============================================================================
# User Story 1: Basic Accordion Creation
# ============================================================================


@pytest.mark.asyncio
async def test_accordion_default_rendering(renderer):
    """Accordion renders with default mode and variant."""
    accordion = Accordion(
        panels=[
            Panel(title="Panel 1", content="Content 1"),
            Panel(title="Panel 2", content="Content 2"),
        ]
    )
    html = await renderer.render(accordion)

    assert 'data-accordion="collapse"' in html
    assert "Panel 1" in html
    assert "Panel 2" in html
    assert "Content 1" in html
    assert "Content 2" in html


@pytest.mark.asyncio
async def test_accordion_generates_unique_ids(renderer):
    """Each panel has unique IDs for ARIA relationships."""
    accordion = Accordion(
        panels=[
            Panel(title="P1", content="C1"),
            Panel(title="P2", content="C2"),
            Panel(title="P3", content="C3"),
        ]
    )
    html = await renderer.render(accordion)

    # Verify heading IDs exist and are unique
    assert 'id="accordion-' in html
    assert '-heading-0"' in html
    assert '-heading-1"' in html
    assert '-heading-2"' in html

    # Verify body IDs exist and are unique
    assert '-body-0"' in html
    assert '-body-1"' in html
    assert '-body-2"' in html


@pytest.mark.asyncio
async def test_accordion_aria_attributes(renderer):
    """ARIA attributes properly link headers and panels."""
    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", is_open=True),
            Panel(title="Q2", content="A2", is_open=False),
        ]
    )
    html = await renderer.render(accordion)

    # First panel (open)
    assert 'aria-expanded="true"' in html
    assert 'aria-controls="accordion-' in html
    assert '-body-0"' in html

    # Second panel (closed)
    assert 'aria-expanded="false"' in html
    assert 'aria-controls="accordion-' in html
    assert '-body-1"' in html

    # Both panels have aria-labelledby
    assert 'aria-labelledby="accordion-' in html


@pytest.mark.asyncio
async def test_accordion_flowbite_classes(renderer):
    """Flowbite classes applied to accordion elements."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        variant=AccordionVariant.DEFAULT,
    )
    html = await renderer.render(accordion)

    # Button classes
    assert "flex items-center justify-between" in html
    assert "w-full" in html
    assert "p-5" in html
    assert "font-medium" in html
    assert "border border-b-0 border-gray-200" in html
    assert "rounded-t-xl" in html
    assert "focus:ring-4" in html
    assert "hover:bg-gray-100" in html

    # Dark mode classes
    assert "dark:border-gray-700" in html
    assert "dark:text-gray-400" in html
    assert "dark:hover:bg-gray-800" in html


@pytest.mark.asyncio
async def test_accordion_data_attribute_collapse(renderer):
    """Collapse mode sets data-accordion='collapse'."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        mode=AccordionMode.COLLAPSE,
    )
    html = await renderer.render(accordion)
    assert 'data-accordion="collapse"' in html


@pytest.mark.asyncio
async def test_accordion_data_attribute_always_open(renderer):
    """Always-open mode sets data-accordion='open'."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        mode=AccordionMode.ALWAYS_OPEN,
    )
    html = await renderer.render(accordion)
    assert 'data-accordion="open"' in html


# ============================================================================
# User Story 2: Accordion Customization
# ============================================================================


@pytest.mark.asyncio
async def test_accordion_flush_variant(renderer):
    """Flush variant removes side borders and rounding."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        variant=AccordionVariant.FLUSH,
    )
    html = await renderer.render(accordion)

    # Flush button classes (border-b only, no rounding, py-5)
    assert "border-b border-gray-200" in html
    assert "py-5" in html
    assert "rounded-t-xl" not in html  # No rounding
    assert "border border-b-0" not in html  # No side borders


@pytest.mark.asyncio
async def test_accordion_color_customization(renderer):
    """Color prop applies background and hover classes."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        color=Color.BLUE,
    )
    html = await renderer.render(accordion)

    # Blue color classes (hover state)
    assert "hover:bg-blue-100" in html
    assert "dark:hover:bg-blue-800" in html or "dark:hover:bg-gray-800" in html


@pytest.mark.asyncio
async def test_accordion_dark_mode_classes_always_included(renderer, context):
    """Dark mode classes always present in light mode context."""
    accordion = Accordion(panels=[Panel(title="Q1", content="A1")])
    html = await renderer.render(accordion, context)  # Light mode context

    # Dark classes must be present even in light mode
    assert "dark:border-gray-700" in html
    assert "dark:text-gray-400" in html
    assert "dark:hover:bg-gray-800" in html or "dark:hover:bg-blue-800" in html
    assert "dark:focus:ring-gray-800" in html


@pytest.mark.asyncio
async def test_accordion_always_open_mode(renderer):
    """Always-open mode allows multiple panels open."""
    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", is_open=True),
            Panel(title="Q2", content="A2", is_open=True),
        ],
        mode=AccordionMode.ALWAYS_OPEN,
    )
    html = await renderer.render(accordion)

    assert 'data-accordion="open"' in html
    # Both panels can be open (no hidden class)
    assert html.count('aria-expanded="true"') == 2


@pytest.mark.asyncio
async def test_accordion_custom_panel_icons(renderer):
    """Custom icons replace default chevron."""
    custom_icon = get_icon(Icon.EXCLAMATION_CIRCLE, class_="w-5 h-5")

    accordion = Accordion(
        panels=[
            Panel(title="Q1", content="A1", icon=SafeStr(custom_icon)),
        ]
    )
    html = await renderer.render(accordion)

    # Custom icon SVG present with w-5 h-5 classes (not w-3 h-3 from default)
    assert "w-5 h-5" in html
    # Exclamation circle has viewBox="0 0 20 20", not chevron's "0 0 10 6"
    assert 'viewBox="0 0 20 20"' in html


# ============================================================================
# User Story 3: HTMX Integration
# ============================================================================


@pytest.mark.asyncio
async def test_accordion_htmx_get_attribute(renderer):
    """HTMX hx-get attribute renders on panel body."""
    accordion = Accordion(
        panels=[
            Panel(
                title="Lazy Load",
                content="Loading...",
                hx_get="/api/content/1",
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-get="/api/content/1"' in html


@pytest.mark.asyncio
async def test_accordion_htmx_trigger_attribute(renderer):
    """HTMX hx-trigger attribute is configurable."""
    accordion = Accordion(
        panels=[
            Panel(
                title="Custom Trigger",
                content="Content",
                hx_get="/api/data",
                hx_trigger="revealed once",
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-trigger="revealed once"' in html


@pytest.mark.asyncio
async def test_accordion_multiple_htmx_attributes(renderer):
    """Multiple HTMX attributes can be combined."""
    accordion = Accordion(
        panels=[
            Panel(
                title="Full HTMX",
                content="Content",
                hx_get="/api/data",
                hx_trigger="revealed",
                hx_swap="innerHTML",
                hx_target="this",
            ),
        ]
    )
    html = await renderer.render(accordion)

    assert 'hx-get="/api/data"' in html
    assert 'hx-trigger="revealed"' in html
    assert 'hx-swap="innerHTML"' in html
    assert 'hx-target="this"' in html


# ============================================================================
# Edge Cases
# ============================================================================


@pytest.mark.asyncio
async def test_accordion_single_panel(renderer):
    """Accordion with single panel renders correctly."""
    accordion = Accordion(panels=[Panel(title="Only Panel", content="Only Content")])
    html = await renderer.render(accordion)

    assert "Only Panel" in html
    assert "Only Content" in html
    assert "-heading-0" in html
    assert "-body-0" in html


@pytest.mark.asyncio
async def test_accordion_empty_content(renderer):
    """Panels with empty content render empty body."""
    accordion = Accordion(panels=[Panel(title="Empty Panel", content="")])
    html = await renderer.render(accordion)

    assert "Empty Panel" in html
    # Panel body exists but is empty
    assert "-body-0" in html


@pytest.mark.asyncio
async def test_accordion_handles_invalid_open_index(renderer):
    """Accordion handles is_open gracefully for all panels."""
    # This test verifies no IndexError when all panels have is_open set
    accordion = Accordion(
        panels=[
            Panel(title="P1", content="C1", is_open=True),
            Panel(title="P2", content="C2", is_open=False),
        ]
    )
    html = await renderer.render(accordion)

    assert 'aria-expanded="true"' in html  # P1
    assert 'aria-expanded="false"' in html  # P2


@pytest.mark.asyncio
async def test_accordion_custom_classes(renderer):
    """Custom classes merge with component classes."""
    accordion = Accordion(
        panels=[Panel(title="Q1", content="A1")],
        class_="my-8 max-w-2xl",
    )
    html = await renderer.render(accordion)

    assert "my-8" in html
    assert "max-w-2xl" in html
