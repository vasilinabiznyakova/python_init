# Collection - a program object (change container) that saves the set of values ​​of one or different types.
# The main properties of collection are:
# - Order
# - Changeability
# - Uniqueness
# Types:
# - Lists (Ordered collections that can contain elements of any type)
# - Tuples (same as lists but you can not change it after it was created)
# - Dictionaries (Collections of key-value pairs, key is unique)
# - Sets (Unordered collections of unique elements. Use wiki to remove duplicates)
# - Frozen Sets (can not be changed)

# my_list = [1, 2, 3]
# print(my_list)
# my_list_id = id(my_list)
# print(my_list_id)
# my_list.append(10)
# print(my_list)
# print(id(my_list))

# print(my_list[2])
# print(my_list[-1]) # the last element of the list

chars = ['a', 'b', 'c']


last = chars.pop(1)
print(chars)
print(last)


chars = ['a', 'b', 'c']
numbers = [1, 2]

chars.extend(numbers)

print(chars)

chars = ["a", "c"]
chars.insert(5, "ffff")
print(chars)
print(chars[2])
chars.clear()
print(chars) # []


chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')

print(c_ind)

count = chars.count("a")
print(count)

# sort will change the original list if you need to save original order you need use sorted
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # print [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)
print(nums)  # print [9, 5, 4, 3, 2, 1, 1]


nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # print [1, 1, 2, 3, 4, 5, 9]
print(nums)  # print [3, 1, 4, 1, 5, 9, 2]

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # print [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # print ['apple', 'banana', 'cherry']

chars =  ['a', 'b']
chars_copy = chars.copy()

print(chars_copy)
print(id(chars_copy))
print(id(chars))

chars = ["banana", "apple", "cherry"]
chars.reverse()
print(chars)

# dictionaries

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # print 'Alice'

# add new key - value
my_dict["age"] = 41  # change age to  41
my_dict["email"] = "alice@example.com"  # add new pair key-value
print(my_dict)


# check if key in dict 
print("name" in my_dict)
print("age" in my_dict)


# methods

# pop() - removes key-value by key and return value
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age") 
print(age) # 25
print(my_dict) # {'name': 'Alice'}

# update() if same key with new value added it will update value by key

my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26})
print(my_dict) # {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# clear() removes all dictionary elements
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()
print(my_dict)

#copy()  creates a shallow copy of the dictionary

# get() get value by key, if no key found will return None
my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Return 25
gender = my_dict.get("gender")  # Return None, as no "gender" in dictionary

print(age)
print(gender)


name = my_dict["name"]  # return 'Alice'
# gender = my_dict["gender"]  # KeyError: 'gender'



# Sets - unordered container that contains only unique elements. Often used to remove duplicates

empty_set = set()
a = set('hello')
b = {1, 2, 3, 4, 5}

print(a)
print(b)

# Methods
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}


numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}


numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

# Mathematical operations on sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}


a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}



a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5} all exept common elements
print(a ^ b)  # {1, 2, 4, 5}


# all elements from both sets exept duplicates
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

# can not be changed after being created (add, remove not possible but union, intersection, difference, symmetric_difference)
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})



# Tuples same as list but can not be modified

my_tuple = tuple() # or
my_tuple = ()
my_tuple = (1, 2, 3)


# Important!!! if you want to create tuple with 1 element need to put coma otherwise you will get just regular var

my_tuple = (1,)
my_tuple_test = (1)

print(my_tuple)
print(my_tuple_test)

# can contain different data types
my_tuple = (1, "Hello", 3.14)
print(my_tuple)

# get element by index
first_item = my_tuple[0]  # get first el
print(first_item)

#String methods
# String -  fixed ordered sequence of characters in some encoding. The default encoding is UTF-8. Immutable

s = "Hello world!"
print(s[0])# H
print(s[-1])# !


s = "Hello world!"
# s[0] = "Q"# TypeError: 'str' object does not support item assignment

# Methods

s = "Hello" 
print(s.upper()) # Print 'HELLO'

s = "Some Text"
print(s.lower())  # print 'some text'

s = "Bill Jons"
print(s.startswith("Bi"))  # Print True

s = "hello.jpg"
print(s.endswith("jpg"))  # print True

s = "hello world".capitalize()  # result: "Hello world"
print(s)

s = "hello world".title()  # result: "Hello World"
print(s)

print("123".isdigit())  # True
print("hello".isalpha())  # True
print(" ".isspace())  # True


#formatting strings

# method format

# Simple row format
name = 'John'
print('Hello, {}!'.format(name))

# Formatting with multiple arguments
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Using named arguments
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Using subscripts to specify the order of arguments
print('Hello, {1}. You are {0} years old.'.format(age, name))



# Slice
#fragment creation in Python is a powerful mechanism for accessing parts of sequences, such as arrays, ordered arrays, and tuples
# start — the index of the element from which the slice begins. If it is not specified, the slice starts from the beginning of the sequence, at 0.
# end — the index of the element to which the slice goes, but attention!, not including it. If it is not specified, the slice goes to the end of the sequence.
# step — defines the step with which elements are selected. If not specified, step 1 is used.

s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Print 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
print(odd_numbers) # Print [1, 3, 5, 7, 9]

odd_numbers = numbers[::2]  # Print [1, 3, 5, 7, 9]

even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]
print(even_numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)

# list copy
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)
