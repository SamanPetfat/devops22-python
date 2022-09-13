from lib2to3.pgen2.token import NEWLINE
import random
from collections import Counter
from turtle import color
# Part 1            ---------------------------
# a list with numbers from 1-100

NEWLINE = "\n"
one_to_hundred = [x for x in range(1, 101)]
print(one_to_hundred)
print(NEWLINE)

# Part 2             ---------------------------
# Even numbers try 1

even_numbers = [num for num in range(2,61,2)]
print(even_numbers)

# Even numbers try 2 (same answer as even try 1)

# even_numbers1 = range(2,61)
# for num in even_numbers:
#     if num % 2 == 0:
#         print(even_numbers)
#         break



# Part 3             ---------------------------
# Odd numbers Try 1 (compact)

odd_numbers = [num for num in range (1,71) if num % 2 == 1]
print(odd_numbers)

# Odd numbers Try 2 (detailed, same answer as  odd try 1)

# odd_numbers1 = range(1,71)
# for num in odd_numbers:
#     if num % 2 == 1:
#         print(odd_numbers)
#         break


# Part 4.1              ---------------------------
#  Store and randomly Shuffle numbers between 1-300 and print out 100  unique numbers
print(NEWLINE)

mylist = [num for num in range(1,301)]

random.shuffle(mylist)
print(mylist[:100])

print(NEWLINE)


# Part 4.2              ---------------------------
# Make a list with random numbers, including duplicates (non-unique)
mylist1 = [num for num in range(1,301)]
print(random.choices(mylist1,k=100))

print(NEWLINE)

# Part 5.1
# Create a list with 5 colors, not containing "red"

my_colors = ["blue","yellow","green","orange","purple"]
print(my_colors)
# Part 5.2 create a list containing red and 2 more random colors from "My_colors"- list
red_color = ["red"]
new_mix = random.choices(my_colors,k=2)
red_color.extend(new_mix)
print(red_color)

print(NEWLINE)
# 5.3 print the list lenght using Len() function & print out the unique colors, using F-string.
rand_colours = [random.choice(red_color) for i in range(50)]
print(rand_colours)
print(f"The lenght is: {len(rand_colours)}")


# Edit: you can use Join() to join the colors, and it will remove the [] in the console.
print(f"My first list of colors has: {len(my_colors)} colors: {my_colors}.")
print(f"My second list of colors has: {len(red_color)} colors: {red_color}.")
print(f"And my third list of colors has: {len(rand_colours)} colors.{rand_colours[:3]}.")



