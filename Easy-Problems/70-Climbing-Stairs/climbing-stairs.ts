// Problem #70 - CLIMBING STAIRS --> PLUS ADDITIONAL PROBLEM

// There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
// Given N, write a function that returns the number of unique ways you can climb the staircase.
// The order of the steps matters.

// For example, if N is 4, then there are 5 unique ways:

// 1, 1, 1, 1
// 2, 1, 1
// 1, 2, 1
// 1, 1, 2
// 2, 2

// ADD-ON PROBLEM
// What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
// For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

//---------------------------------------------------------------------------------------------------------------------------

function climbStairs(n: number): number {
    if (n === 0 || n === 1) {
        return 1;
    }

    let memo = new Array(n + 1).fill(1);

    for (let i = 2; i <= n; i++) {
        memo[i] = memo[i - 1] + memo[i - 2];
    }

    return memo[n];
}

function climbStairsX(n: number, X: number[]): number {
    if (n === 0) return 1;

    let memo = new Array(n + 1).fill(1);

    for (let i = 2; i <= n; i++) {
        for (const step of X) {
            if (i - step >= 0) {
                memo[i] += memo[i - step];
            }
        }
    }

    return memo[n];
}

//---------------------------------------------------------------------------------------------------------------------------

// MEMOIZATION WITH RECURSION
// Not optimal as it requires more space and stack mamangement --> But possible

function climbStairsMemo(n: number): number {
    let memo: Record<number, number> = {};

    // Record<number, number> --> a utility type that defines an object type with specific properties
    // // Record<K, T> --> a built-in TypeScript utility type that creates an object type where:
    // // // K is the type of the keys.
    // // // T is the type of the values.

    function climb(n: number) {
        if (n === 0 || n === 1) return 1;

        if (!memo[n]) {
            memo[n] = climb(n - 1) + climb(n - 2);
        }

        return memo[n];
    }

    return climb(n);
}

console.log("Base Prob", climbStairs(50));
console.log("Add Prob", climbStairsX(50, [1, 3, 5]));

console.log("Memo + Recur", climbStairsMemo(50));
