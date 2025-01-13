// PROBLEM #3223 - MINIMUM LENGTH OF STRING AFTER OPERATIONS

// You are given a string s.

// You can perform the following process on s any number of times:
//     Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
//     Delete the closest character to the left of index i that is equal to s[i].
//     Delete the closest character to the right of index i that is equal to s[i].

// Return the minimum length of the final string s that you can achieve.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to have the same character on the left and right to be able to remove a singular character (either left or right)
//      So, if we have three characters, we can remove one from either side and have a single remaining character
//      If we have two characters, we cannot remove any because there is not a matching character on both sides of either

// If we count the characters on the string, each odd number of character will leave one behind and each even number will leave two
//      We can count these final numbers to determine the minimum string after the operations

// ---------------------------------------------------------------------------------------------------------------------------

function minimumLength(s: string): number {
    // I chose to use an array here to track the number of each character in the string --> Could be an object as well {char: frequency}
    let charArr = new Array(26).fill(0);

    // Loop through the characters to update the corresponding index of the array
    for (let i = 0; i < s.length; i++) {
        // The subtraction sets the charCode at a value between 0-25 correlated to the letter in the alphabet
        charArr[s.charCodeAt(i) - "a".charCodeAt(0)]++;
    }

    console.log(`Characters: ${charArr}`);

    // Set our variable for our min string length result
    let result = 0;
    for (const val of charArr) {
        // For each value, if there are no characters in the string we can ignore and move to next value
        if (val === 0) continue;

        // Otherwise, we can use val % 2 to determine the remainder
        //      If it is an even number, the remainder is 0 so we simply add 2 to the result --> The minimum of even characters that remain
        //      If it is an odd number, the remainder is 1 so 2 - 1 is 1 and we add that to the result --> Represents the minimum of odd characters that remain
        result += 2 - (val % 2);
    }

    console.log(`Result: ${result}`);
    return result;
}
