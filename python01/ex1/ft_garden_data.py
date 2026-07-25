class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")



def ft_garden_data(plant_list: list[Plant]) -> None:
    for plant in plant_list:
        plant.show()

def main():
    print("=== Garden Plant Registry ===")
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    ft_garden_data(plants)


if __name__ == '__main__':
    main()
