import random


def guess_random_number(tries: int, start: int, stop: int):
    # get a random int between the start and stop arguments
    random_num = random.randint(start, stop)
    while tries != 0:  # while you have not ran out of attempts
        print('Tries remaining : %d' % tries)
        guess = int(input('Guess a number between %d and %d : ' %
                    (start, stop)))  # get user's guess
        if random_num > guess:  # if number guessed is lower than the random number
            print('Guess higher! ')
        elif random_num < guess:  # if number guessed is higher than random number
            print('Guess lower! ')
        else:  # if user guessed correctly
            print('You guessed the correct number!')
            return
        tries -= 1  # one less attempt remaining
    print('You failed. The number was %d :( ' % random_num)



