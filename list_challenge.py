import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:  # while there is something in the diamonds list
    user_input = input('Enter) ... Pick a card\nQ) ... Quit\n')  # get user input
    if user_input.upper() == 'Q':  # set input to lowercase : if they select q or Q
        break  # exit loop
    else:  # if user wishes to continue
        length = len(diamonds)  # get length
        newCard = diamonds[random.randint(0, length - 1)]  # randomly select new card
        diamonds.remove(newCard)  # remove from original list
        hand.append(newCard)  # append to user's hand
        print('Your hand : %s ' % hand)  # print users hand
        print('Remaining cards : %s ' % diamonds)  # print original deck
    if not diamonds:  # if there is nothingn left in the diamonds list
        print('There are no more cards to pick')
