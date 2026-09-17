#!/usr/bin/env python3
import sys


def parse_inventory() -> dict:
    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error- invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error- invalid parameter '{arg}'")
            continue

        item_name, qty_str = parts[0], parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}'- discarding")
            continue

        try:
            quantity = int(qty_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    if total_qty > 0:
        for item, qty in inventory.items():
            percentage = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {percentage:.1f}%")

    if inventory:
        most_abundant = None
        least_abundant = None

        for item, qty in inventory.items():
            if most_abundant is None or qty > inventory[most_abundant]:
                most_abundant = item
            if least_abundant is None or qty < inventory[least_abundant]:
                least_abundant = item

        print(
            f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
