# PROBLEM #1331 - RANK TRANSFORM OF AN ARRAY

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

# ---------------------------------------------------------------------------------------------------------------------------


def arrayRankTransform(arr: list[int]) -> list[int]:
    if len(arr) < 1:  # Base case to exit if an empty arr is given
        return arr

    # Create a temporary sorted set of the numbers from the array --> Used for ranking
    temp = sorted(set(arr))

    # Used to store the key (original number from arr) and the value (ranking in the array)
    dict = {}

    # Begin ranking at a value of 1 as the lowest --> Not the 0 we begin the loop with
    for num in range(len(temp)):
        dict[temp[num]] = num + 1

    # This returns an array with each number in arr set to it's corresponding ranking from the dictionary=
    return [dict[num] for num in arr]


# ---------------------------------------------------------------------------------------------------------------------------

vals1 = [40, 10, 20, 30, 40]
print(arrayRankTransform(vals1))
