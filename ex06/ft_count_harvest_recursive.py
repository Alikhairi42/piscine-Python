def count_helper(current_day, max_day):
    if current_day > max_day:
        print("Harvest time!")
        return
    else:
        current_day += 1
        print("Day", current_day)
        count_helper(current_day, max_day)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_helper(0, days - 1)
