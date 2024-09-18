balance = 100

action = input("Do you want to 'check' balance or 'deposit'?: ").lower()

if action == "check":
    print(f"Your current balance is: ${balance}")
elif action == "deposit":
    new_balance = int(input("How much would you like to deposit?: "))
    print(f"Your new balance is now: ${balance + new_balance}")
else:
    print("Sorry that is an unknown command.")