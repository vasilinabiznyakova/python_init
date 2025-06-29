import re
from collections import Counter

with open("logs.txt") as f:
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    counter = Counter(re.findall(pattern, f.read())) # will return sorted 
    print(counter.most_common(5))
