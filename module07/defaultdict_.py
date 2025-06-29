from collections import defaultdict


phone_numbers = [
    "0509993636",
    "0679993636",
    "0959993636",
    "0969993636",
    "0509993637",
    "0639993636",
    "0939993636",
    "0509993632",
    "0339993632",
]


phones_per_operator = defaultdict(list)

for number in phone_numbers:
    if number.startswith(("063", "093")):
        phones_per_operator["Life"].append(number)

print(phones_per_operator)
