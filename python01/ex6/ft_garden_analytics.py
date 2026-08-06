#!/usr/bin/env python3

class Plant:
	class Stats:
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


	def __init__(self, name: str, height: float, days: int):
		self._name = name
		self._height = height
		self._days = days
		self._stats = self.Stats()

	def show(self) -> None:
		print(f"{self._name}: {self._height}cm, {self._days} days old")
		self._stats.log_show()

	def grow(self, cm: float):
		self._height = round(self._height + cm, 2)
		self._stats.log_grow()

	def age(self, add: int = 1):
		self._days += add
		self._stats.log_age()

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
			print(f"Age updated: {self._days} days")


	@staticmethod
	def is_older_than_year(age: int) -> bool:
		return age > 365


	@classmethod
	def anonymous(cls):
		return cls("Unknown plant", 0.0, 0)


class Tree(Plant):
	class TreeStats(Plant.Stats):
		def __init__(self):
			super().__init__()
			self._shade_calls = 0

		def log_shade(self):
			self._shade_calls += 1

		def display(self):
			super().display()
			print(f"{self._shade_calls} shade")

	def __init__(self, name, height, days, trunk):
		super().__init__(name, height, days)
		self.trunk_diameter = trunk
		self._stats = Tree.TreeStats()

	def produce_shade(self):
		print(f"{self._name} is producing shade")
		self._stats.log_shade()

	def show(self):
		super().show()
		print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
	def __init__(
		self, name: str, height: float, days: int,
		harvest_season: str
	):
		super().__init__(name, height, days)
		self.harvest_season = harvest_season
		self.nutritional_value = 0

	def grow(self, cm: float):
		self._height = round(self._height + cm, 2)

	def age(self, add: int = 1):
		self._days += add
		self.nutritional_value += add

	def show(self):
		super().show()
		print(f"  Harvest season: {self.harvest_season}")
		print(f"  Nutritional value: {self.nutritional_value}")


class Flower(Plant):
	def __init__(self, name: str, height: float, days: int, color: str):
		super().__init__(name, height, days)
		self.color = color
		self._bloom = False

	def bloom(self):
		self._bloom = True

	def show(self):
		super().show()
		print(f"Color: {self.color}")
		if self._bloom:
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet")

class Seed(Flower):
	def __init__(self, name: str, height: float, days: int, color: str, seed_count: int = 42):
		super().__init__(name, height, days, color)
		self._seed_count_when_bloomed = seed_count
		self.seeds = 0

	def bloom(self):
		super().bloom()
		self.seeds = self._seed_count_when_bloomed

	def show(self):
		super().show()
		print(f"Seeds: {self.seeds}")

def display_plant_stats(plant: Plant):
	print(f"[statistics for {plant._name}]")
	plant._stats.display()


def ft_garden_analytics():
	print("=== Garden statistics ===")

	print("=== Check year-old")
	print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
	print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
	print("")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()
	display_plant_stats(rose)

	print("[asking the rose to grow and bloom]")
	rose.grow(8.0)
	rose.bloom()
	rose.show()
	display_plant_stats(rose)
	print("")

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	display_plant_stats(oak)

	print("[asking the oak to produce shade]")
	oak.produce_shade()
	display_plant_stats(oak)

	print("")

	print("=== Seed")
	sunflower = Seed("Sunflower", 80.0, 45, "yellow", seed_count=42)
	sunflower.show()

	print("[make sunflower grow, age and bloom]")
	sunflower.grow(30.0)
	sunflower.set_age(65)
	sunflower.bloom()
	sunflower.show()
	display_plant_stats(sunflower)
	print("")

	print("=== Anonymous")
	anon_plant = Plant.anonymous()
	anon_plant.show()
	display_plant_stats(anon_plant)


if __name__ == "__main__":
	ft_garden_analytics()
