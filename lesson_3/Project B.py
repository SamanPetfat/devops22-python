
# Empty list created to be filled.
from multiprocessing.sharedctypes import Value
from operator import itemgetter


persons = []


# Creating the character with different values using saved-input from user into variables to keep track.
# Also using ".lower()" so its non-case sensetive, in case user inputs Caps into name.
name_person_1= input("Please enter name for person 1: ").lower()
age_person_1 = int(input("please enter age for person 1: ")) # using Int before input
shoesize_person_1 = float(input("Please entere shoe-size for person 1: ")) # using Float class 

# Creating a tuple to save several variables, into 1 variable.
person_1 = (name_person_1, age_person_1, shoesize_person_1)

# saving person_1 into the previously empty list we created at the beggining.
persons.append(person_1)


# and now doing the same thing, but with person 2.


# Second person
name_person_2= input("Please enter name for person 2: ").lower()
age_person_2 = int(input("please enter age for person 2: "))
shoesize_person_2 = float(input("Please entere shoe-size for person 2: "))
person_2 = (name_person_2, age_person_2, shoesize_person_2)
persons.append(person_2)

# Third person
name_person_3= input("Please enter name for person 3: ").lower()
age_person_3 = int(input("please enter age for person 3: "))
shoesize_person_3 = float(input("Please entere shoe-size for person 3: "))
person_3 = (name_person_3, age_person_3, shoesize_person_3)
persons.append(person_3)


# Printing a space between next excersice
print("\n")


# Here we sort the shoe-size and age of the 3 people we saved into "persons"- list.
# Then we use the "key=itemgetter()" to first pick the person with the biggest shoesize, ( hence why we picked (2) )
# Note that it will be sorted, so the last person will have the biggest shoe-size.
shoe_size_sorted = sorted(persons, key=itemgetter(2))
age_sorted = sorted(persons, key=itemgetter(1))

# We save the Oldest person in an new variable that is sorted in a list. 
oldest = age_sorted[2]

# but we also need the median-shoesize, and we did save the shoe-sizes, sorted.
shoesize_median = shoe_size_sorted[1]

# We print out using F-strings to Calculate and output our variables.
print(f'Name of oldest person:\nName: {oldest[0].capitalize()}\nShoe size: {oldest[2]}')
print("\n")
print(f'Name of person with median shoe-size:\n{shoesize_median[0].capitalize()}\nAge: {shoesize_median[1]}\nShoe size: {shoesize_median[2]}')
print("\n")
Searches = {
    "age": {
        str(age_person_1): person_1,
        str(age_person_2): person_2,
        str(age_person_3): person_3

    },
    "shoe": {
        str(shoesize_person_1): person_1,
        str(shoesize_person_2): person_2,
        str(shoesize_person_3): person_3
    },
    "name": {
        str(name_person_1): person_1,
        str(name_person_2): person_2,
        str(name_person_3): person_3
    },
}
prop, Value = input("Enter name, age, or shoe, followed by a Value here: ").split(" ")
found_person = Searches[prop][Value]
print("Found Person")
print(f"\tName: {found_person[0]}")
print(f"\tAge: {found_person[1]}")
print(f"\tShoe size: {found_person[2]}")