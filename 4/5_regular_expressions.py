# To work with regular expressions in Python, the re module is used.

"""
The main functions of the re module that we will consider below are:

re.search(pattern, string) - searches for the first occurrence of a pattern in a string.
re.findall(pattern, string) - finds all occurrences of a pattern in a string.
re.sub(pattern, repl, string) - replaces occurrences of a pattern with another string.
re.split(pattern, string) splits a string by a pattern.

re.search(pattern, string)
The Match object has properties and methods that are used to retrieve information about the search and the result:

Match.span() returns a tuple containing the start and end positions of the match.
Match.string returns the string passed to the function.
Match.group() returns the part of the string that was matched.

You can use the .group() method on this object to retrieve the matching part of the string.
"""

import re

text = "Learning Python can be fun."
pattern = "Python"
match = re.search(pattern, text) # Found: Python

if match:
    print("Found:", match.group())
else:
    print("Not found.")

text = "Вивчення Python може бути веселим."

pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Found:", match.group())  # Found: веселим


import re

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())


import re

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

print(match)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)


import re

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches)
import re

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches)



text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе список всіх слів у рядку
