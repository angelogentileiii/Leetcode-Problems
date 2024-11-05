// PROBLEM #2914 - MINIMUM NUMBER OF CHANGES TO MAKE A BINARY STRING BEAUTIFUL

// You are given a 0-indexed binary string s having an even length.

// A string is beautiful if it's possible to partition it into one or more substrings such that:

// Each substring has an even length.
// Each substring contains only 1's or only 0's.
// You can change any character in s to 0 or 1.

// Return the minimum number of changes required to make the string s beautiful.

// Example 1:

// Input: s = "1001"
// Output: 2
// Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
// It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
// It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

// ---------------------------------------------------------------------------------------------------------------------------

function minChanges(s: string): number | void {
    // Base case that returns when the string has an odd length --> Cannot be made beautiful
    if (s.length % 2 !== 0) {
        console.log("Cannot make string beautiful!");
        return;
    }

    // Variable for capturing the total number of changes necessary
    let count = 0;

    // Loop through the string and compare pairs of numbers
    for (let i = 0; i <= s.length; i += 2) {
        if (s[i] !== s[i + 1]) {
            count += 1;
        }
    }

    // The count now represents the minimum number of changes necessary to create the pairs (make it beautiful)
    console.log(count);
    return count;
}

minChanges("10101");
minChanges("11000111");
