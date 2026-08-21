#!/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def water_plants(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'.")


def test_watering_system() -> None:
    try:
        print("Testing valid plants...")
        print("Opening watering system")

        water_plants("Tomato")
        water_plants("Lettuce")
        water_plants("Carrots")
        print("Closing watering system\n")

        print("Testing invalid plants...")
        print("Opening watering system")
        water_plants("Tomato")
        water_plants("lettuce")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors")
