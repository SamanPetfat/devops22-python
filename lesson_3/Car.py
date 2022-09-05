
from audioop import reverse
from ctypes import Union
from enum import unique

# 1. The Datatype used here is called Integer, also called Int.
X = 1
Y = 4

# 2. Addresses Is using Dictionary type variable
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}

# 3. Using the Dictionary variable, we can bring out the address using the name attached to the string, and printing it.
print(addresses["Bella"])

# 4. By using the dictionary variable, we can also add new addresses, listing the name and save it to the new adress.
addresses["Daniel"] = "prinsgränd 2"
# 4.1 And then calling the name using the dictionary will automatically call the address of that person ( as seen on #3 )
print(addresses["Daniel"])

# 5. Using the "len()" function, while calling addresses gives us a count, of how many keys "addresses".
print(len(addresses))

# 5.1 Using "sorted" function, we sort the name in an alphabetical order, save the last name in a variable called "last_name",
# 5.1 and print it, calling the dictionary, and the "last_name"
sorted_addresses = sorted(addresses)
last_name = sorted_addresses[-1]
print(addresses[last_name])


# 5.1 This line of code switches the items in between ":" to the other side. Using "sorted", i sort the addresses in Aphabetic order
# 5.1 and printing it out.
addresses = {v: k for k, v in addresses.items()}

# 5.2 And again we use the "sorted" method to sort the addresses 
# 5.2 and save the first variable into a list where the first address gets called.
sorted_addresses = sorted(addresses)
first_address = sorted_addresses[0]
print(addresses[first_address])



# 6. The variable "cars" is using a method called "list" to store more than 1 value.
cars = ["Volvo", "Opel", "BMW"]

# 7. Printing "cars[X]" gives us the value of the middle choise in "cars"- list.
print(cars[X])

# 8. Printing "cars[Y]" gives us an IndexError where the list-index is out of range.
# -- > print(cars[Y]) (Putting it in Quarantine, so it doesnt discturb the following codes.)

# 9. After sorting "cars"-list with "sort" , printing "cars[0]" gives us the results: BMW.
cars.sort()
print(cars[0])

# 10. Created a new variable called "cars_2" and applied another value/key to the list using the ".append" method.
# 10. Both "cars_2" and "cars" now have the same "ingredients".
cars_2 = cars
cars.append("Saab")

# 10. printing the two different variables to check their values/keys
print(cars_2)
print(cars)

# Sorted cars and Reversed, using "reverse" and duplicated.
sorted_cars = sorted(cars*2,reverse=True)
print(sorted_cars)

# Putting "cars" into a list called "cars_3" and showing that
# putting another item into the "cars" variable, doesnt affect the list.

# List
cars_3 = list(cars)
print(cars_3)

# Adding car into "cars" and printing to show output
cars.append("Skoda")
print(cars)


# printing to show that it's unnaffected.
print(cars_3)

unique_cars = cars
print (unique_cars)


# The Datatype of numbers1-2 are Lists.
# there are 4(8) integer values and one "X" (and "Y")



numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

# By using this method i can check what Class numbers 1 and 2 is using. 
# And Output should be  a : 'set' - class.
print (type(numbers1))
print (type(numbers2))


# This exersice wants us to find the intersection between 2 variables.
# We use the intersection method to help us find it.
# While first printing the numbers to see what we have, and then using "numbers1" and compare it with "number2".
print(numbers1,numbers2)
print(numbers1.intersection(numbers2))

# The "union()" method will print out both num1 and 2 without mixing all numbers.
# it only prints out the non-used values. i believe it removes the duplicates.
print(numbers1.union(numbers2))

# This explaines itself, since the method is name after what it does.
# It finds and prints the symmetric difference between num1, and 2.
print(numbers1.symmetric_difference(numbers2))