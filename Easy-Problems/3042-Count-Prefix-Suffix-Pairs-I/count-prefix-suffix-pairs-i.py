# PROBLEM #3042 - COUNT PREFIX AND SUFFIX PAIRS I

# You are given a 0-indexed string array words.

# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

# isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.

# For example:
#   isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

# ---------------------------------------------------------------------------------------------------------------------------

# BRUTE FORCE SOLUTION

# Utilize nested for loops to check each string against all possible options in the remaining array --> As long as left index < right index (i < j)


def countPrefixSuffixPairsBrute(words: list[str]) -> int:
    n = len(words)
    count = 0

    # Nested for loops to iterate with two pointers --> The current word and possible words with pref/suff
    for i in range(n - 1):
        # This loop moves through all words from the right index onward --> Following the (i < j) condition
        for j in range(i + 1, n):
            # Utilize the helper function to determine if the first word is a pref/suff of the second
            if isPrefixAndSuffix(words[i], words[j]):
                # If so, increment successful count
                count += 1

    print(f"Final Count: {count}")
    return count


# Helper function to determine is one string is a prefox/suffix of another
def isPrefixAndSuffix(str1: str, str2: str) -> bool:
    n1, n2 = len(str1), len(str2)

    # If the first string is longer than the second, we know it cannot be a prefix and suffix of the second string
    if n1 > n2:
        return False

    # Two variables to represent the current prefix and suffix of the second string up to the length of the first string
    prefix = str2[:n1]
    # We can split the suffix using the negative index which moves our suffix from the last character towards the beginning the value of len(str1)
    suffix = str2[-n1:]

    print(f"Prefix: {prefix}")
    print(f"Suffix: {suffix}")

    # We return the boolean if our prefix and suffix are equal to our first string
    return prefix == str1 and suffix == str1

    # return str2.startsWith(str1) and str2.endsWith(str1) --> Could also use the built in method rather than splitting


# countPrefixSuffixPairsBrute(["a", "aba", "ababa", "aa"])

# ---------------------------------------------------------------------------------------------------------------------------

# PREFIX AND SUFFIX TRIE SOLUTION

# Build a trie where we can store the prefix and suffix of each word
# As we input into the trie, we will add pairs (first letter, last letter) and move inward until the word is submitted
# Then we add use another function to search the trie with each word to determine if it is a substring (prefix & suffix)

# I've moved my Trie logic (standard build) to a separate module and imported for cleanliness --> Click on the import to view structure

from Utils.Python.Trie import PrefixSuffixTrie


def countPrefixSuffixPairs(words: list[str]) -> int:
    # Initialize result to track the total number of prefix-suffix pairs
    result = 0

    # Initialize the Trie to store the prefix-suffix combinations
    trie = PrefixSuffixTrie()

    # Iterate through the words in reverse order
    for word in words[::-1]:
        # Search for how many matching prefix-suffix pairs already exist in the Trie
        result += trie.search_word(word)

        # Insert the current word into the Trie to build the prefix-suffix pairs
        trie.insert_word(word)

        # Print the Trie structure after inserting each word for debugging purposespy
        print(f" Trie After Current Word: {word}")
        print(trie.root.pretty_print())

    # Print the final state of the Trie and the result
    print(f"Completed Trie {trie.root.pretty_print()}")
    print(f"Result: {result}")

    # Return the final result
    return result


countPrefixSuffixPairs(["a", "ababa", "aa", "aba"])
