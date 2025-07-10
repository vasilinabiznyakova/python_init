class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()

        # Приклад логування
        print(
            f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}"
        )

    def say_hello(self) -> str:
        return f"Hello! I am {self.name}"

    def __check_adulthood(self) -> bool: # this is private method
        return self.age >= 18


bill = Human("Bill")
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")

jill = Human("Jill", 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")


# __str__ and __repr__ methods

# __repr__ is intended to create a formal string representation of an object.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


original_point = Point(2, 3)
print(repr(original_point))

# Використання рядка, повернутого __repr__, для створення нового об'єкта
new_point = eval(repr(original_point))
print(new_point)


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human = Human("Alice", 30)
print(human)
