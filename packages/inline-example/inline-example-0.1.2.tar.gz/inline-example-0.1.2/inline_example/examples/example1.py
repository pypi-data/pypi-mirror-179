from inline_example import inline_example
from pathlib import Path

def quick_template():
    """Provides a template for using this library."""
    example_path = Path(__file__).parent / 'examples/example.py'
    inline_example(
        example_path=example_path,
        write_mode='w+')

# now your user could call this:

# from yourpackage.your_module import quick_template
# quick_template()