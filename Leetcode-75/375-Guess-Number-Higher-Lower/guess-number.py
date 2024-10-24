# PROBLEM #375 - GUESS NUMBER HIGHER OR LOWER

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# ---------------------------------------------------------------------------------------------------------------------------

import random

# Helper function for GUESS API
def guess(picked: int, num: int) -> int:
    if num > picked: return -1
    if num < picked: return 1
    return 0

def guessNumber(n: int) -> int:
    picked = random.randint(1, n) # Pick a random number within our constraints to use with Guess API

    left, right = 1, n # Setup two pointers --> Our lower bound and our upper bound

    while left <= right: # Initialize a loop to move through the possible answers
        mid = (left + right) // 2 # Begin at the middle of the range --> DIVIDE AND CONQUER
        result = guess(picked, mid) # See where our first guess (middle) lands

        if result == 0:
            return mid # We've found the randomly picked number
        elif result == -1:
            right = mid - 1 # Move the upper bound down to be within the current mid that was too high
        else:
            left = mid + 1 # Move the lower bound up to be within the current mid that was too low

# ---------------------------------------------------------------------------------------------------------------------------

print(guessNumber(5000))