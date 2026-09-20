#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    print(f"Watering {plant_name}: ", end="")

    if plant_name != plant_name.capitalize():
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'"
        )

    print("[OK]")


def test_watering_system():
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    test_watering_system()

    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()