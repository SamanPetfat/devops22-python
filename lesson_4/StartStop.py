user_start_integer = int(input("Write a number to start with: "))
user_stop_integer = int(input("Write a number to stop at: "))

sum = 0

# So this was the code i used, until i saw your Solution on github, and noticed that
# it will only count and sum up IF the first number was smaller than the second one.
# otherwise it gives the sum of 0.

# while user_start_integer < user_stop_integer:
 #   print(user_start_integer)
  #  sum += user_start_integer
   # user_start_integer = user_start_integer + 1


# So i rewrote the code to work.
# Edit: its the same problem, it work if its start from 4, and stops on 2:
# meaning it cannot count upp from 4, cus 2 is less than 4.
# so both codes give the same answers i presume.

for i in range(user_start_integer, user_stop_integer):
    print(i)
    sum += i


print (f"sum = {sum}")