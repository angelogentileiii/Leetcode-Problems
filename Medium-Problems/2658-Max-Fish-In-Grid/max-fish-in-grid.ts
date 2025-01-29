// PROBLEM #2658 - MAXIMUM NUMBER OF FISH IN A GRID

// You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
//   - A land cell if grid[r][c] = 0
//   - A water cell containing grid[r][c] fish, if grid[r][c] > 0

// A fisher can start at any water cell (r, c) and can do the following operations any number of times:
//   - Catch all the fish at cell (r, c)
//   - Move to any adjacent water cell

// Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

// An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// ---------------------------------------------------------------------------------------------------------------------------

function findMaxFish(grid: number[][]): number {
    console.log("Initial Grid:");
    grid.forEach((row) => console.log(row));

    const rows = grid.length;
    const cols = grid[0].length;

    // Initialize the visited array
    const visited: boolean[][] = Array.from({ length: rows }, () =>
        Array(cols).fill(false)
    );

    console.log("\nInitial Visited Array:");
    visited.forEach((row) => console.log(row));

    let maxFish = 0;

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (grid[row][col] > 0 && !visited[row][col]) {
                const totalFish = calcFish(grid, visited, row, col);

                console.log(`\nTotal Fish for Choice: -- ${totalFish} --`);

                maxFish = Math.max(maxFish, totalFish);
            }
        }
    }

    console.log("\nCompleted Visited Array:");
    visited.forEach((row) => console.log(row));

    console.log(`\n-- Result: ${maxFish} --\n`);

    return maxFish;
}

function calcFish(
    grid: number[][],
    visited: boolean[][],
    row: number,
    col: number
): number {
    if (
        row < 0 ||
        row >= grid.length ||
        col < 0 ||
        col >= grid[0].length ||
        grid[row][col] === 0 ||
        visited[row][col]
    ) {
        return 0;
    }

    visited[row][col] = true;

    let totalFish = grid[row][col];

    console.log(
        `\nIteration Visited Array: (${row}, ${col}) - Fish: ${totalFish}`
    );
    visited.forEach((row) => console.log(row));

    const directions = [
        [0, 1], // Right
        [0, -1], // Left
        [1, 0], // Down
        [-1, 0], // Up
    ];

    for (const [dr, dc] of directions) {
        totalFish += calcFish(grid, visited, row + dr, col + dc);
    }

    return totalFish;
}

// Test cases
findMaxFish([
    [0, 2, 1, 0],
    [4, 0, 0, 3],
    [1, 0, 0, 4],
    [0, 3, 2, 0],
]);
findMaxFish([
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
]);
findMaxFish([
    [5, 6, 7, 0],
    [0, 0, 0, 4],
    [2, 0, 0, 3],
    [2, 4, 5, 8],
]);
