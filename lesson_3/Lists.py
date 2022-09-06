from itertools import count
from multiprocessing.reduction import duplicate
from re import X, search
from turtle import color

my_list = []

color1 = "red"
my_list.append(color1)
print(my_list[0])

my_list.append("blue")
my_list.append("yellow")

print(my_list[1])
print(my_list[2])
print("blue" in my_list)
print("green" is not my_list)

my_second_list = []

my_second_list.append("Green")
my_second_list.append("Orange")

combined_colors = [my_list + my_second_list]
print(combined_colors)


color_red1 = "red"
color_yellow1 = "yellow"
duplicate_colors = [(color_red1), (color_yellow1)]*3


print(duplicate_colors[0:4])

print(duplicate_colors.count(color_red1))

print(duplicate_colors.index(color_yellow1))

print(len(duplicate_colors))


total_numbers = [60,3,6,30,10,15,40]

sorted_total_numbers = sorted(total_numbers)
print(sorted_total_numbers[-1])
print(sorted_total_numbers[0])
