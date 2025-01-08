from typing import Dict, Union, Tuple


class TrieNode:
    def __init__(self):
        # Used to track the frequency of every substring
        self.frequency = 0

        # Maps each character to their respective child nodes --> Continuation of prefix
        self.child_nodes: Dict[Union[str, Tuple[str, str]], "TrieNode"] = {}

    def __repr__(self):
        return f"TrieNode(frequency={self.frequency}, child_nodes={(self.child_nodes.keys())})"

    # Helper function to recursively print the Trie structure in a more readable manner
    def pretty_print(self, level=0):
        # As we have child nodes --> Each child of the char node is indented further
        indent = "  " * level
        result = f"{indent}TrieNode(frequency={self.frequency}, children={list(self.child_nodes.keys())})\n"
        for char, child in self.child_nodes.items():
            result += f"{indent}  '{char}':\n{child.pretty_print(level + 2)}"
        return result


class TrieBase:
    def __init__(self):
        self.root = TrieNode()

    # Insert a path into the tree
    def _insert(self, path: list) -> None:
        curr_node = self.root
        for key in path:
            if key not in curr_node.child_nodes:
                curr_node.child_nodes[key] = TrieNode()
            curr_node = curr_node.child_nodes[key]
            curr_node.frequency += 1

    # Search the tree for a path and return its frequency
    def _search(self, path: list) -> int:
        curr_node = self.root

        print(f"Search Path: {path}")

        for key in path:
            if key not in curr_node.child_nodes:
                print(f"Key {key} not found in {curr_node.child_nodes.keys()}")
                return 0
            curr_node = curr_node.child_nodes[key]
        return curr_node.frequency


class PrefixTrie(TrieBase):
    def insert_word(self, word: str) -> None:
        return self._insert(list(word))

    def search_word(self, word: str) -> bool:
        return self._search(list(word)) > 1


class PrefixSuffixTrie(TrieBase):
    def insert_word(self, word: str) -> None:
        path = [(word[i], word[len(word) - 1 - i]) for i in range(len(word))]
        return self._insert(path)

    def search_word(self, word: str) -> int:
        path = [(word[i], word[len(word) - 1 - i]) for i in range(len(word))]
        return self._search(path)
