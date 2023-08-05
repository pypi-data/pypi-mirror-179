from inspect import stack, getmodule

def inline_example(example_path, write_mode: str = 'w+'):
    with open(example_path, 'r') as i:
        r = i.read()
    
    module = getmodule(stack()[-1][0])
    with open(module.__file__, write_mode, newline='') as out:
        if 'a' in write_mode:
            r = '\n\n' + r
        out.write(r)
