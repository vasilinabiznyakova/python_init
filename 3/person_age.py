from datetime import datetime


def calculate_person_age(date_of_birth: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    today = datetime.today()

    # If the birth date is in the future, we return 0
    if date_of_birth > today:
        return 0

    try:
        date_of_birth_this_year = date_of_birth.replace(year=today.year)
    except ValueError:

        # If it is February 29, and the current hour is not a leap year, we move it to February 28
        date_of_birth_this_year = date_of_birth.replace(year=today.year, day=28)

    age = today.year - date_of_birth.year

    if date_of_birth_this_year > today:
        age -= 1

    return age


# Tests
assert calculate_person_age("2000-01-01") == 25
assert calculate_person_age("2024-02-07") == 1
assert calculate_person_age("2025-09-09") == 0
