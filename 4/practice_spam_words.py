import re

"""
Script which would analyse text and remove spam-words

Python, Guido van Rossum

Python is the best programming language!

* is the best programming language!
"""

SPAM_WORDS_LIST = ["Guido van Rossum", "Python"]

def remove_spam_words(message: str) -> str:

    for spam_word in SPAM_WORDS_LIST:
        message = re.sub(rf"\b{spam_word}\b", "*", message)
    return message

assert remove_spam_words("Guido van Rossum") == "*"
assert remove_spam_words("Python") == "*"
assert remove_spam_words("Python Guido van Rossum") == "* *"
