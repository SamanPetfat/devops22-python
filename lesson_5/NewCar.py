minimum_price = 80000
while True:
    new_car = int(input("Your new car cost ""[\u20AC]: "))
    if new_car < minimum_price:
        print("This doesnt meet the requiermentS:""\u26D4"" Please add more Zeros: ")
    else:
        print("Congratulations on your new car!""\U0001F69C")
        break
