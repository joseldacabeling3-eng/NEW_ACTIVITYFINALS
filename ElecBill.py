print("=== ELECTRIC BILL ===")

name = input("Enter customer name: ")
units = float(input("Enter electricity units: "))

if units >= 0 and units <= 50:
    bill = units * 5
elif units <= 100:
    bill = units * 7
elif units > 100:
    bill = units * 10
else:
    bill = -1

if bill >= 0:
    print("\nCustomer:", name)
    print("Units Used:", units)
    print("Electric Bill: PHP", bill)
else:
    print("Invalid units.")