# PROBLEM #1072 - FLIP COLUMNS FOR MAXIMUM NUMBER OF EQUAL ROWS

# You are given an m x n binary matrix matrix.

# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

# Return the maximum number of rows that have all values equal after some number of flips.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# Flip column values means flipping the same index of a subarray
# So [0][1], [1][1], [2][1] and so on

# Each column has two options:
# Keep the column the same
# Flip the column values

# Combinations will be less than the number of items per row

# Needs to be a pattern to count the number of maximum columns that should be flipped
# If two rows can be made equal --> They are either equivalent or the inverse of the other

# Could convert each row into a string to compare? --> PYTHON YOU CAN USE A TUPLE AS A KEY!
# A hashmap with keys to track which rows have been visited?
# { '0,0,0': 1} --> Track the string and place a counter for amount available
# We should flip the string to check if it is the same or the inverse

# The maximum count in the map should be the total number of rows that can be equal

# ---------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict


def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:
    # This is our dictionary for our counting -- > defaultdict(int) allows each key to have a default value
    # Using 'int' sets each default value to 0
    count = defaultdict(int)

    # Move through each row of the matrix
    for row in matrix:
        # Make each row a key for the count dict
        row_key = str(row)  # Or tuple(row) --> More efficient

        # If the row begins with a 1 --> Not a 0
        if row[0]:
            # We invert the row to match our keys --> Could also use 1 as the indicator as well
            # Cannot simply use row_key[::-1] --> Must flip each number
            # If n is not 0, make it 0 --> Else make it 1
            inv_row = [0 if n else 1 for n in row]

            # Update our row_key variable to the inverted key
            row_key = str(inv_row)  # Could also be tuple(inv_row)

        # We either add to the count or add the key with a value of 1
        # Benefit of the defaultdict used above
        count[row_key] += 1

    print(count)
    print("Answer: ", max(count.values()))

    # Return the maximum value for any key in the dict --> Represents the max rows that can be equal
    return max(count.values())


maxEqualRowsAfterFlips([[0, 1], [1, 1]])
maxEqualRowsAfterFlips([[0, 1], [1, 0]])
