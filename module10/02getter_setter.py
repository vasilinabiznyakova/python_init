# class SimpleDict:
#     def __init__(self):
#         self.__data = {}
#     # The __getitem__ method defines how an object of a class should behave when accessing its elements by index or key. It takes a key or index as an argument and should return the value associated with that key or index.
#     def __getitem__(self, key):
#         return self.__data.get(key, "Key not found")
#     # The __setitem__ method defines how an object should behave when assigning a value to an item at a given index or key. It takes two arguments: the key (or index) and the value to be associated with that key.
#     def __setitem__(self, key, value):
#         self.__data[key] = value


# # Використання класу
# simple_dict = SimpleDict()
# simple_dict["name"] = "Boris"
# print(simple_dict["name"])
# print(simple_dict["age"])


from collections import UserList


class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(
                f"Item {item} must be between {self.min_value} and {self.max_value}"
            )

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)

    for el in [20, 22, 25, 27]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)

    print(temperatures)
