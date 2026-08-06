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


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: {plant._name}: {round(plant._height, 1)}cm, "
        f"{plant._days} days old\n"
        )
    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5.0)
    plant.set_age(-10)

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
