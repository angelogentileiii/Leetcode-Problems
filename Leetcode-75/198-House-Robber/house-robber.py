# Problem #198 - HOUSE ROBBER

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# ---------------------------------------------------------------------------------------------------------------------------

# If you rob first house, you cannot rob second house
# If you skip first house, you can rob second house

# [0, 1, 2, 3]
#     Rob 0 -> Skip -> Rob either 2 or 3
#     Skip -> Rob 1 -> Skip
# The maximum at each index is the max between that index - 1 and that index - 2
#     Max at index 0 is 0
#     Max at index 1 is 1
#     Max at index 2 is 2 because 2 is > 1
#     Max at index 3 is 4 because index 1 + index 3 > max at index 2


def rob(nums: list[int]) -> int:
    # Initialize our two options as zero values --> Nothing robbed yet
    house1, house2 = 0, 0

    for i in range(len(nums)):  # Iterating through every house on the street
        # Robbing the first house means adding the value of the index to the house1 value
        rob1 = house1 + nums[i]

        # Robbing the second house means we take the house2 value and skip the current index
        rob2 = house2

        # Find the maximum value at this point in the array between robbing house1 and robbing house 2
        currMax = max(rob1, rob2)

        # Move our house pointer forward to the next house --> Alternates between robbing and skipping per solution
        house1 = house2

        # House 2 now represents the current maximum up to this point (If we skip the next house, we keep this)
        house2 = currMax

    # At the end of our loop, we have updated house2 with the currMax available to that index --> The desired result
    return house2


houses1 = [1, 2, 3, 1]  # Expect 4
houses2 = [2, 7, 9, 3, 1, 2, 7, 9, 3, 1]  # Expect 23

print("Maximum Available:", rob(houses1))
print("Maximum Available:", rob(houses2))
