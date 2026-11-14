print("=== SIMPLE BANK ===")

balance = 1000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Choose an option: "))

if choice == 1:
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful!")
elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance and amount > 0:
        balance -= amount
        print("Withdrawal successful!")
    else:
        print("Invalid amount or insufficient balance.")
elif choice == 3:
    print("Your balance is:", balance)
else:
    print("Invalid choice.")

print("Remaining Balance: PHP", balance)