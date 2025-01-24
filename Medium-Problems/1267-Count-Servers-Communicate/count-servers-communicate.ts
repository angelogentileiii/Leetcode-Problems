// PROBLEM #1267 - COUNT SERVERS THAT COMMUNICATE

// You are given a map of a server center, represented as an m * n integer matrix grid
//   - Where 1 means that on that cell there is a server and 0 means that it is no server

// Two servers are said to communicate if they are on the same row or on the same column

// Return the number of servers that communicate with any other server

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// We need to count the occurrences of servers in each row and column
//   - If there are more than one in either a row or column --> We have connected servers

// We should only update the result based on the individual number of connected computers --> Ensure we do not double count connected computers

// Then we can check if there are more than one computer in a column or row to update our result

//  We can use two simultaneous arrays to track the number of computers in each row/column (corresponding to the 0-index of the array)
//   - Then we can loop through the grid and compare the computer locations to the total in the row or column
//       - If we have a computer and the row or column total is more than 1, we have computers that can communicate and can add to our result

// ---------------------------------------------------------------------------------------------------------------------------

function countServers(grid: number[][]): number {
    console.log("Computer Grid:");
    grid.forEach((row) => console.log(row));
    console.log();

    const rows = grid.length;
    const cols = grid[0].length;

    // Initialize two arrays, one to track the total number of comps per row and one to track total number of comps per column
    //   - Each index represents the corresponding 0-indexed item --> First Row is index 0 and First Column is index 0
    const rowComps: number[] = new Array(rows).fill(0);
    const colComps: number[] = new Array(cols).fill(0);

    // Count the number of servers in each row and column
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            // If there is a computer present in the grid
            if (grid[row][col] === 1) {
                // Update our row and column arrays accordingly
                rowComps[row]++;
                colComps[col]++;
            }
            console.log(
                `Within Loop Row Array: ${rowComps} - Within Loop Col Array: ${colComps}`
            );
        }
    }

    console.log(
        `\nTotal Comps in Rows: ${rowComps} - Total Comps in Columns: ${colComps}\n`
    );

    let result = 0;

    // Check for communicating computers
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            // For each computer that is part of a row or column with more than one computer, increase the result
            if (grid[r][c] === 1 && (rowComps[r] > 1 || colComps[c] > 1)) {
                console.log(`Communicating Comp Found at Row: ${r}, Col: ${c}`);
                result++;
            }
        }
    }

    console.log(`\nTotal Communicating Comps: ${result}\n`);
    return result;
}

countServers([
    [1, 0],
    [0, 1],
]); // Expected Output: 0

countServers([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
]); // Expected Output: 3
