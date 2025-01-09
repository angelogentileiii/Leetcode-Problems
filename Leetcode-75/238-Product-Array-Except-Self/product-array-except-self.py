# PROBLEM #238 - PRODUCT OF ARRAY EXCEPT SELF

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# ---------------------------------------------------------------------------------------------------------------------------

# INITIAL THOUGHTS

# Brute force can use a nested loop --> Iterate over the nums and at each index, we only multiply 1 by every index value except itself
# This solution fails the constraints as it exceeds the time limit available

# We need a solution where in one pass of the array we can multiply from left to right and then from right to left
# Basically like a prefix sum and suffix sum for each index --> [1, 2, 3, 4] --> Prefix = 1 (base) Suffix = 24. Prefix * Suffix = 24 and so on

# ---------------------------------------------------------------------------------------------------------------------------

# BRUTE FORCE SOLUTION
# Nested for loops exceed the time limit and are not efficient to solve the problem


def productExceptSelfBrute(nums: list[int]) -> list[int]:
    result = [1] * len(nums)

    # Our nested loops to move through the array and multiply every index except for i --> INEFFICIENT
    for i in range(len(nums)):
        print(nums[i])
        product = 1
        for j in range(len(nums)):
            if j == i:
                continue
            product *= nums[j]
        result[i] = product
        print(result)


# productExceptSelfBrute([1, 2, 3, 4])
# productExceptSelfBrute([-1, 1, 0, -3, 3])

# ---------------------------------------------------------------------------------------------------------------------------

# My PREFIX/SUFFIX solution using a singular loop


def productExceptSelf(nums: list[int]) -> list[int]:
    # Initialize our result array
    n = len(nums)
    result = [1] * n

    # These are our two starting values for either direction --> Cannot be 0 in multiplication (0 * number = 0....)
    prefix = 1
    suffix = 1

    for i in range(n):
        # Multiply the index of the result by the prefix --> Initially is 1 because we have not put any numbers to our left side of our index
        result[i] *= prefix
        # Update the prefix by multiplying it by the current number --> Will be used in the next iteration since we have passed this number
        prefix *= nums[i]

        # Multiply the index at the end of our array (right side) by our suffix value --> Same premise as prefix but the opposite end
        result[-1 - i] *= suffix
        # Update the suffix by multiplying it by the current number in the same index of the nums array --> Again, used for next iteration
        suffix *= nums[-1 - i]
        print(f"Result in 1st Loop: {result}")

    print(f"Completed Result: {result}")
    return result


# ---------------------------------------------------------------------------------------------------------------------------

# CLEANER AND MORE READABLE VERSION WITH SAME O(1) SPACE COMPLEXITY

# Separating the prefix and suffix logic into two loops allows for the better clarity with the same space/time complexity
#    Overall better practice to write the function in this manner


def productExceptSelfOptimal(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # Our prefix calculation as we move through the array --> Same as before
    prefix = 1
    for i in range(n):
        result[i] *= prefix
        prefix *= nums[i]
        print(f"Result in 1st Loop: {result}")

    # Our suffix calculation --> Now we can iterate from the right to the left instead of utilizing nums[-1 - i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
        print(f"Result in 2nd Loop: {result}")

    print(f"Completed Result: {result}")
    return result


productExceptSelfOptimal([1, 2, 3, 4])
productExceptSelfOptimal([-1, 1, 0, -3, 3])
