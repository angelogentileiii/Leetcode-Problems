// Problem #283 --> MOVE ZEROES

// Remove substrings of 'AB' and 'CD" from the string. Return the minimum length of the string.
// After each removal the string is concatenated.

//---------------------------------------------------------------------------------------------------------------------------

// STACK SOLUTION
function minLength(str: string): number {
    let stack: string[] = [];

    for (let i = 0; i < str.length; i++) {
        if (str[i] === "B") {
            if (stack && stack[stack.length - 1] === "A") {
                stack.pop();
            } else {
                stack.push(str[i]);
            }
        } else if (str[i] === "D") {
            if (stack && stack[stack.length - 1] === "C") {
                stack.pop();
            } else {
                stack.push(str[i]);
            }
        } else {
            stack.push(str[i]);
        }
    }

    return stack.length;
}

//---------------------------------------------------------------------------------------------------------------------------

// TWO-POINTER SOLUTION
function minLength2(str: string): number {
    let chars = str.split(""); // Still technically makes the solution O(n) in JavaScript because we cannot modify string in place
    let index = 0;

    // for (let i = 0; i < chars.length; i++) {
    //     if (chars[i] === "B") {
    //         if (index > 0 && chars[index - 1] === "A") {
    //             index -= 1; // Removes the 'AB' pair bey decrementing the index
    //             // So on next loop, the pair will be overwritten
    //         } else {
    //             chars[index] = chars[i];
    //             index += 1;
    //         }
    //     } else if (chars[i] === "D") {
    //         if (index > 0 && chars[index - 1] === "C") {
    //             index -= 1; // Removes the 'CD' pair bey decrementing the index
    //             // So on next loop, the pair will be overwritten
    //         } else {
    //             chars[index] = chars[i]; // Write the character into the array at the index
    //             index += 1; // Move index forward one
    //         }
    //     } else {
    //         chars[index] = chars[i];
    //         index += 1;
    //     }
    // }

    // SWITCH/CASE STATEMENT INSTEAD
    for (let i in chars) {
        switch (chars[i]) {
            case "B":
                if (index > 0 && chars[index - 1] === "A") {
                    index -= 1;
                } else {
                    chars[index] = chars[i];
                    index += 1;
                }
                break;
            case "D":
                if (index > 0 && chars[index - 1] === "C") {
                    index -= 1;
                } else {
                    chars[index] = chars[i];
                    index += 1;
                }
                break;
            default:
                chars[index] = chars[i];
                index += 1;
                break;
        }
    }
    return index; // Represents the length of the reduced string (final index)
}

const minSeq1 = "ABBCDACBABCDE"; // Answer expected is 5
const minSeq2 = "ABBBABBAB"; // Answer expected is 3

console.log("Answer #1: ", minLength2(minSeq1));
console.log("Answer #2: ", minLength2(minSeq2));
