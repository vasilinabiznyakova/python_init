"""
The user enters a string. We need to count how many characters are in the string and how many spaces are in the string.
"""
string = (input("Enter any string you want to calculate spaces and characters for: "))

total_chars = len(string)
space_count = 0

for char in string:
    if char == " ":
        space_count += 1

print (total_chars)
print(space_count)