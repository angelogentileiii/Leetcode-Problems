// PROBLEM #796 - ROTATE STRING

// Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

// A shift on s consists of moving the leftmost character of s to the rightmost position.

// For example, if s = "abcde", then it will be "bcdea" after one shift.

// ---------------------------------------------------------------------------------------------------------------------------

function rotateString(s: string, goal: string): boolean {
    // If the strings don't match length, they will never be circular
    if (s.length !== goal.length) {
        return false;
    }

    // By concatenating our string "s" --> What have every possible rotation of the string available
    const concat = s + s;

    console.log(concat);
    console.log(concat.indexOf(goal));

    // We check that the goal string is within our new concatenated string by using indexOf
    // If indexOf returns -1 --> The goal string does not exist, we return false
    return concat.indexOf(goal) !== -1;
}

rotateString("abcde", "abced");
rotateString("abcde", "cdeab");
