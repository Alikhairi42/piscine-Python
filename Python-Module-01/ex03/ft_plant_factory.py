#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    p1 = Plant("Rose", 25.0, 30)
    p2 = Plant("Oak", 200.0, 356)
    p3 = Plant("Cactus", 5.0, 90)
    p4 = Plant("Sunflower", 80.0, 45)
    p5 = Plant("Fern", 15.0, 120)

    print("Created: ", end="")
    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
