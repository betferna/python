import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ex2")))

from ft_plant_growth import Garden

def ft_plant_factory():
    plants = [
        Garden("Rose", 15.5, 5),
        Garden("Sunflower", 10.3, 23),
        Garden("Cactus", 5.2, 30),
        Garden("Fern", 20.0, 8),
        Garden("Orchid", 12.8, 15)
    ]
    plants[0].grow(2.5)
    plants[1].grow(5.0)
    for i in range(len(plants)):
        print(f"Created: ", end="")
        plants[i].show()

def main():
    print("=== Plant Factory Output ===")
    ft_plant_factory()


if __name__ == "__main__":
    main()
