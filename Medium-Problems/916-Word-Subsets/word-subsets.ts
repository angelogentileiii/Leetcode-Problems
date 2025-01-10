// PROBLEM #916 - WORD SUBSETS

// You are given two string arrays words1 and words2.

// A string b is a subset of string a if every letter in b occurs in a including multiplicity.

// For example, "wrr" is a subset of "warrior" but is not a subset of "world".

// A string a from words1 is universal if for every string b in words2, b is a subset of a.

// Return an array of all the universal strings in words1. You may return the answer in any order.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// Key focus is this line: A string a from words1 is universal if for every string b in words2, b is a subset of a
// We need to ensure that each character in the words2 list is present in words1 at minimum the same frequency

// First: Count the frequency of each character in words2 --> List or Dict
// Second: Count the frequency of each character in words1 against our frequency data structure
// - As long as there are the frequencies in words1 are >= frequencies in our words2 count --> We are valid

// ---------------------------------------------------------------------------------------------------------------------------

function wordSubsets(words1: string[], words2: string[]): string[] {
    // Initialize the result array --> This will store all the universal strings from words1
    let result: string[] = [];

    // Initialize an array to store the maximum frequency of each character across all words in words2
    let word2Freq = new Array(26).fill(0);

    // Loop through each word in words2 to calculate the frequency of each character across all words
    for (const word of words2) {
        // Get character counts for the current word in words2
        const char_count = count(word);
        console.log(`Word: '${word}' - Frequency Array: ${char_count}`);

        // Update the global frequency array for words2 (we want the maximum frequency for each char)
        for (const [idx, char] of char_count.entries()) {
            word2Freq[idx] = Math.max(word2Freq[idx], char);
        }

        // Print the updated global frequency array after processing each word from words2
        console.log(`Updated Words2 Freq Array: ${word2Freq}\n`);
    }

    // Print the final frequency array after processing all words in words2
    console.log(
        `Final Words2 Frequency Array (Maximum Across All): ${word2Freq}\n`
    );

    // Loop through words1 to compare the frequency array of words2 against each word in words1
    for (const word of words1) {
        // Get character counts for the current word in words1
        const word_count = count(word);
        console.log(`Word: '${word}' - Frequency Array: ${word_count}`);

        // Check if the word from words1 satisfies the universal condition
        if (word_count.every((x, idx) => x >= word2Freq[idx])) {
            console.log(`'${word}' is Universal (Meets the Condition)\n`);
            result.push(word);
        }
    }

    // Print the final result array containing all the universal words
    console.log("Completed Result: ", result);
    return result;
}

// This helper function calculates the frequency of each character in the given word.
function count(word: string): number[] {
    let freq = new Array(26).fill(0); // Initialize an array to store counts for 'a' to 'z'

    // Loop through each character in the word
    for (const char of word) {
        // Calculate the position of the character in the alphabet --> Using the equation we set the code between a range of 0 and 25 (a to z)
        const charCode = char.charCodeAt(0) - "a".charCodeAt(0);

        // Increment the frequency count for the corresponding character
        freq[charCode] += 1;
    }

    return freq;
}

wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]);
