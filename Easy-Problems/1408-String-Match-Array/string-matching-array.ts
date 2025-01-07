// PROBLEM #1408 - STRING MATCHING IN AN ARRAY

// Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

// A substring is a contiguous sequence of characters within a string

// ---------------------------------------------------------------------------------------------------------------------------

// BRUTE FORCE SOLUTION

// This works for this problem since the constraints hold the words array to only 100 items with a maximum of 30 characters each
// Likely the expected solution for this being an EASY problem

// We simply have a nested loop where we test each word as a substring of every other possible word in the array

function stringMatchingBrute(words: string[]): string[] {
    let result: string[] = [];

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words.length; j++) {
            if (words[i] === words[j]) {
                continue;
            }
            if (words[j].includes(words[i])) {
                result.push(words[i]);
            }
        }
    }

    console.log(`Result: ${result}`);
    return result;
}

//  ---------------------------------------------------------------------------------------------------------------------------

//  PREFIX TRIE SOLUTION

//  This solution utilizes a trie to store all possible prefixes available within the words array
//  We can store each prefix and it's frequency of appearance to determine if a word is a substring of another word

// Our TrieNode class will be used for each node of our Trie and keeping track of both the character's frequency and children (next letters)
class TrieNode {
    childNodes: { [key: string]: TrieNode };
    frequency: number;

    constructor() {
        this.childNodes = {};
        this.frequency = 0;
    }

    // Helper function for logging in the console properly --> Indentation based on character index
    prettyPrint(level: number = 0): string {
        const indent = "  ".repeat(level);
        let result = `${indent}TrieNode(frequency=${
            this.frequency
        }, children=[${Object.keys(this.childNodes).join(", ")}])\n`;

        for (const [char, child] of Object.entries(this.childNodes)) {
            result += `${indent}  '${char}':\n${child.prettyPrint(level + 2)}`;
        }

        return result;
    }
}

function stringMatching(words: string[]): string[] {
    // Initialize the result array to store words that are substrings of another word
    let result: string[] = [];

    // Create a root TrieNode for building the prefix Trie
    const root = new TrieNode();

    // First loop: Iterate through each word in the input array
    for (const word of words) {
        // For each word, add all its suffixes to the Trie
        // Example: For "mass", add "mass", "ass", "ss", and "s"
        for (let i = 0; i < word.length; i++) {
            insertWord(root, word.slice(i));
        }
    }

    console.log("Initial Trie Root:");
    console.log(root.prettyPrint()); // Print the Trie structure for debugging

    // Second loop: Check if each word is a substring of another word
    for (const word of words) {
        if (isSubstring(root, word)) {
            result.push(word); // Add the word to the result array if it's a substring
        }
    }

    console.log(`Completed Result: ${result}`); // Log the final result array
    return result; // Return the result array
}

// Helper function to insert a word into the Trie
function insertWord(root: TrieNode, word: string): void {
    let currNode = root;

    // Traverse through each character of the word
    for (const char of word) {
        // If the character is not already a child of the current node, add it
        if (!currNode.childNodes[char]) {
            currNode.childNodes[char] = new TrieNode();
        }

        // Move to the child node corresponding to the character
        currNode = currNode.childNodes[char];

        // Increment the frequency of the node to track how many times this path is visited
        currNode.frequency += 1;
    }
}

// Helper function to check if a word is a substring of another
function isSubstring(root: TrieNode, word: string): boolean {
    let currNode = root;

    // Traverse the Trie using the characters of the word
    for (const char of word) {
        // If the character does not exist in the Trie, the word is not a substring
        if (!currNode.childNodes[char]) {
            return false;
        }

        // Move to the child node corresponding to the character
        currNode = currNode.childNodes[char];
    }

    // If the frequency of the last node is greater than 1, the word is a substring
    return currNode.frequency > 1;
}

stringMatching(["mass", "as", "hero", "superhero"]);
// stringMatchingBrute(["mass", "as", "hero", "superhero"]);
