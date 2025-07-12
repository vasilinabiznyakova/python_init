# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10


# class PositiveNumber:
#     def __init__(self):
#         self.__value = None

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, new_value):
#         if new_value > 0:
#             self.__value = new_value
#         else:
#             print("Only numbers greater zero accepted")


# p = PositiveNumber()
# p.value = 1
# print(p.value)  # 1
# p.value = -1  # Only numbers greater zero accepted
# p._PositiveNumber__value = -1
# print(p.value)  # -1


# class PositiveNumber:
#     def __init__(self):
#         self.__value = None

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, new_value):
#         print(new_value)
#         if new_value > 0:
#             self.__value = new_value
#         else:
#             print("Only numbers greater zero accepted")


# p = PositiveNumber()
# p.value = 1
# print(p.value)  # 1
# p.value = -1  # Only numbers greater zero accepted
# p._PositiveNumber__value = -1
# print(p.value)  # -1


# class Person:
#     def __init__(self, name):
#         self.__name = None
#         self.name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         if (type(name) == str) and (len(name) > 0):
#             self.__name = name


# person = Person(123)
# print(person.name)  # None


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):


#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):


# class Point:
#     def __init__(self, x, y):
#         # Устанавливаем через сеттеры
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#         # Если хотя бы один из атрибутов остался None — обнуляем оба
#         if self.__x is None or self.__y is None:
#             self.__x = None
#             self.__y = None

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#         if isinstance(value, (int, float)):
#             self.__x = value
#         else:
#             print("x має бути числом (int або float)")
#             self.__x = None

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         if isinstance(value, (int, float)):
#             self.__y = value
#         else:
#             print("y має бути числом (int або float)")
#             self.__y = None


# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10


# point2 = Point(5, 10)
# print(point2.x)  # None
# print(point2.y)  # 10


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point ({self.x}, {self.y})"


# a = Point(1, 9)
# print(a)


# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello! I am {self.name}"


# bill = Human("Bill")
# bill_str = str(bill)
# print(bill_str)  # Hello! I am Bill


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point ({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)


# class Adder:
#     def __init__(self, add_value):
#         self.add_value = add_value

#     def __call__(self, value):
#         return self.add_value + value


# two_adder = Adder(2)
# print(two_adder(5))  # 7
# print(two_adder(4))  # 6

# three_adder = Adder(3)
# print(three_adder(5))  # 8
# print(three_adder(4))  # 7


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             new_x = value * self.coordinates.x
#             new_y = value * self.coordinates.y
#             return (new_x, new_y)
#         else:
#             return (self.coordinates.x, self.coordinates.y)

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# vector = Vector(Point(1, 10))

# print(vector())  # (1, 10)


# vector = Vector(Point(1, 10))

# print(vector(5))  # (5, 50)



class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        
        
        

    def __sub__(self, vector):
        
        
        

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    



vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)