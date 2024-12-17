# PROBLEM #2182 - CONSTRUCT A STRING WITH A REPEAT LIMIT

# You are given a string s and an integer repeatLimit.
# Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row.
# You do not have to use all characters from s.

# Return the lexicographically largest repeatLimitedString possible.

# A string a is lexicographically larger than a string b if:
# In the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# lexicographically larger means sorted from z to a --> Z > A but must maintain REPEAT LIMIT
# Sort list and get the characters in this proper order first

# Move through the list and add the characters to a result string as long as they are less than the repeat limit in frequency
# Return the string?

# ---------------------------------------------------------------------------------------------------------------------------


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    # Sort the input string in reverse order --> Lexicographically largest first
    # Reverse = True ensures that we are sorted from Z to A
    chars = sorted(s, reverse=True)
    print(f"Lex Sorted: {chars}")

    # This variable will contain the characters for our final string to return --> In Lexagraphical order
    result = []

    # This variable represents the current count of the current character we are using --> Cannot exceed repeatLimit integer
    count = 0

    # This variable represents the index of the next available character to append to the result once we have reached our count limit
    point = 0

    # Initialize a loop to traverse through the sorted characters in chars
    for i in range(len(chars)):
        # Check if result is not empty and if the last character is the same as our current character
        if result and result[-1] == chars[i]:
            # Check the current count of that character
            if count < repeatLimit:
                # Add the character to the result and increase the count
                result.append(chars[i])
                count += 1
                point += 1
            else:
                # Move the pointer to the next distinct letter --> Only using i + 1 may have us revisit multiple copies of the same letter
                # Use max(point, i + 1) to avoid all duplicate characters more efficiently --> Times out with simply i + 1
                point = max(point, i + 1)

                # While loop where we skip over charaters that are the same as chars[i]
                # This helps us with the max function above, allowing us to skip to the next distinct character more efficiently
                # Continues until end of list or distinct character is found
                while point < len(chars) and chars[point] == chars[i]:
                    point += 1

                if point < len(chars):
                    # Append the viable character
                    result.append(chars[point])

                    print(
                        f"Before Swap: Chars[i] = {chars[i]}, Chars[Point] = {chars[point]}, Chars = {chars}"
                    )

                    # Switch our pointers to move i to the new distinct character
                    chars[i], chars[point] = chars[point], chars[i]

                    print(
                        f"After Swap: Chars[i] = {chars[i]}, Chars[Point] = {chars[point]}, Chars = {chars}"
                    )

                    count = 1

                else:
                    # Can add the break in because we know we cannot add anymore characters to the string
                    break

        else:
            # If the result is empty, we simply add the character and update the count
            result.append(chars[i])
            count = 1

    print(f"Result: {result}")
    print(" ")

    return "".join(result)


repeatLimitedString("cczazcc", 3)

repeatLimitedString("aababab", 2)
