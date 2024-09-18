user_numbers = [23, 15, 12, 30, 10, 25]
input_index = 0

numbers = []

total_sum = 0

while total_sum < 100 and input_index < len(user_numbers):
    next_number = user_numbers[input_index]
    input_index += 1

    numbers.append(next_number)
    total_sum += next_number

print(f"Numbers: {numbers}")
print(f"Total_sum: {total_sum}")