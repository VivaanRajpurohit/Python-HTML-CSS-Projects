pre_determined_number = 50
users_input = int(input("Please choose a number between 1 and 100: "))

while True:
    if pre_determined_number == users_input:
        print(f"You guessed the number {pre_determined_number} correctly")
        break
    else:
        print("You got it wrong, try again!")
        users_input = int(input("Please choose a number between 1 and 100: "))  # Update the user's input