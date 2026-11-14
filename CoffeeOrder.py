print("=== COFFEE ORDER ===")

name = input("Enter your name: ")
print("1. Coffee - 50")
print("2. Iced Coffee - 70")
print("3. Milk Tea - 60")

choice = int(input("Choose your drink: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    total = 50 * quantity
    drink = "Coffee"
elif choice == 2:
    total = 70 * quantity
    drink = "Iced Coffee"
elif choice == 3:
    total = 60 * quantity
    drink = "Milk Tea"
else:
    total = 0
    drink = "Invalid Order"

print("\nCustomer:", name)
print("Order:", drink)
print("Total: PHP", total)