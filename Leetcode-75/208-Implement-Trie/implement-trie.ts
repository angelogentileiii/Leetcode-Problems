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
    childNodes: { [key: string]: TrieNode };
    isEnd: boolean;

    constructor() {
        this.childNodes = {};
        this.isEnd = false;
    }
}

class Trie {
    root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    insert(word: string): void {
        let currNode = this.root;

        for (const char of word) {
            if (!currNode.childNodes[char]) {
                currNode.childNodes[char] = new TrieNode();
            }
            currNode = currNode.childNodes[char];
        }
        currNode.isEnd = true;
    }

    search(word: string): boolean {
        let currNode = this.root;

        for (const char of word) {
            if (!currNode.childNodes[char]) {
                return false;
            }
            currNode = currNode.childNodes[char];
        }
        return currNode.isEnd;
    }

    startsWith(prefix: string): boolean {
        let currNode = this.root;

        for (const char of prefix) {
            if (!currNode.childNodes[char]) {
                return false;
            }
            currNode = currNode.childNodes[char];
        }
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
