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

import { PrefixTrie } from "../../Utils/TypeScript/Trie";

function stringMatching(words: string[]): string[] {
    // Initialize the result array to store words that are substrings of another word
    let result: string[] = [];

    // Create a root TrieNode for building the prefix Trie
    const trie = new PrefixTrie();

    // First loop: Iterate through each word in the input array
    for (const word of words) {
        // For each word, add all its suffixes to the Trie
        // Example: For "mass", add "mass", "ass", "ss", and "s"
        for (let i = 0; i < word.length; i++) {
            trie.insertWord(word.slice(i));
        }
    }

    console.log("Initial Trie Root:");
    console.log(trie.root.prettyPrint()); // Print the Trie structure for debugging

    // Second loop: Check if each word is a substring of another word
    for (const word of words) {
        if (trie.searchWord(word)) {
            result.push(word); // Add the word to the result array if it's a substring
        }
    }

    console.log(`Completed Result: ${result}`); // Log the final result array
    return result; // Return the result array
}

stringMatching(["mass", "as", "hero", "superhero"]);
// stringMatchingBrute(["mass", "as", "hero", "superhero"]);
