"""Utility for comparing component styles against official Flowbite HTML.

This module helps verify that our components match the official Flowbite
styling by comparing rendered class attributes.
"""

import pytest
from htmy import Renderer

from flowbite_htmy.components import Button
from flowbite_htmy.types import Color


def normalize_classes(class_string: str) -> set[str]:
    """Normalize a class string into a sorted set of classes.

    Args:
        class_string: Space-separated CSS classes.

    Returns:
        Set of individual class names.
    """
    return set(class_string.strip().split())


def compare_classes(
    actual: str, expected: str
) -> tuple[set[str], set[str], set[str]]:
    """Compare actual vs expected classes.

    Args:
        actual: Actual class string from our component.
        expected: Expected class string from Flowbite.

    Returns:
        Tuple of (matching, missing, extra) class sets.
    """
    actual_set = normalize_classes(actual)
    expected_set = normalize_classes(expected)

    matching = actual_set & expected_set
    missing = expected_set - actual_set
    extra = actual_set - expected_set

    return matching, missing, extra


@pytest.mark.asyncio
async def test_button_primary_matches_flowbite(renderer: Renderer) -> None:
    """Compare Primary button classes against official Flowbite."""
    # Our component
    button = Button(label="Default", color=Color.PRIMARY)
    html = await renderer.render(button)

    # Extract classes from rendered HTML
    import re

    class_match = re.search(r'class="([^"]+)"', html)
    assert class_match, "No class attribute found"
    actual_classes = class_match.group(1)

    # Official Flowbite HTML for default (primary) button
    expected_classes = (
        "text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 "
        "focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 "
        "me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 "
        "focus:outline-none dark:focus:ring-blue-800"
    )

    matching, missing, extra = compare_classes(actual_classes, expected_classes)

    # Report results
    if missing or extra:
        report = "\n\n=== Button PRIMARY Style Comparison ===\n"
        report += f"Matching classes ({len(matching)}): {sorted(matching)}\n"
        if missing:
            report += f"❌ Missing classes ({len(missing)}): {sorted(missing)}\n"
        if extra:
            report += f"⚠️  Extra classes ({len(extra)}): {sorted(extra)}\n"
        print(report)

    # Assertion: We should have all expected classes
    # Allow extra classes (like custom ones) but not missing ones
    assert not missing, f"Missing Flowbite classes: {sorted(missing)}"


@pytest.mark.asyncio
async def test_button_secondary_matches_flowbite(renderer: Renderer) -> None:
    """Compare Secondary button classes against official Flowbite."""
    button = Button(label="Alternative", color=Color.SECONDARY)
    html = await renderer.render(button)

    import re

    class_match = re.search(r'class="([^"]+)"', html)
    assert class_match
    actual_classes = class_match.group(1)

    # Official Flowbite Alternative button
    expected_classes = (
        "py-2.5 px-5 me-2 mb-2 text-sm font-medium text-gray-900 "
        "focus:outline-none bg-white rounded-lg border border-gray-200 "
        "hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 "
        "focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 "
        "dark:text-gray-400 dark:border-gray-600 dark:hover:text-white "
        "dark:hover:bg-gray-700"
    )

    matching, missing, extra = compare_classes(actual_classes, expected_classes)

    if missing or extra:
        report = "\n\n=== Button SECONDARY Style Comparison ===\n"
        report += f"Matching classes ({len(matching)}): {sorted(matching)}\n"
        if missing:
            report += f"❌ Missing classes ({len(missing)}): {sorted(missing)}\n"
        if extra:
            report += f"⚠️  Extra classes ({len(extra)}): {sorted(extra)}\n"
        print(report)

    assert not missing, f"Missing Flowbite classes: {sorted(missing)}"


@pytest.mark.asyncio
async def test_button_success_matches_flowbite(renderer: Renderer) -> None:
    """Compare Green/Success button classes against official Flowbite."""
    button = Button(label="Green", color=Color.SUCCESS)
    html = await renderer.render(button)

    import re

    class_match = re.search(r'class="([^"]+)"', html)
    assert class_match
    actual_classes = class_match.group(1)

    # Official Flowbite Green button
    expected_classes = (
        "focus:outline-none text-white bg-green-700 hover:bg-green-800 "
        "focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm "
        "px-5 py-2.5 me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 "
        "dark:focus:ring-green-800"
    )

    matching, missing, extra = compare_classes(actual_classes, expected_classes)

    if missing or extra:
        report = "\n\n=== Button SUCCESS/GREEN Style Comparison ===\n"
        report += f"Matching classes ({len(matching)}): {sorted(matching)}\n"
        if missing:
            report += f"❌ Missing classes ({len(missing)}): {sorted(missing)}\n"
        if extra:
            report += f"⚠️  Extra classes ({len(extra)}): {sorted(extra)}\n"
        print(report)

    assert not missing, f"Missing Flowbite classes: {sorted(missing)}"


@pytest.mark.asyncio
async def test_button_danger_matches_flowbite(renderer: Renderer) -> None:
    """Compare Red/Danger button classes against official Flowbite."""
    button = Button(label="Red", color=Color.DANGER)
    html = await renderer.render(button)

    import re

    class_match = re.search(r'class="([^"]+)"', html)
    assert class_match
    actual_classes = class_match.group(1)

    # Official Flowbite Red button
    expected_classes = (
        "focus:outline-none text-white bg-red-700 hover:bg-red-800 "
        "focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm "
        "px-5 py-2.5 me-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 "
        "dark:focus:ring-red-900"
    )

    matching, missing, extra = compare_classes(actual_classes, expected_classes)

    if missing or extra:
        report = "\n\n=== Button DANGER/RED Style Comparison ===\n"
        report += f"Matching classes ({len(matching)}): {sorted(matching)}\n"
        if missing:
            report += f"❌ Missing classes ({len(missing)}): {sorted(missing)}\n"
        if extra:
            report += f"⚠️  Extra classes ({len(extra)}): {sorted(extra)}\n"
        print(report)

    assert not missing, f"Missing Flowbite classes: {sorted(missing)}"
