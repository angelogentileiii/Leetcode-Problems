// PROBLEM #3254 - FIND THE POWER OF K SUBARRAYS 1

// You are given an array of integers nums of length n and a positive integer k.

// The power of an array is defined as:

// Its maximum element if all of its elements are consecutive and sorted in ascending order.
// -1 otherwise.

// You need to find the power of all subarrays of nums of size k.

// Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

// ---------------------------------------------------------------------------------------------------------------------------

function resultsArray(nums: number[], k: number): number[] {
    // If K is only 1, we know that every element is the max of its own subarray
    if (k === 1) return nums;

    // Initialize our two pointers
    let left = 0;
    let right = 1;

    // Initialize our result array
    let result: number[] = [];

    // While our second pointer remains in bounds
    while (right < nums.length) {
        // Check if the last two numbers are consecutive --> In accordance with our problem's condition
        const not_consecutive: boolean = nums[right] - nums[right - 1] !== 1;

        // If block based on consecutive
        if (not_consecutive) {
            // While the first pointer is valid within our nums array and has not crossed our second pointer
            while (left < right && left + k - 1 < nums.length) {
                // We can push -1 to our result array
                result.push(-1);
                // Move our first pointer to the beginning of the next subarray
                left += 1;
            }
            // If it is consecutive and we have found the last number of the subarray of k length
        } else if (right - left == k - 1) {
            // We push the rightmost number into the result array --> It is the maximum due to the consecutive nature
            result.push(nums[right]);
            // Again, move our first pointer to the next subarray
            left += 1;
        }

        // Increase the second pointer after each check to move through the array properly
        right += 1;
    }

    // Return our result which will be len(nums) - k + 1 in length due to checking the subarrays on each iteration
    return result;
}
