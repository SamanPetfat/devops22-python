import string

# list is a type class, such is string. with built in functions. rightclick to check def.
alphabet = list(string.ascii_lowercase)

# create a list and store the alphabet.
stack = [letter for letter in alphabet]
print(stack)

alph_string = " "

while stack:
    alph_string += stack.pop()

print(alph_string)



