# PROBLEM #3254 - FIND THE POWER OF K SUBARRAYS 1

# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.

# You need to find the power of all subarrays of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We need to have two pointers to check each sub array
# The first pointer --> Maintains the beginning of the subarray at each index
# The second pointer --> Checks if the numbers following are consecutive

# If we don't have a consecutive number:
# We need to check that it is a valid beginning to a subarray --> There are k - 1 more numbers till the end of the array
# If so, we can append -1 to the result array and move the pointer forward in the array

# If we have a consecutive number and our second pointer - our first pointer is equal to k - 1 --> We have reached the length of the subarray we need to use
# Then we know that the number at our second pointer is the maximum in the subarray --> Due to consecutive condition
# We can append that number to the result array, move our first pointer to the next subarray beginning

# We would also need to increase the second pointer after each check to ensure we are moving it in correlation for next subarray

# ---------------------------------------------------------------------------------------------------------------------------


def resultsArray(nums: list[int], k: int) -> list[int]:
    # If K is 1, we know the maximum of each subarray is the number itself, so we can return the array as is
    if k == 1:
        return nums

    # Initialize two pointers --> Initial index and one index further right
    left = 0
    right = 1

    # Initialize a blank array to store the result values
    result = []

    # While our right pointer stays within the bounds of the array
    while right < len(nums):
        print("Left: ", left, "Right: ", right)

        # Initialize a variable to check if the number is still consecutive
        not_consecutive = nums[right] - nums[right - 1] != 1

        # If the elements are not consecutive --> Do not match the condition needed in problem
        if not_consecutive:
            # As long as the left value is valid and hasn't exceeded the array length
            while left < right and left + k - 1 < len(nums):
                # We append -1 because we've found a false condition
                result.append(-1)
                # Move the left pointer forward in the array
                left += 1
        # Else, when we've reached the maximum index of the subarray (left and right are the final two indexes)
        elif right - left == k - 1:
            # We know that it is the maximum number --> Do to consecutive nature
            # Append to the result array
            result.append(nums[right])
            # Move the left pointer forward in the array
            left += 1

        # Always move the right pointer to the next position in the array --> Maintain positioning within next subarray or move within current subarray
        right += 1

    # Return the completed result array --> It will be of length n - k + 1 (EX: 7 - 3 + 1 = length of 5)
    return result


print(resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
print(resultsArray([1, 4, 5, 6, 7, 9], 1))
