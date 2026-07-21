class Plant:
    del __init__(self, name:str, height: int, age:int, groweth_rate: int = 1):
        self.name = name
        self.height = height
        self.age = age
        self.growth.rate = growth_rate
def grow(self, cm: float = None):
        """Si no se especifica cuántos cm crece, usa su tasa predeterminada (growth_rate)."""
        if cm is None:
            self.height += self.growth_rate
        else:
            self.height += cm

    def age_up(self, days: int = 1):
        """Aumenta la edad de la planta por el número de días indicados."""
        self.age += days

    def get_info(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


def ft_plant_growth():
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30, growth_rate=0.8)
    initial_height = rose.height

    print(rose.get_info())

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        
        rose.grow()
        rose.age_up(1)
        
        print(rose.get_info())

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
