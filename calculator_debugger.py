def simple_Calculator(number1, operation, number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        print(f"Attempting to divide {number1} by {number2}")
        try:
            return number1 / number2
        except ZeroDivisionError as e:
            print("Error: You can't divide by zero!")
            return None

print(simple_Calculator(10, "/", 10))
