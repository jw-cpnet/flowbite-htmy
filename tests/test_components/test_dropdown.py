"""Tests for Dropdown component."""
import pytest
from flowbite_htmy.components import (
    Dropdown,
    DropdownDivider,
    DropdownHeader,
    DropdownItem,
)
from flowbite_htmy.types import (
    DropdownPlacement,
    DropdownTriggerType,
    DropdownTriggerMode,
)


# T002: DropdownPlacement enum tests
def test_dropdown_placement_enum():
    """Test DropdownPlacement enum values."""
    assert DropdownPlacement.TOP == "top"
    assert DropdownPlacement.BOTTOM == "bottom"
    assert DropdownPlacement.LEFT == "left"
    assert DropdownPlacement.RIGHT == "right"


# T003: DropdownTriggerType enum tests
def test_dropdown_trigger_type_enum():
    """Test DropdownTriggerType enum values."""
    assert DropdownTriggerType.BUTTON == "button"
    assert DropdownTriggerType.AVATAR == "avatar"
    assert DropdownTriggerType.TEXT == "text"


# T004: DropdownTriggerMode enum tests
def test_dropdown_trigger_mode_enum():
    """Test DropdownTriggerMode enum values."""
    assert DropdownTriggerMode.CLICK == "click"
    assert DropdownTriggerMode.HOVER == "hover"


# ========== User Story 1 Tests ==========


# T010: DropdownDivider rendering
@pytest.mark.asyncio
async def test_dropdown_divider_renders(renderer):
    """Test DropdownDivider renders as hr element."""
    divider = DropdownDivider()
    html = await renderer.render(divider)

    assert "<hr" in html
    assert "border-gray-100" in html
    assert "dark:border-gray-600" in html


# T011: DropdownDivider with custom class
@pytest.mark.asyncio
async def test_dropdown_divider_custom_class(renderer):
    """Test DropdownDivider with custom class."""
    divider = DropdownDivider(class_="my-4")
    html = await renderer.render(divider)

    assert "my-4" in html


# T012: DropdownHeader rendering
@pytest.mark.asyncio
async def test_dropdown_header_renders(renderer):
    """Test DropdownHeader renders with label."""
    header = DropdownHeader(label="Account Settings")
    html = await renderer.render(header)

    assert "Account Settings" in html
    assert 'role="presentation"' in html
    assert "text-gray-900" in html
    assert "dark:text-white" in html


# T013: DropdownHeader with custom class
@pytest.mark.asyncio
async def test_dropdown_header_custom_class(renderer):
    """Test DropdownHeader with custom class."""
    header = DropdownHeader(label="Settings", class_="font-bold")
    html = await renderer.render(header)

    assert "font-bold" in html


# T014: DropdownItem simple rendering
@pytest.mark.asyncio
async def test_dropdown_item_simple(renderer):
    """Test simple DropdownItem renders."""
    item = DropdownItem(label="Profile", href="/profile")
    html = await renderer.render(item)

    assert "Profile" in html
    assert 'href="/profile"' in html
    assert 'role="menuitem"' in html
    assert "hover:bg-gray-100" in html
    assert "dark:hover:bg-gray-600" in html


# T015: Dropdown basic rendering with button trigger
@pytest.mark.asyncio
async def test_dropdown_basic_renders(renderer):
    """Test basic dropdown renders with button trigger."""
    dropdown = Dropdown(
        trigger_label="Actions",
        items=[
            DropdownItem(label="Edit", href="/edit"),
            DropdownItem(label="Delete", href="/delete"),
        ],
    )
    html = await renderer.render(dropdown)

    # Trigger button
    assert "Actions" in html
    assert "data-dropdown-toggle" in html
    assert "Edit" in html
    assert "Delete" in html


# T016: Dropdown ARIA attributes
@pytest.mark.asyncio
async def test_dropdown_aria_attributes(renderer):
    """Test dropdown ARIA attributes."""
    dropdown = Dropdown(
        trigger_label="Menu",
        dropdown_id="test-dropdown",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert 'id="trigger-test-dropdown"' in html
    assert 'aria-controls="test-dropdown"' in html
    assert 'aria-expanded="false"' in html
    assert 'aria-haspopup="true"' in html
    assert 'id="test-dropdown"' in html
    assert 'role="menu"' in html
    assert 'aria-labelledby="trigger-test-dropdown"' in html


# T017: Dropdown Flowbite data attributes
@pytest.mark.asyncio
async def test_dropdown_flowbite_data_attributes(renderer):
    """Test dropdown Flowbite data attributes."""
    dropdown = Dropdown(
        trigger_label="Menu",
        dropdown_id="test-menu",
        placement=DropdownPlacement.TOP,
        trigger_mode=DropdownTriggerMode.HOVER,
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert 'data-dropdown-toggle="test-menu"' in html
    assert 'data-dropdown-placement="top"' in html
    assert 'data-dropdown-trigger="hover"' in html


# ========== User Story 2 Tests ==========


# T033: Dropdown with custom color and size
@pytest.mark.asyncio
async def test_dropdown_color_and_size(renderer):
    """Test dropdown with custom color and size."""
    from flowbite_htmy.types import Color, Size

    dropdown = Dropdown(
        trigger_label="Options",
        color=Color.GREEN,
        size=Size.LG,
        items=[DropdownItem(label="Option 1")],
    )
    html = await renderer.render(dropdown)

    assert "bg-green-700" in html
    assert "hover:bg-green-800" in html
    assert "px-5 py-3" in html  # LG size


# T034: DropdownItem with icon
@pytest.mark.asyncio
async def test_dropdown_item_with_icon(renderer):
    """Test DropdownItem with icon."""
    from flowbite_htmy.icons import Icon

    item = DropdownItem(label="Dashboard", icon=Icon.USER, href="/dashboard")
    html = await renderer.render(item)

    assert "Dashboard" in html
    assert "<svg" in html


# T035: DropdownItem disabled state
@pytest.mark.asyncio
async def test_dropdown_item_disabled(renderer):
    """Test disabled DropdownItem."""
    item = DropdownItem(label="Coming Soon", disabled=True)
    html = await renderer.render(item)

    assert "Coming Soon" in html
    assert "opacity-50" in html or "cursor-not-allowed" in html


# T036: Dropdown dark mode classes
@pytest.mark.asyncio
async def test_dropdown_dark_mode_classes(renderer, dark_context):
    """Test dropdown includes dark mode classes."""
    dropdown = Dropdown(
        trigger_label="Menu",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown, dark_context)

    # Dark mode classes should be present
    assert "dark:bg-blue-600" in html or "dark:hover:bg-blue-700" in html
    assert "dark:bg-gray-700" in html  # Menu container
    assert "dark:text-gray-200" in html  # Menu text


# T037: Dropdown with custom classes
@pytest.mark.asyncio
async def test_dropdown_custom_classes(renderer):
    """Test dropdown with custom trigger_class and menu_class."""
    dropdown = Dropdown(
        trigger_label="Custom",
        trigger_class="my-trigger-class",
        menu_class="my-menu-class",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert "my-trigger-class" in html
    assert "my-menu-class" in html


# ========== User Story 3 Tests ==========


# T048: Dropdown with placement options
@pytest.mark.asyncio
async def test_dropdown_placement_options(renderer):
    """Test dropdown with different placements."""
    # Already tested in test_dropdown_flowbite_data_attributes
    # This test validates all 4 placements work
    for placement in [DropdownPlacement.TOP, DropdownPlacement.BOTTOM,
                       DropdownPlacement.LEFT, DropdownPlacement.RIGHT]:
        dropdown = Dropdown(
            trigger_label="Menu",
            placement=placement,
            items=[DropdownItem(label="Item")],
        )
        html = await renderer.render(dropdown)
        assert f'data-dropdown-placement="{placement.value}"' in html


# T049: Dropdown with avatar trigger
@pytest.mark.asyncio
async def test_dropdown_avatar_trigger(renderer):
    """Test dropdown with avatar trigger."""
    dropdown = Dropdown(
        trigger_label="User Menu",
        trigger_type=DropdownTriggerType.AVATAR,
        avatar_src="/images/user.jpg",
        avatar_alt="User profile",
        items=[DropdownItem(label="Profile")],
    )
    html = await renderer.render(dropdown)

    assert 'src="/images/user.jpg"' in html
    assert 'alt="User profile"' in html
    assert "data-dropdown-toggle" in html


# T050: Dropdown with text trigger
@pytest.mark.asyncio
async def test_dropdown_text_trigger(renderer):
    """Test dropdown with text trigger."""
    dropdown = Dropdown(
        trigger_label="Click me",
        trigger_type=DropdownTriggerType.TEXT,
        items=[DropdownItem(label="Action")],
    )
    html = await renderer.render(dropdown)

    assert "Click me" in html
    assert "data-dropdown-toggle" in html
    # Text trigger should not have button background colors
    assert "bg-blue-700" not in html


# T051: Dropdown with hover trigger mode
@pytest.mark.asyncio
async def test_dropdown_hover_mode(renderer):
    """Test dropdown with hover trigger mode."""
    # Already tested in test_dropdown_flowbite_data_attributes
    dropdown = Dropdown(
        trigger_label="Hover",
        trigger_mode=DropdownTriggerMode.HOVER,
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert 'data-dropdown-trigger="hover"' in html


# T052: DropdownItem with HTMX attributes
@pytest.mark.asyncio
async def test_dropdown_item_htmx_attributes(renderer):
    """Test DropdownItem with HTMX attributes."""
    item = DropdownItem(
        label="Load More",
        hx_get="/api/items",
        hx_target="#list",
        hx_swap="beforeend",
    )
    html = await renderer.render(item)

    assert "Load More" in html
    assert 'hx-get="/api/items"' in html
    assert 'hx-target="#list"' in html
    assert 'hx-swap="beforeend"' in html


# T053: Nested dropdown
@pytest.mark.asyncio
async def test_dropdown_nested(renderer):
    """Test nested dropdown (DropdownItem with dropdown prop)."""
    nested_dropdown = Dropdown(
        trigger_label="Settings submenu",
        items=[
            DropdownItem(label="Account", href="/settings/account"),
            DropdownItem(label="Privacy", href="/settings/privacy"),
        ]
    )

    item = DropdownItem(
        label="Settings",
        dropdown=nested_dropdown,
    )
    html = await renderer.render(item)

    assert "Settings" in html
    assert "Account" in html
    assert "Privacy" in html


# ========== Edge Case Tests ==========


# T085: Edge case tests
@pytest.mark.asyncio
async def test_dropdown_disabled_state(renderer):
    """Test dropdown with disabled state."""
    dropdown = Dropdown(
        trigger_label="Disabled",
        disabled=True,
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert "Disabled" in html
    assert "disabled" in html or 'disabled=""' in html


@pytest.mark.asyncio
async def test_dropdown_custom_id(renderer):
    """Test dropdown with custom dropdown_id."""
    dropdown = Dropdown(
        trigger_label="Custom ID",
        dropdown_id="my-custom-dropdown",
        items=[DropdownItem(label="Item")],
    )
    html = await renderer.render(dropdown)

    assert 'id="trigger-my-custom-dropdown"' in html
    assert 'id="my-custom-dropdown"' in html
    assert 'data-dropdown-toggle="my-custom-dropdown"' in html
