# from collections import namedtuple

# """module collections has:
# 1. namedtuple options to create them
# 2. Counter to calculate how often particalar elements are being repeated
# 3. defaultdict The special defaultdict dictionary is a subclass of Python's dict dictionary, which is part of the collections module. This type of dictionary allows you to assign default values ​​to keys that do not already exist in the dictionary.
# """

# Point = namedtuple("Point", ["x", "y"]) # field names x and y

# p = Point(11, y=22)  # Creating a Point instance

# print(p)
# print(p.x)  # 11
# print(p.y)  # 22


# import collections

# # Створення іменованого кортежу Person
# Person = collections.namedtuple(
#     "Person", ["first_name", "last_name", "age", "birth_place", "post_index"]
# )

# # Створення екземпляра Person
# person = Person("Mick", "Nitch", 35, "Boston", "01146")

# # Виведення різних атрибутів іменованого кортежу
# print(person.first_name)
# print(person.post_index)
# print(person.age)
# print(person[3])


# import collections

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# cat = Cat("Simon", 4, "Krabat")

# print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")


# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)


# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)


# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(
#     student_marks
# )  # One of the most popular Counter methods is most_common(), which returns a list of elements and their frequency, starting with the most common ones.

# print(
#     mark_counts.most_common()
# )  # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]

# print(mark_counts.most_common(1))  # [(4, 4)]

# print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]


# from collections import Counter

# # Створення Counter з рядка
# letter_count = Counter("banana")
# print(letter_count)


# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")


# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# print(word_count)
# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")


from collections import defaultdict

# Create defaultdict with list as default factory

d = defaultdict(list)

# Append elements to list for each key
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)

print(d)


words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)


# same result with less code
from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
