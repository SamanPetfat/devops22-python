while True:
    user_input = input("Enter text, or Enter stop to quit: ")
    if user_input == "stop":
        break
print(f"{user_input} has a lenght of {len(user_input)}")