// PROBLEM #2559 - COUNT VOWEL STRINGS IN RANGES

// You are given a 0-indexed array of strings words and a 2D array of integers queries.
// Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
// Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

// Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'. --> NOT 'y'

// Essentially, we need to return an array where each index of that array represents the number of vowel strings within the corresponding query range

// ---------------------------------------------------------------------------------------------------------------------------

function vowelStrings(words: string[], queries: number[][]): any {
    const vowels: string[] = ["a", "e", "i", "o", "u"];
    let sum: number[] = [];
    let result: number[] = [];
    let count = 0;

    // This loop traverses each of our words and checks whether it is a valid vowel string or not
    for (let word of words) {
        // If so, we update the count variable to include the total vowel strings up to the current index
        if (
            vowels.includes(word[0]) &&
            vowels.includes(word[word.length - 1])
        ) {
            console.log(`Vowel String: ${word}`);
            count += 1;
        }

        // At each iteration, we push the count variable into our sum array --> To be used for the queries loop
        sum.push(count);
    }

    // This loop traverses each of our queries and finds the correct amount of vowel strings within the range
    for (let query of queries) {
        const [left, right] = query;

        if (left === 0) {
            // If we begin with a left index of 0, we only need to push the right most value of the sum array into the result --> Follows the same order
            result.push(sum[right]);
        } else {
            // Otherwise, we must subtract the value at the index to the left of our left variable --> So we include the proper range of left to right inclusive
            result.push(sum[right] - sum[left - 1]);
        }
    }

    console.log(`Final Result: ${result}`);
    return result;
}

vowelStrings(
    ["aba", "bcb", "ece", "aa", "e"],
    [
        [0, 2],
        [1, 4],
        [1, 1],
    ]
);
