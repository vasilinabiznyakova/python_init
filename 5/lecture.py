with open ("users.txt", mode = "w") as file: # context manager will close file anyway and this is the best practice 
    age = 30
    name = "addd"
    try:
        info = name + age
    except TypeError as e:
        print(e)
    
    file.write("zzzz")