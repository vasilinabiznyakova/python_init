"""
An enumeration data type, often abbreviated as Enum, is a way of defining a set of named constants in programming languages, allowing the use of more meaningful names for these constants instead of simple numeric values.
"""
from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY


if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")


day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY


from enum import Enum, auto


class OrderStatus(Enum):
    NEW = auto() # automatically assign unique values ​​to each status, avoiding the need to manually specify them.
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)
order1.display_status()
order2.display_status()

