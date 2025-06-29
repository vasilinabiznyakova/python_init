# Oleh
# hlOe

from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

print(is_anagram("oleh", "hlOe"))
