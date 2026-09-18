#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age_days: int
    rate: float

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height = round(self.height + self.rate, 1)


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25.0
    plant1.age_days = 30
    plant1.rate = 0.8
    start_height = plant1.height
    plant1.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    total_growth = round(plant1.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")
