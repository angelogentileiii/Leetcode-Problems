# PROBLEM #2270 - NUMBER OF WAYS TO SPLIT AN ARRAY

# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

# ---------------------------------------------------------------------------------------------------------------------------


def waysToSplitArray(nums: list[int]) -> int:
    # Total represents the total sum of all of the numbers within the nums array --> Used for later computing
    total_sum = sum(nums)

    print(f"Total Sum Value: {total_sum}")

    # Two variables initialized for the sum value of where we can have a valid split and the count for the total valid splits available
    left_sum, count = 0, 0

    # Loop through all of the numbers within the nums array
    for i in range(len(nums) - 1):
        # We add the value of the current iteration to the left value --> Signifying a split at this index
        left_sum += nums[i]

        print(f"Left Sum: {left_sum}")

        # The right (remainder of array) represents the total - our new left sum
        right_sum = total_sum - left_sum

        print(f"Right Sum: {right_sum}")

        # Our conditional statement for the problem --> Sum of the left split must be greater than or equal to sum of right split
        if left_sum >= right_sum:
            count += 1

    # After the loop completes, we have reached our total valid count
    print(f"Count: {count}")
    return count


waysToSplitArray([10, 4, -8, 7])
