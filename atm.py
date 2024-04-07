class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            return "Insufficient funds"

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received ${amount} from {recipient.name}")
        else:
            return "Insufficient funds"

    def show_transaction_history(self):
        return self.transaction_history


class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []

    def show_transaction_history(self):
        return self.transaction_history


def main():
    atm = ATM()
    customer = Customer("Karthika")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Your balance is:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
            print("Deposit successful.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            message = atm.withdraw(amount)
            if message:
                print(message)
            else:
                print("Withdrawal successful.")
        elif choice == '4':
            amount = float(input("Enter amount to transfer: $"))
            recipient_name = input("Enter recipient's name: ")
            recipient = Customer(recipient_name)
            message = atm.transfer(amount, recipient)
            if message:
                print(message)
            else:
                print("Transfer successful.")
        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.show_transaction_history():
                print(transaction)
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
