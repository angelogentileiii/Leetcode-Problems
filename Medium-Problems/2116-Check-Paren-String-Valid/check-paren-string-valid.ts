// PROBLEM #2116 - CHECK IF A PARENTHESIS STRING CAN BE VALID

// A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
//   It is ().
//   It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
//   It can be written as (A), where A is a valid parentheses string.

// You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
//   If locked[i] is '1', you cannot change s[i].
//   But if locked[i] is '0', you can change s[i] to either '(' or ')'.

// Return true if you can make s a valid parentheses string. Otherwise, return false.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to count all of the open and closed parenthesis and compare against the locked array
// If we have the same number of open and closed parenthesis --> Within indexes at 0 able to be either option --> We have succesful string

// Therefore an odd length string is impossible to be valid
// And a string beginning with ")" and locked[0] == '1' is aslo invalid

// ---------------------------------------------------------------------------------------------------------------------------

function canBeValid(s: string, locked: string): boolean {
    const n = s.length;

    // If the string length is odd, it cannot be valid
    //      A valid parentheses string must have an even number of characters
    if (n % 2 !== 0) return false;

    let open_paren = 0;

    // Left-to-right scan to ensure there are no excess closing parentheses
    for (let i = 0; i < n; i++) {
        // If the character is '(' or the position is unlocked (locked[i] == '0'), treat it as an open parenthesis
        if (s[i] == "(" || locked[i] == "0") {
            open_paren++;
        } else {
            // Otherwise, it is a locked ')' and decreases the open count
            open_paren--;
        }

        // If at any point open_paren goes negative, there are too many ')' and the string is invalid
        if (open_paren < 0) return false;
    }

    let close_paren = 0;

    // Right-to-left scan to ensure there are no excess opening parentheses
    for (let i = n - 1; i >= 0; i--) {
        // If the character is ')' or the position is unlocked (locked[i] == '0'), treat it as a closing parenthesis
        if (s[i] == ")" || locked[i] == "0") {
            close_paren++;
        } else {
            // Otherwise, it is a locked '(' and decreases the close count
            close_paren--;
        }

        // If at any point close_paren goes negative, there are too many '(' and the string is invalid
        if (close_paren < 0) return false;
    }

    // If both scans pass, the string can be valid
    //      This means there are no excess ')' from left to right and no excess '(' from right to left
    return true;
}

canBeValid("))()))", "010100");
