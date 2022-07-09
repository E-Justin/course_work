from banking_pkg import account # import module


def atm_menu(name): # display menu
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")  # table header

name = input("Enter name to register: ")  # get name
pin = input("Enter PIN: ")  # get pin
balance = 0  # set balance to 0

print("%s has been registered witha a starting balance of $%d" % (name, balance))


while True:
    print('##### LOGIN #####')
    name_to_validate = input('Enter name : ')  # re-enter name
    pin_to_validate = input('Enter PIN : ')  # re-enter pin
    if name == name_to_validate and pin == pin_to_validate:  # if they are the same, continue
        print('Login successful! ')
        break  # exit loop
    else:  # if not, let user know it was incorrect, and prompt again
        print('Invalid credentials! \n')

while True:
    atm_menu(name)  # display menu
    option = input("Choose an option: ")  # user input to select an option
    if option == '1':
        account.show_balance(balance)  # module account function call to display balance
    elif option == '2':
        balance = account.deposit(balance)  # module account function call to update balance after deposit
        account.show_balance(balance)  # module account function call to update to display balance after deposit
    elif option == '3':
        balance = account.withdraw(balance)  # module account function call to update balance after withdraw
        account.show_balance(balance)  # module account function call to display balance after withdraw
    else:
        account.logout(name)  #module account function call to logout
        break  # exit loop
