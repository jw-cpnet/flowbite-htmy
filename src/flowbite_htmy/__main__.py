"""CLI interface for flowbite-htmy.

This module provides command-line utilities for working with flowbite-htmy.

Usage:
    python -m flowbite_htmy path      # Print the installation path
    python -m flowbite_htmy version   # Print version information
    python -m flowbite_htmy help      # Show help information
"""

import argparse
import sys
from pathlib import Path

from flowbite_htmy import FLOWBITE_VERSION, HTMX_VERSION, TAILWIND_VERSION, __version__


def get_package_path() -> Path:
    """Get the absolute path to the flowbite_htmy package.

    Returns:
        Path object pointing to the package directory.
    """
    return Path(__file__).parent.resolve()


def cmd_path() -> None:
    """Print the installation path of flowbite_htmy.

    This is useful for configuring Tailwind CSS to scan the library's
    Python files for class names.
    """
    path = get_package_path()
    print(path)


def cmd_version() -> None:
    """Print version information."""
    print(f"flowbite-htmy version: {__version__}")
    print(f"Flowbite CSS version: {FLOWBITE_VERSION}")
    print(f"HTMX version: {HTMX_VERSION}")
    print(f"Tailwind CSS version: {TAILWIND_VERSION}")


def cmd_tailwind_config() -> None:
    """Print example Tailwind configuration snippet."""
    path = get_package_path()
    print("// Add this to your tailwind.config.js content array:")
    print(f'"{path}/**/*.py",')
    print()
    print("// Full example:")
    print("module.exports = {")
    print("  content: [")
    print('    "./templates/**/*.html",')
    print('    "./templates/**/*.jinja",')
    print('    "./templates/**/*.jinja2",')
    print(f'    "{path}/**/*.py",  // flowbite-htmy components')
    print('    "./node_modules/flowbite/**/*.js",')
    print("  ],")
    print("  plugins: [")
    print("    require('flowbite/plugin'),")
    print("  ],")
    print("}")


def cmd_help() -> None:
    """Print help information."""
    print("flowbite-htmy CLI")
    print()
    print("Commands:")
    print("  path              Print the installation path")
    print("  version           Print version information")
    print("  tailwind-config   Print example Tailwind configuration")
    print("  help              Show this help message")
    print()
    print("Examples:")
    print("  python -m flowbite_htmy path")
    print("  python -m flowbite_htmy version")
    print("  python -m flowbite_htmy tailwind-config")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="flowbite_htmy",
        description="CLI utilities for flowbite-htmy",
        add_help=False,  # We'll handle help ourselves
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="help",
        choices=["path", "version", "tailwind-config", "help"],
        help="Command to run",
    )

    args = parser.parse_args()

    commands = {
        "path": cmd_path,
        "version": cmd_version,
        "tailwind-config": cmd_tailwind_config,
        "help": cmd_help,
    }

    try:
        commands[args.command]()
    except KeyError:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        cmd_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
