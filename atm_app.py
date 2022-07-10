from banking_pkg import account  # import module


def atm_menu(name):  # display menu
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

while True:  # loop to make sure name entered is between 1 and 10 characters long
    name = input("Enter name to register: \n")  # get name
    length = len(name)  # get length of name entered
    if length <= 10 and length >= 1:  # if length is between 1 and 10
        break  # exit loop and move to getting pin
    else:  # let user know why the name entered was not valid
        print("Name must be between 1 and 10 characters long\n")

while True:  # loop to make sure pin entered is 4 digits long
    pin = input("Enter a 4 digit PIN: \n")  # get pin
    length = len(pin)  # get length
    if length == 4:  # make sure it is 4 digits
        break  # exit loop after validation
    else:  # if the pin is not 4 digits long
        # let user know why validation failed
        print("You must enter a 4 digit pin \n")
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
        # module account function call to display balance
        account.show_balance(balance)
    elif option == '2':
        # module account function call to update balance after deposit
        balance = account.deposit(balance)
        # module account function call to update to display balance after deposit
        account.show_balance(balance)
    elif option == '3':
        # module account function call to update balance after withdraw
        balance = account.withdraw(balance)
        # module account function call to display balance after withdraw
        account.show_balance(balance)
    else:
        account.logout(name)  # module account function call to logout
        break  # exit loop
