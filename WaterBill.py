print("=== WATER BILL CALCULATOR ===")

name = input("Enter customer name: ")
consumption = float(input("Enter water consumption: "))

if consumption <= 10 and consumption >= 0:
    bill = 100
elif consumption <= 20:
    bill = 100 + (consumption - 10) * 15
elif consumption > 20:
    bill = 250 + (consumption - 20) * 20
else:
    bill = -1

if bill >= 0:
    print("\nCustomer:", name)
    print("Water Consumption:", consumption)
    print("Total Bill: PHP", bill)
else:
    print("Invalid consumption.")