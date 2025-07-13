import pickle


class GoogleAccount:
    def __init__(self, username):
        self.username = username

g = GoogleAccount("Oleh")
print(g.__dict__)

class User:
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends
        self.account = GoogleAccount(name + "@gmail.com")

user = User(name="John", age=28, friends=["Jane", "Tom"], balance=20.70, active=True)
print(user.__dict__)


with open("employee.bn", "wb") as f:
    user_data = pickle.dump(user, f)

with open("employee.bn", "rb") as f:
    user = pickle.load(f)

print (type(user))
print(user.friends)
