"""
Lambda functions are short, one-time functions that can be written directly inside code without a name.
lambda x: x + 1

"""
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)


numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x**2, numbers):
    print(i)


"""
The filter() function is used to filter an iteration object, such as a list or tuple, using a given function. It creates an iterator that contains only those elements of the iteration object for which the filter function returns True
filter(function, iterable)

"""

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums))


# but lambda func is not necessary


def is_positive(x):
    return x > 0


nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums))


"""
The any() function is a built-in function that returns True if at least one element of the given iteration object is true. If the iteration object is empty or all of its elements are false, then any() returns False.
"""
nums = [0, False, 5, 0]
result = any(nums)
print(result)


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(result)


"""

The all() function is a built-in function that returns True if all elements in the iteration object passed to it are true.
"""


nums = [1, 2, 3, 4]
result = all(nums)
print(result)

nums = [1, 2, 3, 4]
result = all(nums)  
print(result)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
