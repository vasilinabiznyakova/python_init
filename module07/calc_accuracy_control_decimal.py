print(0.1 + 0.2 == 0.3)  # 0.30000000000000004
print(0.1 + 0.2) # Flase 


from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))


from decimal import (
    Decimal,
    getcontext,
)  # округляет до значащих цифра - ВСЕ важные цифры в числе, вне зависимости от того, до или после точки.!!!!


getcontext().prec = 6 # Now any calculations with Decimal will have precision up to four decimal places.
print(Decimal("1") / Decimal("7"))  # 0.142857

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))  # 0.14285714


"""
Decimal allows selecting different rounding modes.
According to the official Python documentation, here are the main rounding modes:

ROUND_FLOOR
Always rounds the number toward the nearest smaller value, regardless of the number's sign.

ROUND_CEILING
Always rounds the number toward the nearest greater value, regardless of the number's sign.

ROUND_HALF_DOWN
Rounds numbers to the nearest value.
In the case of a tie (e.g., 2.5, where both 2 and 3 are possible), the number is rounded down, i.e., toward the smaller value.

ROUND_HALF_UP
Also rounds numbers to the nearest value.
However, in a tie situation (e.g., 2.5), the number is rounded up, i.e., toward the greater value.

ROUND_UP
Rounds away from zero.
This means positive numbers are rounded upward, and negative numbers are rounded downward (i.e., further from zero).

ROUND_DOWN
Rounds toward zero.
That is, positive numbers are rounded downward, and negative numbers are rounded upward (i.e., closer to zero).

ROUND_HALF_EVEN
Rounds numbers to the nearest value.
This mode, also known as "bankers' rounding", rounds to the nearest even number in case of a tie.
For example, 2.5 becomes 2, and 3.5 becomes 4.
This method helps reduce cumulative rounding errors in large datasets.

The quantize method is often used in financial applications where precise control of the number of decimal places is required, especially in calculations that require strict adherence to certain rounding rules. This ensures accuracy and compliance with requirements that may be imposed by law or accounting standards.

Decimal is a powerful tool for precise calculations that provides a high level of control and flexibility. Its use is critical in financial applications, accounting, and other areas where rounding errors can have serious consequences.
"""
import decimal
from decimal import Decimal

number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print(
    "Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0"))
)  # 1.4

# Округлення вверх при нічиї (ROUND_HALF_UP)
print(
    "Округлення вгору ROUND_HALF_UP:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP),
)  # 1.5

# Округлення вниз (ROUND_FLOOR)
print(
    "Округлення вниз ROUND_FLOOR:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR),
)  # 1.4

# Округлення вверх (ROUND_CEILING)
print(
    "Округлення вгору ROUND_CEILING:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING),
)  # 1.5

# Округлення до трьох десяткових знаків за замовчуванням
print(
    "Округлення до трьох десяткових знаків:",
    Decimal("3.14159").quantize(Decimal("0.000")),
)  # 3.142
