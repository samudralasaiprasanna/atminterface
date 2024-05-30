class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0.0

class ATM:
    def __init__(self):
        self.users = {}  # User ID to User object mapping
        self.current_user = None

    def add_user(self, user_id, pin):
        user = User(user_id, pin)
        self.users[user_id] = user

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            print("Login successful. Welcome, {}!".format(user_id))
        else:
            print("Invalid user ID or PIN. Please try again.")

class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

class Withdraw:
    def withdraw_amount(self, amount, current_user):
        if amount is None or amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return
        if amount > current_user.balance:
            print("Insufficient funds. Please try a lower amount.")
            return
        current_user.balance -= amount
        print("Amount withdrawn: ${}".format(amount))

class Deposit:
    def deposit_amount(self, amount, current_user):
        if amount is None or amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        current_user.balance += amount
        print("Amount deposited: ${}".format(amount))

class Transfer:
    def make_transfer(self, target_user, amount, current_user, users,transaction_history):
        if amount is None or amount <= 0:
            print("Invalid transfer amount. Please enter a positive value.")
            return
        if target_user == current_user.user_id:
            print("You cannot transfer money to yourself.")
            return
        if amount > current_user.balance:
            print("Insufficient funds. Please choose a lower transfer amount.")
            return
        if target_user not in users:
            print("User {} does not exist.".format(target_user))
            return
        target_user_obj = users[target_user]
        current_user.balance -= amount
        target_user_obj.balance += amount
        transaction_history.add_transaction("Transfer of ${}".format(amount,target_user))
        print("Amount transferred to user {}: ${}".format(target_user, amount))

def main():
    atm = ATM()
    transaction_history = TransactionHistory()
    withdraw = Withdraw()
    deposit = Deposit()
    transfer = Transfer()
    
    atm.add_user("user123", "1234")
    atm.add_user("user456","9866")
    atm.add_user("user789","6281")

    while True:
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        atm.login(user_id, pin)

        if atm.current_user:
            while True:
                print("\nSelect an option:")
                print("1. Transactions History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")
                
                choice = input("Enter your choice: ")

                if choice == "1":
                    # Display transaction history
                    if not transaction_history.history:
                        print("No transactions yet.")
                    else:
                        print("Transatin history")
                    for transaction in transaction_history.history:
                        print(transaction)
                elif choice == "2":
                    amount = float(input("Enter the amount to withdraw: $"))
                    withdraw.withdraw_amount(amount,atm.current_user)
                elif choice == "3":
                    try:
                        amount = float(input("Enter the amount to deposit: $"))
                        deposit.deposit_amount(amount, atm.current_user)
                    except ValueError:
                        print("invalid amount.please enter a valid amount to deposite")
                elif choice == "4":
                    target_user = input("Enter the user ID to transfer: ")
                    amount = float(input("Enter the amount to transfer: $"))
                    transfer.make_transfer(target_user, amount, atm.current_user, atm.users,transaction_history)
                elif choice == "5":
                    print("Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()