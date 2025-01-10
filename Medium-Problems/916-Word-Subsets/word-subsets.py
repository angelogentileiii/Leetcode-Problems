# PROBLEM #916 - WORD SUBSETS

# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".

# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# Key focus is this line: A string a from words1 is universal if for every string b in words2, b is a subset of a
# We need to ensure that each character in the words2 list is present in words1 at minimum the same frequency

# First: Count the frequency of each character in words2 --> List or Dict
# Second: Count the frequency of each character in words1 against our frequency data structure
# - As long as there are the frequencies in words1 are >= frequencies in our words2 count --> We are valid

# ---------------------------------------------------------------------------------------------------------------------------


def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    # Initialize our result array --> Where we will append all universal strings from words1
    result: list[str] = []

    # Initialize an array to store the maximum frequency of each character across all words in words2
    words2_freq = [0] * 26

    # Loop through words2 to calculate the frequency of each character across all words in array
    for word in words2:
        # Get character counts for the current word
        char_count = count(word)
        print(f"Word: '{word}' - Frequency Array: {char_count}")

        # Update the global frequency array for words2
        for idx, char in enumerate(char_count):
            words2_freq[idx] = max(words2_freq[idx], char)

        print(f"Updated Words2 Freq Array: {words2_freq}\n")

    print(f"\nFinal Words2 Frequency Array (Maximum Across All): {words2_freq}\n")

    # Loop through words1 to compare words2 frequency array against each word in words1
    for word in words1:
        # Get character counts for the current word in words1
        word_count = count(word)
        print(f"Word: '{word}' - Frequency Array: {word_count}")

        # Check if it satisfies the universal condition
        if all(x >= y for x, y in zip(word_count, words2_freq)):
            print(f"'{word}' is Universal (Meets the Condition)\n")
            result.append(word)

    print(f"Final Result: {result}")
    return result


# This helper function calculates the frequency of each character in the given word.
def count(word: str) -> list[int]:
    freq = [0] * 26  # Array to store counts for 'a' to 'z'

    # Increment the count for the corresponding character
    for char in word:
        # Utilize ord(char) - ord('a') to set the unicode range between 0-25 --> For our array
        freq[ord(char) - ord("a")] += 1

    # Return the frequency array for this word
    return freq


wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"])
