from inline_example import inline_example
from pathlib import Path

def quick_template():
    """Provides a template for using this library."""

    example_path = Path(__file__).parent / 'examples/example.py'
    error_message = "# uh oh! This example failed to load."

    inline_example(
        example_path=example_path,
        write_mode='w+',
        error_message=error_message)
