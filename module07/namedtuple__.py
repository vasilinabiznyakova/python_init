from collections import namedtuple

name = "Simon" 
age = 2
owner = "Yura"

cat = ["Simon", 2, "Yura"]
print(cat[1])


Cat = namedtuple("Cat",["nick", "age", "owner"])


simon = Cat("Simon", 2, owner="Yura")
print(simon)
print(type(simon))
print(simon.age)
print(simon.nick)

# used not as often
