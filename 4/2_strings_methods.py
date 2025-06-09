s = "Hi there!"

start = 0
end = 7
# will find from start of the string till the end and return first match
print(s.find("er", start, end))  # 5 return index of first match at string
print(s.find("q"))  # -1 return - 1 if sub was not found
# will find from end of the string till the start
print(s.rfind("o"))


s = "Some words"
# will return Value error of index not found
print(s.index("o"))
print(s.rindex("o"))

"""
separator - the separator by which to split the string. If not specified, the string is split on any space.
maxsplit - the maximum number of splits. A value of -1 means "no limit".
"""
# str.split(separator=None, maxsplit=-1)


text = "hello world"
result = text.split()
print(result)  # Print: ['hello', 'world']


text = "apple,banana,cherry"
result = text.split(",")
print(result)  # Print: ['apple', 'banana', 'cherry']


list_of_strings = ["Hello", "world"]
result = " ".join(list_of_strings)
print(result)  # Print: 'Hello world'

elements = ["earth", "air", "fire", "water"]
result = ", ".join(elements)
print(result)  # Print: 'earth, air, fire, water'

# remove spaces
clean = "   spacious   ".strip()
print(clean)  # spacious


# str.replace(old, new, count=-1) count of maximum q-ty of changes
text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)


print("TestHook".removeprefix("Test"))  # Hook
print("TestHook".removeprefix("Hook"))  # TestHook


print("TestHook".removesuffix("Test"))
print("TestHook".removesuffix("Hook"))


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split(
    "?"
)  # The first value of the list is written to the _ variable, and the second to the query.
print(query)  # q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t


obj_query = {}
for el in query.split("&"):
    key, value = el.split("=")
    obj_query.update({key: value.replace("+", " ")})
print(obj_query)


number = "12345"
print(number.isdigit())  # True

text = "Number123"
print(text.isdigit())  # False


for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - its digit")
    else:
        print(f"'{char}' - its not digit")
