"""
usually it should be 4 spaces for block of instructions

You can also highlight multiple levels of nesting by adding 4 more spaces to the left for all statements in the block
"""

x = 5
y = 10

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("This is just for demostration instructionss levels of nesting")
    else:  # x > 0, y < 0
        print("This is just for demostration instructionss levels of nesting")
else:
    if y >= 0:  # x < 0, y > 0
        print("This is just for demostration instructionss levels of nesting")
    else:  # x < 0, y < 0
        print("This is just for demostration instructionss levels of nesting")


""""
Ternary operators in Python are an elegant way to express conditional expressions in a shorthand form.
Ternary returns value, if else execute actions
"""

is_nice = True

state = "nice" if is_nice else  "not nice"

print(state)

some_data = None
msg = some_data or "Data was not returned"

print(msg)


#also possible such usage but its not good practice

 
a = 0
b = "positive" if a > 0 else "negative" if a < 0 else "zero"
print ( "a is", b)

#Operator match is more flexible version of if else
#we use it when we need to perform several actions that depands on one variable
#doesnt recognize >< etc
# match if more prefereable as we can use several values 
# usage case is when we  processing commands
some_variable = True
match some_variable:
    case "case_1":
        print("Execute smth")
    case "True":
        print("Execute true")
    case _: #unknown case
        print("Unknown fruit.")


pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]: # The _ character in the template is used as a "placeholder" meaning "any other value".
        # dog + cat
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Only dog
        print("There's a dog.")
    case _:
        # Other combinations
        print("No dogs.")
