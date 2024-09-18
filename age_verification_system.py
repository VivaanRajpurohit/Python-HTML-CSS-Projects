while True:
    user_input = input("Please enter your age or type 'quit' to exit: ")

    if user_input == "quit":
        print("exiting the age verification system.")
        break

    try:
        age = int(user_input)
    except ValueError:
        print("Please enter a valid numerical age.")
        continue
    
    if 0 >= age >= 120:
        print("Please enter a realistic age.")
        continue
    
    if age < 18:
        print("you must be older than 18 to participate.")
        
    print("Sucess! The age was verified, you are eligible to participate")
    break
else:
    print("The age verification system was exited")