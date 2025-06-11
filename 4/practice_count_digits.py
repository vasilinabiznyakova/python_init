import re



def validate_pincode(pincode: str) -> bool:
    return (
        re.match(r"^(?:\d{4}|\d{6})$", pincode) is not None
    )  # we use is not None bec match returns either string or None


assert validate_pincode("1234") == True
assert validate_pincode("654321") == True
assert validate_pincode("a12345") == False
assert validate_pincode("12345") == False
