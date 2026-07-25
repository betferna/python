import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ex1")))

from ft_garden_data import Plant

class PlantSecurity(Plant):
    def __init__(self, name:str, height: float, days:int):
        super().__init__(name, height, days)
        self._name = name
        self.set_height = height
        self.set_age = days
        
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._days = 0
        else:
            self._days = int(days)

        print(
            f"Plant created: {self._name}: {round(self._height, 1)}cm, "
            f"{self._days} days old\n"
        )

        def get_name(self) -> str:
            return self._name

        def get_height(self) -> float:
            return self._height

        def get_age(self) -> int:
            return self._days

        def set_height(self, new_height: float):
            if new_height < 0:
                print(f"{self._name}: Error, height can't be negative")
                print("Height update rejected")
            else:
                self._height = float(new_height)
                print(f"Height updated: {round(self._height)}cm")

        def set_age(self, new_age: int):
            if new_age < 0:
                print(f"{self._name}: Error, age can't be negative")
                print("Age update rejected\n")
            else:
                self._days = int(new_age)
                print(f"Age updated: {self._days} days\n")

        def get_info(self) -> str:
            return (
                f"{self._name}: {round(self._height, 1)}cm, "
                f"{self._days} days old"
            )


def ft_garden_security():
    print("=== Garden Security System ===")

    plant = PlantSecurity("Rose", 15.0, 10)

    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5.0)
    plant.set_age(-10)

    print(f"Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
