numbers = [1,2,3,42,15]

# finite iteration
for number in numbers:
    print(number)
# conditional iteration
# while <conditiion == True>:
#     #
#     #
#     #

# greatest common divisor

first = int(input("Enter 1st int"))
second = int(input("Enter 2nd int"))


gsd = min(first, second)

while  not (first % gsd == 0 and second % gsd == 0):
    gsd -= 1


print(gsd)


# TERNARY

age = 18

can_drink_beer = False
if age >= 18:
    can_drink_beer = True
else:
    can_drink_beer = False

# same with ternary
can_drink_beer = True if age >=18 else False

can_drink_beer = age >= 18

ip = "129.12.12.12"

role = "admin" if  ip in ["129.12.12.12"] else "user"

print(role)

text ="to Be or not to BE"
print(text.lower())
print(text.upper())
print(text.isupper())
print(text.islower())


print(ord("a")) # order# in utf8 for letter

print(text.split()) # but you must save

print(text.find("Be"))

# Caesar encryption + 3 position used Affine cipher but with any number for shift

# key = 3
# alphabet
# for
# if

# def
def encrypt_by_key(message, key=3): # function signature and inside () parameters, you can assign default params
    # function body
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""

    message = message.upper()

    for letter in message:
        if letter in alpha:
            index = (alpha.find(letter) + key) % len(alpha)
            cipher += alpha[index]
        else:
            cipher += letter
    print(cipher)

# function call
# keyword arguments can be replaced by order
encrypt_by_key(key=3, message="Brute is killerZ!!!")  # arguments
# position arguments should go before keyword args
encrypt_by_key( -3, message="EUXWH LV NLOOHUC!!!")


def connect_to_db(login, password, db_name="users_db", index=False):
    pass

connect_to_db("admin", "123", index=True)

def connect_db(*args, **kwargs):
    pass


cars = {
    "Ford": 2005,
    "BMW": 2019,
    "Mitsubishi": 2005
}

print(cars.keys())

for key in cars: #for dictionaries
    print(key)

for key in cars.values():
    print(key)


for element in cars.items():
    print(element[0])
    print(element[1])

# the most correct way to get every element
# "Ford | BMW | Mitsubishi"
for model, year in cars.items():
    print(model)
    print(year)


models = list(cars.keys())
models.sort(reverse=True)
header = " | ".join(models)
print(header)

message = " Hello,,son,, When are you coming home,,,,,"

def dad_filter(message):
    while ",," in message:
        message = message.replace(",,", ",")
    return message.strip(",")

result = dad_filter(message)
print(result)



