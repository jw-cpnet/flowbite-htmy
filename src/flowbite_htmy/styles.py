"""Standard Flowbite CSS class sets for consistent styling.

These constants can be reused when building custom components that need
Flowbite-consistent styling without duplicating Tailwind class strings.

Example:
    ```python
    from flowbite_htmy.styles import INPUT_CLASSES, LABEL_CLASSES
    html.label("Name", class_=LABEL_CLASSES)
    html.input_(class_=INPUT_CLASSES)
    ```
"""

# Standard form input classes (used by Input, Select, Textarea)
INPUT_CLASSES = (
    "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg "
    "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
    "dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 "
    "dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
)

# Standard form label classes
LABEL_CLASSES = "block mb-2 text-sm font-medium text-gray-900 dark:text-white"

# Standard select classes (same as input but may diverge in future)
SELECT_CLASSES = INPUT_CLASSES

# Standard helper text classes
HELPER_TEXT_CLASSES = "mt-2 text-sm text-gray-500 dark:text-gray-400"

__all__ = [
    "INPUT_CLASSES",
    "LABEL_CLASSES",
    "SELECT_CLASSES",
    "HELPER_TEXT_CLASSES",
]
