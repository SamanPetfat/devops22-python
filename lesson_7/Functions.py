# 1. Functions
from multiprocessing.resource_sharer import stop
from string import ascii_lowercase

# 1. Functions
def do_nothing():
    pass
print(do_nothing()) # 1.1 -> None 

# 2. Getting started. function prints "Hello World"
def greet():
    print("Hello world") # Prints Hello world.
greet()
# 2.1 function prints True
def result():
    x = 1 == 1.0
    # print(1==1.0)
    print(x)
result()

# 2.2 Function reverses alphabet.
#ALT:

# def rev_alpha():
#   print(string.ascii_lowercase[::-1]) -- Slice Operator.

def reversedalphabet():
    alphabet = [letter for letter in ascii_lowercase]
    stack = ""
    while alphabet:
        stack += alphabet.pop()
    print(stack)
reversedalphabet()

# 3.
def greetuser(name):
    print(f"hello {name}")

greetuser("saman")

# 3.1
def stringcap(word):
    print(word.upper())
stringcap("hello there")

# 3.2
# ALT
# def number_printer(stop)
#   print(list(range(1,stop)))
# number_printer()

def numbstop(stop):
    for i in range(1,stop+1):
        print(i, end=" ")
numbstop(20)