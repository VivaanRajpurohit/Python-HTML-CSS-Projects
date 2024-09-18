def safe_division():
    try:
        divisor = int(input("Input a number to divide 10 by: "))
        result = 10 / divisor
    except ZeroDivisionError as e:
        print("Error: You cant divide by zero!")
    except ValueError as e:
        print("Error: Please enter a valid integer")

safe_division()