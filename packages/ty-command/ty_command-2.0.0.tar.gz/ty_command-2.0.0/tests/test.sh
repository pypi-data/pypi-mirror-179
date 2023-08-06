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

./ty -m mypy test-bad.py
