// Problem #283 --> MOVE ZEROES

// Given an integer array of "nums", move all 0's to the end of the array,
// while MAINTAINING relative order of the non-zero elements

// Sorting must be done in place without making a copy of the array

// FIRST THOUGHTS:
// Merge Sort --> Inplace sorting to move zeroes to the end (O(n log n) Time)
// ---> Too much calculation that is not needed

// Two Pointer --> Linear solution (O(n) Time)
// ---> Faster time complexity and in place

// Example: Input [0, 1, 0, 3, 12] becomes [1, 3, 12, 0, 0]

function moveZeroes(nums: number[]): void {
    let insertIndex = 0; // Tracks the position of where the next non-zero element gets placed

    for (let i = 0; i < nums.length; i++) {
        const val = nums[i]; // Store the current value for the iteration
        console.log("Value stored:", val);
        console.log("Current iteration index:", i);
        console.log("Current index to insert:", insertIndex);
        nums[i] = 0; // Set that index to zero
        if (val !== 0) {
            // If the value stored is not zero, do this condition
            nums[insertIndex] = val; // Place the value in the insertIndex position
            insertIndex++; // Increment the insertIndex to the next position
            console.log("Nums after change:", nums);
        } else {
            console.log("No change made:", nums);
        }
        console.log(" ");
    }
}

const moveZeroesTS = [0, 1, 0, 3, 12];

moveZeroes(moveZeroesTS);

console.log("solution", moveZeroesTS);
