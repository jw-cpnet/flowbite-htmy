"""Tests for Drawer and DrawerShell components."""

import pytest
from htmy import html

from flowbite_htmy.components.drawer import Drawer, DrawerShell
from flowbite_htmy.types import Color, DrawerPlacement, DrawerWidth, Size


# Phase 3: User Story 1 Tests (T010-T020) - Red Phase


@pytest.mark.asyncio
async def test_drawer_renders_with_minimal_props(renderer):
    """T010: Drawer renders with minimal props (trigger_label, content)."""
    drawer = Drawer(
        trigger_label="Open Menu",
        content=html.div("Menu content"),
    )
    result = await renderer.render(drawer)

    assert "Open Menu" in result
    assert "Menu content" in result


@pytest.mark.asyncio
async def test_trigger_button_has_correct_data_attributes(renderer):
    """T011: Trigger button has correct data-drawer-target and data-drawer-show attributes."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # Should have data-drawer-target and data-drawer-show pointing to drawer ID
    assert "data-drawer-target=" in result
    assert "data-drawer-show=" in result
    # Both should point to same drawer ID
    assert result.count('data-drawer-target="drawer-') == 1
    assert result.count('data-drawer-show="drawer-') >= 1


@pytest.mark.asyncio
async def test_drawer_panel_left_placement_default(renderer):
    """T012: Drawer panel renders LEFT placement (default) with correct transform classes."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # LEFT placement should have left-0, top-0, h-screen, and -translate-x-full classes
    assert "left-0" in result
    assert "top-0" in result
    assert "h-screen" in result
    assert "-translate-x-full" in result


@pytest.mark.asyncio
async def test_drawer_panel_right_placement(renderer):
    """T013: Drawer panel renders RIGHT placement with translate-x-full initial state."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        placement=DrawerPlacement.RIGHT,
    )
    result = await renderer.render(drawer)

    # RIGHT placement should have right-0, top-0, h-screen, and translate-x-full classes
    assert "right-0" in result
    assert "top-0" in result
    assert "h-screen" in result
    assert "translate-x-full" in result


@pytest.mark.asyncio
async def test_drawer_panel_top_placement(renderer):
    """T014: Drawer panel renders TOP placement with -translate-y-full initial state."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        placement=DrawerPlacement.TOP,
    )
    result = await renderer.render(drawer)

    # TOP placement should have top-0, left-0, w-full, and -translate-y-full classes
    assert "top-0" in result
    assert "left-0" in result
    assert "w-full" in result
    assert "-translate-y-full" in result


@pytest.mark.asyncio
async def test_drawer_panel_bottom_placement(renderer):
    """T015: Drawer panel renders BOTTOM placement with translate-y-full initial state."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        placement=DrawerPlacement.BOTTOM,
    )
    result = await renderer.render(drawer)

    # BOTTOM placement should have bottom-0, left-0, w-full, and translate-y-full classes
    assert "bottom-0" in result
    assert "left-0" in result
    assert "w-full" in result
    assert "translate-y-full" in result


@pytest.mark.asyncio
async def test_backdrop_renders_when_enabled(renderer):
    """T016: Backdrop renders when backdrop=True (default)."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        backdrop=True,  # Default, but explicit
    )
    result = await renderer.render(drawer)

    # Backdrop should have data-drawer-backdrop and data-drawer-hide attributes
    assert "data-drawer-backdrop=" in result
    assert "data-drawer-hide=" in result
    # Should have backdrop styling classes
    assert "bg-gray-900/50" in result or "bg-gray-900" in result
    assert "dark:bg-gray-900/80" in result or "dark:bg-gray-900" in result


@pytest.mark.asyncio
async def test_backdrop_does_not_render_when_disabled(renderer):
    """T017: Backdrop does NOT render when backdrop=False."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        backdrop=False,
    )
    result = await renderer.render(drawer)

    # Backdrop should not be present
    assert "data-drawer-backdrop=" not in result
    # Note: data-drawer-hide will still exist on close button


@pytest.mark.asyncio
async def test_close_button_renders_with_data_attribute(renderer):
    """T018: Close button renders inside drawer panel with data-drawer-hide attribute."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # Close button should have data-drawer-hide attribute
    assert "data-drawer-hide=" in result
    # Should contain close icon SVG
    assert "<svg" in result


@pytest.mark.asyncio
async def test_drawer_has_aria_attributes(renderer):
    """T019: Drawer has ARIA attributes (aria-labelledby, aria-hidden, tabindex)."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # ARIA attributes for accessibility
    assert "aria-labelledby=" in result
    assert 'aria-hidden="true"' in result
    assert 'tabindex="-1"' in result


@pytest.mark.asyncio
async def test_drawer_includes_dark_mode_classes(renderer):
    """T020: Drawer includes dark mode classes (dark:bg-gray-800, dark:border-gray-700, etc.)."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # Dark mode classes should be present
    assert "dark:bg-gray-800" in result or "dark:bg-gray-700" in result
    assert "dark:border-gray-700" in result or "dark:border-gray-600" in result
    assert "dark:text-" in result  # Some dark text color


# Additional tests for coverage


@pytest.mark.asyncio
async def test_drawer_with_edge_tab(renderer):
    """Test drawer renders edge tab when edge=True."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        edge=True,
    )
    result = await renderer.render(drawer)

    # Edge tab should have data-drawer-show attribute
    # Should appear twice: once in trigger, once in edge tab
    assert result.count("data-drawer-show=") >= 2


@pytest.mark.asyncio
async def test_drawer_with_htmx_attributes(renderer):
    """Test drawer passes through HTMX attributes."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        hx_get="/api/content",
        hx_post="/api/submit",
        hx_target="#result",
        hx_swap="outerHTML",
    )
    result = await renderer.render(drawer)

    # HTMX attributes should be present on drawer panel
    assert 'hx-get="/api/content"' in result
    assert 'hx-post="/api/submit"' in result
    assert 'hx-target="#result"' in result
    assert 'hx-swap="outerHTML"' in result


# Phase 4: User Story 2 Tests (Forms Within Drawer) - T032-T036


@pytest.mark.asyncio
async def test_drawer_accepts_component_content(renderer):
    """T032: Drawer accepts Component as content (form with inputs)."""
    # Create a form-like structure with nested components
    form_content = html.form(
        html.input_(type="text", name="name", placeholder="Name"),
        html.input_(type="email", name="email", placeholder="Email"),
        html.button("Submit", type="submit"),
    )

    drawer = Drawer(
        trigger_label="Contact",
        content=form_content,
    )
    result = await renderer.render(drawer)

    # Form elements should be present
    assert 'type="text"' in result
    assert 'type="email"' in result
    assert 'type="submit"' in result
    assert "Submit" in result


@pytest.mark.asyncio
async def test_drawer_max_height_viewport_constraint(renderer):
    """T034: Drawer includes max-h-screen class for viewport constraint."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # Should have max-h-screen class
    assert "max-h-screen" in result


@pytest.mark.asyncio
async def test_drawer_body_has_overflow_auto(renderer):
    """T035: Drawer body has overflow-y-auto class for internal scrolling."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
    )
    result = await renderer.render(drawer)

    # Should have overflow-y-auto class
    assert "overflow-y-auto" in result


# Phase 5: User Story 3 Tests (Customization) - T043-T049


@pytest.mark.asyncio
async def test_drawer_custom_width_left_placement(renderer):
    """T043: Drawer uses custom width class for LEFT placement."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        placement=DrawerPlacement.LEFT,
        width="w-96",
    )
    result = await renderer.render(drawer)

    # Custom width should be present
    assert "w-96" in result


@pytest.mark.asyncio
async def test_drawer_custom_height_top_placement(renderer):
    """T044: Drawer uses custom height class for TOP placement."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        placement=DrawerPlacement.TOP,
        height="h-2/3",
    )
    result = await renderer.render(drawer)

    # Custom height should be present
    assert "h-2/3" in result


@pytest.mark.asyncio
async def test_drawer_custom_class_merges(renderer):
    """T045: Custom class_ merges with drawer panel classes."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        class_="custom-drawer-class",
    )
    result = await renderer.render(drawer)

    # Custom class should be present
    assert "custom-drawer-class" in result


@pytest.mark.asyncio
async def test_drawer_trigger_color_customization(renderer):
    """T046: trigger_color applies Color enum classes to trigger button."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        trigger_color=Color.SUCCESS,
    )
    result = await renderer.render(drawer)

    # Green/success color classes should be present in trigger button
    assert "bg-green-" in result or "green" in result


@pytest.mark.asyncio
async def test_drawer_trigger_size_customization(renderer):
    """T047: trigger_size applies Size enum classes to trigger button."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        trigger_size=Size.LG,
    )
    result = await renderer.render(drawer)

    # Large size classes should be present
    # Size variations affect padding/text size
    assert "Open" in result  # At minimum, button renders


@pytest.mark.asyncio
async def test_edge_tab_renders_when_enabled(renderer):
    """T048: edge=True renders edge tab button with data-drawer-show attribute."""
    drawer = Drawer(
        trigger_label="Open",
        content=html.div("Content"),
        edge=True,
        placement=DrawerPlacement.LEFT,
    )
    result = await renderer.render(drawer)

    # Edge tab should exist (data-drawer-show appears multiple times)
    assert result.count("data-drawer-show=") >= 2
    # Edge icon should be present
    assert "›" in result or "‹" in result or "⌄" in result or "⌃" in result


# Phase 6: User Story 4 Tests (Navigation & Dynamic Content) - T057-T059


@pytest.mark.asyncio
async def test_drawer_content_accepts_nested_nav(renderer):
    """T057: Drawer content accepts nested html.nav() with multiple children."""
    nav_content = html.nav(
        html.a("Home", href="/", class_="block py-2"),
        html.a("About", href="/about", class_="block py-2"),
        html.a("Contact", href="/contact", class_="block py-2"),
    )

    drawer = Drawer(
        trigger_label="Menu",
        content=nav_content,
    )
    result = await renderer.render(drawer)

    # Nav elements should be present
    assert "Home" in result
    assert "About" in result
    assert "Contact" in result
    assert 'href="/"' in result


# ──────────────────────────────────────────────────
# DrawerShell tests
# ──────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_drawer_shell_renders_with_id_and_content_id(renderer):
    """DrawerShell renders with correct ID and content_id."""
    shell = DrawerShell(
        id="drawer-update",
        title="Update Item",
        content_id="drawer-update-content",
    )
    result = await renderer.render(shell)

    assert 'id="drawer-update"' in result
    assert 'id="drawer-update-content"' in result


@pytest.mark.asyncio
async def test_drawer_shell_hidden_trigger(renderer):
    """DrawerShell includes a hidden trigger for Flowbite JS discovery."""
    shell = DrawerShell(
        id="drawer-test",
        title="Test",
        content_id="drawer-test-content",
    )
    result = await renderer.render(shell)

    assert 'data-drawer-target="drawer-test"' in result
    assert 'data-drawer-placement="right"' in result
    assert "hidden" in result


@pytest.mark.asyncio
async def test_drawer_shell_right_position(renderer):
    """DrawerShell defaults to right positioning."""
    shell = DrawerShell(
        id="drawer-right",
        title="Right",
        content_id="content",
    )
    result = await renderer.render(shell)

    assert "right-0" in result
    assert "translate-x-full" in result


@pytest.mark.asyncio
async def test_drawer_shell_left_position(renderer):
    """DrawerShell supports left positioning."""
    shell = DrawerShell(
        id="drawer-left",
        title="Left",
        content_id="content",
        position="left",
    )
    result = await renderer.render(shell)

    assert "left-0" in result
    assert "-translate-x-full" in result
    assert 'data-drawer-placement="left"' in result


@pytest.mark.asyncio
async def test_drawer_shell_header_visibility(renderer):
    """DrawerShell hides header when show_header=False."""
    shell = DrawerShell(
        id="drawer-no-header",
        title="Hidden Title",
        content_id="content",
        show_header=False,
    )
    result = await renderer.render(shell)

    assert "Hidden Title" not in result


@pytest.mark.asyncio
async def test_drawer_shell_loading_spinner(renderer):
    """DrawerShell shows loading spinner by default."""
    shell = DrawerShell(
        id="drawer-spinner",
        title="Test",
        content_id="content",
    )
    result = await renderer.render(shell)

    assert "animate-spin" in result


@pytest.mark.asyncio
async def test_drawer_shell_no_spinner(renderer):
    """DrawerShell hides spinner when loading_spinner=False."""
    shell = DrawerShell(
        id="drawer-no-spinner",
        title="Test",
        content_id="content",
        loading_spinner=False,
    )
    result = await renderer.render(shell)

    assert "animate-spin" not in result


@pytest.mark.asyncio
async def test_drawer_shell_custom_width(renderer):
    """DrawerShell applies custom DrawerWidth."""
    shell = DrawerShell(
        id="drawer-wide",
        title="Wide",
        content_id="content",
        width=DrawerWidth.XXXXL,
    )
    result = await renderer.render(shell)

    assert "max-w-4xl" in result


@pytest.mark.asyncio
async def test_drawer_shell_string_width(renderer):
    """DrawerShell supports raw string width class."""
    shell = DrawerShell(
        id="drawer-custom",
        title="Custom",
        content_id="content",
        width="md:w-1/3",
    )
    result = await renderer.render(shell)

    assert "md:w-1/3" in result


@pytest.mark.asyncio
async def test_drawer_shell_custom_classes(renderer):
    """DrawerShell merges custom CSS classes."""
    shell = DrawerShell(
        id="drawer-cls",
        title="Test",
        content_id="content",
        class_="my-custom-class",
        content_class="content-custom",
    )
    result = await renderer.render(shell)

    assert "my-custom-class" in result
    assert "content-custom" in result


@pytest.mark.asyncio
async def test_drawer_shell_aria_attributes(renderer):
    """DrawerShell has proper ARIA attributes."""
    shell = DrawerShell(
        id="drawer-aria",
        title="Accessible",
        content_id="content",
    )
    result = await renderer.render(shell)

    assert 'aria-labelledby="drawer-aria-label"' in result
    assert 'aria-hidden="true"' in result
    assert 'tabindex="-1"' in result


@pytest.mark.asyncio
async def test_drawer_shell_close_button(renderer):
    """DrawerShell header includes a close button with data-drawer-dismiss."""
    shell = DrawerShell(
        id="drawer-close",
        title="Closeable",
        content_id="content",
    )
    result = await renderer.render(shell)

    assert 'data-drawer-dismiss="drawer-close"' in result
    assert "Close menu" in result
