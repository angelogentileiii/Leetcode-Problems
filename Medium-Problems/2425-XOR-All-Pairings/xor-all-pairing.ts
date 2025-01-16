// PROBLEM #2425 - BITWISE XOR OF ALL PAIRINGS

// You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers
// There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2
//   - every integer in nums1 is paired with every integer in nums2 exactly once

// Return the bitwise XOR of all integers in nums3

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// I'm not an expert on bitwise operations, so this was quite difficult for me
// From what I gathered, we need to use the XOR operator (^) to perform that action cumulatively on each index
// Then we can return the necessary result. Originally, I simply returned x1 ^ x2 (where each variable represents the cumulative XOR of that array)

// What I found was that when you perform an even number of XOR operations on a single number, you receive a zero value (e.g., 5 ^ 5 = 0).
// If you perform XOR an odd number of times, you receive the number itself (e.g., 5 ^ 5 ^ 5 = 5) --> This is the core to solve this problem.

//  - If the length of a list is even, its elements cancel each other out and contribute 0 to the result
//  - If the length of a list is odd, its elements contribute to the result because they appear an odd number of times
//  - We determine the parity (odd/even) of each list and include its cumulative XOR value in the result only if its length is odd

// The final result is:
//   - 0 if both list lengths are even
//   - The cumulative XOR of nums1 if nums2 has an even length
//   - The cumulative XOR of nums2 if nums1 has an even length
//   - The total XOR of nums1 and nums2 if both lists have odd lengths

// ---------------------------------------------------------------------------------------------------------------------------

function xorAllNums(nums1: number[], nums2: number[]): number {
    // Calculate the lengths of the two input arrays
    const n1 = nums1.length;
    const n2 = nums2.length;

    // Initialize the result variable to store the final XOR value
    let result = 0;

    // Check if the second array has an odd length
    if (n2 % 2 === 1) {
        // If nums2 is odd, each element in nums1 will appear an odd number of times in the resulting pairs
        // Add the XOR of all elements in nums1 to the result
        for (const num of nums1) {
            result ^= num;
        }
    }

    console.log(`Result with XOR Nums1: ${result}`);

    // Check if the first array has an odd length
    if (n1 % 2 === 1) {
        // If nums1 is odd, each element in nums2 will appear an odd number of times in the resulting pairs
        // Add the XOR of all elements in nums2 to the result
        for (const num of nums2) {
            result ^= num;
        }
    }

    console.log(`Result with XOR Nums2: ${result}`);

    // Return the final result
    console.log(`Result: ${result}`);
    return result;
}

xorAllNums([65, 111111, 42], [10, 2, 5, 0]);
