class Account():
    
    # Constructor
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    # Methods
    def deposit(self, amount):
        print("Deposit Accepted")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Fail to withdraw \nAvailable funds: ${self.balance} \nWithdraw amount: ${amount}")
        else:
            print("Withdrawal successful")
            self.balance -= amount
            print(f"Available funds: ${self.balance} \nWithdraw amount: ${amount}")
  
    # Special methods
    
    # Print object values
    def __str__(self):
        return (f"Account owner: {self.owner} \nAccount balance: ${self.balance}")
    # Delete object
    def __del__(self):
        print("Your bank account has been deleted")

    # Menu option
    def menu(self):
        print("\nOption:")
        print("1. Check account balance")
        print("2. Withdraw funds")
        print("3. Deposit funds")
        print("4. Delete account")
        print("5. EXIT")

    def option(self, num = 0):
        # Prompt for option
        num = 0
        while num != 5:
            # Display menu
            menu()
            num = int(input("Enter your option: "))
            if num == 1:
            # Display account information
                print(acct1)
            elif num == 2:
                # Prompt if user want withdraw money  
                withdraw = int(input("Withdraw amount: "))
                withdraw(withdraw)
            elif num == 3:
                # Prompt if user want to deposit money
                deposit = int(input("Deposit amount: "))
                deposit(deposit)
            elif num == 4:
                delete = input("Do you want to delete your account? (Y/N): ")
                if delete.lower() == 'y':
                    del acct1
                    break
            else:
                print("Invalid option")
        print("Thankyou for banking with us!")