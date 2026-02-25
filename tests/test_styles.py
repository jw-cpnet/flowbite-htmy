"""Tests for styles module."""

from flowbite_htmy.styles import (
    HELPER_TEXT_CLASSES,
    INPUT_CLASSES,
    LABEL_CLASSES,
    SELECT_CLASSES,
)


def test_input_classes_contains_expected_styles():
    """Test INPUT_CLASSES contains standard Flowbite input styles."""
    assert "bg-gray-50" in INPUT_CLASSES
    assert "border-gray-300" in INPUT_CLASSES
    assert "rounded-lg" in INPUT_CLASSES
    assert "dark:bg-gray-700" in INPUT_CLASSES


def test_label_classes_contains_expected_styles():
    """Test LABEL_CLASSES contains standard label styles."""
    assert "text-sm" in LABEL_CLASSES
    assert "font-medium" in LABEL_CLASSES
    assert "dark:text-white" in LABEL_CLASSES


def test_select_classes_matches_input():
    """Test SELECT_CLASSES defaults to INPUT_CLASSES."""
    assert SELECT_CLASSES == INPUT_CLASSES


def test_helper_text_classes_contains_expected_styles():
    """Test HELPER_TEXT_CLASSES contains expected styles."""
    assert "text-sm" in HELPER_TEXT_CLASSES
    assert "text-gray-500" in HELPER_TEXT_CLASSES
    assert "dark:text-gray-400" in HELPER_TEXT_CLASSES
