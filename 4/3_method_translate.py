"""
The translate() method in Python is used to transform strings by replacing certain characters with other characters. This method allows you to specify which characters should be replaced and what to replace them with, using what is called a "translation table" - a special dictionary that defines the mapping of the replacements.
Transaltion table is done with the help of method 
str.maketrans(intab, outtab, removetab)
"""
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))  # Th3s 3s str3ng 2x1mpl2

# this will remove chars aeiou
intab = "aeiou"
trantab = str.maketrans("", "", intab)

str = "This is string example"
print(str.translate(trantab))  # Ths s strng xmpl


symbols = "0123456789ABCDEF"
code = [
    "0000",
    "0001",
    "0010",
    "0011",
    "0100",
    "0101",
    "0110",
    "0111",
    "1000",
    "1001",
    "1010",
    "1011",
    "1100",
    "1101",
    "1110",
    "1111",
]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c #This is a built-in function used to get the Unicode code of a character.
    MAP[ord(s.lower())] = c

print(MAP)


result = "34 DF 56 AC".translate(MAP)
print(result)


morze_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

# Convert dictionary keys to Unicode codes
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)
