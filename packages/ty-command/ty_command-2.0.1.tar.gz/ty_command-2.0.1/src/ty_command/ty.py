#!/usr/bin/env python3
# Copyright (c) 2021-2022 Ryan Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""# ty 🦆
A configurable type-checking Python command.

    usage: ty [-h|--help] [-q] [...] [file.py] [...]

| flag      | description                                                     |
|-----------|-----------------------------------------------------------------|
| -h/--help | Help message                                                    |
| -q        | Supress non-error type checker output and tty version/copyright |

## Install:

    pip install ty-command

## Typical usage examples:

    $ ty            # same as `python3 -m mypy .`
    $ ty file.py    # same as `python3 -m mypy .` + `python3 file.py`

Optional `pyproject.toml` file to configure type checker:

    [tool.ty]
    type_checker = "pyright" # "mypy" is the default, "pytype" also available

## Tip:

Did you know `python3 -` opens the terminal? `ty -` does too, and type checks!
"""

# NOTE I'd like this file to be useful by itself without any auxiliary files.
#      That's also why I'm not naming it main.py.

import sys
from functools import wraps
from os import environ
from os.path import isfile
from re import MULTILINE, sub
from shutil import which
from subprocess import CompletedProcess, run
from textwrap import dedent
from typing import Any, Callable, Dict, List, NoReturn, Tuple

import tomli

SUPPORTED_TYPE_CHECKERS = ["mypy", "pyright", "pytype"]

__version__ = "2.0.1"

_HELP = False
_QUIET = False
_TERMINAL = False
_GENERIC_ERROR_MSG = "Internal logic error."


class TyError(Exception):
    pass


def _pyproject_toml() -> str:
    # TODO what about in above dirs?
    #      for example im in /pkg/src and there's no pyproject.toml
    #      figure out how Black acts and copy that
    return "./pyproject.toml"


def _type_checker() -> str:
    try:
        with open(_pyproject_toml(), "r") as f:
            toml = f.read()
        # TODO Use built-in if available and tomli if not
        type_checker = tomli.loads(toml)["tool"]["ty"]["type_checker"]
    except:  # TODO whats the exception
        return "mypy"
    assert type(type_checker) == str
    return type_checker


def _return_code(process: CompletedProcess[bytes]) -> int:
    return process.returncode


def _run_python(
    argv: List[str], *, type_checking: bool = False
) -> CompletedProcess[bytes]:

    cmd = [which("python3")] + argv

    global _TERMINAL
    # FIXME this is a hack
    if "-i" in cmd:
        _TERMINAL = True

    process = run(cmd, capture_output=True if not _TERMINAL else False)
    # TODO handle KeyboardInterrupt
    #      pressing control + d is handled fine
    #      control + c KeyboardInterrupt spews out some trackback

    def stdout_stderr(p: CompletedProcess[bytes]) -> Tuple[str, str]:
        if not _TERMINAL:
            return process.stdout.decode("utf-8"), process.stderr.decode("utf-8")
        return "", ""

    stdout, stderr = stdout_stderr(process)
    # TODO make a table of which file descriptors mypy pyright and pytype put
    #      their error and output info because I'm confused
    if not type_checking:
        # NOTE we're passing `-q` to python, so python handles being quiet
        sys.stdout.write(stdout)
        sys.stderr.write(stderr)
    else:
        if _QUIET and _return_code(process) == 0:
            sys.stderr.write(stderr)
        elif _QUIET and _return_code(process) != 0:
            sys.stdout.write(stdout)  # mypy, pyright write errors to stdout
            sys.stderr.write(stderr)
        else:
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)  # doesnt do anything for mypy
    return process


def _run_type_checker(checker: str) -> CompletedProcess[bytes]:
    if checker not in SUPPORTED_TYPE_CHECKERS:
        raise TyError(
            f"Checker `{checker}` is not a supported type checker: \
            `{SUPPORTED_TYPE_CHECKERS}`!"
        )
    cmd = ["-m", checker, "."]
    match checker:
        case "pyright" | "pytype" | "mypy":
            return _run_python(cmd, type_checking=True)
        case _:
            raise TyError(_GENERIC_ERROR_MSG)


def _help_message() -> str:
    return (
        "\n".join(
            list(
                filter(
                    "".__ne__,
                    [
                        x.lstrip()
                        for x in sub(r"[#]{1,6} ", "", __doc__, MULTILINE).splitlines()
                    ],
                )
            )
        )
        + "\n"
    )


def _find_file_index(argv: List[str]) -> int:
    # TODO help flag must be first
    for i, arg in enumerate(argv):
        if arg[-3:] == ".py":  # ''[-n:] slice never raises index error
            return i
    return len(argv)


def _set_flags(argv: List[str]) -> None:
    global _HELP
    global _QUIET
    global _TERMINAL
    for i in range(_find_file_index(argv)):
        match argv[i]:
            case "-q":
                _QUIET = True
            case "-h" | "--help":
                _HELP = True
            case "-":
                _TERMINAL = True
            case _:
                pass


def _execute_python(argv: List[str]) -> int:
    # TODO look at:
    # https://docs.python.org/3/library/os.html?highlight=os%20execve#os.execve
    return _return_code(_run_python(argv))


def _execute_type_checker(checker: str) -> int:
    return _return_code(_run_type_checker(checker))


def main() -> int:
    argv: List[str] = sys.argv[1:]
    environ["MYPY_FORCE_COLOR"] = str(1)  # cheeky, unstable, and mypy specific!
    environ["FORCE_COLOR"] = str(1)  # works for pyright, didn't check pytype
    _set_flags(argv)
    if _HELP:
        sys.stdout.write(_help_message())
        return 0
    if (type_status := _execute_type_checker(_type_checker())) != 0:
        return type_status
    if len(argv) == 0 or (len(argv) == 1 and "-q" in argv):
        return 0
    return _execute_python(argv)


if __name__ == "__main__":
    main()
