# Problem #3264 --> FINAL ARRAY STATE AFTER K MULTIPLICATION OPERATIONS 1

# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS:

# First we need to find the minimum value of nums at each operation --> Before we multiply the smallest number for that operation but after the prior operation
# Then we multiply this number by the multiplier
# Take the new integer and replace the original integer at the original index in nums
# This action must be performed K times --> Loop

# ---------------------------------------------------------------------------------------------------------------------------


# Longer method --> Initial solution
def getFinalState(nums: list[int], k: int, multiplier: int) -> list[int]:
    # Initialize the base loop --> Will not be using the variable so we can use "_"
    for _ in range(k):

        # Make a copy of the nums list --> So we can keep it intact for swapping later
        sorted_nums = nums.copy()

        # Sort our copied list to find smallest integer
        sorted_nums.sort()
        print(f" Sorted list: {sorted_nums}")

        # Smallest integer is at the 0 index
        print(f"Smallest integer: {sorted_nums[0]}")

        # Find the index of the smallest number in the original list
        idx = nums.index(sorted_nums[0])

        # Update the original index with the multiplied value
        nums[idx] = nums[idx] * multiplier

        print(f"After Multiplication Replacement: {nums}")

    return nums


# Cleaner and shorter code solution
def getFinalStateShort(nums: list[int], k: int, multiplier: int) -> list[int]:
    # Our initial loop does not change
    for _ in range(k):
        # Find the minimum index of nums -> Rather than finding the minimum number ourselves we can use built in func
        idx = nums.index(min(nums))

        # Update the index with the multiplied value
        nums[idx] = nums[idx] * multiplier

        print(f"After Multiplication Replacement: {nums}")

    return nums


getFinalStateShort([2, 1, 3, 5, 6], 5, 2)
getFinalStateShort([1, 2], 3, 4)
