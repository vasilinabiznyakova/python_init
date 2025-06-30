"""
Currying is a programming technique where a function that takes multiple arguments is converted into a sequence of functions, each of which takes a single argument.
# """
# def add(a):
#     def add_b(b):
#         return a + b

#     return add_b


# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)


# def apply_discount(price: float, discount_percentage: int) -> float:
#     return price * (1 - discount_percentage / 100)


# # Використання
# discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
# print(discounted_price)

# discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
# print(discounted_price)


from typing import Callable


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)
