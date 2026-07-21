class Plant:
    def __init__(self, name: str, height: float, age: int)
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: float = 1.0):
        self.height += cm
        
    def get_info(self) -> str:
        return f"- {self.name}: {round(self.height, 2)} cm, {self.age} days old"

    def ft_plant_factory():
        print("=== Plant Factory Creation ===")

    plants = [
        Plant("Rose", 15.5, 5),
        Plant("Sunflower", 10.3, 23),
        Plant("Cactus", 5.2, 30),
        Plant("Fern", 20.0, 8),
        Plant("Orchid", 12.8, 15)
    ]

    print(f"Created {len(plants)} plants successfully!\n")

    print("=== Simulating Growth ===")
    plants[0].grow(2.5)
    plants[1].grow(5.0)
    print("Some plants grew!\n")

    print("=== Factory Inventory ===")
    for i in range(len(plants)):
        print(plants[i].get_info())


if __name__ == "__main__":
    ft_plant_factory()
