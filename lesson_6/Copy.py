from copy import copy
from distutils.command.build_scripts import first_line_re


first_string = "hello"

second_string = first_string

third_string = first_string[:]

second_string = "Hiya"

print(first_string)
print(second_string)
print(third_string)

# Second string changed. but the first is still the same, as the third.
