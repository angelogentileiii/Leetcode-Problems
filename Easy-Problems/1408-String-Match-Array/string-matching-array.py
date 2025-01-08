# PROBLEM #1408 - STRING MATCHING IN AN ARRAY

# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

# ---------------------------------------------------------------------------------------------------------------------------

# BRUTE FORCE SOLUTION

# This works for this problem since the constraints hold the words array to only 100 items with a maximum of 30 characters each
# Likely the expected solution for this being an EASY problem

# We simply have a nested loop where we test each word as a substring of every other possible word in the array


def stringMatchingBrute(words: list[str]) -> list[str]:
    # Initialize our result arr to store our valid words
    result: list[str] = []

    # Outer loop moves through the words array with one pointer
    for i in range(len(words)):
        # Inner loop moves through the words array with a separate pointer
        for j in range(len(words)):
            # For each inner iteration we check two conditions
            # Is the word identical --> If so, pass this word
            if words[i] == words[j]:
                continue
            # If the current word of the outer loop is a substring of our inner loop
            if words[i] in words[j]:
                result.append(words[i])
                # We break because we no longer need to check this word if we have already found a valid substring
                break

    print(f"Completed Result: {result}")
    return result


# ---------------------------------------------------------------------------------------------------------------------------

# PREFIX TRIE SOLUTION

# This solution utilizes a trie to store all possible prefixes available within the words array
# We can store each prefix and it's frequency of appearance to determine if a word is a substring of another word

# I've moved my Trie logic (standard build) to a separate module and imported for cleanliness --> Click on the import to view structure

from Utils.Python.Trie import PrefixTrie


def stringMatching(words: list[str]) -> list[str]:
    # We initialize our result array which will store any strings that are substrings of another
    result: list[str] = []

    # We initialize our trie structure with a root node
    trie = PrefixTrie()

    print("Initial Trie Root:")
    print(trie.root.pretty_print())

    # First loop is an iteration through each word in the words array to insert into our prefix trie
    for word in words:
        # This inner loop moves us through each character of each word
        for i in range(len(word)):
            # This will insert each word into our trie by an increasingly long prefix --> Until the word is completed
            #   If the word is MASS --> first we enter 'M', then 'MA', then 'MAS', and so on
            trie.insert_word(word[i:])

    print("\nFinal Trie Structure:")
    print(trie.root.pretty_print())

    # Second loop is an iteration through the same words but uses the helper function to check if each word is a substring of another
    for word in words:
        if trie.search_word(word):
            result.append(word)

    print(f"Result Arr: {result}")
    return result


# ---------------------------------------------------------------------------------------------------------------------------

stringMatching(["mass", "as", "hero", "superhero"])
# stringMatchingBrute(["mass", "as", "hero", "superhero"])
