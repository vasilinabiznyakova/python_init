def login_required(role = "user"):
    def func_wrapper(func):
        def wrapper(*args, **kwargs):
           if role == "admin":
            return func(*args, **kwargs)
           else:
              raise PermissionError("Not Admin") 
        return wrapper
    return func_wrapper

role = input("What's your role >>>")

@login_required(role=role)
def open_profile(user_id):
    print(f"<h1>User {user_id}</h1>")

open_profile(12)
