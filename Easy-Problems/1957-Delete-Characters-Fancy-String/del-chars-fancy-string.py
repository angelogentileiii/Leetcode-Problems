# PROBLEM #1957 - DELETE CHARACTERS TO MAKE A FANCY STRING

# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

# ---------------------------------------------------------------------------------------------------------------------------


def makeFancyString(s: str) -> bool:
    result: list[str] = []

    for i in range(len(s)):
        if (
            len(result) >= 2
            and result[len(result) - 2] == s[i]
            and result[len(result) - 1] == s[i]
        ):
            continue
        result.push(s[i])

    return "".join(result)


# MORE EFFICIENT SOLUTION --> ONLY PUSH CHARACTERS UP TO MAXIMUM OF TWO CONSECUTIVE CHARS


def makeFancyString(s: str) -> bool:
    # Result string to store "beautiful string"
    result = ""

    # Character that can't be reached for initial value --> Keeps track of character prior
    prevChar = ">"

    # Variable to represent our current character count --> Always begins at 1 when we first see the character
    count = 1

    # For each character in original string
    for char in s:
        # If the character was not present before
        if char != prevChar:
            # The count remains at one
            count = 1
            # Push the character into the result string
            result += char
        # else if it was the previous character and the count is less than 2 --> Wouldn't get past first condition if it wasn't previous character
        elif count < 2:
            # Increase the count by 1
            count += 1
            # Add the character to the result because we are still within our bounds of three repeated characters
            result += char

        # Update our prevChar variable
        prevChar = char

    return result
