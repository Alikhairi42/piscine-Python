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


def ft_Plant():
    raise PlantError("The tomato plant is wilting!")
def ft_Water():
    raise WaterError("Not enough water in the tank!")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        ft_Plant()
    except PlantError as error:
        print("Caught PlantError:",error)
    
    print("Testing WaterError...")
    try:
        ft_Water()
    except WaterError as error:
        print("Caught WaterError:",error)
    
    print("\nTesting catching all garden errors...")
    
    try:
        ft_Plant()
    except GardenError as error:
        print("Caught GardenError:", error)
        
    try:
        ft_Water()
    except GardenError as error:
        print("Caught GardenError:", error)

    print("\nAll custom error types work correctly!")

