inventory = ["Apples", "Bananas", "Carrots"]

new_product = "Oranges"
if new_product not in inventory: 
    inventory.append(new_product)
    print(f"{new_product} added to inventory")
else:
    print(f"{new_product} is already in inventory")

product_check = "Bananas"
if product_check in inventory:
    print(f"{product_check} is in stock")
else:
    print(f"{product_check} is not in stock")

product_to_remove = "Carrots"
if product_to_remove in inventory:
    inventory.remove("Carrots")
    print(f"{product_to_remove} removed from inventory")
else:
    print(f"{product_to_remove} not found in inventory")

print("Updated inventory", inventory)