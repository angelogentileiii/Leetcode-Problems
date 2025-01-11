# PROBLEM #1400 - CONSTRUCT K PALINDROM STRINGS

# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# If the len(s) is the same as k --> We return True because each string is one character
# If k > len(s) --> We return False because we don't have enough characters to make enough palindrom strings

# We need to count each character in the string for it's frequency --> Use a dict/map for this
# If we have more characters that have odd values than the value k --> We return false
# - Each palindrom string can have at most one odd character --> The center index of the string
# We can count the total amount of odd values --> if > k, then we return False, else True

# ---------------------------------------------------------------------------------------------------------------------------


def canConstruct(self, s: str, k: int) -> bool:
    n = len(s)

    # Our dict to use to count each character within s
    freq = {}

    # If k is larger than n --> We know we don't have enough characters to make the necessary strings
    if k > n:
        return False

    # If k is equal to n --> We can return True because each string has only one character
    if k == n:
        return True

    # Loop to count each character within s
    for char in s:
        # This sets the value to 1 if the character is new --> Or adds 1 to the current value of that char
        freq[char] = freq.get(char, 0) + 1

    print(f"Frequency Map: {freq}")

    # Can also use the Counter class rather than the for loop and a map
    #   from collections import Counter
    #   freq = Counter(s)

    # Variable to keep track of our characters with odd frequencies
    odd_count = 0

    # Check each value within freq to see if it is an odd number --> If so, increase our odd_count
    for val in freq.values():
        if val % 2:
            odd_count += 1

    # If we have a higher count of odd characters than the value of k --> We cannot make the proper number of palindrom strings while using every character
    if odd_count > k:
        return False

    # Otherwise, we have enough characters to do so and we return True
    return True


# ---------------------------------------------------------------------------------------------------------------------------


# Utilizing a set and a single for loop to keep track of odd character frequencies


def canConstructSet(self, s: str, k: int) -> bool:
    n = len(s)

    # If k is larger than n --> Not enough characters to form k strings
    if k > n:
        return False

    # If k is equal to n --> Each string can have one character
    if k == n:
        return True

    # Track characters with odd frequencies using a Set
    odd_set = set()

    # Iterate over the string and track odd frequencies
    for char in s:
        # Check character's presence in the set (odd/even count tracking)
        if char in odd_set:
            # Remove if already present (even count)
            odd_set.remove(char)
        else:
            # Add if not present (odd count)
            odd_set.add(char)

    # If the set size is larger than k --> We have too manmy odd characters to be able to build the palindromes while using all characters
    if len(odd_set) > k:
        return False

    # If odd characters count is <= k, we can construct the palindromes
    return True


canConstruct("annabelle", 2)
canConstructSet("leetcode", 3)
