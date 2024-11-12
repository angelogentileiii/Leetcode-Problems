// PROBLEM #2070 - MOST BEAUTIFUL ITEM FOR EACH QUERY

// You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

// You are also given a 0-indexed integer array queries.
// For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j].
// If no such item exists, then the answer to this query is 0.

// Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to iterate through the prices and find the maximum beauty for that particular price --> Sorting would likely make this easier
// We track the prices and the maximum beauty at that price in two arrays
// We need to track the current maximum as well to use as a reference for total maximum
// Return a result array that returns the maximum beauty of that query or 0 if it does not exist

// ---------------------------------------------------------------------------------------------------------------------------

function maximumBeauty(items: number[][], queries: number[]): number[] {
    // Sort items by price --> First index of items
    items.sort((a, b) => a[0] - b[0]);
    console.log("Sorted Items: ", items);

    // Variable references for later use / maxBeauty comparison
    const prices: number[] = [];
    const maxBeautyAtPrice: number[] = [];
    let maxBeauty = 0;

    // Iterate throught the list of items
    for (const [price, beauty] of items) {
        // Find the maximum beauty at each price point
        maxBeauty = Math.max(maxBeauty, beauty);

        // We push the price and the maximum to their respective arrays --> Maintaing same index is important for later
        prices.push(price);
        maxBeautyAtPrice.push(maxBeauty);
    }

    const result: number[] = [];

    // Iterate through each query to compare against our beautifies to find the maximum beauty
    for (let query of queries) {
        // Find the index by using our helper function to find the right most index --> Subtract one to ensure it is less than or equal to the query
        const index = binarySearchRight(prices, query) - 1;

        // Conditional to push into the result array
        if (index >= 0) {
            result.push(maxBeautyAtPrice[index]); // This is why it is important to maintain the matching index above
        } else {
            result.push(0);
        }
    }

    return result;
}

function binarySearchRight(arr: number[], target: number): number {
    let left = 0;
    let right = arr.length;

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        console.log("Mid", mid);

        if (arr[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

const items1 = [
    [1, 2],
    [3, 2],
    [2, 4],
    [5, 6],
    [3, 5],
];
const queries1 = [1, 2, 3, 4, 5, 6];

console.log(maximumBeauty(items1, queries1));
