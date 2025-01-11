// PROBLEM #1400 - CONSTRUCT K PALINDROM STRINGS

// Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// If the len(s) is the same as k --> We return True because each string is one character
// If k > len(s) --> We return False because we don't have enough characters to make enough palindrom strings

// We need to count each character in the string for it's frequency --> Use a dict/map for this
// If we have more characters that have odd values than the value k --> We return false
// - Each palindrom string can have at most one odd character --> The center index of the string
// We can count the total amount of odd values --> if > k, then we return False, else True

// ---------------------------------------------------------------------------------------------------------------------------

function canConstruct(s: string, k: number): boolean {
    const n = s.length;

    // If k is larger than n --> We don't have enough characters to make k strings
    if (k > n) return false;

    // If k is equal to n --> Each string can consist of exactly one character, so return true
    if (k === n) return true;

    // Object to count the frequency of each character in the string
    let freq: { [key: string]: number } = {};

    // Loop to populate the frequency map
    for (const char of s) {
        // If the character is not in the map, initialize it to 1, otherwise increment its count
        if (!freq[char]) {
            freq[char] = 1;
        } else {
            freq[char]++;
        }
    }

    // Log the frequency map to debug the character counts
    console.log(`Frequency Count: ${JSON.stringify(freq)}`);

    // Variable to track the number of characters with odd frequencies
    let oddCount = 0;

    // Iterate over the frequency map to count characters with odd frequencies
    for (const val of Object.values(freq)) {
        if (val % 2) {
            oddCount++;
        }
    }

    // If the number of odd-frequency characters is greater than k,
    // we cannot construct k palindrome strings using all characters
    if (oddCount > k) return false;

    // Otherwise, it is possible to construct k palindrome strings
    return true;
}

// ---------------------------------------------------------------------------------------------------------------------------

// Utilizing a set and a single for loop to keep track of odd character frequencies

function canConstructSet(s: string, k: number): boolean {
    const n = s.length;

    // If k is larger than n --> Not enough characters to form k strings
    if (k > n) return false;

    // If k is equal to n --> Each string can have one character
    if (k === n) return true;

    // Track characters with odd frequencies using a Set
    const oddSet = new Set<string>();

    // Iterate over the string and track odd frequencies
    for (const char of s) {
        // Check character's presence in the set (odd/even count tracking)
        if (oddSet.has(char)) {
            oddSet.delete(char); // Remove if already present (even count)
        } else {
            oddSet.add(char); // Add if not present (odd count)
        }

        console.log(`Char Set: ${Array.from(oddSet)}`);
    }

    // If the set size is larger than k --> We have too manmy odd characters to be able to build the palindromes while using all characters
    if (oddSet.size > k) return false;

    // If odd characters count is <= k, we can construct the palindromes
    return true;
}

console.log(canConstructSet("annabelle", 2));
console.log(canConstructSet("leetcode", 3));
