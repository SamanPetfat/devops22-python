from copy import copy, deepcopy


names = ["olle","pelle","johan"]
names_copy = copy(names)
names_deep_copy = deepcopy(names)

names.pop()
names.append("tor")


print(names)
print(names_copy)
print(names_deep_copy)

# original list changes but not the copies.