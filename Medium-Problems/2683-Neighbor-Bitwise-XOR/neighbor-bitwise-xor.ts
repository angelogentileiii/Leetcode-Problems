// PROBLEM #2683 - NEIGHBORING BITWISE XOR

// A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n.

// Specifically, for each index i in the range [0, n - 1]:
//   - If i = n - 1, then derived[i] = original[i] ⊕ original[0].
//   - Otherwise, derived[i] = original[i] ⊕ original[i + 1].

// Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.

// Return true if such an array exists or false otherwise.
//   - A binary array is an array containing only 0's and 1's

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// XOR can be used to check if certain operations or relationships are balanced
//   - So the cumulative XOR of derived would tell us whether the transformation "cancels out" or not (returns a 0)
//   - If the cumulative XOR returns an integer, it indicates that something is not balanced in the transformation process
//       - The original array could not be valid then --> There is "additional" information that prevents the transformation from being valid

// So all we need to find is:
//   - XOR = 0: The transformation is balanced and likely valid (a valid original array can exist)
//   - XOR ≠ 0 (like 1): The transformation is unbalanced and therefore not valid (no valid original array can exist)

// ---------------------------------------------------------------------------------------------------------------------------

function doesValidArrayExist(derived: number[]): boolean {
    // Get the length of the derived array
    const n = derived.length;

    // Initialize a variable to hold the XOR of all elements in derived
    let result = 0;

    // Loop through each element in the derived array
    for (const i of derived) {
        // XOR the current element of derived with `res` --> Cumulative XOR
        result ^= i;

        console.log(`Result in Loop: ${result}`);
    }

    console.log(`Result: ${result === 0} \n`);
    // Return True if `res` is 0, otherwise False
    return result === 0;
}

doesValidArrayExist([1, 1, 0]);
doesValidArrayExist([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]);
