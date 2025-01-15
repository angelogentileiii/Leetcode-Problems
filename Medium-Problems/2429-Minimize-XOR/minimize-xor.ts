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
    const num1Bits = num1.countBits(); // NEED FUNCTION FOR COUNTING BITS

    console.log(`Num1 '1' Bits: ${num1Bits}`);

    const num2Bits = num2.countBits(); // NEED FUNCTION FOR COUNTING BITS

    console.log(`Num2 '1' Bits: ${num2Bits}`);

    // Comparison logic of the '1' bits from both of our numbers
    while (num1Bits < num2Bits) {}

    while (num1Bits > num2Bits) {}

    console.log(`Final Updated NUmber: ${num1}\n`);
    return num1;
}
