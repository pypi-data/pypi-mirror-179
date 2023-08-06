# Version 0.

- [x] When entering the terminal with `ty -`, black isort and the type checker should run. If they didn't run it would offer no benefit to using `py` and sometimes I want to test something in a terminal and running the suite would be helpful to not import something with type errors in the tty.
- [ ] If `ty` is used to run a file in a different folder, it uses the default `mypy`
because it can't find a `pyproject.toml` in the `$(realpath dirname $PWD)`. Should it do this? Is it possible to find what module a script belongs to?
What happens for namespace packages?
- [ ] Fix the paths in the tests folders using new `example` path

# Version 1.

- [x] Just one file, this whole thing should be email'able as one file, even if I install it with pip and pip needs stuff I'd like it to be just one file in the src
- [x] 'do one thing well', just type check, no formatting
    - I think I want to remove formatting with black and isort, I find when I'm working on something I want to type check every single time I run, but I only really want to format once at the end before committing.
        - I've actually had times where isort has broken my programs, when I'm type checking I don't want my programs to break
- [x] Install with pip, as a command line command
    - There's currently four steps in the install process, that's 3 too many.
    - I've never done this, but my understanding is it has to do with `entry_points`, see (this could be wrong, but asking online I was told it has something to do with `entry_points`):
        - NEW THING: https://packaging.python.org/en/latest/specifications/entry-points/
        - OLD THING: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
    - One main issue is how do you `brew install coreutils` on macos? Worst case I could issue a runtime warning, as I do for the `py` command with instructions
- [ ] I should figure out a way to use pytest for this
    - [ ] parameterize python version at least [3.9, 3.10] and then [mypy, pyright, pytype (only 3.9 at the moment)]
- [x] What's the default type checker?
    - mypy
        - I really don't like having to add `ignore_missing_imports` everytime I use mypy, I really want to make it the default like with the `--pretty`. On the other hand, maybe I should remove all default opinions so `mypy` behaves how `mypy` behaves
    - pyright
        - has the problem that the fast version is `npm`, which I don't know how to install with pip. the pip pyright version is very slow to startup and I can't figure out how to make it not check for updates.
        - has a lot of noise in the output
    - pytype
        - doesn't support 3.10, which means as a default it's probably not the best because people (me) will want to use up to date python versions
- [x] I need 3.11 for the built in toml parsing, although I guess if I'm installing with pip a python dependency is fine. It's slightly unfortunate
- [x] Add `-h/--help` logic
- [x] Add `-q` logic
- [ ] If you run this from ty you stall, probably something wrong about subprocess vs process:
    ```py
    from subprocess import run

    run(["python3", "-"])
    ```
- [ ] Check the PID is the same for type checking and running python
- [ ] Fix stdout colors:
    - [x] mypy
    - [x] pyright
    - [ ] pytype
    ```
    Ryans-MacBook-Air:junk ryan$ ty x.py
    Success: no issues found in 1 source file # NOT COLOR D:
    hi
    Ryans-MacBook-Air:junk ryan$ ty -
    Success: no issues found in 1 source file # IN COLOR :D
    Python 3.10.6 (main, Aug 30 2022, 04:58:14) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
- [ ] Fix terminal KeyboardInterrupt
- [x] Fix quiet when running file
    ```py
    Ryans-MacBook-Air:junk ryan$ ty -q x.py
    Success: no issues found in 1 source file
    hi
    ```
- [x] Fix quiet flag when success otherwise
    ```
    (v1.0.0) Ryans-MacBook-Air:ty-command ryan$ ty
    Success: no issues found in 7 source files
    (v1.0.0) Ryans-MacBook-Air:ty-command ryan$ ty -q
    >>>
    ```
- [x] Fix `ty -q` when pyright selected
    ```
    (main) Ryans-MacBook-Air:leetcode ryan$ ty -q
    Unexpected option -q.
    pyright --help for usage
    ```
    the pyright stderr doesnt show all errors:
    ```
    >>> from subprocess import run
    >>> x =run(['ty'], capture_output = True)
    >>> x.stdout
    b'No configuration file found.\npyproject.toml file found at /Users/ryan/leetcode.\nLoading pyproject.toml file at /Users/ryan/leetcode/pyproject.toml\nAssuming Python version 3.10\nAssuming Python platform Darwin\nAuto-excluding **/node_modules\nAuto-excluding **/__pycache__\nAuto-excluding **/.*\nSearching for source files\nFound 9 source files\npyright 1.1.273\n/Users/ryan/leetcode/old-leetcode.py\n  /Users/ryan/leetcode/old-leetcode.py:3335:20 - error: Expression of type "Unknown | bool | None" cannot be assigned to return type "bool"\n  \xc2\xa0\xc2\xa0Type "Unknown | bool | None" cannot be assigned to type "bool"\n  \xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0Type "None" cannot be assigned to type "bool" (reportGeneralTypeIssues)\n1 error, 0 warnings, 0 informations \nCompleted in 1.535sec\n'
    >>> x.stderr
    b'stubPath /Users/ryan/leetcode/typings is not a valid directory.\n'
    ```
- [x] Add py `py [-X[.Y]]` logic, my main worry is that while using sys.executable
- [ ] I think pytype is broken on 3.10 it would be nice if I could raise an error instead of pytype
    - [ ] On PyPI pytype supports 3.10 (in terms of it being allowed to pip install) but then says 'You need a Python 3.7-3.9 interpreter to run pytype, as well as an interpreter in $PATH for the Python version of the code you're analyzing (supported: 3.7-3.9).' So even if I could figure out how to get pip to tell me this info it would not help. I could manually maintain it but that seems horrible.
- [ x ] Support windows... On a similar note I think I can say an install is optional in the pyproject.toml, it would be good to say pyright and pytype are optional in case the install doesn't work
  - [ ] add windows workflow for case
  - [ ] dont let people use pyright and pytype on windows because it's broken currently
- [ ] There's such a thing as a dynamic version setting (it inspects into the file to get the version number), I don't have the link right now someone told you on discord
