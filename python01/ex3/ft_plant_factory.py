#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../ex2")))

from ft_plant_growth import Garden


def ft_plant_factory():
    plants = [
        Garden("Rose", 25.5, 30),
        Garden("Oak", 200.0, 365),
        Garden("Cactus", 5.0, 90),
        Garden("Sunflower", 80.0, 45),
        Garden("Orchid", 15.0, 120)
    ]
    plants[0].grow(2.5)
    plants[1].grow(5.0)
    for i in range(len(plants)):
        print("Created: ", end="")
        plants[i].show()


def main():
    print("=== Plant Factory Output ===")
    ft_plant_factory()


if __name__ == "__main__":
    main()
