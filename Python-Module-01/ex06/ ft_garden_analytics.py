#!/usr/bin/env python3


class Plant:

    class Statistics:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self):
            self._grow_count += 1

        def increment_age(self):
            self._age_count += 1

        def increment_show(self):
            self._show_count += 1

        def display(self):
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Statistics()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self._height += 8.0
        self._stats.increment_grow()

    def age(self):
        self._age += 1
        self._stats.increment_age()

    def show(self):
        self._stats.increment_show()
        print(
            f"{self._name}: {self._height}cm, "
            f"{self._age} days old"
        )

    def display_statistics(self):
        self._stats.display()


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")

        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade_count = 0

    def produce_shade(self):
        self._shade_count += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def display_statistics(self):
        super().display_statistics()
        print(f"{self._shade_count} shade")


class Seed(Flower):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self):
        super().bloom()
        self._seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant):
    plant.display_statistics()

if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year?->",
        Plant.is_older_than_year(30)
    )
    print(
        "Is 400 days more than a year?->",
        Plant.is_older_than_year(400)
    )

    print("=== Flower")

    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[statistics for Rose]")
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()

    print("[statistics for Rose]")
    display_statistics(rose)

    print("=== Tree")

    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[statistics for Oak]")
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("[statistics for Oak]")
    display_statistics(oak)

    print("=== Seed")

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()

    print("[statistics for Sunflower]")
    display_statistics(sunflower)

    print("=== Anonymous")

    anonymous = Plant.create_anonymous()
    anonymous.show()

    print("[statistics for Unknown plant]")
    display_statistics(anonymous)