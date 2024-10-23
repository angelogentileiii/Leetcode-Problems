# PROBLEM #62 - UNIQUE PATHS

# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# ---------------------------------------------------------------------------------------------------------------------------

def uniquePathsDP(m: int, n: int) -> int:
    # Build the 2D Matrix to emulate the board given (n columns by m rows)
    dp = [[0] * n for _ in range(m)]

    print(dp)

    # Every item in the first row should be the number 1 --> there is only one possible combination to reach each square here
    for i in range(m):
        dp[i][0] = 1

    # Every item in the first column should be the number 1 --> there is only one possible combination to reach each square here
    for j in range(n):
        dp[0][j] = 1

    print(dp)

    # Each square is a result of the sum of the combinations to reach the square above and to the left of the current square
    #   Begin at index 1 for row and column because we've already set our base cases for index 0 of each
    for i in range(1, m):
        for j in range(1, n):
            top = dp[i-1][j] # The value of the cell above the current
            left = dp[i][j-1] # The value of the cell to the left of the current
            dp[i][j] = top + left
            print(dp)

    print(dp)

    # Return the cell at [m-1] row and [n-1] column as that is the last row in our matrix --> Represents the total combinations available
    return dp[m-1][n-1]

# ---------------------------------------------------------------------------------------------------------------------------

# print("Factorial: ", uniquePaths(3, 7))
print("Dynamic Program: ", uniquePathsDP(3, 7))
