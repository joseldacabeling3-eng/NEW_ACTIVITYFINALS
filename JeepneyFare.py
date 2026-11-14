print("=== JEEPNEY FARE CALCULATOR ===")

name = input("Enter passenger name: ")
distance = float(input("Enter distance in kilometers: "))

if distance > 0 and distance <= 4:
    fare = 13
elif distance > 4:
    fare = 13 + (distance - 4) * 1.50
else:
    fare = 0

if fare > 0:
    print("\nPassenger:", name)
    print("Distance:", distance, "km")
    print("Fare: PHP", fare)
else:
    print("Invalid distance.")