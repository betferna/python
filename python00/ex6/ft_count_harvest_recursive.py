def ft_count_harvest_recursive(days: int | None = None, current: int = 1):
    if days == None :
        days = int(input("Days until harvest: "))
    print(f"Day {current}")
    if current == days :
        print("Harvest day!")
        return
    ft_count_harvest_recursive(days, current+1)

