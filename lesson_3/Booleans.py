x = True
y = False
z = True

# 1. If any of the Variables are True, the results will output the value "true"
result = x or y or z
print(result)

# if it were for all booleans to be true, this part of the excersize would result in "True",
# (x = True, y = False, z = True) although we have one Boolean that is false, wich will result in False.
result = x and y and z
print (result)

# if any of the Booleans result in False, this will output False.
result = not x and y and z
print(result)

# IF we switch all of the previous Booleans to different values, the result will end up beeing false.
result = not x and not y and not z
print(result)


