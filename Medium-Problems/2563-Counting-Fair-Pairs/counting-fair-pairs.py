# PROBLEM #2563 - COUNTING THE NUMBER OF FAIR PAIRS

# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper

# ---------------------------------------------------------------------------------------------------------------------------


def countFairPairs(nums: list[int], lower: int, upper: int) -> int:
    # Sort the array list for binary search
    nums.sort()
    result = 0

    # Function for our binary search
    def binary_search(left: int, right: int, target: int) -> int:

        while left <= right:
            # Find the midpoint of the range
            mid = left + (right - left) // 2

            # If the number is greater than or equal to our target --> Move the right pointer
            if nums[mid] >= target:
                right = mid - 1

            # Otherwise move the left pointer
            else:
                left = mid + 1

        # We return right because it will represent the largest number within the bounds --> Both upper and lower
        return right

    # Iterate through each num of the nums array
    for i in range(len(nums)):
        # Upper and lower numeric bounds by subtracting the current number
        up = upper - nums[i]
        low = lower - nums[i]

        # Use binary search to find the upper index of the array that matches condition for current number
        upper_index = binary_search(i + 1, len(nums) - 1, up + 1)

        # Use binary search to find the lower index of the array that matches condition for current number
        lower_index = binary_search(i + 1, len(nums) - 1, low)

        # print("Up Idx: ", upper_index)
        # print("Low Idx: ", lower_index)

        # Add all possible combinations, the indexes between the upper and lower bounds --> the difference between the upper idx - the lower idx
        result += upper_index - lower_index

    print(result)
    return result


# ---------------------------------------------------------------------------------------------------------------------------

# Solution with only one iteration involved --> Rather than calling binary search on each number of nums


def countFairPairs2(nums: list[int], lower: int, upper: int) -> int:
    nums.sort()
    print(lower_bound(nums, upper + 1) - lower_bound(nums, lower))

    # Return the lower bound of upper + 1 minus the lower bound of lower to encompass all possible pairs in the array
    # essentially upper_index - lower_index = the window of all possible pairs available
    return lower_bound(nums, upper + 1) - lower_bound(nums, lower)


# This function helps find our lower bound on both occasions --> With the upper + 1 and the lower value
def lower_bound(nums: list[int], value: int) -> int:
    # Setup the range for the iteration
    left = 0
    right = len(nums) - 1

    # Setup the result to return for the possible combinations as we move through the range
    result = 0

    # Iterate through the range with a while loop
    while left < right:
        # Calculate the sum of each pointer -> left + right in array
        sum = nums[left] + nums[right]

        # The value represents the current boundary we are looking to calculate --> Being less than the value ensures we are >= lower and < upper + 1 (<= upper)
        if sum < value:
            # Add the window to the result
            result += right - left
            # Move the left pointer up one and check again
            left += 1
        else:
            # Move the right pointer down one and check again
            right -= 1
    # Return the point where the pointers overlap --> the maximum index where the sum < value
    return result


countFairPairs([0, 1, 7, 4, 4, 5], 3, 6)
countFairPairs([1, 7, 9, 2, 5], 11, 11)

countFairPairs2([0, 1, 7, 4, 4, 5], 3, 6)
countFairPairs2([1, 7, 9, 2, 5], 11, 11)
