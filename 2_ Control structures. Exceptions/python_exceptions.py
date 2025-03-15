"""
An exception in Python is an interpreter-level error caused by the inability to execute a particular statement for any reason (variable does not exist, syntax error, missing attribute, division by zero operation, etc.).
Exception types:
1) SyntaxError
2) IndentationError (an error that occurs if an error is made in delimiting blocks of instructions with spaces.)
3) TabError occurs if spaces and tabs are used to separate blocks of instructions in the same file.
4) TypeError
5) ValueError 
6) ZeroDivisionError 
"""

"""
Exception handling mechanism
try ... except ...
"""

val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")
