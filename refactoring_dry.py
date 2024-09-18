item1_price = 19.99
item1_tax_rate = 0.08

item2_price = 23.50
item2_tax_rate = 0.08
def calculate_price_after_tax(price, tax_rate):
    return price + (price * tax_rate)

item1_price_after_tax = calculate_price_after_tax(item1_price, item1_tax_rate)
item2_price_after_tax = calculate_price_after_tax(item2_price, item2_tax_rate)

print(f"Item 1 price after tax: ${item1_price_after_tax: .2f}")
print(f"Item 2 price after tax: ${item2_price_after_tax: .2f}")