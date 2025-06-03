# work_experience = int(input("Enter your full work experience in years: "))
# developer_type = None

# if work_experience <= 1:
#     developer_type = "Junior"
#     print(developer_type)
# elif work_experience <= 5:
#     developer_type = "Middle"
# else:
#     developer_type = "Senior"

#     print(developer_type)


# num = int(input("Enter a number: "))

# if num > 0: 
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
#         print (result)
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

#     print(result)


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num >= 0:
#     sum += num
#     print(sum)
#     num -= 1
#     print(num)

# print(num)
# print(sum)
    

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#         result += 1
    
# print (result)


# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool / quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def greeting():
#     print('Hello world')

# greeting()


# def invite_to_event (username):
#     message = f'Dear {username}, we have the honour to invite you to our event'
#     return message

# print(invite_to_event('Vas'))


# def discount_price(price, discount):
#     def apply_discount():
#       nonlocal price 
#       price = price * (1 - discount)
#       return price
    
#     price = apply_discount()

#     return price

# print(discount_price(20, 0.1))

# def get_fullname(first_name, last_name, middle_name = ""):

#     if middle_name:
#         message = f'{first_name} {middle_name} {last_name}'
#     else:
#         message = f'{first_name} {last_name}'

#     return message

# print(get_fullname('a', 'b', 'c'))


# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         spaces = (length - len(string)) // 2
#         string = ' ' * spaces + string
#         return string
    
    

# print(format_string("abaa", 15))


# def first(size, *args):
#     return size + len(args)
    

# print(first(5, 5))


# def second(size, **kwargs):
#     return size + len(kwargs)
    

# print(first(5, f = 5))



