import re

message = "People love Python"

res = re.search("Python", message)

res = re.search("^Py", message)

print(res)
