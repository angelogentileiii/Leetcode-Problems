// PROBLEM #208 - IMPLEMENT TRIE (PREFIX TREE)

// A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
// There are various applications of this data structure, such as autocomplete and spellchecker.

// Implement the Trie class:
//   Trie() Initializes the trie object.
//   void insert(String word) Inserts the string word into the trie.
//   boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
//   boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

// ---------------------------------------------------------------------------------------------------------------------------

// You are provided with the framework of the Trie (__init__, methods) but no TrieNode class.

class TrieNode {
    // A map to store child nodes, where keys are characters and values are TrieNode instances
    childNodes: { [key: string]: TrieNode };
    // A flag to indicate if this node represents the end of a word
    isEnd: boolean;

    constructor() {
        // Initialize the child nodes map and set the end flag to false
        this.childNodes = {};
        this.isEnd = false;
    }
}

class Trie {
    // The root node of the Trie
    root: TrieNode;

    constructor() {
        // Initialize the Trie with a new root node
        this.root = new TrieNode();
    }

    // Inserts a word into the Trie.
    // - Traverses the Trie, creating new nodes as needed for each character in the word.
    // - Marks the last node as the end of the word.
    insert(word: string): void {
        let currNode = this.root;

        // Iterate over each character in the word
        for (const char of word) {
            // If the character is not already a child, create a new TrieNode
            if (!currNode.childNodes[char]) {
                currNode.childNodes[char] = new TrieNode();
            }
            // Move to the next node
            currNode = currNode.childNodes[char];
        }

        // Mark the last node as the end of the word
        currNode.isEnd = true;
    }

    // Searches for a word in the Trie.
    // - Returns true if the word exists and ends at a valid node.
    // - Returns false if the word is not found or does not end at a valid node.
    search(word: string): boolean {
        let currNode = this.root;

        // Traverse the Trie for each character in the word
        for (const char of word) {
            // If the character is not a child, the word does not exist
            if (!currNode.childNodes[char]) {
                return false;
            }
            // Move to the next node
            currNode = currNode.childNodes[char];
        }

        // Check if the current node marks the end of the word
        return currNode.isEnd;
    }

    //  Checks if there is any word in the Trie that starts with the given prefix.
    //  - Returns true if the prefix exists, false otherwise.
    startsWith(prefix: string): boolean {
        let currNode = this.root;

        // Traverse the Trie for each character in the prefix
        for (const char of prefix) {
            // If the character is not a child, the prefix does not exist
            if (!currNode.childNodes[char]) {
                return false;
            }
            // Move to the next node
            currNode = currNode.childNodes[char];
        }

        // If traversal completes, the prefix exists in the Trie
        return true;
    }
}

// Test inputs:
let trie = new Trie();
const output = [
    trie,
    trie.insert("apple"),
    trie.search("apple"),
    trie.search("app"),
    trie.startsWith("app"),
    trie.insert("app"),
    trie.search("app"),
];

console.log(output);
