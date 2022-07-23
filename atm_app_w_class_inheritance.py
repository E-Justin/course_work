class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        #new_name = input('What do you want to change your name to? ')
        new_name = 'Bobby'
        self.name = new_name

    def change_pin(self):
        #new_pin = int(input('What do you want to change your pin to? '))
        new_pin = 4321
        self.pin = new_pin

    def change_password(self):
        #new_password = input('What do you want to change your password to? ')
        new_password = 'newpassword'
        self.password = new_password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print('%s has an account balance of: %d ' % (self.name, self.balance))

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, amount: float, transfer_to: str) -> bool:
        print('You are transfering %d to %s' % (amount, transfer_to.name))
        print('Authentication required')
        your_pin = int(input("Enter your pin: "))  # get pin from user
        if your_pin == self.pin:  # if they entered the correct pin
            self.balance -= amount  # decrement user balance by amount transfered
            # increment other person's balance by the amount transfered
            transfer_to.balance += amount
            print('Transfer Authorized')
            print('Transfering %d to %s ' % (amount, transfer_to.name))
            return True
        else:  # if the pin entered was incorrect
            print('Invalid PIN. Transaction canceled. ')
            return False

    def request_money(self, amount: float, request_from: str) -> bool:
        print('You are requesting %d from %s ' % (amount, request_from.name))
        print('User authentication is required.... ')
        # get other person's pin from user
        their_pin = int(input("Enter %s's pin : " % (request_from.name)))
        if their_pin == request_from.pin:  # if they entered the correct pin
            # get password from user
            your_password = input("Enter your password : ")
            if your_password == self.password:  # if password entered is correct
                self.balance += amount  # increment users's balance by amount requested
                # decrement other person's balance by amount requested
                request_from.balance -= amount
                print('Request authorized')
                return True
        if their_pin != request_from.pin:  # if incorrect pin was given
            print('Invalid password. Transaction canceled')
        if your_password != self.password:  # if incorrect password was given
            print('Invalid password. Transaction canceled')
            return False


###   Driver Code for Task 1  ###
'''User1 = User('Bob', 1234, 'password')

print('Name    : %s\nPin     : %d\nPassword: %s' %
      (User1.name, User1.pin, User1.password))'''
###          END TASK 1       ###

###     TASK 2 Driver Code    ###
'''User1 = User('Bob', 1234, 'password')
print(User1.name, User1.pin, User1.password)
User1.change_name()
User1.change_pin()
User1.change_password()
print(User1.name, User1.pin, User1.password)'''
### End of Task 2 Driver Code ###

###     TASK 3 Driver Code    ###
'''BankUser1 = BankUser('Bob', 1234, 'password')
print(BankUser1.name, BankUser1.pin, BankUser1.password, BankUser1.balance)'''
### End of Task 3 Driver Code ###

###     TASK 4 Driver Code    ###
'''U1 = BankUser('Bob', 1234, 'password')
U1.show_balance()
U1.deposit(1000)
U1.show_balance()
U1.withdraw(500)
U1.show_balance()'''
### End of Task 4 Driver Code ###

###     TASK 5 Driver Code    ###
user1 = BankUser('Bob', 1234, 'password')  # instantiate class
user2 = BankUser('Mustafa', 1010, 'password')  # instantiate class

user2.deposit(5000)  # deposit 5,000
# show balances
user2.show_balance()
user1.show_balance()
print(' ')


# transfer 500
if user2.transfer_money(500, user1) is True:  # if transfer was successful
    # show balances
    user2.show_balance()
    user1.show_balance()
    print(' ')
    user2.request_money(250, user1)  # request 250

# show balances again
user2.show_balance()
user1.show_balance()
### End of Task 5 Driver Code ###
