def ft_garden_intro(name: str, height: int, age: int):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


def main():
    name = "Rose"
    height = 25
    age = 30
    ft_garden_intro(name, height, age)


if __name__ == '__main__':
    main()
