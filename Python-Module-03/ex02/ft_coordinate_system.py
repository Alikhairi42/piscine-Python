#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            return (x, y, z)

        except ValueError as error:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    print(f"Error on parameter '{part.strip()}': {error}")
                    break


def calculate_distance(
    point1: tuple[float, float, float],
    point2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first = get_player_pos()

    print(f"Got a first tuple: {first}")
    print(
        f"It includes: X={first[0]}, "
        f"Y={first[1]}, Z={first[2]}"
    )

    center = (0.0, 0.0, 0.0)
    distance = calculate_distance(first, center)

    print(f"Distance to center: {distance:.4f}")

    print("Get a second set of coordinates")
    second = get_player_pos()

    distance = calculate_distance(first, second)

    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance:.4f}"
    )


if __name__ == "__main__":
    main()