# import pickle

# some_data = {(1, 3.5): "tuple", 2: [1, 2, 3], "a": {"key": "value"}}

# byte_string = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_string)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False

# import pickle

# some_data = {(1, 3.5): "tuple", 2: [1, 2, 3], "a": {"key": "value"}}

# file_name = "data.bin"

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)

# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False


# import pickle


# def write_contacts_to_file(filename, contacts):
#     with open(filename, "wb") as fh:
#         pickle.dump(contacts, fh)


# def read_contacts_from_file(filename):
#     with open(filename, "rb") as fh:
#      unpacked = pickle.load(fh)
#      return unpacked


import json

some_data = {"key": "value", 2: [1, 2, 3], "tuple": (5, 6), "a": {"key": "value"}}
file_name = "data.json"

with open(file_name, "w") as fh:
    json.dump(some_data, fh)

with open(file_name, "r") as fh:
    unpacked = json.load(fh)

unpacked is some_data  # False
unpacked == some_data  # False

unpacked["key"] == some_data["key"]  # True
unpacked["a"] == some_data["a"]  # True
unpacked["2"] == some_data[2]  # True
unpacked["tuple"] == [5, 6]  # True


import json


def write_contacts_to_file(filename, contacts):
    data = {
        "contacts": contacts 
    }

    with open(filename, "w") as fh:
        json.dump(data, fh, indent=2)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
        return unpacked