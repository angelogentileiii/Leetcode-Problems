# PROBLEM #1267 - COUNT SERVERS THAT COMMUNICATE

# You are given a map of a server center, represented as a m * n integer matrix grid
#   - Where 1 means that on that cell there is a server and 0 means that it is no server

# Two servers are said to communicate if they are on the same row or on the same column

# Return the number of servers that communicate with any other server

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We need to count the occurences of servers in each row and column
#   - If there are more than one in either a row or column --> We have connected servers

# We should only update the result based on the individual number of connected computers --> Ensure we do not double count connected computers

# Then we can check if there are more than one comp in a column or row to update our result

#  We can use two simultaneous arrays to track the number of computers in each row/column (corresponding to the 0-index of the array)
#   - Then we can loop through the grid and compare the computer locations to the total in the row or column
#       - If we have a computer and the row or column total is more than 1, we have computers that can communicate and can add to our result

# ---------------------------------------------------------------------------------------------------------------------------


def countServer(grid: list[list[int]]) -> list[int]:
    print("Computer Grid: ")
    print("\n".join(map(str, grid)))
    print()

    rows = len(grid)
    cols = len(grid[0])

    # Initialize two arrays, one to track the total number of comps per row and one to track total number of comps per column
    #   - Each index represents the corresponding 0-indexed item --> First Row is index 0 and First Column is index 0
    row_comps: list[int] = [0] * rows
    col_comps: list[int] = [0] * cols

    for row in range(rows):
        for col in range(cols):
            # If there is a computer present in the grid
            if grid[row][col] == 1:
                # update our row and col arrays accordingly
                row_comps[row] += 1
                col_comps[col] += 1

            print(
                f"Within Loop Row Array: {row_comps} - Within Loop Col Array: {col_comps}"
            )

    print(f"Totals Comps in Rows: {row_comps} - Total Comps in Columns: {col_comps}")

    result = 0

    for r in range(rows):
        for c in range(cols):
            # for each computer that is either part of a row or column where there are more than one computers, we increase our result
            if grid[r][c] == 1 and (row_comps[r] > 1 or col_comps[c] > 1):
                print(f"Communicating Comp Found at Row: {r}, Col: {c}")
                result += 1

    print(f"\nTotal Communicating Comps: {result}\n")
    return result


countServer([[1, 0], [0, 1]])  # Expected Output: 0
countServer([[1, 0, 1], [0, 1, 0], [1, 0, 0]])  # Expected Output: 3
