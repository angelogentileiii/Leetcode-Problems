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


class TrieNode:
    def __init__(self):
        # Used to track the frequency of every substring
        self.frequency = 0

        # Maps each character to their respective child nodes --> Continuation of prefix
        self.child_nodes = {}

    def __repr__(self):
        return f"TrieNode(frequency={self.frequency}, child_nodes={(self.child_nodes)})"

    # Helper function to recursively print the Trie structure in a more readable manner
    def pretty_print(self, level=0):
        # As we have child nodes --> Each child of the char node is indented further
        indent = "  " * level
        result = f"{indent}TrieNode(frequency={self.frequency}, children={list(self.child_nodes.keys())})\n"
        for char, child in self.child_nodes.items():
            result += f"{indent}  '{char}':\n{child.pretty_print(level + 2)}"
        return result


def stringMatching(words: list[str]) -> list[str]:
    # We initialize our result array which will store any strings that are substrings of another
    result: list[str] = []

    # We initialize our trie structure with a root node
    root = TrieNode()

    print("Initial Trie Root:")
    print(root.pretty_print())

    # First loop is an iteration through each word in the words array to insert into our prefix trie
    for word in words:
        # This inner loop moves us through each character of each word
        for i in range(len(word)):
            # This will insert each word into our trie by an increasingly long prefix --> Until the word is completed
            #   If the word is MASS --> first we enter 'M', then 'MA', then 'MAS', and so on
            insert_word(root, word[i:])

    print("\nFinal Trie Structure:")
    print(root.pretty_print())

    # Second loop is an iteration through the same words but uses the helper function to check if each word is a substring of another
    for word in words:
        if isSubstring(root, word):
            result.append(word)

    print(f"Result Arr: {result}")
    return result


# Helper function to insert each word into our Trie by character --> Following the prefix structure
def insert_word(root: TrieNode, word: str) -> None:
    curr_node = root

    # Loop through the characters in the word to insert into the tree to properly update nodes and frequencies
    for char in word:
        # If a particular character has not yet been entered, we create a new child node for that prefix path
        if char not in curr_node.child_nodes:
            curr_node.child_nodes[char] = TrieNode()

        # Update the current node to the current visited character's node
        curr_node = curr_node.child_nodes[char]

        # Update the frequency of that character --> We have visited it once more
        curr_node.frequency += 1


# Helper function to traverse our Trie for each word to determine if it has been used more than once
def isSubstring(root: TrieNode, word: str) -> bool:
    curr_node = root

    # Move each character through the tree --> Utilize the child_nodes to ensure we are following the same string path
    for char in word:
        curr_node = curr_node.child_nodes[char]

    # Returning thid boolean ensures that we have the encountered the same string more than once in our array
    return curr_node.frequency > 1


stringMatching(["mass", "as", "hero", "superhero"])
# stringMatchingBrute(["mass", "as", "hero", "superhero"])
