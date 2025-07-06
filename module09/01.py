# class User:
#     name = 'Anonymous'
#     age = 15

# user1 = User()
# print(user1.name)
# print(user1.age)

# user2 = User()
# user2.name = "John"
# user2.age = 90

# print(user2.name)


# class MyClass:
#     def __init__(self, value): # Any class method must always have at least one argument self, this is a requirement of Python syntax,
#         self.instance_field = value  # Поле класу


# obj1 = MyClass(5)
# obj2 = MyClass(10)


# print(obj1.instance_field)
# print(obj2)


# class Person:
#     def __init__(self, name: str, age: int): # The __init__() method is a special constructor method that is automatically executed when each new instance of the Person class is created.
#         self.name = name
#         self.age = age

#     def say_name(self) -> None:
#         print(f"Hi! I am {self.name} and I am {self.age} years old.")

#     def set_age(self, age: int) -> None:
#         self.age = age


# bob = Person("Boris", 34)

# bob.say_name()
# bob.set_age(25)
# bob.say_name()


# object field and class attribute


# class Person:
#     count = 0

#     def __init__(self):
#         self.count = 10


# person = Person()
# print(person.count)  # 10
# person.count = 12

# print (person.count) # 12
# print(Person.count)  # 0


# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack(self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form


# # Створення об'єкта Pikachu
# pikachu = Pokemon("Pikachu", "Electric", 100)

# # Використання методів
# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")


"""
Conceptions OOP

1. Encapsulation - hiding the internal structure of a class and protecting its data from direct access from the outside. Is implemented through the usage of attibutes and methods:
- public - accessible to outside the class
- protected - accessible to the class and derived class
- private  - not accessible outside the class

But need to note that in fact all of them are changeable in Python but it considered to be bad practice
2. Inheritance
Inheritance is an OOP mechanism that allows one class to inherit properties and methods from another class. In Python, this is done by declaring a class that "inherits" from another class.

A base or superclass is a class from which properties and methods are inherited.

A derived or subclass is a class that inherits properties and methods from a base class.
3. Polymorfism

Polymorphism is one of the key concepts of OOP, which allows objects to have different forms or behaviors based on their types.
**Duck Typing** is a concept in programming that plays an important role in dynamically typed languages like Python. The name comes from the English saying: *“If it walks like a duck and quacks like a duck, then it’s probably a duck.”*

In the context of programming, **duck typing** means that instead of checking an object's type before using it, it's more important to focus on whether the object has the necessary methods or properties required to perform a specific function or operation.


4. Abstraction

"""
# ____________________Encapsulation_______________________

class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active  # this is protected and in order to change it we are supposed to use method

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):  #  change protected attribute it we are supposed to use method
        self._is_active = active


p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin  # Attributes that are considered private are denoted by two underscores __ and cannot be accessed directly from outside the class.

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True, False)
# print(p.__is_admin)  # AttributeError: 'Person' object has no attribute '__is_admin'


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True, False)
print(p._Person__is_admin) # no error


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin


p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())


# ____________________Inheritance_______________________


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"

# Derived classes can define their own constructors. If we want to preserve the behavior of the base class and add new properties, we can use the super() construct to call the base class constructor.

class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self):
        return "Woof"


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):

    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_cow.make_sound())  # Виведе "Moo"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"


# _____________Multilevel inheritance and  Method Resolution Order (MRO)

# you can inherit from several classes but what if they have same attributes with the same names

"""
MRO (Method Resolution Order) in Python works as follows:
It looks for the attribute in the class itself. This is why you can "override" attributes from parent classes.
It searches for the attribute in the first parent (the one listed first in the inheritance list).
It searches in the next parent in the list, continuing as long as there are parents left.
It searches in the parents of the first parent.

It repeats step 4 for all parents.

If the attribute is still not found, an exception is raised.
The search stops as soon as the attribute is found.
"""

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return "Chirp"


class Parrot(Bird):
    def can_fly(self):
        return True


class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"


my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))


# ____________________Polymorphysm ana duck typing______________________
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
