
# Return exercise 1.
from ast import Num
from ctypes.wintypes import WORD
from os import sep
from tkinter import Y


def returninteger():
    return 1

def returntuple(x,y):
    return x, y

def returnboolean():
    return True

def returnfloat():
    return 1.0

def fullname(first,last):

    fullname= first,last
    return fullname

def calculate_area_rectangle(base,height):

    return base*height

def returnsum(values):

    return sum(values)

def test(word,repeat):
    return f"{word}\n"*repeat

result = test("hello",3)
result2 =test("goodbye",3)
print(result,end="")
print(result2)