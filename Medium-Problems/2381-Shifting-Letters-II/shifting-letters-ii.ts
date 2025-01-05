// PROBLEM 2381 - SHIFTING LETTERS II

// You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]
// For every i, shift the characters in s from the index start[i] to the index end[i] (inclusive)
// --> Forward if direction[i] = 1, or shift the characters backward if direction[i] = 0

// Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a')
// Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z')

// Return the final string after all such shifts to s are applied

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// PREFIX SUM TECHNIQUE
// Similar to problem #2559 -> Calculate all of the shifts possible BEFORE performaing the shifts
// If we shift for each index of the shifts array, it can become a very slow process --> My first solution failed on Leetcode because of this

// ---------------------------------------------------------------------------------------------------------------------------

function shiftingLetters(s: string, shifts: number[][]): any {
    // Initialize an array that will keep track of the move direction at each index of s
    // The extra element (s.length + 1) helps us manage the shifts at the end of the range --> So we don't modify the array beyond the last letter (avoids error)
    let moves = new Array(s.length + 1).fill(0);

    console.log(`Moves Array: ${moves}`);

    // Iterate through the shifts array to update our moves array --> Calculate how we will shift each element
    for (let shift of shifts) {
        const [start, end, direction] = shift;

        console.log(`Start: ${start}, End: ${end}, Direction: ${direction}`);

        // Where the range of the current shift begins --> Set to 1 means it will increase the characters vs. -1 which will reverse
        // If two shifts affect the same index, the net effect (shift) will be the sum of their indvidual directions
        moves[start] += direction === 1 ? 1 : -1;

        // Ensure that the end is updated inclusively, so we update end + 1 to ensure that we update the moves array properly
        // If end + 1 exceeds or equals the length of the string, we don’t need to apply a shift beyond the last index of the string --> It is out of bounds
        if (end + 1 < s.length) {
            // At the end we perform the opposite functionality of our start by -= the same conditional
            moves[end + 1] -= direction === 1 ? 1 : -1;
        }

        console.log(`Moves After Direction: ${moves}`);
    }

    // The currentShift within the moves array --> At each index, we will update the value with the cumulative shift necessary (All overlapping range shifts)
    let currShift = 0;

    // Make the string into an array to perform mutable actions --> Strings are immutable
    let result = s.split("");

    // Set a variable for the base code used to set an order to the characters --> Essentially the code value to the letter 'a' (A reference point for conversion)
    // This will help us zero index the letters in the alphabet later on --> 'b'.charCodeAt(0) - base = 1 and 'z'.charCodeAt(0) - base = 25 (zero indexed)
    // This also helps with the wraparound from z to a and a to z
    const base = "a".charCodeAt(0);

    // Iterate through the characters of the string --> To use with our moves array
    for (let i = 0; i < s.length; i++) {
        // Update the total direction of our current move by creating the cumulative sum of all indexes of moves up to this point
        currShift += moves[i];

        console.log(
            `Current Shift: ${((currShift % 26) + 26) % 26} - Current Letter: ${
                s[i]
            }`
        );

        // The netShift represents the total amount of characters needed to move either positive or negative for the current index
        // This ensures that the calculation is always a NON-NEGATIVE number between 0 and 25
        // currShift % 26 finds the remainder when currShift is divided by 26 --> ensure that we will wraparound from z to a and a to z
        // We add the 26 to this remainder to ensure that we are always positive between 0 and 25 --> -1 become 25 which is z
        // Because of that addition, we can exceed our valid char range, so again we find the remainder by using modulo 26 which then computes our final answer
        const netShift = ((currShift % 26) + 26) % 26;

        // The letter code of the current letter at this index in the string
        const letterCode = s.charCodeAt(i);

        // The calculation to determine the new letterCode with the calculated shift determined by the moves array
        // We take the letterCode and subtract the base to zero index it, then we add the shift to determine where the new character will be
        // Then we find the remainder from the alphabet (Which also assists in the wraparound condition) and we add the base of 97 back to find the accurate character code
        const shiftedCode = ((letterCode - base + netShift) % 26) + base;

        console.log(
            `Original Letter: ${
                s[i]
            } - ${letterCode} to New Letter: ${String.fromCharCode(
                shiftedCode
            )} - ${shiftedCode}`
        );

        // We are directly updating the corresponding index of the result array with the final shifted code converted back to a string --> The correct final character
        result[i] = String.fromCharCode(shiftedCode);
    }

    console.log(`Result String: ${result.join("")}`);

    // We rejoin the characters within the result array to output the updated string
    return result.join("");
}

// ---------------------------------------------------------------------------------------------------------------------------

shiftingLetters("abc", [
    [0, 1, 0],
    [1, 2, 1],
    [0, 2, 1],
]);

shiftingLetters("dztz", [
    [0, 0, 0],
    [1, 1, 1],
]);
