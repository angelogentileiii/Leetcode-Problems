# PROBLEM #2559 - COUNT VOWEL STRINGS IN RANGES

# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'. --> NOT 'y'

# Essentially, we need to return an array where each index of that array represents the number of vowel strings within the corresponding query range

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# My initial thought was to iterate through the ranges of the queries to count the number of vowel strings per range
# It's a brute force solution that would simply count as we move through the range --> However, this also means recounting for each range that overlaps

# One option is utilizing another array that keeps track of the sum of vowel strings at every index of the words array
# We could then use these sums to simply calculate the value of any particular range by using a formula like (right value - (left value - 1))
# This would then be all of the possible vowel strings available without having to repeatedly check for each range in queries

# ---------------------------------------------------------------------------------------------------------------------------


def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    # All of the letters to be included as vowels --> Our condition in the problem
    vowels = {"a", "e", "i", "o", "u"}

    # Initialize two empty arrays --> One for the total vowel strings at each index, and one for our result of the ranges
    sum: list[int] = []
    result: list[int] = []

    # Initialize our count variable --> Keeps track of vowel strings encountered in first loop
    count = 0

    for word in words:
        # Check if the first and last letter of the word are vowels
        if word[0] in vowels and word[-1] in vowels:
            # Increase the counter
            count += 1
        # Append the count up until the current word's index
        sum.append(count)

        print(f"Sum Arr after Each Word: {sum}")

    # This array now holds all of the total vowel strings at each index for the words array
    print(f"Completed Sum Arr: {sum}")

    # Now we handle the individual queries (ranges) we are looking for
    for query in queries:
        # Separate the left and right of the range for the query
        left, right = query

        print(f"Left: {left} and Right: {right} of Query")

        # If the query begins at the beginning of the array (0 Index) then we simply need to add the value at the right index to the result
        if left == 0:
            result.append(sum[right])
        else:
            # Otherwise, we need to subtract the left from the right
            # We use one position prior to the left in order to encapsulate the accurate number of strings within the range (Left to Right inclusive)
            result.append(sum[right] - sum[left - 1])

        print(f"Result after Each Query: {result}")

    return result


vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]])
