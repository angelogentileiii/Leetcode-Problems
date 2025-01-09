# PROBLEM #208 - IMPLEMENT TRIE (PREFIX TREE)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
#   Trie() Initializes the trie object.
#   void insert(String word) Inserts the string word into the trie.
#   boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#   boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# ---------------------------------------------------------------------------------------------------------------------------

# You are provided with the framework of the Trie (__init__, methods) but no TrieNode class.


class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes, where keys are characters and values are TrieNode objects
        self.child_nodes = {}
        # Boolean flag to indicate if this node marks the end of a word
        self.isEnd = False

    # Custom string representation for debugging and visualization
    def __repr__(self, level=0):
        indent = "  " * level  # Indentation based on the level of the node
        # Start the representation with the current node's details
        result = f"{indent}TrieNode(isEnd={self.isEnd}, children=["

        # Recursively format child nodes
        if self.child_nodes:
            for key, child in self.child_nodes.items():
                result += f"\n{indent}  '{key}': {child.__repr__(level + 1)}"
            result += f"\n{indent}]"
        else:
            result += "])"  # Close the bracket if no child nodes

        return result


class Trie:
    def __init__(self):
        # Root node of the Trie
        self.root = TrieNode()

    # Custom string representation for the Trie, matching expected output for LeetCode solutions
    def __repr__(self):
        return "null"

    # Inserts a word into the Trie.
    # - For each character in the word, checks if a corresponding child node exists.
    # - If not, creates a new child node for that character.
    # - Marks the final node as the end of a word.
    def insert(self, word: str) -> str:
        curr_node = self.root

        # Traverse the Trie, creating nodes as needed
        for char in word:
            if char not in curr_node.child_nodes:
                # Create a new node for the character if it doesn't exist
                curr_node.child_nodes[char] = TrieNode()
            curr_node = curr_node.child_nodes[char]  # Move to the next node

        # Mark the end of the word
        curr_node.isEnd = True

        # Return "null" for consistent output in LeetCode, not required for core functionality
        return "null"

    # Searches for a word in the Trie.
    # - Returns True if the word exists and ends at a valid node.
    # - Returns False if the word is not found or does not end at a valid node.
    def search(self, word: str) -> bool:
        curr_node = self.root

        # Traverse the Trie for each character in the word
        for char in word:
            if char not in curr_node.child_nodes:
                return False  # Character not found, word does not exist
            curr_node = curr_node.child_nodes[char]  # Move to the next node

        # Check if the current node marks the end of the word
        return curr_node.isEnd

    # Checks if there is any word in the Trie that starts with the given prefix.
    # - Returns True if the prefix is found in the Trie.
    # - Returns False otherwise.
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        # Traverse the Trie for each character in the prefix
        for char in prefix:
            if char not in curr_node.child_nodes:
                return False  # Character not found, prefix does not exist
            curr_node = curr_node.child_nodes[char]  # Move to the next node

        # If traversal completes, the prefix exists in the Trie
        return True


# Test inputs:
trie = Trie()
output = [
    trie,
    trie.insert("apple"),
    trie.search("apple"),
    trie.search("app"),
    trie.startsWith("app"),
    trie.insert("app"),
    trie.search("app"),
]

print(output)

# print(trie.root)
