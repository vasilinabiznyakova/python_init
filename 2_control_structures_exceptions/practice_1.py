'''
We need to write code which will help to control budget

100$

Enter week budget

Enter daily spent
'''

#First step: Enter budget

# weekly_budget = input("Enter your weekly budget: ")
# weekly_budget = int(weekly_budget)

try:
    weekly_budget = int(input("Enter your weekly budget: "))
except ValueError:
    print("Weekly budget value is not correct. We are setting budget to 100...")
    weekly_budget = 100
    
print(weekly_budget + 100)