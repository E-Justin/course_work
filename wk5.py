import random
import pyinputplus as pyip


def guess_random_number(tries: int, start: int, stop: int):
    # get a random int between the start and stop arguments
    random_num = random.randint(start, stop + 1)
    while tries != 0:  # while you have not ran out of attempts
        print('Tries remaining : %d' % tries)
        #! bonus task 1
        guess = pyip.inputInt(prompt='Guess a number between %d and %d : ' %
                              (start, stop), min=start, lessThan=stop)  # get user's guess
        if random_num > guess:  # if number guessed is lower than the random number
            print('Guess higher! ')
        elif random_num < guess:  # if number guessed is higher than random number
            print('Guess lower! ')
        else:  # if user guessed correctly
            print('You guessed the correct number!')
            return
        tries -= 1  # one less attempt remaining
    print('You failed. The number was %d :( ' % random_num)


# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries: int, start: int, stop: int):
    # get random number between the values entered as arguments
    random_num = random.randint(start, stop + 1)
    print('The number for the program to guess is %d' %
          random_num)  # display randomly generated number
    for i in range(start, stop):  # iterate from teh start all the way to the stop number
        print('The number of tries left : %d ' %
              tries)  # show number of tries left
        # show number the program is guessing this round
        print('The program is guessing ... %d' % i)
        if i == random_num:  # if the program guessed correctly
            print('The program guessed the correct number!')
            return  # exit function
        tries -= 1  # decrement tries by 1
        if tries == 0:  # if the program has exhausted all of its attempts
            print('The program failed to guess the correct number. ')
            break  # exit function


#  guess_random_num_linear(5, 0, 10)

def guess_random_num_binary(tries: int, start: int, stop: int):
    # get random number between start and stop arguments
    random_num = random.randint(start, stop + 1)
    print('Random number to find : %d ' % random_num)
    while start <= stop and tries != 0:  # while there are attempts left and start is less than or equal to stop
        pivot = (start + stop) // 2  # get middle num
        if pivot == random_num:  # if program guessed it correctly
            print('Found it!  %d ' % random_num)
            return  # exit function
        else:  # if program guessed incorrectly
            if random_num < pivot:  # if the number to guess is less than the pivot
                stop = pivot - 1
                print('Guessing lower.')
            else:  # if the number to guess is greater than pivot
                start = pivot + 1
                print('Guessing higher. ')
        tries -= 1
    print('Your program failed to find the number')


# print(guess_random_num_binary(5, 0, 100))
