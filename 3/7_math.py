"""

Constants:

math.pi - constant π (approximately 3.14159...);
math.e - constant e, base of natural logarithms (approximately 2.71828...);
math.tau - constant τ, equal to 2π (approximately 6.28318...);
math.inf - infinity notation;
math.nan - 'Not a Number' notation;


Number rounding functions:

math.ceil(x) - rounds a real number x to the nearest higher integer;
math.floor(x) - rounds a real number x to the nearest lower integer;
math.trunc(x) - truncates the fractional part of a real number x, and returns the integer part of the number;
"""
import math

# Output number
x = 3.7

# Using different rounding methods
ceil_result = math.ceil(x)  # Rounding up
floor_result = math.floor(x)  # Rounding down
trunc_result = math.trunc(x)  # Truncation of fractional part

print(ceil_result, floor_result, trunc_result)


# Using constants
print(math.pi)  # Prints an approximate value of π

# Trigonometry
angle = math.radians(60)  # Converting from degrees to radians
print(math.sin(angle))  # Sine of an angle

# Root
print(math.sqrt(9))  # Square root of 9

# Logarithms
print(math.log(10, 2))  # Logarithm of 10 to base 2


print(0.1 + 0.2 == 0.3)  # This return False
print(0.1 + 0.2)  # 0.30000000000000004

# The math.isclose function is used to compare two numbers with a certain tolerance.
r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # True


import math

r = math.isclose(0.1, 0.10000000009)
print(r)  #  True
