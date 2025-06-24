"""
2 ways to import:
import math
from math import pi, sin
"""
# import some_test_module

# print(some_test_module.say_hello("World"))

# from some_test_module import say_hello as greeting # its called alias

# print(greeting("Vas"))

"""
Search Priority	Location
1️⃣ Current working directory	.
2️⃣ Directories in PYTHONPATH	(if set)
3️⃣ Standard library	/Lib/
4️⃣ Installed packages	/site-packages/
"""


# dir() used to get a list of attributes (including methods) of an object or module

from some_test_module import say_hello as greeting

# returns a list of defined names in a namespace.
# With no arguments, it produces an alphabetically sorted list of names in the current local symbol table
# print(
#     dir()
# )  # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greeting']


print(greeting("World"))


print(dir())


