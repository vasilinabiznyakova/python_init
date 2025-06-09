this_is_string = "Hi there!"

the_same_string = "Hi there!"

this_is_string == the_same_string  # True

# The \ character at the end of the first and second lines of code tells the interpreter to ignore the end of the line and continue immediately with the next one.
one_line_text = (
    "Textual data in Python is handled with str objects,"
    " or strings. Strings are immutable sequences of Unicode"
    " code points. String literals are written in a variety "
    " of ways: single quotes, double quotes, triple quoted."
)

print(one_line_text)

# Implicit string concatenation
("spam " "eggs") == "spam eggs"  # True

query = (
    "SELECT * " "FROM some_table " "WHERE condition1 = True " "AND condition2 = False"
)

# Special characters in Python strings, also known as escaped characters  are used to represent certain control sequences or to include characters that cannot be entered directly into a line of code.
"""
\n - line wrapping
\f - page wrapping
\r - Return the cursor to the beginning of the line without moving to a new line.
\t - horizontal tab
\v - vertical tab
"""
print("Hello\nWorld")
print("Hello\tWorld")

# The output is as follows: when we encounter the \r character, we return to the beginning of the line and continue output. This overwrites the previous output
print("Hello my little\rsister") # sistermy little


print("Hello\bWorld")  # HellWorld The output is one character to the left and outputs the remainder after the control character.

print("Hello\\World")  # Also if we need to output a backslash

print("It's a beautiful day")
print('He said, "Hello"')
