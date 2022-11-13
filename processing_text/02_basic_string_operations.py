import string

print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string2 = "Supercalifragilistic"
test_string3 = "90210"


def print_letters_only():
    result = "".join([c for c in test_string1 if c in string.ascii_letters])
    print(result)


print_letters_only()


print(test_string1.isalpha(), test_string2.isalpha(), test_string3.isalpha())
print(test_string1.isalnum(), test_string2.isalnum(), test_string3.isalnum())
print(test_string1.isnumeric(), test_string2.isnumeric(), test_string3.isnumeric())
