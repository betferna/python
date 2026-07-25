import sys
import os
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../ex4")))
from ft_garden_security import PlantSecurity


class Flower(PlantSecurity):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self._bloom = False

    def bloom(self):
        self._bloom = True


class Tree(PlantSecurity):
    def __init__(
        self, name: str, height: float,
        days: int, trunk_diameter: float
    ):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self._shade = False

    def produce_shade(self):
        self.shade = True


class Vegetable(PlantSecurity):
    def __init__(
        self, name: str, height: float, days: int,
        harvest_season: str
    ):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm: float):
        self.height = round(self.height + cm, 2)

    def age(self, add: int = 1):
        self.days += add
        self.nutritional_value += add

    def show(self):
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
