// PROBLEM #2429 - MINIMIZE XOR

// Given two positive integers num1 and num2, find the positive integer x such that:
//   - x has the same number of set bits as num2, and
//   - The value x XOR num1 is minimal.

// Note that XOR is the bitwise XOR operation.

// Return the integer x. The test cases are generated such that x is uniquely determined.

// The number of set bits of an integer is the number of 1's in its binary representation.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// Bit wise operations mean utilizing the binary code version of the integer ('0101') to calculate values
// This problem wants us to modify num1 to have the same number of 1 bits in our binary code as num2
//   - While also keeping num1 as small as possible as an integer

// XOR means 'Exclusive OR'
//  - A logical operation that compares two binary bits. The result of XOR is:
//      - 1 if the bits are different (one is 1 and the other is 0).
//      - 0 if the bits are the same (both are 0 or both are 1).
//  - If we compare 3 ('011') and 5 ('101') --> We get the number 6 ('110')
//      - First and second bits are different (return 1) but final bit is the same (return 0)

// By determining the number of bits in each num then increasing or decreasing num1 acccordingly,
// we ensure that we are only performing the minimum operations to complete our solution
//  - Indirectly fulfilling the condition of x XOR num1 is minimal

// in TYPESCRIPT/JAVASCRIPT, this problem is a bit more complicated as we need to create a helper function to count our '1' bits within our arguments
//  - There is no built in bit counter function

// ---------------------------------------------------------------------------------------------------------------------------

function minimizeXor(num1: number, num2: number): number {
    // Helper function to count the number of '1' bits in a number (since there is no-built in function like Python's bit_count())
    const bitCount = (num: number): number => {
        let count = 0;
        while (num > 0) {
            count += num & 1; // Check if the least significant bit is 1 (rightmost bit)

            // Can check the console to see how the bits are shown and counted in this function
            console.log(`Num: ${num} - Binary: ${num.toString(2)}`);

            num >>= 1; // Shift right by 1 to process the next bit
        }
        return count;
    };

    // Count the '1' bits in num1
    let num1Bits = bitCount(num1);
    console.log(`Bits in Num1: ${num1Bits}`);

    // Count the '1' bits in num2
    const num2Bits = bitCount(num2);
    console.log(`Bits in Num2: ${num2Bits}`);

    // If num1 has more '1' bits than num2, reduce the number of '1' bits in num1
    while (num1Bits > num2Bits) {
        // Turn off the rightmost '1' bit in num1
        num1 &= num1 - 1;

        // Decrease the bit count since we removed a '1' bit
        num1Bits -= 1;
        console.log(`Updated num1 Val: ${num1} - '1' Bits: ${num1Bits}`);
    }

    // If num1 has fewer '1' bits than num2, increase the number of '1' bits in num1
    while (num1Bits < num2Bits) {
        // Turn on the rightmost '0' bit in num1
        num1 |= num1 + 1;

        // Increase the bit count since we added a '1' bit
        num1Bits += 1;
        console.log(`Updated num1 Val: ${num1} - '1' Bits: ${num1Bits}`);
    }

    console.log(`Final Updated Number: ${num1}\n`);
    return num1;
}

// Example calls to demonstrate the function
minimizeXor(8, 7); // Output: 11
minimizeXor(127, 8); // Output: 64
