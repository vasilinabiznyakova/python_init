"""
While some actions are being exectuted with files it better to use try...except block
It will work ok but the code looks overweighted 
"""
fh = open("text.txt", "w")
try:
    # Perform file operations
    fh.write("Some data")
finally:
    # Closing the file in a finally block ensures that the file is closed even if an error occurs
    fh.close()


"""
better practice is using of context manager "with"
"""

with open('text.txt', 'w') as fh:
# Perform operations on the file
    fh.write('Some data')
# The file will be automatically closed after exiting the with block,it is doing the same logic as we had in original example


with open ("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")
with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
