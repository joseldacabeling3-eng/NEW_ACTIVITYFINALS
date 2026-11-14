print("=== LAUNDRY SERVICE ===")

name = input("Enter customer name: ")
kilos = float(input("Enter clothes weight in kilos: "))

if kilos > 0:
    total = kilos * 35
    print("Customer:", name)
    print("Weight:", kilos, "kg")
    print("Total: PHP", total)
else:
    print("Invalid weight.")