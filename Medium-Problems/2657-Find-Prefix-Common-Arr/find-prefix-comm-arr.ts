// PROBLEM #2657 - FIND THE PREFIX COMMON ARRAY OF TWO ARRAYS

// You are given two 0-indexed integer permutations A and B of length n.

// A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

// Return the prefix common array of A and B.

// A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to iterate through each array (A & B) and count the integers seen up until that point
// We can use an Array where the indexes represent each number in the array since the constraint shows --> 1 <= A[i], B[i] <= n
//   - No index value can be larger than n itself
// If we encounter two numbers at any iteration through the arrays --> We have found common numbers between the two

// ---------------------------------------------------------------------------------------------------------------------------

function findThePrefixCommonArray(A: number[], B: number[]): number[] {
    // Whether we use A or B here is irrelevant since both arrays are the same size
    const n: number = A.length;

    // A variable that we will use to store the value of total common numbers at each index
    let commonNums: number = 0;

    // Initialize an array to store our total common numbers at each index --> Should be equal to the length of n
    const result: number[] = new Array(n).fill(0);

    // Initialize an array to store our counts for each number at each index --> Make it n + 1 because any index can be <= n
    const numCount: number[] = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        // We update the value of the index at the A value
        numCount[A[i]] += 1;

        // Check if that value now becomes 2 --> We've encountered this number prior
        if (numCount[A[i]] === 2) {
            // If so, we have a common number and tally our counter once
            commonNums += 1;
        }

        // We update the value of the index at the B value
        numCount[B[i]] += 1;

        // If that value becomes two (no higher) --> We have found another common number for the first time
        if (numCount[B[i]] === 2) {
            // Again, update the common counter
            commonNums += 1;
        }

        // After both conditions, we can update the result array of the current index with the total number of common integers we have passed to this point
        result[i] = commonNums;
        console.log(`Result After Iteration: ${result}`);
    }

    console.log(`Result: ${result}`);
    return result;
}

// SOLUTION UTILIZING A DICTIONARY INSTEAD OF A LIST

// Essentially the same solution but utilizing a dictionary can account for integers outside the range of n or for a diverse set of integers within our range
function findThePrefixCommonArrayDict(A: number[], B: number[]): number[] {
    const n: number = A.length;
    let commonNums: number = 0;
    const result: number[] = new Array(n).fill(0);

    // Use a dictionary (object) for counting instead of the list
    const numCount: Record<number, number> = {};

    for (let i = 0; i < n; i++) {
        // Increment count for A[i]
        numCount[A[i]] = (numCount[A[i]] || 0) + 1;

        if (numCount[A[i]] === 2) {
            commonNums += 1;
        }

        // Increment count for B[i]
        numCount[B[i]] = (numCount[B[i]] || 0) + 1;

        if (numCount[B[i]] === 2) {
            commonNums += 1;
        }

        result[i] = commonNums;
        console.log(`Result After Iteration: ${result}`);
    }

    console.log(`Result: ${result}`);
    return result;
}

findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]);

findThePrefixCommonArrayDict([1, 3, 2, 4], [3, 1, 2, 4]);
