#!/usr/bin/env python3

import sys


inventory = {}

print("=== Inventory System Analysis ===")

for arg in sys.argv[1:]:
    if ":" not in arg:
        print(f"Error- invalid parameter '{arg}'")
        continue

    parts = arg.split(":")
    item = parts[0]
    quantity = parts[1]

    try:
        quantity = int(quantity)
    except ValueError as e:
        print(f"Quantity error for '{item}': {e}")
        continue

    if item in inventory:
        print(f"Redundant item '{item}'- discarding")
        continue

    inventory[item] = quantity


print(f"Got inventory: {inventory}")

item_list = list(inventory.keys())
print(f"Item list: {item_list}")

total = sum(inventory.values())
print(f"Total quantity of the {len(item_list)} items: {total}")

for item in inventory.keys():
    quantity = inventory[item]
    percentage = round(quantity / total * 100, 1)
    print(f"Item {item} represents {percentage:.1f}%")

most_item = None
most_quantity = 0

least_item = None
least_quantity = None

for item in inventory.keys():
    quantity = inventory[item]

    if quantity > most_quantity:
        most_quantity = quantity
        most_item = item

    if least_quantity is None or quantity < least_quantity:
        least_quantity = quantity
        least_item = item

print(
    f"Item most abundant: {most_item} "
    f"with quantity {most_quantity}"
)

print(
    f"Item least abundant: {least_item} "
    f"with quantity {least_quantity}"
)

inventory.update({"magic_item": 1})

print(f"Updated inventory: {inventory}")