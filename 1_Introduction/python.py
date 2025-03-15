# age = float(input("Enter your age with float"))
# age = 4*age
# print(f'age {age}')
my_list = []
my_list.insert
# my_list = list()
# empty_list = [1]
# empty_list.append(1)
# print(empty_list)

# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)  # Виведе ['apple', 'banana', 'cherry']
# words.sort(reverse=False)
# count = words.count("apple")
# index = words.index('banana')
# print(index)

# some_iterable = ["a", "b", "c"]
# last_letter = some_iterable[-1]
# print(last_letter)
#Словник — це контейнер, який зберігає пари ключ-значення.
# Ключем може бути будь-який незмінний тип даних Python (число, рядок, кортеж тощо)
#if we write down the same key, the set will leave the last one key - value pair
my_dict = {"key": "value"}
print(my_dict["key"])
# to get keys
print('keys', my_dict.keys())
print('values', my_dict.values())
print('items', my_dict.items()) #key-value pairs type tuple
#Щоб змінити значення або додати нову пару ключ-значення, використовуйте ключ для присвоєння нового значення
# my_dict["key"] = "new value"
# my_dict["new key"] = "additional value"
# print(my_dict)
# del my_dict["key"]
# print(my_dict)
# print("key" in my_dict) #searching by key
# print("additional value" in my_dict)
#******Методи словників**************
#*** pop() => delete el by key****
# my_dict = {"age": 40, "name": "Vasilina"}
# print(my_dict)
# my_dict.pop("age")
# print(my_dict)
#**** update() => update dictionary by new pair key/value or by new dict****
# my_dict = {"name": "Alice", "age": 25}
# my_dict.update({"email": "alice@example.com", "age": 26})
# print(my_dict)
#*** clear() => delete everything from dict ***
# my_dict = {"age": 40, "name": "Vasilina"}
# my_dict.clear()
# print(my_dict)
#*** get() => get by key, no error if nothing is found it will return None ***
# my_dict = {"name": "Alice", "age": 25}
# result = my_dict.get("name")
# print(result)

# non_existing_result = my_dict.get("something")
# print(non_existing_result)

#if you getting value by [] and it doesn't exist in dict, it will throw KeyError
# my_dict = {"name": "Alice", "age": 25}
# result = my_dict["name"]
# print(result)

# non_existing_result = my_dict["something"]
# print(non_existing_result)
# !!!!!! more preferable to use get as it doesnt call error and more flexible

#******Множини = SETS**************

#Множини — це неврегульований контейнер, який містить тільки унікальні елементи. Саме для цього вони і використовуються. У множину можна додавати тільки незмінні типи даних.
# Щоб створити порожню множину, потрібно викликати функцію set(). Не приймають списки
# empty_set = set()
#Множини не мають визначеного порядку елементів. Ви не можете звернутися до елементів множини через індекс або отримати їх у певному порядку.
#Для створення заповненої множини достатньо передати будь-який об'єкт, що ітерується, у функцію set
#Унікальність множини передбачає, що якщо множина вже містить такий елемент, то спроба додати ще один такий самий нічого не змінить.
# a = set('hello')
# print(a)
# usage case is when we should fast delete duplicates for example from list
# lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
# d_list = set(lst)
# lst = list(d_list)
# print(lst)
# #methods of sets
# # add(elem) 
# d_list.add(5)
# print(d_list)
# # remove(elem) if element doesnt exist it will throw exception
# d_list.remove(1)
# # d_list.remove(10)
# # discard(elem)  if element doesnt exist wont throw exception
# d_list.discard(10)

#******Математичні операції над множинами**************

a = {1, 2, 3}
b = {3, 4, 5}

#to find intersections of 2 sets -> method intersection or operator &
# print(a & b)
# print (a.intersection(b))

#to find differences -> method difference or operator -
print(a.difference(b))
print(a - b)

#symetric difference is all elements which exist in one set and doesnt exist in other -> sy
# include all elements from 1 set and 2 set exept same
# symmetric_difference or operator ^.

print(a.symmetric_difference(b))
print(a ^ b)

#join to sets wo duplicates -> union or |

print (a.union(b))
print (a | b)

#frozensets can not be changed
# still can be done operations which doesnt change set like union, intersection, difference, symmetric_difference
# can be created by fuction frozenset()
my_frozenset = frozenset([1, 2, 3])

#******Tuples*************
# similar to lists but can not be changed, tuple use (), list use []
#create tuple can be done with () or wo them
#!Important if you want create tuple with 1 el, coma must be set after this element my_tuple = (1,)
# it happens because Python uses ( ) as mathematic symbols
#Tuple can contain different types elements
#access to elements done by indexes
# Usage: 
# 1. storing a set of constants or when a function returns multiple values.
# 2. dictionary keys, since the keys must be immutable
#the main difference between tuples and lists is mutability, structure is the sam
#but if in tuple one of el is list then the el inside list can be changed

my_tuple = (1, 2, 3)
my_tuple2 = 1, 2, 3
my_tuple_el = my_tuple[0]
print(my_tuple_el)

print("DEBUG", my_tuple.count(2)) #count el q-ty

#****String methods*****
#String is immuatable ordered sequence of characters in some encoding. Def encoding UTF-8
#this is collection of characters
#to create string must include certain set of characters in quotes or double quotes
# you can refer to elements by index
s = "Hello world!"
print(s[0])# H
print(s[-1])# !

#methods:
#1 upper case
s = "Hello world!"
print(s.upper())

#2 lower case
s = "Hello world!"
print(s.lower())

#3 check if string starts with a substring
s = "Hello world!"
print(s.startswith('He')) #True

#4 check if string ends with a substring, used for checking files extentions
s = "hello.jpg"
print(s.endswith('jpg'))

#5 capitalize 1st letter
s = "hello world".capitalize()
print(s) #Hello world


#6 capitalize 1st letter of every substring

s = "hello world".title()
print(s) #Hello World

#7 if string consist of digits, letters
"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True

#8 split devide the string by space
s = "Hello Shiny world"
list_s = s.split()
print("split method", s.split())

#9 join is called for devider
print("join by _", "_".join(list_s))

#10 isalpha check if string is only letters, if any spaces it will return False
print("method isalpha","S123".isalpha())

#11 isalnum check if string is only letters&num
print("method isalnum","S123".isalnum())

#12 isnumeric check if string is only num
print("method isnumeric","S123".isnumeric())

#13 isidentifier()


#****String formatting*****
#Introduced in Python 3, .format() allows flexible formatting.
name = "Bob"
age = 30
formatted_string = "My name is {} and I am {} yo".format(name, age)
print(formatted_string)
#Positional arguments
print("Hello, {1}! My name is {0}.".format("Alice", "Bob"))
#Named arguments
print("Hello, {name}! You are {age} years old.".format(name="Charlie", age=22))
#Number Formatting
print("Pi is approximately {:.2f}".format(3.1415926535))

# Using f-strings (Python 3.6+)
name = "David"
age = 40
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)


# Python Slices
#sequence[start(i):end(e):step] //все може бути відємним навіть крок, можна використовувати змінні
#if start not noted by default from index 0
# end - index of last el but not include it to slice, by default till the end of sequences
# step by def is 1 if not noted
# slices can be used to create copy of lists [::]



s = "Hello, World!"
first_five = s[:5]
print(first_five) #Hello

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:10:2]) #odd_numbers
print(numbers[1::2]) #even_numbers
print(numbers[2:10:3]) #three_numbers


#We can use negative indices in slices, it can replace reverce method

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)

'''
we can use 0.5 and .5 in Python means the same
we can 
a = '5'
b = '5'
result = a + b #will be 25
'''


'''
casting types привеення типів
instruction is every line of code, степ логічний
expression то коли ми задэм значення a = 1 + 2 то є будь який рядок де відбуваеєтьс присвоєння значення змінній
'''
# True  False
# 1000  0
# "asd" ''
#        None

#при видаленні зі списку 1 видалить спочатку 1 а потім False бо намагається привести його до цифри

a = '5'
b = '5'

print(type(a + b))
print(type(int(a) + int(b)))
a = 5
b = 10
b+=a # збільшення на а 
b-=a
b + a # логічна операція

list = [1,2,'a'] #list, order is always saved, can be changed
print(type(list))
print(list[-1])
print(list.pop()) #last el
print(list[len(list)-1]) #lengh of list and

#for lists if we create one list and assign its value to another list
# change one of el it will be change in both
# we would need to use copy to create new list but copy doesnt do deep copy (if inside list [] it will still be passed by link, it means that if we change el in one of them it will be changed in both!!!![], if we need copy of children elements we need do it separately) 

some_list  = [1, 2, 3, [1, 2, 3]]
some_list2 = some_list
some_list[0] = 10
print(some_list)
print(some_list2)

some_list  = [1, 2, 3, [1, 2, 3]]
# some_list2 = some_list.copy()
# some_list2[-1][2] = 5
# print(some_list)
# print(some_list2)


#in practice usually do like this:

some_list2 = some_list[:]
print(some_list2)


#is ASKI - це тільки латиниця

""""
Парадигми програмування:
1. Функціональна
Функциональная парадигма программирования — это подход к написанию кода, в котором программы строятся из функций. Главное в этом подходе:

1) Функции как математические — функции принимают входные данные и возвращают результат без побочных эффектов (то есть, не меняют глобальные переменные, не пишут в файлы и т. д.).
2) Избегание изменения данных — вместо изменения существующих данных создаются новые.
3) Функции — граждане первого класса — функции можно передавать как аргументы, возвращать из других функций, хранить в переменных.
4) Декларативность — код описывает, что нужно сделать, а не как (например, map, filter, reduce вместо циклов).

2. Процедурна

Процедурная парадигма программирования — это подход, в котором программа строится из последовательности команд (инструкций), сгруппированных в процедуры (функции).

Основные принципы:
Последовательность шагов – код выполняется сверху вниз, строка за строкой.
Разбиение на процедуры (функции) – для повторяющихся действий создаются функции, чтобы не дублировать код.
Изменяемое состояние – переменные можно изменять в ходе выполнения программы.
Использование циклов и условий – for, while, if-else и другие конструкции управляют потоком выполнения.

3. ООП

Объектно-ориентированное программирование (ООП) — это парадигма программирования, в которой программа строится из объектов, объединяющих данные (свойства) и логику (методы).

🔹 Основные принципы ООП:
Классы и объекты – класс — это шаблон, а объект — это экземпляр класса.
Инкапсуляция – объединение данных и методов в объекте, скрытие деталей реализации.
Наследование – возможность одного класса унаследовать свойства и методы другого.
Полиморфизм – способность объектов разных классов использовать один интерфейс.

Да, можно и часто нужно использовать все парадигмы вместе! Это называется многопарадигменное программирование.

4. Декларативная

Чаще всего в пайтоне используется объектно-ориентированное программирование
"""


print(0.1+0.2) #0.30000000000000004

print(1-0.9) #0.09999999999999998
""""
386 архітектура процессора дає неточності при роботі з числами
Такие результаты связаны с представлением чисел с плавающей запятой (floating-point) в памяти компьютера.

🔹 Почему так происходит?
Компьютер хранит числа в двоичной системе

Десятичные дроби (например, 0.1, 0.2, 0.9) не всегда имеют точное представление в двоичной системе.
Например, 0.1 в двоичной системе — это бесконечная дробь:
Copy
Edit
0.1 (десятичное) = 0.0001100110011001100110011... (двоичное)
При округлении теряется точность, что и приводит к небольшим ошибкам.
IEEE 754 – стандарт хранения чисел с плавающей запятой

Числа хранятся в приближенной форме, из-за чего могут возникать небольшие ошибки при вычислениях.
🔹 Как избежать таких ошибок?
❗ 1. Округление с round()

python
Copy
Edit
print(round(0.1 + 0.2, 2))  # 0.3
print(round(1 - 0.9, 2))    # 0.1
🔹 round(value, n) округляет число до n знаков после запятой.

❗ 2. Использование decimal для точных расчетов Если требуется максимальная точность (например, в финансовых расчетах), используй decimal.Decimal:

python
Copy
Edit
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("1") - Decimal("0.9"))    # 0.1
🔹 Преимущество – decimal хранит числа в точном десятичном формате.

❗ 3. Использование fractions для дробей Для работы с дробями можно использовать модуль fractions:

python
Copy
Edit
from fractions import Fraction

print(Fraction(1, 10) + Fraction(2, 10))  # 3/10
print(float(Fraction(1, 10) + Fraction(2, 10)))  # 0.3
🔹 Полезно, если работаешь с дробными числами без необходимости округления.

🔥 ARM не решит проблему, потому что она связана с самим принципом хранения чисел, а не с конкретной архитектурой процессора.
"""