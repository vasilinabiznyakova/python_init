# users = ["\nOleh", "\nAlina", "\nMax"]
# with open ("users.txt", mode = "rb") as file: # reading is done by symbols so read and move cursor
#     print(file.read())
# data = file.read(5)
# print(data)
# print(file.tell()) #6
# data = file.read(5)
# print(data)
# print(file.tell()) #11
# file.seek(0)
# print(file.tell()) #0


# context manager will close file anyway and this is the best practice
# age = 30
# name = "addd"
# try:
#     info = name + age
# except TypeError as e:
#     print(e)

# file.write("\nzzzz") # to append from new line

# pass

# file will be created in the directory you run the script

# mode = "w" will recreate the file
# mode = "a" will add to file new content
# mode = "x" create file if not esxist if exist will give exception

# def factorial(n):
#     if n == 1:
#         return n

#     return n * factorial(n - 1)

from pathlib import Path

# def parse_folder(path):
#     for el  in path.iterdir():
#         if el.is_dir():
#             parse_folder(el)
#             print (f"This is folder {el}")
#         else:
#             print(f"This is folder {el}")

# parse_folder(Path("."))