#!/usr/bin/env python3


class Plant:
    _name: str
    _height: float
    _age: int

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = 0.0
        self._age = 0

        if height >= 0:
            self._height = height

        if age >= 0:
            self._age = age

        print(
            f"Plant created: {self._name}: "
            f"{self._height}cm, {self._age} days old"
        )

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    p1 = Plant("Rose", 15.0, 10)

    print("")
    p1.set_height(25.0)
    p1.set_age(30)

    print("")
    p1.set_height(-10.0)
    p1.set_age(-5)

    print("")
    print(
        f"Current state: {p1._name}: "
        f"{p1.get_height()}cm, {p1.get_age()} days old"
    )
