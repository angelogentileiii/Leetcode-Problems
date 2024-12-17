// PROBLEM #2182 - CONSTRUCT A STRING WITH A REPEAT LIMIT

// You are given a string s and an integer repeatLimit.
// Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row.
// You do not have to use all characters from s.

// Return the lexicographically largest repeatLimitedString possible.

// A string a is lexicographically larger than a string b if:
// In the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.
// If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

// ---------------------------------------------------------------------------------------------------------------------------

function repeatLimitedString(s: string, repeatLimit: number): string {
    // Split and sort the characters of the string in lexagraphical order --> Z to A
    let chars = s.split("");
    chars.sort((a, b) => b.localeCompare(a));

    console.log(`Chars Lex Sorted: ${chars}`);

    // Initialize result and our two pointers for our count and our position
    let result: string[] = [];
    let count = 0;
    let point = 0;

    // Loop through all of the available characters
    for (let i = 0; i < chars.length; i++) {
        // If the result already has characters and the last character of result matches the current character
        if (result[result.length - 1] === chars[i]) {
            // If the current count of the character is within bounds
            if (count < repeatLimit) {
                // Simply add to result and increase our counter
                result.push(chars[i]);
                console.log(`Within RepeatLimit: ${result}`);
                count++;
            } else {
                // Find the next distinct character
                point = Math.max(point, i + 1);

                // Update point until we reach end of the string or a distinct character
                while (point < chars.length && chars[point] === chars[i]) {
                    point++;
                }

                // If we are within bounds continue
                if (point < chars.length) {
                    // Add the character to the result
                    result.push(chars[point]);
                    console.log(`Found New Char: ${result}`);

                    // Swap our chars at i to ensure we can continue in the proper order
                    // Moves our chars[i] pointer to the new distinct character and puts the pointer to the next character in the list
                    [chars[i], chars[point]] = [chars[point], chars[i]];

                    // Reset the count to 1
                    count = 1;
                } else {
                    // Otherwise we cannot add to our result string anymore
                    break;
                }
            }
        } else {
            // If the result is empty or we have a new character, we can simply push into the result and keep/reset the counter at 1
            result.push(chars[i]);
            console.log(`Empty Result or Last Character is Diff: ${result}`);
            count = 1;
        }
    }

    console.log(`Completed Result: ${result.join("")}`);
    console.log(" ");

    return result.join("");
}

repeatLimitedString("cczazcc", 3);

repeatLimitedString("aababab", 2);
