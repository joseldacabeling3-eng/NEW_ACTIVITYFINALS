print("=== MOVIE TICKET BOOKING ===")

name = input("Enter your name: ")

print("1. Regular - 150")
print("2. VIP - 250")

choice = int(input("Choose ticket type: "))
tickets = int(input("Number of tickets: "))

if choice == 1 and tickets > 0:
    total = 150 * tickets
    ticket = "Regular"
elif choice == 2 and tickets > 0:
    total = 250 * tickets
    ticket = "VIP"
else:
    total = 0
    ticket = "Invalid"

print("\nName:", name)
print("Ticket:", ticket)
print("Total Payment: PHP", total)