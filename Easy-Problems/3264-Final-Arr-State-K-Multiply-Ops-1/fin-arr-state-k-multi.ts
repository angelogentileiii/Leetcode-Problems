// Problem #3264 --> FINAL ARRAY STATE AFTER K MULTIPLICATION OPERATIONS 1

// You are given an integer array nums, an integer k, and an integer multiplier.

// You need to perform k operations on nums. In each operation:

// Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
// Replace the selected minimum value x with x * multiplier.
// Return an integer array denoting the final state of nums after performing all k operations.

// ---------------------------------------------------------------------------------------------------------------------------

function getFinalState(
    nums: number[],
    k: number,
    multiplier: number
): number[] {
    // Initial loop to perform the operation K times
    for (let i = 0; i < k; i++) {
        // Find the index of the smallest number in the array
        let idx = nums.indexOf(Math.min(...nums));

        console.log(`Index of Smallest Number: ${idx}`);

        // Replace the value in the array with the multiplied value
        nums[idx] = nums[idx] * multiplier;

        console.log(`After Multiplication: ${nums}`);
    }

    return nums;
}

getFinalState([2, 1, 3, 5, 6], 5, 2);
getFinalState([1, 2], 3, 4);
