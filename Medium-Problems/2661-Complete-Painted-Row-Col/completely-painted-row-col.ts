// PROBLEM #2661 - FIRST COMPLETELY PAINTED ROW OR COLUMN

// You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

// Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

// Return the smallest index i at which either a row or a column will be completely painted in mat.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// The goal is to find which row or column will be visited fully first
// We can to create a dictionary to store each values precise position in the matrix
//   - Could also use a nested loop --> One for Rows and one for Cols
// We need to store the total number of rows and columns in the matrix --> Can use two frequency arrays for this
// As we move through our arr --> We mark each cell that has been visited in row/column
//   - If the cell reaches 0, we have visited it the maximum amount of times (dictionary)
//   - If the cell reaches the total number of rows or columns, we've also visited the maximum (nested for loops)

// ---------------------------------------------------------------------------------------------------------------------------

function firstCompleteIndex(arr: number[], mat: number[][]): number {
    // Output the original matrix to the console for debugging purposes
    console.log(`Original Matrix: ${mat}`);

    // Store the number of rows and columns in the matrix
    const rows = mat.length;
    const cols = mat[0].length;

    // Initialize two arrays to keep track of unpainted cells:
    // - row_count: number of unpainted cells in each row (start with all columns unpainted)
    // - col_count: number of unpainted cells in each column (start with all rows unpainted)
    const row_count = new Array(rows).fill(cols); // Each row starts with `cols` unpainted cells
    const col_count = new Array(cols).fill(rows); // Each column starts with `rows` unpainted cells

    // Output the initial state of row_count and col_count for debugging
    console.log(`Row Count: ${row_count} - Col Count: ${col_count}`);

    // Create a dictionary (hash map) to store the position of each number in the matrix
    // The key will be the number from the matrix and the value will be an array [row, col]
    const position: { [key: number]: [number, number] } = {};

    // Fill the position dictionary with the coordinates of each number in the matrix
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            position[mat[r][c]] = [r, c]; // Store the (row, col) pair for the number at mat[r][c]
        }
    }

    // Output the position dictionary to the console for debugging
    console.log(`Position Dict: ${JSON.stringify(position)}`);

    // Iterate over each element in the `arr` array, checking its "painted" status
    for (let i = 0; i < arr.length; i++) {
        const val = arr[i]; // Current value in the array

        // Output the current index and value to the console for debugging
        console.log(`Curr Idx: ${i} - Curr Val: ${val}`);

        // Look up the position of the current value in the matrix using the position dictionary
        const [r, c] = position[val];

        // "Paint" the current cell by decreasing the count of unpainted cells in the respective row and column
        row_count[r] -= 1;
        col_count[c] -= 1;

        // Check if either the row or column is completely painted (no unpainted cells left)
        if (row_count[r] === 0 || col_count[c] === 0) {
            console.log(`First Painted Idx: ${i}\n`);
            return i; // Return the index where a full row or column was painted
        }
    }

    // Edge case consideration
    // If no row or column is fully painted, return -1 (indicating no such index exists)
    return -1;
}

firstCompleteIndex(
    [1, 3, 4, 2],
    [
        [1, 4],
        [2, 3],
    ]
); // Expected Index: 2

firstCompleteIndex(
    [2, 4, 1, 3, 5, 6],
    [
        [6, 2],
        [1, 3],
        [5, 4],
    ]
); // Expected Index: 3
