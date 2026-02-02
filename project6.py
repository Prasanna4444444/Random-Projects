balance = 10000  # initial balance

def show_menu():
    print("\n🏧 SIMPLE ATM SYSTEM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"💰 Your current balance is: Rs. {balance}")

    elif choice == "2":
        amount = int(input("Enter amount to deposit: Rs. "))
        if amount > 0:
            balance += amount
            print(f"✅ Rs. {amount} deposited successfully.")
        else:
            print("❌ Invalid amount.")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("❌ Invalid amount.")
        elif amount > balance:
            print("⚠️ Insufficient balance.")
        else:
            balance -= amount
            print(f"✅ Rs. {amount} withdrawn successfully.")

    elif choice == "4":
        print("👋 Thank you for using the ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
