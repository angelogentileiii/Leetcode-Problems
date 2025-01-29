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


# ---------------------------------------------------------------------------------------------------------------------------


def findMaxFish(grid: list[list[int]]) -> int:
    print("Initial Grid:")
    print("\n".join(str(row) for row in grid))

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    print(f"\nInitial Visited Array: ")
    print("\n".join(str(row) for row in visited))

    max_fish = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0 and not visited[row][col]:
                total_fish = calcFish(grid, visited, row, col)

                print(f"\nTotal Fish for Choice: -- {total_fish} --")

                max_fish = max(max_fish, total_fish)

    print(f"\nCompleted Visited Array: ")
    print("\n".join(str(row) for row in visited))

    print(f"\n-- Result: {max_fish} --\n")
    return max_fish


def calcFish(
    grid: list[list[int]], visited: list[list[int]], row: int, col: int
) -> int:
    if (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[0])
        or grid[row][col] == 0
        or visited[row][col]
    ):
        return 0

    visited[row][col] = True

    total_fish = grid[row][col]

    print(f"\nIteration Visited Array: {(row, col)} - Fish: {total_fish}")
    print("\n".join(str(row) for row in visited))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in directions:
        total_fish += calcFish(grid, visited, row + dr, col + dc)

    return total_fish


findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
findMaxFish([[5, 6, 7, 0], [0, 0, 0, 4], [2, 0, 0, 3], [2, 4, 5, 8]])
