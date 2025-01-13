# PROBLEM #3223 - MINIMUM LENGTH OF STRING AFTER OPERATIONS

# You are given a string s.

# You can perform the following process on s any number of times:
#     Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
#     Delete the closest character to the left of index i that is equal to s[i].
#     Delete the closest character to the right of index i that is equal to s[i].

# Return the minimum length of the final string s that you can achieve.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We need to have the same character on the left and right to be able to remove a singular character (either left or right)
#      So, if we have three characters, we can remove one from either side and have a single remaining character
#      If we have two characters, we cannot remove any because there is not a matching character on both sides of either

# If we count the characters on the string, each odd number of character will leave one behind and each even number will leave two
#      We can count these final numbers to determine the minimum string after the operations

# ---------------------------------------------------------------------------------------------------------------------------

from collections import Counter


def minimumLength(s: str) -> int:
    # Create a counter dictionary to store the frequency of each character in the string
    char_count = Counter(s)

    print(f"Characters: {char_count}")

    # Initialize our result variable to store the length of our minimum string
    result = 0

    # Loop through the values within the dictionary
    for char in char_count.values():
        # For each value, we add to our result array either a 1 if the value is odd (char % 2 leaves a remainder) or 2 if the value is even (no remainder left)
        result += 1 if char % 2 else 2

    print(f"Result: {result}")
    return result


# Set version of the solution without overhead of the Counter Dictionary --> Though at most the dictionary would have 26 Key/Value pairs so it's still efficient
def minimumLengthSet(s: str) -> int:
    # Initialize our result variable to store the minimum length
    result = 0

    # For each character in our set --> Only iterate over unique characters present
    for ch in set(s):
        # We count the individual characters --> Utilizes built in count method with leverages C for efficiency
        count = s.count(ch)
        print(f"Char: {ch} - Count: {count}")

        # Result utilizes the same equation to determine the minimum number of characters present
        result += 1 if count % 2 else 2

    print(f"Result: {result}")
    return result


minimumLength("abaacbcbb")
minimumLengthSet("abaacbcbb")
