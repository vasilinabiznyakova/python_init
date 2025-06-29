def my_generator():
    yield 1 # yield is similar to return, but the next time the function is called, it continues from where it left off, instead of starting over.
    yield 2
    yield 3


gen = my_generator()

# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3


def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print(number)
