
print("=== ELECTRIC FAN SHOP ===")

name = input("Customer name: ")

print("1. Small Fan - PHP 500")
print("2. Medium Fan - PHP 800")
print("3. Large Fan - PHP 1200")

choice = int(input("Choose fan: "))

if choice == 1:
    fan = "Small Fan"
    price = 500
elif choice == 2:
    fan = "Medium Fan"
    price = 800
elif choice == 3:
    fan = "Large Fan"
    price = 1200
else:
    fan = "Invalid"
    price = 0

print("\n=== PURCHASE DETAILS ===")
print("Customer:", name)
print("Fan:", fan)
print("Price: PHP", price)
