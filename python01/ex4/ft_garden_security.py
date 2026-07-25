class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = int(age)

        print(
            f"Plant created: {self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old\n"
        )

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float):
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, new_age: int):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._age = int(new_age)
            print(f"Age updated: {self._age} days\n")

    def get_info(self) -> str:
        return (
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )


def ft_garden_security():
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)

    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5.0)
    plant.set_age(-10)

    print(f"Current state: {plant.get_info()}")


if __name__ == "__main__":
    ft_garden_security()
