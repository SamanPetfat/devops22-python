# 1. Raise input validation

#ALT convert value value variable to float.

# def ....
#    try: 
#       float_Value = float(value)
#    except ValueError:
#       raise TypeError(Value not float.)
#    if not isinstance(value, float):
#       raise TypeError("value is not a float")


def is_float(value):
    if not isinstance(value, float):
        raise TypeError("value is not a float")
my_var = 2.0
is_float(my_var)


def int_input():
    try:
        return int(input("write an integer: "))
    except:
        print("sorry not an int")
        return int_input()

def even_input():
    number = int_input()
    if not number % 2:
        raise Exception("even numbers are not allowed")
    return number

even_input()


# raise mean we created a wrong, to be sent to a code that is or signal a wrong has be done in a code.
# you can raise inside an except.


# 3.

def div(x,y):
    not_a_string(y)
    try:
        return x/y
    except ZeroDivisionError:
        print("division by zero is not allowed")

def not_a_string(y):
    if isinstance(y, str):
        raise TypeError("string is not allowed")



# import 4.
from math import sqrt
from random import randint
print(sqrt(16)) # can give a float number.
print(randint(1,10)) # randomize a number between 1-9


#lambda

mylist = list(range(1,11))
mylist1 = list(range(2,11))

print(list(map(lambda x: x + 1, mylist ))) #prints from 2..11
print(list(map(lambda x: x + 1, mylist1 ))) # prints from 3..11