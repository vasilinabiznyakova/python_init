"""
Functions are the way of grouping code that do exact task

Function created with the help of keyword def

def say_hello():
		# body
    print('Hello world')

# End of function say_hello()

# function execution
say_hello()

# unction execution
say_hello()


Function arguments
Some data that can be passed to function when its being executed

Parameters of function is those name that noted when function is declared

Typing function parameters

!!! In Python, starting with version 3.5, you can use "type hints" to indicate the expected types of parameters. This makes your code more understandable and can help you spot potential errors.

Return result is done by operator return 

Procedure and function the difference is that procedure do not return anyhting, while fucntion returns
basic synth
def my_function() -> ReturnType:
    # do something
    return result


"""

def print_max(a: int, b: int):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'equal', b)
    else:
        print(b, 'max')

print_max(3, 4)  # direct transfer of values

x = 5
y = 7
print_max(x, y)  # passing variables as arguments



def add_numbers ( num1: int, num2: int ) -> int:
    sum = num1 + num2
    return sum
result = add_numbers(5, 10)
print(result)


"""Principles of object mutability in Python
Immutable types in Python are those that cannot be changed after they are created.
They are: integers int, real numbers float, strings str, and tuples
Variable types, such as lists, dicts, and sets, can be mutated. When a mutable object is passed to a function, a reference to that object is passed, and changes made inside the function are reflected in the original object.

"""

def modify_string(original: str) -> str:
    original = "changed"
    return original

str_var = "original"
print(modify_string(str_var))  # type: changed
print(str_var)                # type: original



def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # print: [1, 2, 3, 4]


# if you do not want to change original object use method of copy
def string_to_codes(string: str) -> dict:
# Initialize a dictionary to store codes
    codes = {} 
# Iterate through each character in the string
    for ch in string: 
# Check if the character is already in the dictionary
        if ch not in codes:
# Add the character-code pair to the dictionary 
            codes[ch] = ord(ch) 
    return codes

result = string_to_codes("Hello world!")
print(result)


"""
Visibility areas (LEGB)
1) L - Local  => internal level, where the name is defined inside a function or block of code.
2) E - Enclosing => This is a scope that encloses the local scope. If a function is inside another function, the names defined in the enclosing function will be available to the inner function.Inner function can read but not change aouter data
3)G - Global => module 
To change a global variable inside a function, you must use the global keyword.
4) B - Built-in => This is the outermost level that contains the names built into Python.
"""


x = 50

def func():
    global x
    print('x =', x)  # x equal 50
    x = 2
    print('Changing global value x to', x)  # ЗChanging global value x to 2

func()
print('Value x is', x)# Value x is 2



""""
Key function arguments

Key arguments in Python functions are a way of passing arguments to a function where each argument is given a name.
"""

def greet(name, message="Hello"): # name is a positional parameter and message is a key parameter.
    print(f"{message}, {name}!")

greet("Alex")  


#Example of using the *args parameter
#you can pass as many arguments to the function as you need without having to define them

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

#Example of using the **kwargs parameter
# function can take any number of keyword arguments

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)


# both can be used together but *args should be used at the first place

