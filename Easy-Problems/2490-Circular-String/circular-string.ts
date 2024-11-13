// PROBLEM 2490 - CIRCULAR STRING

// A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

// For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
// Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

// A sentence is circular if:

// The last character of a word is equal to the first character of the next word.
// The last character of the last word is equal to the first character of the first word.
// For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
// However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

// Given a string sentence, return true if it is circular. Otherwise, return false.

// ---------------------------------------------------------------------------------------------------------------------------

function isCircularSentence(sentence: string): any {
    // Split the sentence into an array by whitespace
    const senArr = sentence.split(" ");
    console.log(senArr);

    // Grab the first and last word for initial comparison
    const firstWord = senArr[0];
    const lastWord = senArr[senArr.length - 1];

    console.log(firstWord, lastWord);

    // Compare the first letter of first word and last letter of last word
    if (firstWord[0] !== lastWord[lastWord.length - 1]) {
        return false;
    }

    // Loop through all words beginning at the second word
    for (let i = 1; i < senArr.length; i++) {
        // Variable for readability in if statement
        let prevWord = senArr[i - 1];

        // Compare the first letter of the current word to the last letter of the previous word
        if (senArr[i][0] !== prevWord[prevWord.length - 1]) {
            console.log(false);
            return false;
        }
    }

    // If all conditions pass, we have a circular sentence
    console.log(true);
    return true;
}

isCircularSentence("leetcode exercises sound delightful");
isCircularSentence("ab a");
