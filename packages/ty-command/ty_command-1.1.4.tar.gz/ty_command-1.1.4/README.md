# ty 🦆
A configurable type-checking Python command.

    usage: ty [-X[.Y]] [-h|--help] [-q] [...] [file.py] [...]

| flag      | description                                                     |
|-----------|-----------------------------------------------------------------|
| -h/--help | Help message                                                    |
| -q        | Supress non-error type checker output and tty version/copyright |
| -X.Y      | Launch Python version MAJOR.MINOR (`py` must be available)      |

## Install:

    pip install ty-command

## Typical usage examples:

    $ ty            # same as `python3 -m mypy .`
    $ ty file.py    # same as `python3 -m mypy .` + `python3 file.py`

Optional `pyproject.toml` file to configure type checker:

    [tool.ty]
    type_checker = "pyright" # "mypy" is the default, "pytype" also available

## Tip

Did you know `python3 -` opens the terminal? `ty -` does too, and type checks!
