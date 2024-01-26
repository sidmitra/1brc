"""
`mypyc mypy_*.py` generates .so files for the machine arch.

"""
import sys

if __name__ == "__main__":
    from mypy_process import process

    filename = sys.argv[1]
    process(filename)
