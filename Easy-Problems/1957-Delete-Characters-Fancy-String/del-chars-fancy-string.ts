// PROBLEM #1957 - DELETE CHARACTERS TO MAKE A FANCY STRING

// A fancy string is a string where no three consecutive characters are equal.

// Given a string s, delete the minimum possible number of characters from s to make it fancy.

// Return the final string after the deletion. It can be shown that the answer will always be unique.

// ---------------------------------------------------------------------------------------------------------------------------

function makeFancyString(s: string): string {
    let result = "";
    let prevChar = ">";
    let count = 1;

    // Iterate through each character of the string --> Minimum time complexity
    for (let char of s) {
        // If it differs from the previous character, we add to the result and the count remains one
        if (char !== prevChar) {
            count = 1;
            result += char;
            // If it is the same as the previous character but our count is within the bounds of three consecutive numbers, we add to result and increase the count
        } else if (count < 2) {
            count += 1;
            result += char;
        }

        console.log(result);

        // Updated the previous character variable after each iteration
        prevChar = char;
    }

    return result;
}

makeFancyString("leeetcode");
