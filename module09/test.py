# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# animal = Animal("Simon", 10)
# animal.change_weight(12)

# print(animal.weight)


# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name  # object variable
#         Person.count += 1 # class variable

#     def how_many_persons(self):
#         print(f"Количество людей сейчас {Person.count}")


# first = Person("Boris")
# first.how_many_persons()
# second = Person("Alex")
# first.how_many_persons()


# class Person:
#     count = 0

#     def __init__(self):
#         pass


# person = Person()
# print(person.count)  # 0


# class Person:
#     count = 0

#     def __init__(self):
#         self.count = 10


# person = Person()
# print(person.count)  # 10


# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color):
#         Animal.color = color


# first_animal = Animal("Pasha", 5)
# second_animal = Animal("Inigo", 7)

# first_animal.change_color("red")

# print(first_animal.color)
# print(second_animal.color)


# class Human:
#     name = ""

#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""

#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = "Bob"
# p_dev.voice()  # Hello! My name is Bob
# p_dev.make_some_code()  # My Programming language is Python

# js_dev = JSDeveloper()
# js_dev.make_some_code()  # My Programming language is JavaScript


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed

#     def say(self):
#         return "Meow"


# cat = Cat("Simon", 10, "british")
# print(cat.nickname)  # Simon
# print(cat.breed)  # british
# print(cat.weight)  # 10


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address


# class Cat(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)

#     def say(self):
#         return "Meow"


# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# cat = Cat("Simon", 10, "british", owner)


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address ):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#         owner_info = {
#             "name": self.name,
#             "age": self.age,
#             "address": self.address
#         }
#         return owner_info


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner

#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"

# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# class DogCat(Dog, Cat):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# from collections import UserDict


# class ValueSearchableDict(UserDict):
#     def has_in_values(self, value):
#         return value in self.data.values()


# as_dict = ValueSearchableDict()
# as_dict["a"] = 1
# as_dict.has_in_values(1)  # True
# as_dict.has_in_values(2)  # False


# from collections import UserList


# class CountableList(UserList):
#     def sum(self):
#         return sum(map(lambda x: int(x), self.data))


# countable = CountableList([1, "2", 3, "4"])
# countable.append("5")
# countable.sum()  # 15


# from collections import UserString


# class TruncatedString(UserString):
#     MAX_LEN = 7

#     def truncate(self):
#         self.data = self.data[: self.MAX_LEN]


# ts = TruncatedString("abcdefghjklmnop")
# ts.truncate()
# print(ts)  # abcdefg


import string


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print("Name is too short, need more than 3 symbols. Try again.")
    except NameStartsFromLowError:
        print("Name should start from capital letter. Try again.")
