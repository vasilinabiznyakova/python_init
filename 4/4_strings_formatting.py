for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)
"""
In the expression :.2f:

: introduces a format specification.
.2 means that two digits should be printed after the decimal point.
f indicates the format of a real number.
"""
price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)

"""

outputs three values ​​in a string:
num is the number itself,
num**2 is its square,
num**3 is its cube,

and aligns each value in the center in a field 10 characters wide.
"""
width = 5
for num in range(12):
    print(f"{num:^10} {num**2:^10} {num**3:^10}")

"""  
The field width specifies the minimum width of the field in which the content will be placed. If the content is shorter than the field width, it will be padded with spaces.
The alignment specifies how the content will be aligned within the specified field width. The possible alignment options are:
    
<: Left-align content.
>: Right-align content.
^: Center-align content.
=: Used to align numbers, with the sign (if present) displayed on the left and the number on the right of the field.
"""
name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Print: '     Alice' (Right-align)


# f"{value:<width>.<precision>%}"
"""
where:

value - the value to be converted to a percentage.
<width> - the total width of the field; optional.
<precision> - the number of digits after the decimal point; optional.
"""
completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  #'75.6%'

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted) # 50%
