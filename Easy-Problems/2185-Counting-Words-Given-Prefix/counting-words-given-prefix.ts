// PROBLEM #2185 - COUNTING WORDS WITH A GIVEN PREFIX

// You are given an array of strings words and a string pref.

// Return the number of strings in words that contain pref as a prefix.

// A prefix of a string s is any leading contiguous substring of s.

// ---------------------------------------------------------------------------------------------------------------------------

function prefixCount(words: string[], prefix: string): number {
    // Initialize our count variable --> Will output total words with prefix
    let count = 0;

    // Loop through each word of the words array
    for (const word of words) {
        // Option #1: Slice the word from the beginning to the length of the prefix --> Check if the sliced string and the prefix match
        // if (word.slice(0, prefix.length) === prefix) count++;

        // Option #2: Utilize built in method to determine if word begins with the prefix
        if (word.startsWith(prefix)) count++;
    }

    console.log(`Result: ${count}`);
    return count;
}

prefixCount(["pay", "attention", "practice", "attend"], "at");
