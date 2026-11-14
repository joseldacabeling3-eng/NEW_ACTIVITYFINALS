print("=== BUS TICKET ===")

name = input("Enter passenger name: ")

print("1. Calbayog to Catbalogan - 150")
print("2. Calbayog to Tacloban - 250")
print("3. Calbayog to Manila - 1200")

choice = int(input("Choose destination: "))
quantity = int(input("Number of tickets: "))

if choice == 1:
    destination = "Catbalogan"
    total = 150 * quantity
elif choice == 2:
    destination = "Tacloban"
    total = 250 * quantity
elif choice == 3:
    destination = "Manila"
    total = 1200 * quantity
else:
    destination = "Invalid"
    total = 0

print("Passenger:", name)
print("Destination:", destination)
print("Total: PHP", total)