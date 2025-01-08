// PROBLEM #3042 - COUNT PREFIX AND SUFFIX PAIRS I

// You are given a 0-indexed string array words.

// Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

// isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.

// For example:
//   isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

// Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

// ---------------------------------------------------------------------------------------------------------------------------

// BRUTE FORCE SOLUTION

// Utilize nested for loops to check each string against all possible options in the remaining array --> As long as left index < right index (i < j)

function countPrefixSuffixPairsBrute(words: string[]): number {
    let count = 0;

    for (let i = 0; i < words.length; i++) {
        for (let j = i + 1; j < words.length; j++) {
            if (isPrefixAndSuffix(words[i], words[j])) {
                count += 1;
            }
        }
    }

    console.log(`Final Result: ${count}`);
    return count;
}

function isPrefixAndSuffix(str1: string, str2: string): boolean {
    const n1 = str1.length;
    const n2 = str2.length;

    if (n1 > n2) return false;

    const prefix = str2.slice(0, n1);
    const suffix = str2.slice(-n1);

    console.log(`Prefix: ${prefix} -- Suffix: ${suffix}`);

    return prefix === str1 && suffix === str1;
}

// countPrefixSuffixPairsBrute(["a", "ababa", "aa", "aba"]);

// ---------------------------------------------------------------------------------------------------------------------------

// PREFIX AND SUFFIX TRIE SOLUTION

// Build a trie where we can store the prefix and suffix of each word
// As we input into the trie, we will add pairs (first letter, last letter) and move inward until the word is submitted

// Then we add a function to search the trie with each word to determine if it is a substring (prefix & suffix)

import { PrefixSuffixTrie } from "../../Utils/TypeScript/Trie";

function countPrefixSuffixPairs(words: string[]): number {
    let result = 0;
    let trie = new PrefixSuffixTrie();

    for (let i = words.length - 1; i >= 0; i--) {
        const word = words[i];
        console.log(`Curr Word: ${word}`);

        result += trie.searchWord(word);

        trie.insertWord(word);

        console.log(`Tree After Current Word: ${word}`);
        console.log(trie.root.prettyPrint());
    }

    console.log(`Result: ${result}`);
    return result;
}

countPrefixSuffixPairs(["a", "ababa", "aa", "aba"]);
