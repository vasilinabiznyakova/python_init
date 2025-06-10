"""
The re.split() function in Python's re module is used to split a string based on a given regular expression.
 This allows you to split text into parts based on more complex criteria than the simple string split() method.
 import re

list_of_elements = re.split(pattern, string)
"""


import re

text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)  # Виведе список слів у рядку
