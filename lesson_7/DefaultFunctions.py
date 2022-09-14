# Default functions.
# 1.
def default_number_printer(start=1, stop=11):
    print(list(range(start,stop)))
default_number_printer()


# 2.
def default_string_reverse(string1="hello",reverse=False):
    if reverse == True:
        string1 = string1[::-1]
        print(string1)
    else:
        print(string1)
default_string_reverse() #trying out to see what code it spits by default

# 2.1
default_string_reverse("hello", reverse=True) # what outputs if entered manually