// PROBLEM #2064 - MINIMIZED MAXIMUM PRODUCTS DISTRIBUTED TO ANY STORE

// You are given an integer n indicating there are n specialty retail stores.
// There are m product types of varying amounts, which are given as a 0-indexed integer array quantities,
// where quantities[i] represents the number of products of the ith product type.

// You need to distribute all products to the retail stores following these rules:

// A store can only be given at most one product type but can be given any amount of it.
// After distribution, each store will have been given some number of products (possibly 0).
// Let x represent the maximum number of products given to any store.
// You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

// Return the minimum possible x.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// Initially thought we could do something as simple as sum the quantities and divide by stores to determine the maximum given to any store.
// Does not take into account only distributing one item per store

// We can use BINARY SEARCH to determine the maximum available to distribute to each store
// If we divide each quantity by a number in our array, we can find the smallest number that allows all products to be distributed

// ---------------------------------------------------------------------------------------------------------------------------

function minimizedMaximum(n: number, quantities: number[]): number {
    // Helper function
    function canDistribute(quant: number): boolean {
        // Always initialize stores that have been used as 0 to begin
        let stores = 0;

        // Iterate through each quantity of each item
        for (let q of quantities) {
            // The maximum stores that can be given the current quantity of the particular item
            // We divide the current quantity (ex: 11) by our midpoint to split it by (ex: 6) this would give us two stores
            stores += Math.ceil(q / quant);
            console.log("Stores: ", stores);
        }

        // If the stores, after checking all product quanities is less than or equal to n (Total Stores)
        // then we can successfully distribute the products split this way
        return stores <= n;
    }

    let left = 1; // Represents the left most bound of the quantity we would distribute to a store
    let right = Math.max(...quantities); // The rightmost bound of the quantity distributed
    let result = 0; // Will store the minimum viable quantity to distribute

    while (left <= right) {
        // Find the midpoint of possible quantities to distribute
        const mid = left + Math.floor((right - left) / 2);
        console.log("Midpoint: ", mid);

        // If we have enough stores to distribute all items in this quantity --> Returns true
        if (canDistribute(mid)) {
            result = mid; // Temporarily update result to this quantity
            right = mid - 1; // Move the right pointer down to check again
        } else {
            left = mid + 1; // If we don't, we need to up the quantity per store --> Move left pointer up in quantity
        }
    }

    console.log("Total Max Distributed: ", result);
    return result;
}

minimizedMaximum(6, [11, 6]);
