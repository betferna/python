#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")

    def grow(self, cm: float) -> None:
        self._height = round(self._height + cm, 2)

    def age(self, add: int = 1) -> None:
        self._days += add

        if self._height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(self._height)

        if self._days < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = int(self._days)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {round(self._height)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._days = int(new_age)
            print(f"Age updated: {self._days} days\n")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        color: str
    ) -> None:
        super().__init__(name, height, days)
        self.color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float,
        days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self._shade = False

    def produce_shade(self) -> None:
        self.shade = True


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, days: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm: float) -> None:
        self._height = round(self._height + cm, 2)

    def age(self, add: int = 1) -> None:
        self._days += add
        self.nutritional_value += add

    def show(self) -> None:
        super().show()
        print(f"  Harvest season: {self.harvest_season}")
        print(f"  Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
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
