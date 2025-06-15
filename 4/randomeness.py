import random

    # a = ["Ivan", "Max", "Alina", "Olha"]

    # res = random.choice(a)
    # print(res)

    # res = random.choices(a, k=2)
    # print(res)

    # res = random.choices(a, k=1000)
    # print(res)

    # random.shuffle(a)

    # print(a)


coin = {1: "Орел", 2: "Решка"}
sequence = []

count_0 = 0
count_p = 0

while count_0 < 4 and count_p < 4:
    choice = random.randint(1, 2)
    if choice == 1:
        count_0 += 1
        count_p = 0 

        count_0 = 0
        count_p += 1
    name = coin[choice]
    sequence.append(name)

print(sequence)
