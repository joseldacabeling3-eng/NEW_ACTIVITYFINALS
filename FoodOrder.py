print("=== FOOD ORDERING ===")

print("1. Burger - 80")
print("2. Pizza - 120")
print("3. Fries - 50")

choice = int(input("Choose your food: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    food = "Burger"
    total = 80 * quantity
elif choice == 2:
    food = "Pizza"
    total = 120 * quantity
elif choice == 3:
    food = "Fries"
    total = 50 * quantity
else:
    food = "Invalid"
    total = 0

print("\nFood:", food)
print("Total: PHP", total)