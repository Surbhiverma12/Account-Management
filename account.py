
def read_account(account, code):
    with open("account_details.txt", "r") as file:
        for i in file:
            name,acc_no, acc_code, balance = i.split()
            if acc_no == account and acc_code == code:
                return name, acc_no, acc_code, float(balance)
        else:
            print("Account no. or code is invalid!!")
            return None


def update_account(account, code, new_balance):
    lines = []
    with open("account_details.txt", 'r') as file:
        for i in file:
            name, acc_no, acc_code, balance = i.split()

            if acc_no == account and acc_code == code:
                lines.append(f'{name} {acc_no} {acc_code} {new_balance}\n')
                print(lines)
            else:
                lines.append(i)
                # print(lines)
    with open("account_details.txt", 'w') as file:
        file.writelines(lines)

def add_account():
    name = input("Enter account holder's name: ")
    account = input("Enter new account number: ")
    code = input("Set a secret code for the account: ")
    initial_balance = float(input("Enter the initial balance: "))

    # Check if the account already exists
    if read_account(account, code) is None:
        with open("account_details.txt", "a") as file:
            file.write(f"{name} {account} {code} {initial_balance}\n")
        print(f"\nAccount for {name} created successfully with Account No: {account}!")
    else:
        print("Account already exists with the same number or code!")



def deposit(account, code, amount):
    name, acc_no, acc_code, balance = read_account(account, code)
    balance+=amount
    update_account(account, code, balance)
    print(f'\nDeposited: {amount} \nCurrent balance: {balance}')

def withdraw(account, code, amount):
     name, acc_no, acc_code, balance = read_account(account, code)
     if balance > amount:
         balance-=amount
         update_account(account, code, balance)
         print(f'\nWithdraw: {amount} \nCurrent balance: {balance}')
     else:
        print("\nNot sufficient balance")
        print(f'\nWithdraw: {amount} \nCurrent balance: {balance}')
        return




def main_menu():
    print("Welcome to Bank")

    while True:
        print("\n1. Add New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            option = int(input("\nEnter your choice: "))

            if option == 1:
                add_account()

            elif option == 2:
                account = input("Enter the account number: ")
                code = input("Enter the code: ")
                if read_account(account, code) is None:
                    continue
                amount = float(input("\nEnter the deposit amount: "))
                deposit(account, code, amount)
                print("\nThank you!\n")

            elif option == 3:
                account = input("Enter the account number: ")
                code = input("Enter the code: ")
                if read_account(account, code) is None:
                    continue
                amount = float(input("\nEnter the withdrawal amount: "))
                withdraw(account, code, amount)
                print("\nThank you!\n")

            elif option == 4:
                print("Goodbye!")
                break

            else:
                print("\nInvalid choice, try again!!")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

# Call the main menu to start the program
main_menu()
