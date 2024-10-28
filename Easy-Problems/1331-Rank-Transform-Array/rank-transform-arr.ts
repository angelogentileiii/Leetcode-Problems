// PROBLEM #1331 - RANK TRANSFORM OF AN ARRAY

// Given an array of integers arr, replace each element with its rank.

// The rank represents how large the element is. The rank has the following rules:

// Rank is an integer starting from 1.
// The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
// Rank should be as small as possible.

// ---------------------------------------------------------------------------------------------------------------------------

function arrayRankTransform(arr: number[]): number[] {
    // Create a temporary set that holds the unique values of the original array in sorted form
    let temp: Set<number> = new Set([...arr].sort((a, b) => a - b));

    console.log(temp);
    console.log(arr);

    // Create an empty dictionary and a rank value to begin --> Use both to store values for later mapping
    let dict: { [key: string]: number } = {};
    let rank = 1;

    // Loop through each value in the set to assign the ranking value
    temp.forEach((value) => {
        // { number: rank }
        dict[value] = rank;
        rank++;
    });

    console.log(dict);

    // Map the original array to the values of the corresponding ranking
    return arr.map((num) => dict[num]);
}

// ---------------------------------------------------------------------------------------------------------------------------

const vals1 = [40, 10, 20, 30, 40];

console.log(arrayRankTransform(vals1));
