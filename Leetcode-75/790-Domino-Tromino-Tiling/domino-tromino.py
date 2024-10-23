# PROBLEM #790 - DOMINO AND TROMINO TILING

# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

#   X    &    X X
#   X         X

# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7.

# In a tiling, every square must be covered by a tile. 
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

#---------------------------------------------------------------------------------------------------------------------------

# If N = 0 --> There is only one way to tile (do nothing)
# If N = 1 --> There is only one way to tile (domino)
# If N = 2 --> There are two ways to tile (domino vertical or horizontal)
# If N = 3 --> There are three ways to tile with dominoes and two additional ways with trominoes
# If N = 4 --> There are five ways to tile with dominoes and six additional ways with trominoes
# If N = 5 --> There are eleven ways to tile with dominoes and 13 additional ways with trominoes

#---------------------------------------------------------------------------------------------------------------------------

# What are our possible combinations?

#   full[n] = full[n-1] + full[n-2] + topMissing[n-1] + bottomMissing[n-1]

#       We can add a vertical domino at n-1, two horizontal dominoes at n-2 OR we need to add an L shape with either the top or bottom missing previously

#   topMissing[n] = bottoMissing[n-1] + full[n-2] --> n-2 because we need two empty spaces to add the tromino
#   bottomMissing[n] = topMissing[n-1] + full[n-2] --> Same as topMissing, must satisfy condition when full

def numTilings(n: int) -> int:
    MOD = 10 ** 9 + 7

    # Set our base cases for combinations --> We know at board 0 and board 1 the combinations

    full, topMiss, bottomMiss = {0:1, 1:1}, {0:1, 1:0}, {0:1, 1:0}

    for i in range(2, n+1): # We have the first two indexes completed --> Run till we include n
        full[i] = full[i-1] + full[i-2] + topMiss[i-1] + bottomMiss[i-1] # All possible combinations to complete the board
        topMiss[i] = bottomMiss[i-1] + full[i-2] # Ways to build a board where the top is missing within the contraint
        bottomMiss[i] = topMiss[i-1] + full[i-2] # Ways to build a board where the bottom is missing within the constraint

    return full[n] % MOD

# Can reduce space complexity by only keeping track of the four positions at any given time --> Rather than total combinations at each index
#   This solution becomes O(1) space complexity because only 4 variables are stored and updated at any time

def numTilingsRework(n: int) -> int:
    MOD = 10 ** 9 +7

    # Four variables for position to track --> Previous Full is n-2 and full is n-1
    previousFull, full, topMiss, bottomMiss = 1, 1, 0, 0

    for _ in range(2, n+1):
        previousFull, full, topMiss, bottomMiss = full, full + previousFull + topMiss + bottomMiss, bottomMiss + previousFull, topMiss + previousFull

    return full % MOD

#---------------------------------------------------------------------------------------------------------------------------

#RECURSIVE APPROACH

from functools import lru_cache

def numTilingsRecur(n: int) -> int:
    MOD = 10**9 + 7

    @lru_cache # Decorator to cache prior results to limit computing --> Still O(n^2) Time Complexity
    def countWays(topRow: int, bottomRow: int) -> int:

        # firstRow: 
            # Represents the number of columns covered in the first row of the board
            # This keeps track of how many spaces have been filled in the top row
        # bottomRow: 
            # Represents the number of columns covered in the second row of the board
            # This keeps track of how many spaces have been filled in the bottom row

        if topRow > n or bottomRow > n: return 0 # Means we have gone beyond the boundary of the board
        if topRow == n and bottomRow == n: return 1 # Means that we have succeeded in tiling the board to that combination (Top and Bottom are full)

        ways = 0 # Intialization for possible ways to tile

        if topRow == bottomRow: # Both rows have the same number of tiles covered (No open spaces)
            ways = (
                countWays(topRow + 2, bottomRow + 2) + # Place a 2x2 square (Covers both rows simultaneously)
                countWays(topRow + 1, bottomRow + 1) + # Place two 2x1 tiles (One in each row)
                countWays(topRow + 2, bottomRow + 1) + # Place an L shaped Tromino tile
                countWays(topRow + 1, bottomRow + 2) # Place an inverted Tromino tile
            )
        elif topRow > bottomRow: # If the topRow has more tiles than the bottomRow
            ways = (
                countWays(topRow, bottomRow + 2) + # Place one horizontal domino (1x2) in Bottom Row
                countWays(topRow + 1, bottomRow + 2) # Place an inverted Tromino tile
            )
        else: # If the bottomRow has more tiles than the topRow
            ways = (
                countWays(topRow + 2, bottomRow) + # Place one horizontal domino (1X2) in Top Row
                countWays(topRow + 2, bottomRow + 1) # Place an L shaped Tromino tile
            )

        return ways % MOD
    
    return countWays(0,0)

# SPACE COMPLEXITY --> O(n^2)
# TIME COMPLEXITY --> O(n^2)

#---------------------------------------------------------------------------------------------------------------------------

# ITERATIVE APPROACH

def numTilingsIter(n: int) -> int:
    if n == 2: return 2 
    if n <= 1: return 1

    MOD = 10**9 + 7

    dp = [0] * (n + 1) # Creates an array up to size n
    dp[0] = 1 # One way to fill empty board --> Do Nothing
    dp[1] = 1 # One way to fill n = 1 board --> Vertical Tile
    dp[2] = 2 # Two ways to fill n=2 board --> Two Vertical or Two Horizontal Tiles

    # [1, 1, 2] -> Index is the length of the board
    # dp[3] = 2 * dp[3-1] + dp[3-3] --> 2 * dp[2] + dp[0] --> 2 * 2 + 1 = 5

    for i in range(3, n + 1):
        dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
        # 2 * dp[i-1]
            # Place one vertical domino covering the top and bottom row (1x2 piece)
            # The remaining board is 2 * dp[i-1]
        # dp[i-3]
            # Place a Tromino tile
    return dp[n]

# SPACE COMPLEXITY --> O(n)
# TIME COMPLEXITY --> O(n)

#---------------------------------------------------------------------------------------------------------------------------

print(numTilings(4))
print(numTilingsRework(5))

print(" ")

print(numTilingsRecur(4))
print(numTilingsRecur(5))

print(" ")

print(numTilingsIter(4))
print(numTilingsIter(5))