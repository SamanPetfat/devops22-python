
import numbers
 # first we welcome the User, and then ask user to write a number.
 # we save that number into a variable called "game_master".
print("""Welcome to the NumberChecker!
Enter a number and i will tell you if its Even or Odd""")
game_master = int(input("Enter a number: "))

 # we write a loop, where "if the number the user input, divides evenly (how many times does 2 go into 4? exactly 2 times)= even = true.
 # Else we print that the number is Odd, because it will leave a "remainder",-
 # - Meaning: how many times goes 2 into 5? 2 times, and leaves 1 remainder. = Odd = False.
if game_master % 2 == 0:
    print ("Your number is even: ", game_master)
else: print("Your number is odd: ", game_master)