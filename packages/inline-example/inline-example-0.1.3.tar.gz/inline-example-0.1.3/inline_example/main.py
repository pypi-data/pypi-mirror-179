from inspect import stack, getmodule
from os.path import exists


def inline_example(
    example_path: str, 
    write_mode: str = 'w+',
    error_message: str = "# Attempted inline example failed."
) -> None:
    """Writes the content in `example_path` to the calling file.

    Args:
        example_path (str): Path to the example file.
        write_mode (str, optional): The mode in which the file is opened. Defaults to 'w+'.
        error_message (str, optional): What to insert if something goes wrong. 
            Defaults to "# Attempted inline example failed.".
    """

    # open example and get contents
    example = None
    if exists(example_path):
        with open(example_path, 'r') as i:
            example = i.read()

    # set error message if example not found
    if not example:
        example = error_message
        write_mode = 'a+'
    
    # write to caller's current file
    module = getmodule(stack()[-1][0])
    with open(module.__file__, write_mode) as out:
        if 'a' in write_mode:
            example = '\n\n' + example
        out.write(example)
