from pathlib import Path
from blueprinter import inline_snippet


def quick_template():
    """Provides a template for using this library."""

    example_path = Path(__file__).parent / 'examples/example.py'
    error_message = "# uh oh! This example failed to load."

    inline_snippet(
        example_path=example_path,
        write_mode='w+',
        error_message=error_message)
