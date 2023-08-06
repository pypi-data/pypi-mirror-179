#!/usr/bin/env bash
set -oux pipefail
./ty

./ty -h
./ty --help

./ty test-good.py
./ty test-bad.py
./ty test-good.py 1 2 3
./ty test-bad.py 1 2 3
./ty -O test-good.py 1 2 3
./ty -O test-bad.py 1 2 3

./ty -q
./ty -q test-good.py 1 2 3
./ty -q test-bad.py 1 2 3
./ty -q -O test-good.py 1 2 3
./ty -q -O test-bad.py 1 2 3

cat test-tty-stdin.py | ./ty test-tty-stdin.py
./ty -
./ty -q -

./ty -c "print(1)"
./ty -c "print(1);   print(2)"
./ty -q -c "print(1);   print(2)"

rm -rf .venv-test/
./ty -m venv .venv-test
rm -rf .venv-test/
./ty -q -m venv .venv-test
rm -rf .venv-test/

./ty -X importtime -c 'import asyncio'
./ty -q -X importtime -c 'import asyncio'

./ty -V
./ty -V -V
./ty -V -V -V # does the same as -V -V

# these tests can fail if you don't actually have the 3.X verion installed which
# is correct, ty should fail by returning py's message which looks like this:
# $ py -3.8
# No executable found for Python 3.8
./ty -3 -V
./ty -3.8 -V
./ty -3.9 -V
./ty -3.10 -V
./ty -3.9 -O -i test-good.py 1 2 3
./ty -3.9 -q -O -i test-good.py 1 2 3
./ty -3.9 -O -i -q test-good.py 1 2 3

./ty -m mypy test-bad.py
