def say_hello(name):
    print(f"Hello {name}")


def main():
    print("You imported hello.py")
    say_hello("user")


if __name__ == "__main__":
    main()


# if the script is called directly, it is the "entry point" and __name__ == "__main__".


import sys

print(sys.modules["os"])


# print(sys.modules.keys())
# print(sys.builtin_module_names)
# print(sys.path)


for arg in sys.argv:
    print(arg)


"""

The __init__.py file is a service file that the interpreter will execute the first time the package is imported.
"""
