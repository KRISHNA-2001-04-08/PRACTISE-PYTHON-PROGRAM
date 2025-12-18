balance = 5000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin != pin:
    print("❌ Invalid PIN")
else:
    # ATM runs for 5 operations only
    for _ in range(5):
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("💰 Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("✅ Deposited successfully")
            else:
                print("❌ Invalid amount")

        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("✅ Collect your cash")
            else:
                print("❌ Insufficient balance or invalid amount")

        elif choice == 4:
            print("🙏 Thank you for using ATM")
            break

        else:
            print("❌ Invalid choice")
