// PROBLEM #62 - UNIQUE PATHS

// There is a robot on an m x n grid.
// The robot is initially located at the top-left corner (i.e., grid[0][0]).
// The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
// The robot can only move either down or right at any point in time.

// Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

// The test cases are generated so that the answer will be less than or equal to 2 * 109.

// ---------------------------------------------------------------------------------------------------------------------------

// Helper function to calculate the factorial --> 5! means 5 * 4 * 3 * 2 * 1 which equals = 120
function factorial(x: number): number {
    let result = 1;

    for (let i = 2; i <= x; i++) {
        result *= i;
    }

    return result;
}

function uniquePaths(m: number, n: number): number {
    const totalMoves = m + n - 2; // The total number of moves you make is m + n - 2 (because you move right n-1 times and down m-1 times)
    const downMoves = m - 1; // Total down moves possible
    const rightMoves = n - 1; // Total right moves possible

    return (
        factorial(totalMoves) /
        (factorial(downMoves) * factorial(totalMoves - downMoves)) // The same as factorial(rightMoves) but keeps logic cleaner and focused on just downMoves
    );
}

// ---------------------------------------------------------------------------------------------------------------------------

// DYNAMIC PROGRAMMING SOLUTION

function uniquePathsDP(m: number, n: number): number {
    // const dp: number[][] = new Array(m)
    //     .fill(null)
    //     .map(() => new Array(n).fill(0));

    const dp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    // console.log(dp);

    // The first row each space can only be reached by one possible move --> Move right
    for (let i = 0; i < m; i++) {
        dp[i][0] = 1;
    }

    // console.log(dp);

    // The first column each space can only be reached by one possible move --> Move down
    for (let j = 0; j < n; j++) {
        dp[0][j] = 1;
    }

    // console.log(dp);

    // Fill the rest of the table by using a recursive relation to the other spaces --> Pascal's triangle style
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // The sum of the cells to the top and the left --> The total combinations to move down and right
        }
    }

    // Log final dp matrix
    console.log("Final dp matrix:");
    logMatrix(dp);

    return dp[m - 1][n - 1]; // Returns the bottom right most combination in our table
}

// ---------------------------------------------------------------------------------------------------------------------------

// Helper function to log the dp matrix in a readable format
function logMatrix(matrix: number[][]): void {
    matrix.forEach((row) => {
        console.log(row.join(" ")); // Join each row's elements into a string separated by spaces
    });
}

// ---------------------------------------------------------------------------------------------------------------------------

console.log("Factorial: ", uniquePaths(3, 7));
console.log("Dynamic Program: ", uniquePathsDP(3, 7));
