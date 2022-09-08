enter_name = input("Hello, and welcome to the VIP Section. Please enter your name: \n").capitalize()


vip_names = ("Daniel", "Simon", "Emmy","Felicia","Robin")

if enter_name in vip_names:
    print(f"Welcome {enter_name}. You are on the list!")
else: print("Sorry, you are not on the list..")