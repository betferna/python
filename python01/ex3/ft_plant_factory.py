class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: float = 1.0):
        self.height += cm

    def show(self) -> str:
        return (
            f"Created: {self.name}: {round(self.height, 2)} cm, "
            f"{self.age} days old"
        )


def ft_plant_factory():
    plants = [
        Plant("Rose", 15.5, 5),
        Plant("Sunflower", 10.3, 23),
        Plant("Cactus", 5.2, 30),
        Plant("Fern", 20.0, 8),
        Plant("Orchid", 12.8, 15)
    ]
    plants[0].grow(2.5)
    plants[1].grow(5.0)
    for i in range(len(plants)):
        print(plants[i].show())

def main():
    print("=== Plant Factory Output ===")
    ft_plant_factory()


if __name__ == "__main__":
    main()