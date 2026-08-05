class Plant:
    class StatsSystem:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def log_grow(self):
            self._grow_calls += 1

        def log_age(self):
            self._age_calls += 1

        def log_show(self):
            self._show_calls += 1

        def display(self):
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._stats = self.StatsSystem()

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, cm: float = 1.0):
        if cm > 0:
            self._height += cm
            self._stats.log_grow()

    def set_age(self, days: int):
        if days >= 0:
            self._age = days
            self._stats.log_age()

    def show(self):
        self._stats.log_show()
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self):
        self._is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, seed_count: int = 42):
        super().__init__(name, height, age, color)
        self._seed_count_when_bloomed = seed_count
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = self._seed_count_when_bloomed

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class TreeStatsSystem(Plant.StatsSystem):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def log_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.TreeStatsSystem()

    def produce_shade(self):
        self._stats.log_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


def display_plant_stats(plant: Plant):
    """Muestra las estadísticas de cualquier tipo de planta."""
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


def ft_garden_analytics():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", seed_count=42)
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.set_age(65)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    anon_plant = Plant.anonymous()
    anon_plant.show()
    display_plant_stats(anon_plant)


if __name__ == "__main__":
    ft_garden_analytics()
