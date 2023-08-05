from pathlib import Path
from .inline import inline_snippet


def inline():
    """Provides a template for using this library."""

    example_path = Path(__file__).parent / 'examples/inline_snippet.py'
    error_message = "# uh oh! This snippet failed to load."

    inline_snippet(
        example_path=example_path,
        write_mode='w+',
        error_message=error_message)