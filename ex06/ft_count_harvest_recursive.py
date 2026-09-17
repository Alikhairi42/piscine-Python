def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    for i in range(days, 0, -1):
        print("Day", i)
    print("Harvest time!")
