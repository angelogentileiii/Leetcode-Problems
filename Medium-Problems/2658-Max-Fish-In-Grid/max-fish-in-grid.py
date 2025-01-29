# PROBLEM #2658 - MAXIMUM NUMBER OF FISH IN A GRID

# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#   - A land cell if grid[r][c] = 0
#   - A water cell containing grid[r][c] fish, if grid[r][c] > 0

# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
#   - Catch all the fish at cell (r, c)
#   - Move to any adjacent water cell

# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We create a helper function that when we choose a particular cell, we check all possibly directions for a non-zero value
#   - This helper function will be called recursively, so that we then check subsequent combinations to find the total from a particular path

# We initialize an array to store whether or not a cell has already been visited --> To avoid overlapping on our path

# With each choice, we need to compare the total fish available with our maximum fish currently found
#   - By the end of our grid, we will have the maximum-fish by choosing the optimal beginning cell within the grid

# ---------------------------------------------------------------------------------------------------------------------------


def findMaxFish(grid: list[list[int]]) -> int:
    print("Initial Grid:")
    print("\n".join(str(row) for row in grid))

    # Initialize variables for our total rows and total columns
    rows = len(grid)
    cols = len(grid[0])

    # Initialize a grid that tracks whether or not a cell has been visited in our recursive function call --> Utilize booleans but could be integers as well
    visited = [[False] * cols for _ in range(rows)]

    print(f"\nInitial Visited Array: ")
    print("\n".join(str(row) for row in visited))

    # Initialize variable that will store our maximum fish accumulated --> Updates will be made at each cell choice that leads to an increased number of fish
    max_fish = 0

    # Iterate through our entire grid (cell by cell)
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell has fish (val greater than 0) and it has not been visited previously (it is not part of another path already traversed)
            if grid[row][col] > 0 and not visited[row][col]:
                # Call our helper function on each valid starting cell in the grid --> Will not call on water cells or cells already visited as noted
                curr_total = calcFish(grid, visited, row, col)

                print(f"\nTotal Fish for Choice: -- {curr_total} --")

                # Check the maximum fish against the current total from the cell chosen --> Update max_fish accordingly
                max_fish = max(max_fish, curr_total)

    print(f"\nCompleted Visited Array: ")
    print("\n".join(str(row) for row in visited))

    print(f"\n-- Result: {max_fish} --\n")
    return max_fish


# Helper function for checking path of fish within grid and returning the total fish available to a chosen cell path
def calcFish(
    grid: list[list[int]], visited: list[list[int]], row: int, col: int
) -> int:

    # Conditional statement that rules out all cases where the path would break
    if (
        row < 0  # We have extended out of bounds (low end)
        or row >= len(grid)  # We have extended out of bounds (high end)
        or col < 0  # We have extended out of bounds (low end)
        or col >= len(grid[0])  # We have extended out of bounds (high end)
        or grid[row][col] == 0  # There are no fish in the current cell
        or visited[row][col]  # The cell has already been visited
    ):
        return 0

    # Mark the current cell as visited in our visited graph
    visited[row][col] = True

    # Set the total fish for this path to our beginning cell --> This is what our minimum for this path will be
    total_fish = grid[row][col]

    print(f"\nIteration Visited Array: {(row, col)} - Fish: {total_fish}")
    print("\n".join(str(row) for row in visited))

    # Each tuple contains possible directions to check for our path --> Recursive calls of this function
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # For each direction, we call this function and add the fish value to the total_fish for this path --> Either 0 because we have hit our conditional or the value of the cell itself
    for dr, dc in directions:
        total_fish += calcFish(grid, visited, row + dr, col + dc)

    # After the loop, the final return value of total_fish will represent the total fish for the path available from the original cell chosen
    return total_fish


findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
findMaxFish([[5, 6, 7, 0], [0, 0, 0, 4], [2, 0, 0, 3], [2, 4, 5, 8]])
