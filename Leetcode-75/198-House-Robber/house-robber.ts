// PROBLEM #198 - HOUSE ROBBER

// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed.
// The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
// and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house,
// return the maximum amount of money you can rob tonight without alerting the police.

// ---------------------------------------------------------------------------------------------------------------------------

// If you rob first house, you cannot rob second house
// If you skip first house, you can rob second house

// [0, 1, 2, 3]
//     Rob 0 -> Skip -> Rob either 2 or 3
//     Skip -> Rob 1 -> Skip
// The maximum at each index is the max between that index - 1 and that index - 2
//     Max at index 0 is 0
//     Max at index 1 is 1
//     Max at index 2 is 2 because 2 is > 1
//     Max at index 3 is 4 because index 1 + index 3 > max at index 2

function rob(nums: number[]): number {
    let [house1, house2] = [0, 0];

    for (let i = 0; i < nums.length; i++) {
        const rob1 = house1 + nums[i];
        const rob2 = house2;

        const currMax = Math.max(rob1, rob2);
        house1 = house2;
        house2 = currMax;
    }

    return house2;
}

const houses1 = [1, 2, 3, 1];
const houses2 = [2, 7, 9, 3, 1, 2, 7, 9, 3, 1];

console.log("Maximum Available:", rob(houses1)); // Expect 4
console.log("Maximum Available:", rob(houses2)); // Expect 23
