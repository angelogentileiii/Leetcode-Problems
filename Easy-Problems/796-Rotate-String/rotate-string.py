# PROBLEM #796 - ROTATE STRING

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# ---------------------------------------------------------------------------------------------------------------------------


def rotateString(s: str, goal: str) -> bool:
    # If the strings are not equal in length, we know we cannot rotate properly
    if len(s) != len(goal):
        return False

    # Concatenate the string --> A rotated string will exist within a string consisting of two of our original strings
    concat = s + s

    # In Python, we can check for a substring by simply writing the following statement --> Will return a boolean
    return goal in concat


print(rotateString("abcde", "abced"))  # Expect False
print(rotateString("abcde", "cdeab"))  # Expect True
