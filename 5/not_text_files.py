with open("raw_data.bin", "wb") as fh:
    fh.write(b"Hello world!")

"""
file opening mode -  b, short for bytes. 
In this mode, you will get a file object for working with the file in byte-line mode - "wb" to write 
byte strings or byte arrays.

bytes - an immutable type used to represent bytes.
bytearray - a mutable type that allows you to modify bytes after they are created.
Byte strings are important for working with network protocols (e.g., TCP/IP), serial ports, telnet, and other protocols where data is transmitted as a stream of bytes.
Byte is regular string but only 1 byte is used for 1 symbol

A bit (short for "binary digit") is the basic unit of information in computing and digital communication. A bit can have one of two values: 0 or 1.
A byte is a sequence of 8 bits, which is the standard unit of measurement for the amount of information in computers. One byte can represent 256 different states. From 00000000 to 11111111 in binary format or from 0 to 255 in decimal, which allows you to encode a wide range of information, such as characters of text, parts of images or sound.
Bytestrings have the same restrictions and rules as regular strings. For example, you can use the methods upper(), startswith(), index(), find(), and so on.
Indexing works the same way as regular strings

ASCII - American Standard Code for Information Interchange
"""

s = b"Hello!"
print(s[1])  # Print: 101 (its ASCII-code for symbol 'e')

# way1  to create byte string
byte_string = b"Hello world!"
print(byte_string)

# way2 to create byte string - method encode(), syntax str.encode(encoding="utf-8", errors="strict")
byte_str = "some text".encode()
print(byte_str)

# numbers =>>> byte strings

# Convert a list of numbers to a byte string
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
# Hexadecimal format is used here for convenient display of bytes. The \x character is an indicator of the hexadecimal representation of each byte
print(byte_numbers)  # Print the byte representation of the numbers b'\x00\x80\xff'

for num in [127, 255, 156]:
    print(hex(num))


"""
String encoding (ASCII, UTF-8, CP1251)
ASCII -  256 symbols total, 1 symbol = 1 byte
UTF-8 - 1 symbol = 1 - 4 bytes  1 112 064 symbols
also there can be other encodings

When working with files on Windows, encoding issues often occur because Windows commonly uses CP-1251 for Cyrillic, while UTF-8 is the universal modern standard. If a file is saved in one encoding but opened in a program expecting another, it may lead to unreadable characters or errors.
To avoid these problem its recommended explicitly note the encoding
"""
ord("a")  # 97 in UTF-8
chr(128)  # 'd' from UTF-8


s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)


print(b"Hello world!".decode("utf-16"))


# Opening a text file with explicit UTF-8 encoding
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# Since strings and byte strings in Python are immutable, the bytearray container allows efficient modification of raw binary data without creating new copies.
# you can change it as if it is unicode

byte_array = bytearray(b"Kill Bill")
print(ord("B"))
byte_array[0] = ord("B")
byte_array[5] = ord("K")
print(byte_array)

# you can edit, add symbols
byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)

# you can decode bytearray easiliy
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Print: 'Hello World'

# Comparison of strings
# 1. Converting strings to single case. .lower() or.upper() methods

string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Same lines")
else:
    print("Different lines")


"""
But string comparison in Python can give ambiguous results due to the fact that in UTF-8 encoding the same character can be represented by multiple codes, for example, the character 'ê' can be represented by the code U+00EA, or as a sequence of two codes U+0065 and U+0302.
Method casefold will resolve this issue
"""
text = "Python Programming"
print(text.casefold())


german_word = "straße"  # Lower case
search_word = "STRASSE"  # Upper case

# Comparison with lower()
lower_comparison = german_word.lower() == search_word.lower()

# Comparison with casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Comparison with lower(): {lower_comparison}")
print(f"Comparison with casefold(): {casefold_comparison}")
