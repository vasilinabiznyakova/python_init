# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

# int

# poem = "str"
# print(dir(poem)) #

name = input("Enter your name >>>> ")
played_total = 1
try:
    played_total = int(input("Enter your total  >>>> ")) 
    played_total =played_total / 0
except ValueError:
 played_total = 0
except ZeroDivisionError:
   print("zero devision")
played_total+=1

message = f"Welcome to game {name} total played {played_total}"
print(message)


