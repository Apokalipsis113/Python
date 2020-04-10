###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
import math
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

# Another hint:
guess = input("What is your guess? 3 digist separated by space")
print(guess)

tmp_guess = guess.split()
print(tmp_guess)
tmp = []
for i in tmp_guess:
    tmp.append(int(i))
print(tmp)

def check(guess, source):
    MATCH = "Match"
    CLOSE = "Close"
    FAR = "Far"
    result = str()
    for i in range(len(guess)):
        if guess[i] == source[i]:
            result = result + MATCH + " "
        elif abs( guess[i] - source[i]) == 1:
            result = result + CLOSE + " "
        else:
            result = result + FAR + " "
    return result



print(check(tmp, digits[:3]))


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
