"""
Association offers an alternative to inheritance that can avoid some of its drawbacks. Association in OOP is a concept that describes the relationship between classes through their objects. In this context, a class can include another class as one of its fields, which is described by the word "has".
Association is divided into two main types: composition and aggregation, each of which has its own characteristics and applications.

aggregation - is a type of relationship between objects that also represents a "whole" to "part" relationship, but in this case the "parts" can exist independently of the "whole." This means that if the "whole" is destroyed, the "parts" can continue to exist independently.

composition -  a type of relationship between objects where one object is a part of another. In a composition relationship, the "part" cannot exist without the "whole." This means that if the "whole" is destroyed or removed, the "part" will also be destroyed or removed.
Let's imagine that we are developing a project management software. In this system, each "Project" (Project class) can contain several "Tasks" (Task class), and these tasks have no meaning outside the context of their project. If a project is deleted, all its tasks must also be deleted.
"""

# example for aggregation
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info())
print(cat.get_info())


# example for composition
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()


# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()
