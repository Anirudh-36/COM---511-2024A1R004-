"""canteen_storage.py - saving and reading order records (Milestone 5)."""

import canteen_utils

FILENAME = "canteen_order.txt"


def save_order(order, filename=FILENAME):
    """Append one completed order to the text file (append mode)."""

    items_text = ";".join(f"{name}:{qty}" for name, qty in order.items.items())

    record = (f"{order.order_id}|{order.student_name}|{items_text}|"
              f"{order.calculate_total()[2]:.2f}|{canteen_utils.get_timestamp()}\n")

    with open(filename, "a") as file:
        file.write(record)


def read_orders(filename=FILENAME):
    """Return all saved records. Raises FileNotFoundError if the file is missing."""

    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def next_order_id(filename=FILENAME):
    """Order IDs start at 101 and grow with the number of saved orders."""

    try:
        return 101 + len(read_orders(filename))
    except FileNotFoundError:
        return 101
