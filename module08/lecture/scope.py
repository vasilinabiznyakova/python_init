# for i in range (9):
#     # loops doesn't have namespace/scope
#     name = "Oleh"

# print (i)
# print(name)

# global scope => local scope (func / class) => local scope (func / class)
# username = "Vas"
# def congratulate_user():
#     global username # if you use global you must do it prior username you ar going to replace the value for by convention
#     username = "Alex"
#     print(f"Happy birthday {username}")

# congratulate_user()
# print(username) # error


# congratulate_user()
# print(username)  # error

username = "Vas"


def congratulate_user():
    username = "Alex"  # Local to 'congratulate_user'

    def format_username():
        nonlocal username  # Refers to 'username' in the outer 'congratulate_user' scope
        username = "Ivan"
        return username

    format_username()
    print(f"Happy birthday {username}")


congratulate_user()


print(globals())
print(locals())

