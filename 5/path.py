"""
The pathlib module in Python is a modern filesystem tool that provides an object-oriented interface for working with paths.
It replaces the deprecated os module, which is still used in older code examples.
The two main classes in this module are Path and PurePath.
PurePath is a base class in pathlib that provides object-oriented methods for manipulating paths without accessing the file system. It can be used to work with paths on various operating systems. PurePath allows you to perform operations such as splitting a path into parts, checking suffixes, filenames, paths, etc.
"""
from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix:", p.suffix)
print("Parent:", p.parent)


from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text())  # Hello, world!
print("Exists:", p.exists())  # Exists: True


# Initial path
base_path = Path("/usr/bin")

# Adding additional parts to the path
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Print: /usr/bin/subdir/script.py


# Converting a relative path to an absolute one

relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)


# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()

# current_working_directory = Path(
#     "E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04"
# )
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)


# Початковий шлях до файлу
original_path = Path("example.txt")

# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)

# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")


# Створення об'єкту Path для файлу
file_path = Path("example.txt")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)


# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Бінарні дані для запису
data = b"Python is great!"

# Запис байтів у файл
file_path.write_bytes(data)


# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)
