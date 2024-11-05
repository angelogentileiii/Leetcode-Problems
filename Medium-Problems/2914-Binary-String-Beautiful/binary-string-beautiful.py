# PROBLEM #2914 - MINIMUM NUMBER OF CHANGES TO MAKE A BINARY STRING BEAUTIFUL

# You are given a 0-indexed binary string s having an even length.

# A string is beautiful if it's possible to partition it into one or more substrings such that:

# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.

# Return the minimum number of changes required to make the string s beautiful.

# Example 1:

# Input: s = "1001"
# Output: 2
# Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
# It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
# It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

# ---------------------------------------------------------------------------------------------------------------------------


def minChanges(s: str) -> int:
    # Base case, if the string is odd in length, we cannot make it beautiful
    if len(s) % 2 != 0:
        return

    count = 0  # Variable for tracking changes necessary to the string

    # Loop through each pair of items within the string --> Ensures we won't go out of bounds
    for num in range(0, len(s), 2):
        # Compare each pairs numbers --> If they don't match we will have to make a change here
        if s[num] != s[num + 1]:
            # Update the count to reflect the necessary change made
            count += 1

    # When we finish the loop we have a count of the minimum changes necessary to update the string
    print(count)
    return count


minChanges("10101")
