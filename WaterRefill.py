print("=== WATER REFILLING STATION ===")

print("1. Small Container - 20")
print("2. Medium Container - 30")
print("3. Large Container - 40")

choice = int(input("Choose container size: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    size = "Small"
    total = 20 * quantity
elif choice == 2:
    size = "Medium"
    total = 30 * quantity
elif choice == 3:
    size = "Large"
    total = 40 * quantity
else:
    size = "Invalid"
    total = 0

print("\nContainer:", size)
print("Quantity:", quantity)
print("Total Payment: PHP", total)