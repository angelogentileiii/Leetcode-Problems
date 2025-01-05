// PROBLEM #2270 - NUMBER OF WAYS TO SPLIT AN ARRAY

// You are given a 0-indexed integer array nums of length n.

// nums contains a valid split at index i if the following are true:

// The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
// There is at least one element to the right of i. That is, 0 <= i < n - 1.
// Return the number of valid splits in nums.

// ---------------------------------------------------------------------------------------------------------------------------

function waysToSplitArray(nums: number[]): number {
    // Find the total sum of the array --> Will be used to later calculate our right value at each split
    const totalSum = nums.reduce((acc, curr) => {
        return acc + curr;
    }, 0);

    console.log(`Total Sum: ${totalSum}`);

    // Two variables for the sum of our left side split and for our total valid count of splits
    let leftSum = 0;
    let count = 0;

    // Loop through the values of nums --> Exclude the final index since that is not a valid split
    for (let i = 0; i < nums.length - 1; i++) {
        // Increase the left sum by the next included value of nums
        leftSum += nums[i];

        // Calculate the new remaining sum after updating the leftSum
        const rightSum = totalSum - leftSum;

        console.log(`Left Sum: ${leftSum} - Right Sum: ${rightSum}`);

        // Our conditional statement to determine if the split is valid
        if (leftSum >= rightSum) {
            count += 1;
        }
    }

    console.log(`Total Valid Splits: ${count}`);
    return count;
}

waysToSplitArray([10, 4, -8, 7]);
