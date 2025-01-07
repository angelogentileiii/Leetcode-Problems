// PROBLEM #2390 - REMOVING STARS FROM A STRING

// You are given a string s, which contains stars *.

// In one operation, you can:
//   Choose a star in s.
//   Remove the closest non-star character to its left, as well as remove the star itself.

// Return the string after all stars have been removed.

// Note:
//   The input will be generated such that the operation is always possible.
//   It can be shown that the resulting string will always be unique.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// Utilize a stack as we traverse the characters in the string
// If it is a '*' we pop off of the top of the stack, otherwise we append the letter to the stack
// Maintains removing all items that had last entered the stack --> The character just prior to the '*'

// ---------------------------------------------------------------------------------------------------------------------------

function removeStars(s: string): string {
    // Initialize our stack
    let stack: string[] = [];

    // Loop through each character of our input string
    for (const char of s) {
        // If the character is not a '*', simply push onto the stack
        // Otherwise, we pop the last seen character off of the stack --> Represents the character to the left of the current '*' found
        if (char !== "*") {
            stack.push(char);
        } else {
            stack.pop();
        }
        console.log(`Stack within Loop: ${stack}`);
    }

    console.log(`Stack after Loop: ${stack}`);

    // Join the updated stack back into a string as per the parameters
    console.log(`Result: ${stack.join("")}`);
    return stack.join("");
}

// As many have noted on Leetcode, this is a fairly straightforward stack problem that appears too clear to be ranked as a Medium problem

removeStars("leet**cod*e");
