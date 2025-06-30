# def my_function():
#     print("Hello, world!")


# f = my_function
# f()


# from typing import Callable


# def add(a: int, b: int) -> int:
#     return a + b


# def multiply(a: int, b: int) -> int:
#     return a * b


# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)


# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply)


# """Closures are a powerful concept in programming.Closures occur when an inner function remembers the state of its environment at the time of its creation and can use those variables even after the outer function has completed its execution."""


# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function


# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()


from typing import Callable


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count

    return increment


# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
