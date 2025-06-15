# snake_case
# PascalCase
# camelCase
# kebab-case
def convert_camel_to_snake(key:str):
    res = ""
    for char in key:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    return res

user_status = "userIsAuthenticated" # user_is_authenticated

result = convert_camel_to_snake(user_status)
print(result)
# .isupper()
# for
