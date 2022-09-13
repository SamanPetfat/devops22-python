from enum import unique
from random import choices, shuffle
from collections import Counter
from unicodedata import name
# "choices" is a from the "random library", used to generate Multiple data. K decides how many times to repeat it.
name_list = choices(["Saman","Anna","Malin", "Annica","Niclas"], k=100)
print(name_list)

# First create a variable to save the the count in. Then use the "counter" library to count your list of names (100 random of 5 names.)
name_counter = Counter(name_list)
print(name_counter) # print the amount ( name: amount)

# Print the 3 most common. First use the Counter variable you created. "name_counter" and then the method "most.common(3)".
print(name_counter.most_common(3))

# Print the least common. same method, but use -1 to read the last one used. ( check if Sorted is needed.)
# Edit: To print the last name, you leave the () empty but fill in a [] with a number. such as -1 to get the last value.
# The value inside 
print(name_counter.most_common()[-3:])


# Create a variable called unique names., sort the list using "Sorted", use the "list(set)" to determine any duplicates.
# Print the Unique names.


# ALTERNATIVE
# unique_list = []
# for a in name_list:
#    if a not in unique_list:
#       unique_list.append(a)


unique_names = sorted(list(set(name_list)))
print(unique_names)

# shuffle the names using "shuffle", that is imported using lib (from random import shuffle). print names.
shuffle(unique_names)
print(unique_names)

# Sort the names and print them in reverse using "sort(reverse=true)"
unique_names.sort(reverse=True)
print(unique_names)
