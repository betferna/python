#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, cm: float) -> None:
        self.height = round(self.height + cm, 2)

    def age(self, add: int = 1) -> None:
        self.days += add


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth()
