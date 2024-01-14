import sys

if __name__ == "__main__":
    from mypy_process import process

    filename = sys.argv[1]
    process(filename)
