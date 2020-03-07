# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:04:51 2019

@author: User
@name: Bank account
"""
from MyMainPackage import Account_module
        
def main():

    # Prompt user for inputs
    owner = input("Enter your name: ")
    balance = int(input("Enter your balance: "))

    # Add user input into an account object
    acct1 = Account_module.Account(owner, balance)

    # Prompt for option
    num = 0
    while num != 5:
        # Display menu
        acct1.menu()
        num = int(input("Enter your option: "))
        if num == 1:
        # Display account information
            print(acct1)
        elif num == 2:
            # Prompt if user want withdraw money  
            withdraw = int(input("Withdraw amount: "))
            acct1.withdraw(withdraw)
        elif num == 3:
            # Prompt if user want to deposit money
            deposit = int(input("Deposit amount: "))
            acct1.deposit(deposit)
        elif num == 4:
            delete = input("Do you want to delete your account? (Y/N): ")
            if delete.lower() == 'y':
                del acct1
                break
        elif num == 5:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option")




if __name__ == '__main__':
    main()