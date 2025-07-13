from enum import Enum

class UserRole(Enum):
    ADMIN_ROLE = "admin"
    MODERATOR_ROLE = "moderator"
    USER_ROLE = "user"

print(type(UserRole.ADMIN_ROLE))  # <enum

print(type(UserRole.ADMIN_ROLE.value)) # str

role = input("What's your role >>> ")

match role:
    case UserRole.ADMIN_ROLE.value | UserRole.MODERATOR_ROLE.value:
        pass
    case UserRole.USER_ROLE.value:
        pass
    case _:
        pass
