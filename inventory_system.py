"""Inventory management system for tracking items, quantities, and stock levels."""

import json
from datetime import datetime

# Global dictionary to store stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item or quantity type.")
        return

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Handles case when item doesn't exist
        print(f"Item '{item}' not found in inventory.")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with empty inventory.")


def save_data(file_name="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with stock below the given threshold."""
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # Invalid case (triggers validation)
    remove_item("apple", 3)
    remove_item("orange", 1)  # Non-existent item
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Eval removed for security reasons.")


if __name__ == "__main__":
    main()
