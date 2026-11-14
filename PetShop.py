print("=== PET SHOP ===")

print("1. Dog Food - 120")
print("2. Cat Food - 100")
print("3. Fish Food - 50")

choice = int(input("Choose an item: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Dog Food"
    total = 120 * quantity
elif choice == 2:
    item = "Cat Food"
    total = 100 * quantity
elif choice == 3:
    item = "Fish Food"
    total = 50 * quantity
else:
    item = "Invalid"
    total = 0

print("Item:", item)
print("Total: PHP", total)