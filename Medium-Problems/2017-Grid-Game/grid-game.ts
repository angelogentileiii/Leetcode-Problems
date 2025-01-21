// PROBLEM #2017 - GRID GAME

// You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix
// Two robots are playing a game on this matrix.

// Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

// At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path.
// For all cells (r, c) traversed on the path, grid[r][c] is set to 0.
// Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

// The first robot wants to minimize the number of points collected by the second robot.
// In contrast, the second robot wants to maximize the number of points it collects.

// If both robots play optimally, return the number of points collected by the second robot.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to determine the total values at each index, we can use two prefix sum arrays --> One for each row in grid
// Then we need to calculate the total amount of points on the top row or bottom row up to a particular column
//   - The column represents the point of the grid which the first robot moves downward to exit via the [1][n-1] space (bottom right corner)
// We can do this iteratively by calculating the values at each index of our grid (column positions)
//   - We should use a variable to capture the minimum value at each index
//   - The second robot is looking for the maximum available so that is what should be used to determine the minimum --> The maximum of what remains
//       - The lowest of all of the maximums would then be the second robot's score

// Use prefix sum arrays for each row to calculate cumulative sums:
//   - top_prefix[i] gives the sum of the top row up to index i
//   - bot_prefix[i] gives the sum of the bottom row up to index i
//       - EX: top_prefix[0] would be 0 since we have not included any cells --> top_pref[1] is the total of the first column in the grid (column index of 0)
// Iterate through each column to determine where the first robot drops down:
//   - Calculate the points the second robot can collect in the worst case (maximum remaining points)
// Keep track of the minimum of these worst-case scenarios across all columns

// ---------------------------------------------------------------------------------------------------------------------------

function gridGame(grid: number[][]): number {
    const n = grid[0].length;

    // Two prefix arrays for our total values at each space of the grid
    //   - We initiliaze as (n + 1) in order to have the proper length to account for 1-indexing each value
    //       - This ensures that each index of our prefix arrays returns the sum of all of the values up to that current index
    //           - At the final index (n + 1) --> It is the total value of all indexes within the array
    const topPrefix = new Array(n + 1).fill(0);
    const botPrefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        // We fill out prefix arrays by taking the prior value and adding the current value of the associated grid row and column
        topPrefix[i + 1] = topPrefix[i] + grid[0][i];
        botPrefix[i + 1] = botPrefix[i] + grid[1][i];
    }

    console.log(`Top Prefix:`, topPrefix);
    console.log(`Bottom Prefix:`, botPrefix);
    console.log(" ");

    // We initialize our min_points variable (our result will be stored here) as positive infinity
    //   - This ensures that we will update this variable correctly --> Even on the first comparison
    let minPoints = Infinity;

    for (let j = 0; j < n; j++) {
        // Points remaining on top row after the robot crosses the current column (col)
        //   - The last indexes value minus the value after the current column (can use -1 or n for the last index)
        const pointsTop = topPrefix[n] - topPrefix[j + 1];

        // Points already collected on the bottom row up to the current column (col)
        //   - Since we beging in cell (0, 0), we can simply take the appropriate column value from the bot_pref array
        const pointsBot = botPrefix[j];

        console.log(`Points Top:`, pointsTop);
        console.log(`Points Bottom:`, pointsBot);

        // Worst-case points for the second robot at this column --> The most points available at this particular column
        const secondRobotPoints = Math.max(pointsTop, pointsBot);

        console.log(
            `Current Max:`,
            secondRobotPoints,
            `- Prior Minimum:`,
            minPoints
        );

        // Update the minimum points if this is the smallest worst-case scenario --> If the most points at this column is less than the prior min_points
        minPoints = Math.min(minPoints, secondRobotPoints);

        console.log(`Current Minimum Points:`, minPoints);
        console.log(" ");
    }

    console.log(`-- Final Points for Second Robot:`, minPoints, `--\n`);
    return minPoints;
}

gridGame([
    [3, 3, 1],
    [8, 5, 2],
]); // Expected Result: 4
gridGame([
    [1, 3, 1, 15],
    [1, 3, 3, 1],
]); // Expected Result: 7
