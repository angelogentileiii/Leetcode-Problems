# PROBLEM #2390 - REMOVING STARS FROM A STRING

# You are given a string s, which contains stars *.

# In one operation, you can:
#   Choose a star in s.
#   Remove the closest non-star character to its left, as well as remove the star itself.

# Return the string after all stars have been removed.

# Note:
#   The input will be generated such that the operation is always possible.
#   It can be shown that the resulting string will always be unique.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# Utilize a stack as we traverse the characters in the string
# If it is a '*' we pop off of the top of the stack, otherwise we append the letter to the stack
# Maintains removing all items that had last entered the stack --> The character just prior to the '*'

# ---------------------------------------------------------------------------------------------------------------------------


def removeStars(s: str) -> str:
    # Initialize our stack
    stack: list[str] = []

    # Loop through each character of the string
    for char in s:
        # if the character is not the '*' --> Append to the stack
        if char != "*":
            stack.append(char)
        # Otherwise, we pop off the top of the stack --> Removing the last letter we have encounted (the character to the left of the '*')
        else:
            stack.pop()
            continue

    # Join the items in the stack to return the appropriate string
    print("".join(stack))
    return "".join(stack)


# As many have noted on Leetcode, this is a fairly straightforward stack problem that appears too clear to be ranked as a Medium problem

removeStars("leet**cod*e")
