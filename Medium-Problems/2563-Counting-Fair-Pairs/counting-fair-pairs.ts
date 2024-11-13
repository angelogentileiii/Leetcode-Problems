// PROBLEM #2563 - COUNTING THE NUMBER OF FAIR PAIRS

// Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

// A pair (i, j) is fair if:

// 0 <= i < j < n, and
// lower <= nums[i] + nums[j] <= upper

// ---------------------------------------------------------------------------------------------------------------------------

function countFairPairs(nums: number[], lower: number, upper: number): any {
    // Sort the array to be able to binary search for the correct bounds --> Upper and Lower of pair
    nums.sort((a, b) => a - b);

    // Binary search helper function
    function binarySearch(left: number, right: number, target: number): any {
        while (left < right) {
            let mid = left + Math.floor((right - left) / 2); // Find the midpoint of the array

            console.log(
                `Left: ${left}, Right: ${right}, Mid: ${mid}, Current Num: ${nums[mid]}`
            );

            // Find the corresponding bound --> Representing by the right variable
            if (nums[mid] >= target) {
                // Shift the right bound to one less than prev mid
                right = mid - 1;
            } else {
                // Shift the left bound to one more than prev mid
                left = mid + 1;
            }
        }

        // This will correlate to the proper boundary that fits the paid --> Whether upper or lower based on arguments
        console.log(right);
        return right;
    }

    // Count variable for total number of pairs --> Return for function
    let count = 0;

    // Iterate through the nums array
    for (let i = 0; i < nums.length; i++) {
        // the upper bound and lower bound when paired with each item from nums
        let up = upper - nums[i]; // The largest number we can add to nums[i] to facilitate our upper bound (Example: 6)
        let low = lower - nums[i]; // The smallest number we can add to nums[i] to facilitate our lower bound (Example: 3)

        console.log(`${i + 1} Iteration`);

        // We update the count with each iteration to be the number of combinations between the upper bound and lower bound
        // This is why we subtract up from low --> Gives us all combinations from low to up available in nums per nums[i]
        count +=
            binarySearch(i + 1, nums.length - 1, up + 1) - // We use up + 1 to ensure that the target is <= our upper bound
            binarySearch(i + 1, nums.length - 1, low); // We only use low because our target will be >= our lower bound
    }

    // return the total pairs available after iterating throught the entire array
    console.log(count);
    return count;
}

countFairPairs([0, 1, 7, 4, 4, 5], 3, 6);
