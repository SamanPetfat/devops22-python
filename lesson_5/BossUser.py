print("Hello. please enter your name, salary and currency")
name = input("name: ").lower().capitalize()
salary = float(input("Salary: "))
currency  = (input("Currency: ")).lower().capitalize()
employee1 = name, salary, currency
print(f"hello {employee1[0]}.\nThis is your current Salary: {employee1[1]}/week\nAnd Currency: {employee1[2]}")
# add currency symbol and Currency value.
 
alt1 = "raise"
alt2 = "information"
alt3 = "resignation"

print(f"What can i help you with {employee1[0]}?\nChoose between these alternatives:\n[1]{alt1}\n[2]{alt2}\n[3]{alt3}")
options = ["1", "2", "3"]
question = input()
if question == "1":
    tries = 1
    while True:
        print("How much of a raise are you suggesting?")
        a_raise = float(input())
        procent_raise = round((a_raise / employee1[1])) # procent calc.
        print(procent_raise)
        if procent_raise > 13 or tries == 1:
            print(f"{procent_raise}%?? Nope..")
            tries = 0        
        elif procent_raise <= 13 and tries == 0:
            print(f"{procent_raise}%?? .. ok, you got it!")
            break
    
elif question == "2":
    print("information is not available at this time..")
elif question == "3":
    print("leave your resignation letter to the office on ground level.")

