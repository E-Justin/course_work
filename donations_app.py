from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {
    'admin': 'password123',
}

donations = []

authorized_user = ''

while True:
    show_homepage()
    if authorized_user == '' or authorized_user is None:  # if authorized_user is left blank
        print('You must be logged in to donate. ')
    else:
        print('Logged in as : %s ' % authorized_user)

    # get user selection
    selection = input('Please select an option from the menu : ')

    if selection == '1':
        # prompt user to enter credentials
        username = input('Enter your username ')
        password = input('Enter your password ')
        authorized_user = login(database, username, password)
    elif selection == '2':
        # prompt user to enter credentials
        username = input('Enter your username ')
        password = input('Enter your password ')
        authorized_user = register(database, username)
        if authorized_user != None or authorized_user != '':  # if a valid string was returned
            # add username and password to dictionary
            # add username : password to dictionary
            database[username] = password
    elif selection == '3':
        if authorized_user == '' or authorized_user is None:  # if user is not logged in
            print('You are not logged in . ')
        else:
            donation_string = donate(authorized_user)
            # append donation string to donations list
            donations.append(donation_string)
    elif selection == '4':
        show_donations(donations)
    elif selection == '5':
        print('Goodbye')
        break
    else:
        print('*** Invalid selection ***')
