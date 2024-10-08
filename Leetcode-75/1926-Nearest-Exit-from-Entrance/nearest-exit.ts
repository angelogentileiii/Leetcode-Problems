// Problem #1926 - NEAREST EXIT FROM ENTRANCE IN MAZE

// BREADTH FIRST SEARCH --> BEST SOLUTION TO FIND THE SHORTEST PATH (AKA CLOSEST EXIT)
function nearestExit(maze: string[][], entrance: number[]): number {
    const dirs = [
        [-1, 0], // Up
        [1, 0], // Down
        [0, -1], // Left
        [0, 1], // Right
    ]; // Four directions we can move from each node

    const queue: [number, number][] = [[entrance[0], entrance[1]]]; // Initialize queue with entrance values

    // Build an array of arrays to track visited cells --> Building as such allows us to store booleans, not processing integers throughout
    const visited = Array.from(
        { length: maze.length }, // First argument is the length of the new array --> Same as total rows in the matrix
        () => Array(maze[0].length).fill(false) // Second argument is how to fill the new array --> In this case we do so by building new arrays for each column of the matrix (length of maze[0])
    );

    const [entranceX, entranceY] = entrance; // Destructure to pull out the x, y coordinates of the entrance
    visited[entranceX][entranceY] = true; // Mark entrance as visited in our array

    let step = 0;

    while (queue.length > 0) {
        const stepLength = queue.length;

        for (let i = 0; i < stepLength; i++) {
            const [x, y] = queue.shift()!; // The queue begins with the entrance --> Each iteration utilizes the newX and newY calculated below

            // check that the X or Y coordinates are along an edge and are not the entrance to the maze
            if (
                (x === 0 ||
                    x === maze.length - 1 ||
                    y === 0 ||
                    y === maze[0].length - 1) &&
                (x !== entranceX || y !== entranceY)
            ) {
                return step; // We've found our exit
            }

            // Move in each direction of the current cell
            for (const [dirX, dirY] of dirs) {
                const newX = x + dirX; // Add the X movement to the current cell location
                const newY = y + dirY; // Add the Y movement to the current cell location

                // Check that the new location is within the bounds of the maze, is not a wall (open is "." value), and it has not been already visited
                if (
                    newX >= 0 &&
                    newX < maze.length &&
                    newY >= 0 &&
                    newY < maze[0].length &&
                    maze[newX][newY] === "." &&
                    !visited[newX][newY]
                ) {
                    visited[newX][newY] = true; // Mark the new cell as visited
                    queue.push([newX, newY]); // Push it's coordinates into the queue to be processed
                }
            }
        }
        step += 1;
    }

    return -1;
}

const maze1 = [
    ["+", "+", ".", "+"],
    [".", ".", ".", "+"],
    ["+", "+", "+", "."],
];

const maze2 = [
    ["+", ".", "+", "+", "+", "+", "+"],
    ["+", ".", "+", ".", ".", ".", "+"],
    ["+", ".", "+", ".", "+", ".", "+"],
    ["+", ".", ".", ".", ".", ".", "+"],
    ["+", "+", "+", "+", ".", "+", "."],
];

console.log(nearestExit(maze1, [1, 2])); // Expect 1
console.log(nearestExit(maze2, [0, 1])); // Expect 7
