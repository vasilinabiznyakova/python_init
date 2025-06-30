"""Comprehensions in Python are a way to compactly create collections based on existing collections. Python supports several types of comprehensions: list comprehensions, set comprehensions, and dictionary comprehensions. They allow you to write expressions to create new collections with less code than using loops.
"""
# List Comprehensions
# [new_item for item in iterable if condition]
sq = [x**2 for x in range(1, 6)]
print(sq)


# Set Comprehensions
# {new_item for item in iterable if condition}
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i**2 for i in numbers}
print(sq)


# Dictionary Comprehensions
# {key: value for item in iterable if condition}

sq = {x: x**2 for x in range(1, 10)}
print(sq)
