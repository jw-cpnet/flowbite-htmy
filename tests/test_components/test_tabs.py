"""Tests for Tabs component (US1-US5)."""

import pytest
from htmy import html

from flowbite_htmy.components import IconPosition, Tab, Tabs, TabVariant
from flowbite_htmy.icons import Icon
from flowbite_htmy.types import Color


# User Story 1: Basic Tab Navigation (6 tests)
class TestBasicTabNavigation:
    """Tests for US1: Basic tab switching and navigation."""

    @pytest.mark.asyncio
    async def test_tabs_renders_default_first_tab_active(self, renderer):
        """Given tabs with no active tab specified, first tab should be active."""
        tabs = Tabs(
            tabs=[
                Tab(label="Profile", content=html.p("Profile content")),
                Tab(label="Dashboard", content=html.p("Dashboard content")),
            ]
        )
        html_output = await renderer.render(tabs)

        assert "Profile" in html_output
        assert "Dashboard" in html_output
        assert 'aria-selected="true"' in html_output  # First tab is active
        assert html_output.count('aria-selected="true"') == 1  # Only one active

    @pytest.mark.asyncio
    async def test_tabs_renders_custom_active_tab(self, renderer):
        """Given tabs with is_active=True on second tab, it should be active."""
        tabs = Tabs(
            tabs=[
                Tab(label="Profile", content=html.p("Profile content")),
                Tab(label="Dashboard", content=html.p("Dashboard content"), is_active=True),
            ]
        )
        html_output = await renderer.render(tabs)

        # Second tab should be active
        assert 'aria-selected="true"' in html_output
        assert html_output.count('aria-selected="true"') == 1

    @pytest.mark.asyncio
    async def test_tabs_generates_unique_ids(self, renderer):
        """Tabs should generate unique IDs for tablist, tabs, and panels."""
        tabs = Tabs(
            tabs=[
                Tab(label="Tab1", content=html.p("Content1")),
                Tab(label="Tab2", content=html.p("Content2")),
            ]
        )
        html_output = await renderer.render(tabs)

        # Should have IDs like tabs-{id}, tab-tabs-{id}-0, panel-tabs-{id}-0
        assert 'id="tabs-' in html_output  # Tablist ID
        assert 'id="tab-tabs-' in html_output  # Tab button ID
        assert 'id="panel-tabs-' in html_output  # Panel ID

    @pytest.mark.asyncio
    async def test_tabs_includes_aria_attributes(self, renderer):
        """Tabs should include full ARIA attributes for accessibility."""
        tabs = Tabs(tabs=[Tab(label="Tab1", content=html.p("Content1"))])
        html_output = await renderer.render(tabs)

        # Tablist ARIA
        assert 'role="tablist"' in html_output

        # Tab button ARIA
        assert 'role="tab"' in html_output
        assert "aria-selected=" in html_output
        assert "aria-controls=" in html_output

        # Panel ARIA
        assert 'role="tabpanel"' in html_output
        assert "aria-labelledby=" in html_output

    @pytest.mark.asyncio
    async def test_tabs_includes_flowbite_data_attributes(self, renderer):
        """Tabs should include Flowbite JavaScript data attributes."""
        tabs = Tabs(tabs=[Tab(label="Tab1", content=html.p("Content1"))])
        html_output = await renderer.render(tabs)

        # Flowbite data attributes
        assert "data-tabs-toggle=" in html_output
        assert "data-tabs-target=" in html_output

    @pytest.mark.asyncio
    async def test_tabs_hides_inactive_panels(self, renderer):
        """Inactive tab panels should have hidden class."""
        tabs = Tabs(
            tabs=[
                Tab(label="Tab1", content=html.p("Content1"), is_active=True),
                Tab(label="Tab2", content=html.p("Content2")),
            ]
        )
        html_output = await renderer.render(tabs)

        # Should have at least one hidden class for inactive panel
        assert "hidden" in html_output


# User Story 2: Tab Variants (7 tests)
class TestTabVariants:
    """Tests for US2: Visual variants and color customization."""

    @pytest.mark.asyncio
    async def test_tabs_default_variant(self, renderer):
        """DEFAULT variant should include border-b and bg-gray-100 on active tab."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"), is_active=True)],
            variant=TabVariant.DEFAULT,
        )
        html_output = await renderer.render(tabs)

        assert "border-b" in html_output
        assert "border-gray-200" in html_output
        assert "bg-gray-100" in html_output  # Active tab background
        assert "dark:bg-gray-800" in html_output  # Dark mode

    @pytest.mark.asyncio
    async def test_tabs_underline_variant(self, renderer):
        """UNDERLINE variant should have border-b-2 on active tab."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"), is_active=True)],
            variant=TabVariant.UNDERLINE,
        )
        html_output = await renderer.render(tabs)

        assert "border-b-2" in html_output
        assert "border-blue-600" in html_output  # Active tab underline
        assert "dark:border-blue-500" in html_output

    @pytest.mark.asyncio
    async def test_tabs_pills_variant(self, renderer):
        """PILLS variant should have rounded-lg and bg-blue-600 on active tab."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"), is_active=True)],
            variant=TabVariant.PILLS,
        )
        html_output = await renderer.render(tabs)

        assert "rounded-lg" in html_output
        assert "bg-blue-600" in html_output  # Active pill background
        assert "text-white" in html_output

    @pytest.mark.asyncio
    async def test_tabs_full_width_variant(self, renderer):
        """FULL_WIDTH variant should have w-full and shadow-sm."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"))],
            variant=TabVariant.FULL_WIDTH,
        )
        html_output = await renderer.render(tabs)

        assert "w-full" in html_output
        assert "shadow-sm" in html_output

    @pytest.mark.asyncio
    async def test_tabs_color_customization(self, renderer):
        """Active tab should use custom color (GREEN instead of default BLUE)."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"), is_active=True)],
            variant=TabVariant.UNDERLINE,
            color=Color.GREEN,
        )
        html_output = await renderer.render(tabs)

        # Should have green color classes instead of blue
        assert "green-600" in html_output or "green-500" in html_output

    @pytest.mark.asyncio
    async def test_tabs_dark_mode_classes(self, renderer):
        """All variants should include dark mode classes."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", content=html.p("Content"))],
            variant=TabVariant.DEFAULT,
        )
        html_output = await renderer.render(tabs)

        # Dark mode classes should always be present
        assert "dark:" in html_output

    @pytest.mark.asyncio
    async def test_tabs_custom_classes_merged(self, renderer):
        """Custom classes should be merged with component classes."""
        tabs = Tabs(tabs=[Tab(label="Tab1", content=html.p("Content"))], class_="mt-8 custom-class")
        html_output = await renderer.render(tabs)

        assert "mt-8" in html_output
        assert "custom-class" in html_output


# User Story 3: HTMX Integration (3 tests)
class TestHTMXIntegration:
    """Tests for US3: HTMX lazy loading and dynamic content."""

    @pytest.mark.asyncio
    async def test_tabs_htmx_get_attribute(self, renderer):
        """hx-get attribute should appear on panel, not button."""
        tabs = Tabs(tabs=[Tab(label="Data", hx_get="/api/data")])
        html_output = await renderer.render(tabs)

        assert 'hx-get="/api/data"' in html_output
        # Verify hx-get is on panel (appears after button closes)
        button_end = html_output.find("</button>")
        hx_get_pos = html_output.find('hx-get="/api/data"')
        assert hx_get_pos > button_end  # hx-get comes after button

    @pytest.mark.asyncio
    async def test_tabs_htmx_trigger_attribute(self, renderer):
        """hx-trigger attribute should be on panel."""
        tabs = Tabs(tabs=[Tab(label="Data", hx_get="/api/data", hx_trigger="revealed once")])
        html_output = await renderer.render(tabs)

        assert 'hx-trigger="revealed once"' in html_output

    @pytest.mark.asyncio
    async def test_tabs_htmx_multiple_attributes(self, renderer):
        """Multiple HTMX attributes should all be on panel."""
        tabs = Tabs(
            tabs=[
                Tab(
                    label="Data",
                    hx_get="/api/data",
                    hx_trigger="revealed",
                    hx_swap="innerHTML",
                )
            ]
        )
        html_output = await renderer.render(tabs)

        assert 'hx-get="/api/data"' in html_output
        assert 'hx-trigger="revealed"' in html_output
        assert 'hx-swap="innerHTML"' in html_output


# User Story 4: Icons (4 tests)
class TestTabIcons:
    """Tests for US4: Icon support and positioning."""

    @pytest.mark.asyncio
    async def test_tab_with_icon_left(self, renderer):
        """Icon should appear to the left of label with me-2 spacing."""
        tabs = Tabs(tabs=[Tab(label="Profile", content=html.p("Content"), icon=Icon.USER)])
        html_output = await renderer.render(tabs)

        assert "<svg" in html_output  # Icon SVG present
        assert "me-2" in html_output  # Left icon spacing
        # Icon should appear before "Profile" text
        icon_pos = html_output.index("<svg")
        label_pos = html_output.index("Profile")
        assert icon_pos < label_pos

    @pytest.mark.asyncio
    async def test_tab_with_icon_right(self, renderer):
        """Icon should appear to the right of label with ms-2 spacing."""
        tabs = Tabs(
            tabs=[
                Tab(
                    label="Settings",
                    content=html.p("Content"),
                    icon=Icon.CHEVRON_RIGHT,
                    icon_position=IconPosition.RIGHT,
                )
            ]
        )
        html_output = await renderer.render(tabs)

        assert "<svg" in html_output
        assert "ms-2" in html_output  # Right icon spacing
        # Icon should appear after "Settings" text
        label_pos = html_output.index("Settings")
        icon_pos = html_output.index("<svg")
        assert label_pos < icon_pos

    @pytest.mark.asyncio
    async def test_tab_icon_in_disabled_state(self, renderer):
        """Icon should inherit disabled gray color."""
        tabs = Tabs(
            tabs=[Tab(label="Premium", icon=Icon.USER, disabled=True, content=html.p("Content"))]
        )
        html_output = await renderer.render(tabs)

        assert "<svg" in html_output
        assert "text-gray-400" in html_output  # Disabled color

    @pytest.mark.asyncio
    async def test_tab_icons_across_variants(self, renderer):
        """Icons should maintain size and alignment across variants."""
        tabs = Tabs(
            tabs=[Tab(label="Tab1", icon=Icon.USER, content=html.p("Content"))],
            variant=TabVariant.PILLS,
        )
        html_output = await renderer.render(tabs)

        assert "<svg" in html_output
        assert "w-4" in html_output and "h-4" in html_output  # Consistent size


# User Story 5: Disabled Tabs (3 tests)
class TestDisabledTabs:
    """Tests for US5: Disabled tab behavior."""

    @pytest.mark.asyncio
    async def test_disabled_tab_styling(self, renderer):
        """Disabled tab should have cursor-not-allowed and gray color."""
        tabs = Tabs(tabs=[Tab(label="Premium", disabled=True, content=html.p("Content"))])
        html_output = await renderer.render(tabs)

        assert "text-gray-400" in html_output
        assert "cursor-not-allowed" in html_output
        assert "dark:text-gray-500" in html_output

    @pytest.mark.asyncio
    async def test_disabled_tab_cannot_be_active(self, renderer):
        """Disabled tab should not be active even if is_active=True."""
        tabs = Tabs(
            tabs=[
                Tab(label="Tab1", content=html.p("Content1")),
                Tab(label="Disabled", disabled=True, is_active=True, content=html.p("Content2")),
            ]
        )
        html_output = await renderer.render(tabs)

        # First tab should be active instead (disabled tab ignored)
        assert html_output.count('aria-selected="true"') == 1

    @pytest.mark.asyncio
    async def test_disabled_tab_dark_mode(self, renderer):
        """Disabled tabs should have dark mode classes."""
        tabs = Tabs(tabs=[Tab(label="Premium", disabled=True, content=html.p("Content"))])
        html_output = await renderer.render(tabs)

        assert "dark:text-gray-500" in html_output


# Edge Cases (4 tests)
class TestEdgeCases:
    """Tests for edge cases and error handling."""

    @pytest.mark.asyncio
    async def test_single_tab(self, renderer):
        """Single tab should render full tablist UI."""
        tabs = Tabs(tabs=[Tab(label="OnlyTab", content=html.p("Content"))])
        html_output = await renderer.render(tabs)

        assert 'role="tablist"' in html_output
        assert 'role="tab"' in html_output
        assert "OnlyTab" in html_output

    @pytest.mark.asyncio
    async def test_empty_content(self, renderer):
        """Tab with no content should render empty panel."""
        tabs = Tabs(tabs=[Tab(label="EmptyTab")])  # content=None
        html_output = await renderer.render(tabs)

        assert "EmptyTab" in html_output
        assert 'role="tabpanel"' in html_output

    @pytest.mark.asyncio
    async def test_multiple_active_tabs_first_wins(self, renderer):
        """If multiple tabs have is_active=True, first wins."""
        tabs = Tabs(
            tabs=[
                Tab(label="Tab1", content=html.p("Content1"), is_active=True),
                Tab(label="Tab2", content=html.p("Content2"), is_active=True),
            ]
        )
        html_output = await renderer.render(tabs)

        # Only one active tab
        assert html_output.count('aria-selected="true"') == 1

    @pytest.mark.asyncio
    async def test_custom_tabs_id_override(self, renderer):
        """Custom tabs_id should override auto-generated ID."""
        tabs = Tabs(tabs=[Tab(label="Tab1", content=html.p("Content"))], tabs_id="custom-tabs")
        html_output = await renderer.render(tabs)

        assert 'id="custom-tabs"' in html_output
        assert 'id="tab-custom-tabs-0"' in html_output
        assert 'id="panel-custom-tabs-0"' in html_output
