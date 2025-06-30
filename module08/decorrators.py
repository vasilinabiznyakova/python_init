"""
There is a design pattern called the decorator. This pattern is about extending existing functionality without making any changes to the code of that functionality itself.


**Logging** -  recording information about function calls to ensure transparency and traceability.
**Access control** - checking user permissions before executing a function to control access.
**Caching** -  storing function results to improve efficiency and reduce execution time.
**Argument validation** -  analyzing and modifying arguments before passing them to a function to ensure correctness of the call.

It is very important to use the functools module when creating decorators, this is necessary to preserve the metadata of the original function that we are decorating. The functools.wraps function helps with this by preserving information about the original function, such as the function name and documentation.
"""

# def complicated(x: int, y: int) -> int:
#     return x + y


# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner


# complicated = logger(complicated)
# print(complicated(2, 3))


# """Python has special syntax for decorators"""


# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner


# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y


# print(complicated(2, 3))


from functools import wraps


def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print(complicated(2, 3))
print(complicated.__name__)
