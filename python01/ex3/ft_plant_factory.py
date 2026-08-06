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


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25.5, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Orchid", 15.0, 120)
    ]
    plants[0].grow(2.5)
    plants[1].grow(5.0)
    for i in range(len(plants)):
        print("Created: ", end="")
        plants[i].show()


def main() -> None:
    print("=== Plant Factory Output ===")
    ft_plant_factory()


if __name__ == "__main__":
    main()
