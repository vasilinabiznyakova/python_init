""""
Write script that:
Prints "Fizz" if the number is a multiple of some specific number (e.g. 3);
Prints "Buzz" if the number is a multiple of another specific number (e.g. 5);
Prints "FizzBuzz" if the number is a multiple of both of these numbers;
Otherwise,n_blocks_and_ternary_operators.py prints the number itself.
"""

num = int(input("Type in number you want to check "))
if num % 3 == 0 and num % 5:
    print("FizzBuzz")
if num % 3 == 0:
    print("Fizz")
if num % 5 == 0:
    print("Buzz")