print("=== SCHOOL SUPPLIES ===")

print("1. Notebook - 25")
print("2. Ballpen - 15")
print("3. Pencil - 10")

choice = int(input("Choose an item: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Notebook"
    total = 25 * quantity
elif choice == 2:
    item = "Ballpen"
    total = 15 * quantity
elif choice == 3:
    item = "Pencil"
    total = 10 * quantity
else:
    item = "Invalid"
    total = 0

print("\nItem:", item)
print("Total: PHP", total)