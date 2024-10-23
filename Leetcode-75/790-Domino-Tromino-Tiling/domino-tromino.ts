// PROBLEM #790 - DOMINO AND TROMINO TILING

// You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

//   X    &    X X
//   X         X

// Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7.

// In a tiling, every square must be covered by a tile.
// Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

// ---------------------------------------------------------------------------------------------------------------------------

function numTilings(n: number): number {
    const MOD = 10 ** 9 + 7;

    let full: { [key: number]: number } = { 0: 1, 1: 1 };
    let topMiss: { [key: number]: number } = { 0: 1, 1: 0 };
    let bottMiss: { [key: number]: number } = { 0: 1, 1: 0 };

    for (let i = 2; i <= n; i++) {
        full[i] = full[i - 1] + full[i - 2] + topMiss[i - 1] + bottMiss[i - 1];
        topMiss[i] = bottMiss[i - 1] + full[i - 2];
        bottMiss[i] = topMiss[i - 1] + full[i - 2];
    }

    return full[n] % MOD;
}

function numTilingsRework(n: number): number {
    const MOD = 10 ** 9 + 7;

    let [prevFull, full, topMiss, bottMiss] = [1, 1, 0, 0];

    for (let i = 2; i <= n; i++) {
        [prevFull, full, topMiss, bottMiss] = [
            full % MOD,
            (full + prevFull + topMiss + bottMiss) % MOD,
            (bottMiss + prevFull) % MOD,
            (topMiss + prevFull) % MOD,
        ];
        // The modulo operation is applied after each calculation within the loop, ensuring that no intermediate result grows too large
        //      --> Necessary for Leetcode to pass tests of n >= 50
    }

    return full % MOD;
}

// ---------------------------------------------------------------------------------------------------------------------------

function numTilingsRecur(n: number): number {
    const memo: { [key: string]: number } = {}; // Create an object for memoization

    function countWays(topRow: number, bottomRow: number): number {
        if (topRow > n || bottomRow > n) return 0;
        if (topRow === n && bottomRow === n) return 1;

        const key = `${topRow}, ${bottomRow}`; // TypeScript cannot store tuples as keys, so we convert it into a string

        if (memo[key] !== undefined) return memo[key];

        let ways = 0;
        const MOD = 10 ** 9 + 7;

        if (topRow === bottomRow) {
            ways =
                countWays(topRow + 2, bottomRow + 2) +
                countWays(topRow + 1, bottomRow + 1) +
                countWays(topRow + 2, bottomRow + 1) +
                countWays(topRow + 1, bottomRow + 2);
        } else if (topRow > bottomRow) {
            ways =
                countWays(topRow, bottomRow + 2) +
                countWays(topRow + 1, bottomRow + 2);
        } else {
            ways =
                countWays(topRow + 2, bottomRow) +
                countWays(topRow + 2, bottomRow + 1);
        }

        memo[key] = ways % MOD;

        // console.log(memo); // Logging statement to track the memo

        return memo[key];
    }

    return countWays(0, 0);
}

function numTilingsIter(n: number): number {
    if (n === 2) return 2;
    if (n <= 1) return 1;

    const MOD = 10 ** 9 + 7;
    const tiles = new Array(n).fill(0);

    tiles[0] = 1;
    tiles[1] = 1;
    tiles[2] = 2;

    for (let i = 3; i <= n; i++) {
        tiles[i] = 2 * tiles[i - 1] + tiles[i - 3]; // 2 times the previous combinations plus the combinations three prior
    }

    return tiles[n] % MOD;
}

function numTilingsSpace(n: number): number {
    if (n === 2) return 2; // Base Case for 2x2 Board
    if (n <= 1) return 1; // Base Case for 2x1 Board

    const MOD = 10 ** 9 + 7; // The overflow MOD specified

    let oneRowAgo = 1; // Reoresents dp[n-1] --> Ways from one row prior
    let twoRowsAgo = 1; // Represents dp[n-2] --> Ways from two rows prior
    let currentWays = 2; // Represents dp[n] --> Current number of ways

    for (let i = 3; i <= n; i++) {
        // i begins at 3 for the next row of combinations possible
        let next = (2 * currentWays + twoRowsAgo) % MOD; // We calculate the next value (for row i)
        twoRowsAgo = oneRowAgo; // Update two rows ago
        oneRowAgo = currentWays; // Update the previous row
        currentWays = next; // Update the current row to the next value
    }

    return currentWays; // Return the current value of combinations
}

console.log(numTilings(4));
console.log(numTilings(5));

console.log("Rework: ", numTilingsRework(4));
console.log("Rework: ", numTilingsRework(5));

console.log("Recur: ", numTilingsRecur(4));
console.log("Recur: ", numTilingsRecur(5));

console.log("Iter: ", numTilingsIter(4));
console.log("Iter: ", numTilingsIter(5));

console.log("Space: ", numTilingsSpace(4));
console.log("Space: ", numTilingsSpace(5));
