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
        self.child_nodes = {}
        self.isEnd = False

    # Format the printout of the Node
    def __repr__(self, level=0):
        indent = "  " * level
        # Format the current node's representation
        result = f"{indent}TrieNode(isEnd={self.isEnd}, children=["

        # Recursively format the child nodes if there are any
        if self.child_nodes:
            for key, child in self.child_nodes.items():
                result += f"\n{indent}  '{key}': {child.__repr__(level + 1)}"
            result += f"\n{indent}]"
        else:
            result += "])"

        return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Added to replicate the Leetcode desired solution in the terminal
    def __repr__(self):
        return "null"

    def insert(self, word: str) -> str:
        curr_node = self.root

        for char in word:
            if char not in curr_node.child_nodes:
                curr_node.child_nodes[char] = TrieNode()
            curr_node = curr_node.child_nodes[char]
        curr_node.isEnd = True

        # Only used for my print statement in the terminal to match the expected output on Leetcode --> Not necessary in solution
        return "null"

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.child_nodes:
                return False
            curr_node = curr_node.child_nodes[char]
        return curr_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.child_nodes:
                return False
            curr_node = curr_node.child_nodes[char]

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
