print("=== MOBILE LOAD PROMO ===")

name = input("Enter customer name: ")

print("1. 50 Pesos - 3 Days")
print("2. 100 Pesos - 7 Days")
print("3. 150 Pesos - 15 Days")

choice = int(input("Choose a promo: "))

if choice == 1:
    promo = "50 Pesos"
    days = 3
elif choice == 2:
    promo = "100 Pesos"
    days = 7
elif choice == 3:
    promo = "150 Pesos"
    days = 15
else:
    promo = "Invalid"
    days = 0

print("\nCustomer:", name)
print("Promo:", promo)
print("Validity:", days, "days")