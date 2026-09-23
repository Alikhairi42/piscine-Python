#!/usr/bin/env python3
import typing
import sys

def check():
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file:IO = open(sys.argv[1])
        cat: str = file.read()
        print("---")
        print(cat,end="")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed..")
    except IOError:
        print ("Could not read file: ", sys.argv[1])

if __name__ == "__main__":
    check()