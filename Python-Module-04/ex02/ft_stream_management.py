#!/usr/bin/env python3
import typing
import sys


def check() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file: typing.IO = open(sys.argv[1])
        cat: str = file.read()

        print("---")
        print(cat, end="")
        print("---")

        file.close()
        print(f"File '{sys.argv[1]}' closed.")

        print("Transform data:")
        print("---")

        hacht: str = cat.split("\n")
        for i in range(len(hacht)):
            if hacht[i] != "":
                hacht[i] += "#"

        cat = "\n".join(hacht)

        print(cat, end="")
        print("---")

        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        name: str = sys.stdin.readline().strip()
        print(f"Saving data to '{name}'")
        new_file: typing.IO = open(name, "w")
        new_file.write(cat)
        new_file.close()
        print(f"Data saved in file '{name}'.")

    except IOError as err:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': [Errno 2] No such file or directory: '{sys.argv[1]}'",file=sys.stderr)


if __name__ == "__main__":
    check()