def calculate_total(price):
    total = 0
    for price in price:
        total += price
    return total

cart_prices = [12.99, 23.50, 9.99, 5.99]
total_cost = calculate_total(cart_prices)
print(f"The total cost for the items in the cart is: ${int(total_cost)}")