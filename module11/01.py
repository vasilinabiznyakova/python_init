# # expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

# # file_name = "expenses.txt"
# # with open(file_name, "w") as fh:
# #     for key, value in expenses.items():
# #         fh.write(f"{key}|{value}\n")


# file_name = "expenses.txt"
# expenses = {}
# with open(file_name, "r") as fh:
#     raw_expenses = fh.readlines()
#     for line in raw_expenses:
#         key, value = line.split("|")
#         expenses[key] = int(value)

# print(expenses)


# import pickle

# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 42}

# # Серіалізація об'єкта в байтовий рядок
# serialized_data = pickle.dumps(my_data)
# # Виведе байтовий рядок
# print(serialized_data)

# # Десеріалізація об'єкта з байтового рядка
# deserialized_data = pickle.loads(serialized_data)
# # Виведе вихідний об'єкт Python
# print(deserialized_data)

# import json

# some_data = {
#     "key": "value",
#     2: [1, 2, 3],
#     "my_tuple": (5, 6),
#     "my_dict": {"key": "value"},
# }

# json_string = json.dumps(some_data)
# print(json_string)
# unpacked_some_data = json.loads(json_string)
# print(unpacked_some_data)


# import csv

# with open("eggs.csv", "w", newline="") as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(["Spam"] * 5 + ["Baked Beans"])
#     spam_writer.writerow(["Spam", "Lovely Spam", "Wonderful Spam"])

# with open("eggs.csv", newline="") as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(", ".join(row))


# import csv

# with open("names.csv", "w", newline="") as fh:
#     field_names = ["first_name", "last_name"]
#     writer = csv.DictWriter(fh, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerow({"first_name": "Baked", "last_name": "Beans"})
#     writer.writerow({"first_name": "Lovely", "last_name": "Spam"})
#     writer.writerow({"first_name": "Wonderful", "last_name": "Spam"})

# with open("names.csv", newline="") as fh:
#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row["first_name"], row["last_name"])


# import csv


# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w", newline="") as fh:
#         field_names = ["name", "email", "phone", "favorite"]
#         writer = csv.DictWriter(fh, fieldnames=field_names)
#         writer.writeheader()
#         for contact in contacts:
#             writer.writerow(contact)

# def read_contacts_from_file(filename):
#     contacts = []
#     with open(filename, newline="") as fh:
#         reader = csv.DictReader(fh)
#     for row in reader:
#         contact = {
#             "name": row["name"],
#             "email": row["email"],
#             "phone": row["phone"],
#             "favorite": row["favorite"],
#         }
#         contacts.append(contact)
#     return contacts


# import pickle


# class Human:
#     def __init__(self, name):
#         self.name = name


# bob = Human("Bob")
# encoded_bob = pickle.dumps(bob)

# decoded_bob = pickle.loads(encoded_bob)

# bob.name == decoded_bob.name  # True


import pickle


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # Відновлюємо стан об'єкта
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")


if __name__ == "__main__":
    reader = Reader("data.txt")
    data = reader.read()
    print(data)
    reader.close()

    # Приклад серіалізації об'єкта Reader
    with open("reader.pkl", "wb") as f:
        pickle.dump(reader, f)

    # Приклад десеріалізації об'єкта Reader
    with open("reader.pkl", "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()
