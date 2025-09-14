import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)# Output: array([1, 2, 3, 4, 5])


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr + 2)# Output: array([3, 4, 5, 6, 7])


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)# Output: array([5, 7, 9])

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)


my_list = [1, 2, 3, 4, 5]
print(my_list)# Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)# Output: [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3, 5]
my_list.insert(3, 4)# Insert number 4 at position 3
print(my_list)# Output: [1, 2, 3, 4, 5]


my_list = [1, 2, 3, 4, 5]
my_list.remove(3)# Removes number 3 from the list
print(my_list)# Output: [1, 2, 4, 5]


my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)# Output: [1, 1, 2, 3, 4, 5, 9]


my_dict = {'name': 'John', 'age': 25}
print(my_dict)# Output: {'name': 'John', 'age': 25}

my_dict = {'name': 'John', 'age': 25}
print(my_dict['name'])# Output: John

my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict)# Output: {'name': 'John', 'age': 25, 'city': 'New York'}


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
print(my_dict)# Output: {'name': 'John', 'age': 25}


my_set = set([1, 2, 3, 4, 5])
print(my_set)# Output: {1, 2, 3, 4, 5}


my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)# Output: {1, 2, 3, 4, 5, 6}


my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set)# Output: {2, 3, 4, 5}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))# Output: {4, 5}
print(set1.difference(set2))# Output: {1, 2, 3}
print(set1.symmetric_difference(set2))# Output: {1, 2, 3, 6, 7, 8}

# Stack works by principle Last In First Out (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None


s = Stack()
s.push("a")
s.push("b")
s.push("c")
print(s.peek())  # 'c'
print(s.pop())  # 'c'
print(s.peek())  # 'b'
print(s.is_empty())  # False


# Queue  FIFO (First In First Out)
from queue import Queue

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue)# Output: deque(['a', 'b', 'c'])

# Видаляємо елемент
q.get()
print(q.queue)# Output: deque(['b', 'c'])


from queue import Queue
import random


class Client:
    def __init__(self, name: str):
        self.name = name
        self.operations = random.randint(1, 5)  # Випадкова кількість операцій


class Bank:
    def __init__(self):
        self.clients: "Queue[Client]" = Queue()

    def new_client(self, client: Client) -> None:
        self.clients.put(client)

    def serve_clients(self) -> None:
        while not self.clients.empty():
            current_client = self.clients.get()
            print(
                f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операціями"
            )
            # Тут можна додати час обслуговування та іншу логіку


# Створюємо банк
bank = Bank()

# Додаємо клієнтів
for i in range(5):
    bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
bank.serve_clients()


from collections import deque

d = deque()
print(d)  # deque([])


d.append("right")
d.appendleft("left")
print(d)  # deque(['left', 'right'])


d.pop()
d.popleft()
print(d)  # deque([])


d.extend(["a", "b", "c"])
d.extendleft(["x", "y", "z"])
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])


# The operation of wrapping (rotation) in the context of a drawing indicates the process of moving the first element of the drawing to its end, which is also similar to a cyclic connection

d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

# LinkedList
# This is the structure of the data as it consists of nodes. Kozhen vuzol place the element of data and vkazivnik (link) to the next node in the list. This data structure is dynamic, so its size can change during program development.


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.head: "Node | None" = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: "Node", data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        # Якщо видаляємо голову
        if cur and cur.data == key:
            self.head = cur.next
            return
        # Шукаємо вузол з ключем
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        # Не знайдено
        if cur is None:
            return
        # Обходом прибираємо вузол
        prev.next = cur.next

    def search_element(self, data) -> "Node | None":
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)
    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)
    else:
        print("Елемент не знайдено")


# Chat lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None
        self.prev: "Node | None" = None


class DoublyLinkedList:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    # Додавання вузла на кінець списку
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            assert self.tail is not None
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Додавання вузла на початок списку
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    # Додавання вузла після заданого вузла
    def insert_after(self, prev_node: "Node", data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    # Додавання вузла перед заданим вузлом
    def insert_before(self, next_node: "Node", data):
        if not next_node:
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def remove(self, data) -> bool:
        current_node = self.head
        while current_node:
            if current_node.data == data:
                # знімаємо з ланцюжка
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                # повне від'єднання
                current_node.prev = None
                current_node.next = None
                return True
            current_node = current_node.next
        return False

    def search(self, target_data) -> "Node | None":
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.next
        return None


import hashlib
import os


def get_hash(path):
    """Повертає хеш-значення для файлу."""
    with open(path, "rb") as file:
        bytes = file.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash


def find_duplicates(directory):
    """Шукає дублікати в директорії."""
    hashes = {}
    duplicates = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicates.append((path, hashes[file_hash]))
    return duplicates


# Пошук дублікатів у заданій директорії
duplicates = find_duplicates("/path/to/directory")
for duplicate in duplicates:
    print(f"Дублікатні файли: {duplicate[0]} та {duplicate[1]}")


import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо вершини
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Додаємо з'єднання
G.add_edge("A", "B")
G.add_edge("B", "C")

# Задаємо розташування вершин
positions = {"A": (0, 0.5), "B": (1, 0.5), "C": (2, 0.5)}

# Малюємо граф
plt.figure(figsize=(6, 6))
nx.draw_networkx(
    G,
    pos=positions,
    with_labels=True,
    font_weight="bold",
    node_color="lightblue",
    edge_color="gray",
)
plt.axis("off")
plt.show()
