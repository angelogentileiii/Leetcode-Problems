// PROBLEM #1207 - Unique Number of Occurences

// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

// ---------------------------------------------------------------------------------------------------------------------------

function uniqueOccurrences(arr: number[]): boolean {
    let occurs: { [key: number]: number } = {}; // Establish a map (object) to track occurences of each number

    // Loop through the arr and log the occurences into the map
    for (let num of arr) {
        if (occurs[num]) {
            occurs[num] += 1; // Add an occurence
        } else {
            occurs[num] = 1; // Create a new occurence
        }
    }

    // for (let num of arr) {
    //     !occurs[num] ? (occurs[num] = 1) : (occurs[num] += 1);
    // }

    console.log(occurs);

    const values = Object.values(occurs); // Create a list of the values stored in the map (Not the numbers themselves)
    const uniqueVals = new Set(values); // Create a set (no duplicates) of those values

    return values.length === uniqueVals.size; // If the array length and the set size are identical --> No same number of occurrences
}

console.log(uniqueOccurrences([1, 2, 2, 1, 1, 3]));
console.log(uniqueOccurrences([-3, 2, 2, -3, 1, 3, 4, 1, 2]));
