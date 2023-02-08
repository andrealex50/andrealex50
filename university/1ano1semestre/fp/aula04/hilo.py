# Complete the code to make the HiLo game...

import random
import math

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    tries = 0
    number = 0
    while number != secret:
        tries = tries + 1
        number = int(input('número? '))
        if number < secret:
            print('Low')
        elif number > secret:
            print('High')
        elif number == secret:
            print('You got it!')
            print('It took you {} tries'.format(tries))
        
main()
