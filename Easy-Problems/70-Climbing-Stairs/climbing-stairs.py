# Problem #70 - CLIMBING STAIRS --> PLUS ADDITIONAL PROBLEM

# There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# ADD-ON PROBLEM
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

#---------------------------------------------------------------------------------------------------------------------------

# In the first problem, each step is either the combinations of the step prior or the combinations of the step two prior
    # We know we can only move 1 or 2 steps at a time, so step 2 has the same amount of possibilites as Step 0 + Step 1
        # Step 3 has the same amount of possibilities as Step 1 + Step 2 --> And so on


# In the second portion, we are given the set of steps we can take at any one time
    # This is a bit confusing but still offers the same logic
        # Each step has the same amount of combinations as the step that is that many steps prior
            # So if our number is 7, that steps has the total combinations of step 6 + step 4 + step 2

#---------------------------------------------------------------------------------------------------------------------------

import time

# MEMOIZATION AND ITERATION --> Utilize the array to store the combinations of each step already traversed
def climbStairs(n: int) -> int:
    callTimes = [] # For time and call counter

    # First handle the base cases (There are no other combinations)
    if n == 0 or n == 1: return 1
    
    # Builds an array of all the possible combinations at a given index
    memo = [0] * (n + 1)

    # Set the first two indexes (0 & 1 to the base case)
    memo[0], memo[1] = 1, 1

    # For each index, compute the maximum combinations available at that index
    for i in range(2, n + 1):
        #---------------------------------------------    
        startTime = time.time()
        #---------------------------------------------

        memo[i] = memo[i - 1] + memo[i - 2]

        #---------------------------------------------
        endTime = time.time()
        callTimes.append(endTime-startTime)
        #---------------------------------------------

    print(f"Total time taken by climbStairs: {sum(callTimes):.6f} seconds")
    print(f"Number of calls: {len(callTimes)}")

    # Return the index (step) we are looking to find
    return memo[n]


def climbStairsX(n: int, X: set[int]) -> int:
    # First handle the base case
    if n == 0: return 1

    # Builds an array of all the possible combinations at a given index
    memo = [0] * (n + 1)

    memo[0] = 1

    for i in range(1, n + 1):
        for x in X: # Checks all possible step values
            if i - x >= 0: # If the step was available to be taken already (positive integer return value)
                memo[i] = memo[i - x] # We add the combinations available at that step to the total combinations at this step

    return memo[n]

#---------------------------------------------------------------------------------------------------------------------------

# MEMOIZATION --> CACHING
    # Greatly reduce time complexity here --> A problem where we build off subproblems
    # In these solutions, the recursive calls take more time that the iterative solution above

def climbStairsMemo(n: int) -> int:
    memo = {}

    callTimes = [] # For time and call counter

    def climb(n: int) -> int:
        #---------------------------------------------
        startTime = time.time()
        #---------------------------------------------

        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = climb(n - 1) + climb(n - 2) # Recursive call on prior steps

        #---------------------------------------------
        endTime = time.time()
        callTimes.append(endTime-startTime)
        #---------------------------------------------

        return memo[n]
    
    result = climb(n)
    
    print(f"Total time taken by climbStairsMemo: {sum(callTimes):.6f} seconds")
    print(f"Number of calls: {len(callTimes)}")

    return result

def climbStairsMemoX(n: int, X: set[int]) -> int:
    memo = {}

    def climb(n: int) -> int:
        if n == 0: return 1

        if n in memo: return memo[n]

        memo[n] = 0

        for step in X:
            if n - step >= 0:
                memo[n] += climb(n - step) # Recursive call on remaining steps provided

        print('Within Helper', memo)

        return memo[n]
    
    return climb(n)


print('Base Prob', climbStairs(50))
print('Base with Steps', climbStairsX(5, {1, 3, 5}))

print('Base with Memo', climbStairsMemo(50))
print('Base with Memo & Steps', climbStairsMemoX(5, {1, 3, 5}))