// PROBLEM #2300 - SUCCESSFUL PAIRS OF POTIONS AND SPELLS

// You are given two positive integer arrays spells and potions, of length n and m respectively,
// where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

// You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

// Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

// ---------------------------------------------------------------------------------------------------------------------------

function successfulPairs(
    spells: number[],
    potions: number[],
    success: number
): number[] {
    potions.sort((a, b) => a - b); // First sort the potions to ensure binary search will work

    const totalPotions = potions.length;
    const result: number[] = [];

    // For each spell, we use the binary search to find the successful potions
    for (const spell of spells) {
        let left = 0;
        let right = totalPotions - 1;

        while (left <= right) {
            // Find the midpoint on each search
            const mid = Math.floor((left + right) / 2);

            // If the potion is successful, we move our right bound lower and check again
            if (spell * potions[mid] >= success) {
                right = mid - 1;
            } else {
                // If unsuccessful, we move our left bound higher and check again
                left = mid + 1;
            }
        }
        // Add the number of potions that are successful (left represents the lowest index of success)
        //      Pushing the totalPotions - left means all of the potions that are successful
        //      If left exceeds our right, we break the loop and have totalPotions - the same value --> zero viable potions
        result.push(totalPotions - left);
    }

    return result;
}

console.log(successfulPairs([5, 1, 3], [1, 3, 2, 4, 5], 25));
console.log(successfulPairs([1, 5, 6, 7, 5, 2], [1, 2, 5], 10));
