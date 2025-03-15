""""Flow of execution one by one, from up to down
but there are 3 ways to control this behaviour:
1) conditional execution
num = 15

if num > 10:
    print("num > 10")
else:
    print("num =< 10")

To work with several conditions there is if ... elif ... else
Interpritator of Python find the closest condition can be executed, execute it and finish its work
Keep it in mind!

2) loops
3) exceptions
"""

# a = int(input("Enter any number "))
# if a > 0:
#     print("Number is positive")
# elif a < 0:
#     print("Number is negative")
# else:
#     print("Number is 0")


""""
Python has a mechanism for implicitly casting any type to bool.
The rules: 
"""

#1) num 0 is casted to False
# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")
# 2  None is casted to False
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None")

#3 Empty container, empty string is casted to False
# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")
#4 The rest is being casted to True

""""
Operator IS
checking if 2 obj refers to the same memory area, are they the same obj
mainly used for checking if variable is None or not 

Operator == is used when you need to know if value is same or not


Boolean algebra - It is a branch of mathematics that deals with the study of the truth of expressions and their processing. 
Boolean algebra is built on three basic operations: "and", "or", and "not".
AND: True returned if both conditions are True
OR: True returned if one of opernads is True
NOT: unary operation that returns inverted value
Python uses not, and, or
if you need several conditions to be checked use <and>
"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

my_var = None
if my_var is None:
    print("Only one obj exist for None")
    
print(a is b)  # True
print(a is c)  # False

print (a == b)  # True
print (a == c)  # True


name = "Taras"
age = 22
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")
