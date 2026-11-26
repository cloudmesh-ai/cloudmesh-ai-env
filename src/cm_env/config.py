"""Configuration application script for the ``cm-env`` package.

The script provides a ``main`` function that serves as the entry point for the
``cm-env`` console script defined in ``pyproject.toml``. It accepts a mandatory
positional argument ``path`` which specifies the target directory where the
configuration should be applied. If ``path`` resolves to the current working
directory (e.g., ``.``), the configuration will be applied to the cwd.

For demonstration purposes, the configuration action simply creates (or
overwrites) a ``config.txt`` file in the target directory containing a short
message. In a real-world scenario this could involve copying template files,
setting environment variables, or other project‑specific setup steps.
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from typing import NoReturn


def _error(message: str) -> NoReturn:
    """Print an error message to ``stderr`` and exit with a non‑zero status.

    Args:
        message: The error message to display.
    """
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def apply_config(target: pathlib.Path, python_version: str) -> None:
    """Apply the configuration to ``target``.

    The placeholder implementation creates (or overwrites) a ``config.txt``
    file inside the target directory. It records both the target path and the
    Python version selected via the ``--python`` option.

    Args:
        target: The directory to which the configuration should be applied.
        python_version: The Python interpreter version string (e.g. ``python3.15.2``).
    """
    # Ensure the target directory exists (caller validates) and is a directory.
    config_path = target / "config.txt"
    try:
        config_path.write_text(
            f"Configuration applied to {target}\nPython version: {python_version}\n"
        )
    except OSError as exc:
        _error(f"Failed to write configuration file: {exc}")
    else:
        print(f"Applied configuration to {target} (Python: {python_version})")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command‑line arguments.

    The script expects a mandatory positional argument ``path`` that specifies the
    target directory, and an optional ``--python`` flag to indicate the desired
    Python interpreter version. The ``--python`` option defaults to
    ``python3.15.2``.
    ``argv`` is injected to ease testing.
    """
    parser = argparse.ArgumentParser(
        prog="cm-env",
        description="Apply configuration to a specified directory.",
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to the target directory. Use '.' for the current working directory.",
    )
    parser.add_argument(
        "--python",
        dest="python_version",
        type=str,
        default="python3.15.2",
        help="Python interpreter version to target (default: python3.15.2).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Entry point for the console script.

    Args:
        argv: Optional list of arguments for testing purposes. If ``None`` the
            arguments from ``sys.argv`` (excluding the program name) are used.
    """
    args = parse_args(argv)
    # Resolve the provided path relative to the current working directory.
    target_path = pathlib.Path(args.path).expanduser().resolve()

    # Validate existence and that it is a directory.
    if not target_path.exists():
        _error(f"Target path '{target_path}' does not exist.")
    if not target_path.is_dir():
        _error(f"Target path '{target_path}' is not a directory.")

    apply_config(target_path, args.python_version)


if __name__ == "__main__":
    # When executed as a script (e.g., ``python -m cm_env.config``) we forward
    # the real command‑line arguments.
    main()
