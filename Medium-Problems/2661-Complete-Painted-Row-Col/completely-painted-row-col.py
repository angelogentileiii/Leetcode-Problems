# PROBLEM #2661 - FIRST COMPLETELY PAINTED ROW OR COLUMN

# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# The goal is to find which row or column will be visited fully first
# We can to create a dictionary to store each values precise position in the matrix
#   - Could also use a nested loop --> One for Rows and one for Cols
# We need to store the total number of rows and columns in the matrix --> Can use two frequency arrays for this
# As we move through our arr --> We mark each cell that has been visited in row/column
#   - If the cell reaches 0, we have visited it the maximum amount of times (dictionary)
#   - If the cell reaches the total number of rows or columns, we've also visited the maximum (nested for loops)

# ---------------------------------------------------------------------------------------------------------------------------


def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    print(f"Original Matrix: {mat}")

    # Two variables to store the total number of rows and total number of columns in our matrix
    rows = len(mat)
    cols = len(mat[0])

    # Two Arrays to store the total rows and columns for each index of the matrix --> Will use to decrease to zero (fully painted row or column)
    #   - row_count: represents how many columns are unpainted across the rows
    #   - col_count: represents how many rows are unpainted across the columns
    row_count = [cols] * rows
    col_count = [rows] * cols

    print(f"Row Count: {row_count} - Col Count: {col_count}")

    # Build a position dictionary where each value of the matrix stores it's corresponding tuple with it's row/column position --> {1:(0,0), 4: (0,1), ...}
    position = {mat[r][c]: (r, c) for r in range(rows) for c in range(cols)}

    # The above is the same as building with the following structure:
    #   position = dict()
    #   for i in range(rows):
    #       for j in range(cols):
    #           position[mat[i][j]] = (i, j)

    print(f"Position Dict: {position}")

    # Iterate through our array and use enumerate to pull out the current value and the current index
    for idx, val in enumerate(arr):
        print(f"Curr Idx: {idx} - Curr Val: {val}")

        # Find the row and column within the position dictionary for the particular value --> That values location in the matrix
        r, c = position[val]

        # We decrease the corresponding value in each array as we have now "painted" that value
        row_count[r] -= 1
        col_count[c] -= 1

        # We check after each iteration if we have reached 0 --> Meaning there are no open cells in either the row or the column (All cells have been painted)
        if not row_count[r] or not col_count[c]:
            print(f"First Painted Idx: {idx}\n")
            return idx

    # Edge case consideration
    # If after iteration, we have not painted all cells --> We can return -1 to show that no index in the array is valid for the problem
    return -1


firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]])  # Expected Index: 2
firstCompleteIndex([2, 4, 1, 3, 5, 6], [[6, 2], [1, 3], [5, 4]])  # Expected Index: 3
