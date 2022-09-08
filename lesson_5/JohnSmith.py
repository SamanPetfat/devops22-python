from ast import Slice


firstname = "john"
lastname = "smith"
tele = "00468123456789"

print(f"{firstname} {lastname} {tele}")

fullname = (firstname + " " + lastname)
print(len(fullname))

print(f"{firstname}\n{tele}")

print(firstname + " " + lastname + " " + tele)
print(f"{firstname} {lastname} {tele}")
print('{}'.format(firstname),(lastname),(tele))
print('%s' % firstname,lastname,tele)


#Excersice 2 Slice


print(fullname[0:6])

print(fullname[1:9])

print(fullname.upper()[0:9:2])

print(fullname[-1:-7:-1])

print(fullname[5:6:1])

