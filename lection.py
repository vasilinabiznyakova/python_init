def find_max_vowels(text):
    vowels = "aeiouy"
    for char in text:
        if char.lower() not in vowels:
            text = text.replace(char, ".")

    chains = text.split(".")
    # chains.sort(key = len)
    # max_seq = chains[-1]
    # print(chains)
    max_seq = max(chains, key=len)
    return max_seq, len(max_seq)
    # print (text)

text = "Alloha everyone adss assaaaaaaaa addfg"

# len()
# if
# for / while
# keep track of vowels
# sort

max_seq, length = find_max_vowels(text)
print(max_seq)
print(length)
