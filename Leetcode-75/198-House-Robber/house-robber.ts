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
