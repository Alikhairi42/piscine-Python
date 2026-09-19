#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")

    elif operation_number == 1:
        10 / 0

    elif operation_number == 2:
        open("missing_file.txt")

    elif operation_number == 3:
        "hello" + 42

    else:
        return


def test_error_types() -> None:
    print("=== Testing different error types ===")

    try:
        garden_operations(0)
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    print("Program continues after ValueError")

    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print("Program continues after ZeroDivisionError")

    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    print("Program continues after FileNotFoundError")

    try:
        garden_operations(3)
    except TypeError as error:
        print(f"Caught TypeError: {error}")

    print("Program continues after TypeError")

    print("=== Multiple errors with one try ===")

    try:
        garden_operations(0)
    except (
        ValueError,
        ZeroDivisionError,
        FileNotFoundError,
        TypeError,
    ) as error:
        print(f"Caught error: {error}")

    print("Program continues after multiple-error handler")


if __name__ == "__main__":
    test_error_types()