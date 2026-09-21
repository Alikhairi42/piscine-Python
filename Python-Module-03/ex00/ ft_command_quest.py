#!/usr/bin/env python3

import sys


def main() -> None:
    try:
        print("=== Command Quest ===")
        print("Program name:", sys.argv[0])

        if len(sys.argv) == 1:
            print("No arguments provided!")
            print("Total arguments:", len(sys.argv))
        else:
            print("Arguments received:", len(sys.argv) - 1)

            for i in range(1, len(sys.argv)):
                print(f"Argument {i}: {sys.argv[i]}")

            print("Total arguments:", len(sys.argv))

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()