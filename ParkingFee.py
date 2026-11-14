print("=== PARKING FEE ===")

name = input("Enter vehicle owner's name: ")
hours = int(input("Enter parking hours: "))

if hours > 0 and hours <= 2:
    fee = 30
elif hours > 2:
    fee = 30 + (hours - 2) * 10
else:
    fee = 0

print("Owner:", name)
print("Parking Fee: PHP", fee)