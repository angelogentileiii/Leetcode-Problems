// PROBLEM #238 - PRODUCT OF ARRAY EXCEPT SELF

// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

// ---------------------------------------------------------------------------------------------------------------------------

// INITIAL THOUGHTS

// Brute force can use a nested loop --> Iterate over the nums and at each index, we only multiply 1 by every index value except itself
// This solution fails the constraints as it exceeds the time limit available

// We need a solution where in one pass of the array we can multiply from left to right and then from right to left
// Basically like a prefix sum and suffix sum for each index --> [1, 2, 3, 4] --> Prefix = 1 (base) Suffix = 24. Prefix * Suffix = 24 and so on

// ---------------------------------------------------------------------------------------------------------------------------

// BRUTE FORCE SOLUTION
// Nested for loops exceed the time limit and are not efficient to solve the problem

function productExceptSelfBrute(nums: number[]): number[] {
    const n = nums.length;
    let result: number[] = new Array(n).fill(1);

    // Our nested loops to move through the array and multiply every index except for i --> INEFFICIENT
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (j === i) continue;
            result[i] *= nums[j];
        }
    }

    console.log(`Result `, result);
    return result;
}

// productExceptSelf([1, 2, 3, 4]);
// productExceptSelf([-1, 1, 0, -3, 3]);

// ---------------------------------------------------------------------------------------------------------------------------

function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    let result: number[] = new Array(n).fill(1);

    // Our prefix calculation as we move through the array --> We multiply each index by the product of the numbers prior
    // Initially is 1 because we have not put any numbers to our left side of our index
    let prefix = 1;
    for (let i = 0; i < n; i++) {
        result[i] *= prefix;

        // Update the prefix by multiplying it by the current number --> Will be used in the next iteration since we have passed this number
        prefix *= nums[i];
        console.log("Result in 1st Loop: ", result);
    }

    // Multiply the index at the end of our array (right side) by our suffix value --> Same premise as prefix but the opposite end
    let suffix = 1;
    for (let i = n - 1; i >= 0; i--) {
        result[i] *= suffix;

        // Update the suffix by multiplying it by the current number in the same index of the nums array --> Again, used for next iteration
        suffix *= nums[-1 - i];
        suffix *= nums[i];
        console.log("Result in 2nd Loop: ", result);
    }

    console.log(`Result: `, result);
    return result;
}

productExceptSelf([1, 2, 3, 4]);
productExceptSelf([-1, 1, 0, -3, 3]);
