print("=== SHOPPING CART ===")

item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\nItem:", item)
print("Price: PHP", price)
print("Quantity:", quantity)
print("Total: PHP", total)