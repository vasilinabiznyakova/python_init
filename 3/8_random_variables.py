"""
A random variable is a variable whose value is the result of chance events or experiments. There are two main types of random variables: discrete and continuous.
discrete:

these are those that take a limited number of values ​​or values ​​that can be calculated.

continuous:

They can take on any value within a certain range. For example, a variable that represents the time it takes to complete a certain task is a continuous random variable.
For generating random (pseudo-random) numbers, Python has the random package. It is good enough for a number of common tasks, but not for cryptography. As soon it will start to repeat
"""
import random

dice_roll = random.randint(1, 6)  # a <= N <= b
print(f"You got {dice_roll}")

num = random.random() #a number between 0.0 (inclusive) and 1.0 (exclusive)
print(num)


fill_percentage = random.random() * 100
print(f"Fill: {fill_percentage:.2f}%")

"""
☝ A percentage is a way of expressing a number as a part of a hundred. One percent, written as 1%, is equivalent to 1/100 or one hundredth. So when we say something is 50%, it means 50 out of 100 or half of a whole.
To convert a percentage to a fraction, we divide the number by 100. For example, 20% would become 20/100 or 0.20. To convert a fraction to a percentage, we multiply it by 100. So, 0.20 would become 20%.
"""

"""
random.randrange(start, stop[, step]) returns a randomly selected number from the given range.
start (inclusively) - start range, by default 0 
stop (noninclusively) - end range - obligatory
step
"""

print(random.randrange(10))  # The upper limit is 10, but it doesn't include

# random number from 1 to 10, and only odd numbers:
target = random.randrange(1, 11, 2)
print(f"Target: {target}")


cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6"]

random.shuffle(cards) # method will shuffle the list in random order

print(f"Shuffled deck: {cards}")


fruits = ["apple", "banana", "orange"]
print(random.choice(fruits)) # will select random el from the list


"""
random.choices(population, weights=None, cum_weights=None, k=1)


population - a sequence list from which a selection is to be made.
weights - an optional list that specifies the probabilities (weights) of each element in the population list. These weights determine how likely it is that a particular element will be selected. The length of the weights list must be equal to the length of the population list.

cum_weights is also an optional list of cumulative weights. If specified, the weights list is ignored. The cumulative weight of each element is defined as the sum of its weight plus the weights of all previous elements.
k: Number of elements to select. Default k=1.
"""


participants = [
    "Anna",
    "Bogdan",
    "Victor",
    "Galina",
    "Dmitry",
    "Olena",
    "Zhenya",
    "Zoryan",
    "Igor",
    "Josyp",
]
team = random.sample(
    participants, 4
)  # If there is a need to select N elements from a list and they are not repeated
print(f"Team: {team}")

# returns a random real number N such that a <= N <= b.
price = random.uniform(50, 100)
print(f"random price: {price:.2f}")
