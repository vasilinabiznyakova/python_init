"""
Used to implement repeated actions
there are 2 types: 
1) for
2) while
for used for iterations by elements of any order, list, tuple, string etc.
for element in sequence:
#do actions with elements
while execute block of code untill condition is True, once condition is False the loop breaks
while condition:
    # block of code for execution
    for in dict will iterate keys this way we can change values by this
"""

# fruit = 'apple'
# for char in fruit:
#     print(char)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")


# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)


# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

# k = 0
# while k < 10:
#     k += 1
#     print(k)

"""
"Infinite loops" and break
Infinite loops are often used where you need to interact with the client, waiting for input from them, and only ending when some condition occurs.
"""
# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

"""
Ending an iteration with continue
"""

a = 0

while a < 6:
    a += 1
    if not a % 2 :
        continue
    print(a)
for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} even.")
    else:
        print(f"{i} odd.")

"""
Extending the capabilities of the for loop:
- range
range(stop): Creates a sequence of numbers from 0 to stop - 1
range(start, stop): Generates numbers from start to stop - 1
range(start, stop, step): Creates numbers from start to stop - 1, with a step of step.
- enumerate
used when you need to get access to index
enumerate(sequence, start = 0)
- zip
The zip function is used to iterate over multiple iterables at once. It zips up the elements from each iterable, creating tuples of those elements
"""
#range examples
for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)

# enumerate function examples 

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


# zip function example
list1 = ["green", "tasty", "red"]
list2 = ["apply", "cherry", "tomato"]
for number, letter in zip(list1, list2):
    print(number, letter)

#if collections have different length they stop when the shortest one is finished 
list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d", "e"]
for number, letter in zip(list1, list2):
    print(number, letter)


# loops and dictionaries
# dictionary is iterated container
print("loops and dictionaries: ")

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)

# this is the same as above
for key in numbers.keys():
    print(key)


for val in numbers.values():
    print(val)

# so dictionaries have stucture d.keys() and d.values()
#to iterate over the key-value pairs of a dictionary, we need to use the items method. At each iteration, we will get a (key, value) pair


for key, value in numbers.items():
    print(key, value)


#!!!!! Important while you iterate thorugh dictionary you can not remove elements from dictionary, you can not add anything from dictionary but you still can change values if you iterate by keys


n = None
while n is None: # crucial important to use the checking like this
    a = input("Enter number: ")
    if a.isnumeric():
        n = int(a)
print(n)
print(type(n))


# while True: # used so that the action is executed constantly