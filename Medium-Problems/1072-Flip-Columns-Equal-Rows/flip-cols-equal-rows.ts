// PROBLEM #1072 - FLIP COLUMNS FOR MAXIMUM NUMBER OF EQUAL ROWS

// You are given an m x n binary matrix matrix.

// You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

// Return the maximum number of rows that have all values equal after some number of flips.

// ---------------------------------------------------------------------------------------------------------------------------

function maxEqualRowsAfterFlips(matrix: number[][]): number {
    // Initialize an object with string keys --> The rows
    // The values will represent the number of times that string appears
    let count: { [key: string]: number } = {};

    // Iterate through each row of the matrix
    for (const row of matrix) {
        // Turn each row into a string --> For the key
        let rowKey = row.join(",");

        console.log("Row Key: ", rowKey);

        // If the first object of the row is not 0
        if (row[0] === 1) {
            // We invert the row, as it may be the opposite of a prior string
            // Inverse and same strings require the same amount of column changes to be equal
            let invRow: number[] = row.map((num) => (num === 0 ? 1 : 0));

            // Set the inverted string to the rowKey variable
            rowKey = invRow.join(",");

            console.log("Inverted: ", rowKey);
        }

        // If the rowKey is in the object, we increase the value by 1, if not, we make the value 1
        count[rowKey] = (count[rowKey] || 0) + 1;
    }

    console.log(Math.max(...Object.values(count)));

    // Return the maximum of all of the values within the object
    // Represents the number of rows we can make equal with column changes
    return Math.max(...Object.values(count));
}

maxEqualRowsAfterFlips([
    [0, 1],
    [1, 1],
]);

maxEqualRowsAfterFlips([
    [0, 1],
    [1, 0],
]);
