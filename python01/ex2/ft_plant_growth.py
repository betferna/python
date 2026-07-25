import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ex1")))

from ft_garden_data import Plant

class Garden(Plant):
    def __init__(self, name: str, height: float, days: int):
        super().__init__(name, height, days)

    def grow(self, cm: float = 0.8):
        self.height = round(self.height + cm, 2)

    def age(self, add: int = 1):
        self.days += add


def ft_plant_growth():
    print("=== Garden Plant Growth ===")

    rose = Garden("Rose", 25.0, 30)
    initial_height = rose.height

    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        rose.grow()
        rose.age()

        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 2)}cm")



if __name__ == "__main__":
    ft_plant_growth()
