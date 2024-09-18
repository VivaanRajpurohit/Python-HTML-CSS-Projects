item_name = input("What is the name of the item: ")
quantity = int(input("How many of this item did you buy: "))
item_price = float(input("How much did this item cost: "))

total_price = quantity * item_price

receipt = "Item: {item}, Quantity: {quantity}, Price Per Item: ${price:.2f}, Total Cost: ${total:.2f}.".format(
    item=item_name, quantity=quantity, price=item_price, total=total_price
)

print(receipt)
