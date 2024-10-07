// Problem #841 - KEYS AND ROOMS

// DEPTH FIRST SEARCH --> RECURSION
function canVisitAllRoomsDFS(rooms: number[][]): boolean {
    let visited: boolean[] = new Array(rooms.length).fill(false);

    function traverse(room: number): void {
        visited[room] = true;
        for (const key of rooms[room]) {
            if (!visited[key]) {
                return traverse(key);
            }
        }
    }

    traverse(0);

    return visited.every((roomVisited) => roomVisited);
}

// BREADTH FIRST SEARCH
function canVisitAllRoomsBFS(rooms: number[][]): boolean {
    const visited: boolean[] = new Array(rooms.length).fill(false);
    const queue: number[] = [0]; // Initialize the queue with the first room we can enter
    visited[0] = true;

    while (queue.length) {
        const room = queue.shift()!; // Pulls the next room to evaluate from the queue

        // Must use "FOR __ OF __" here --> To get the actual value within the array (Not the string index)
        for (const key of rooms[room]) {
            // Loops through the found rooms and visits them (adding to queue to visit children)
            if (!visited[key]) {
                visited[key] = true;
                queue.push(key); // Add the found key's room to the queue
            }
        }
    }

    return visited.every((roomVisited) => roomVisited);
}

const rooms1 = [[1], [2], [3], []]; // Expect True
const rooms2 = [[1, 3], [3, 0, 1], [2], [0]]; // Expect False

console.log("DFS: ", canVisitAllRoomsDFS(rooms1));
console.log("DFS: ", canVisitAllRoomsDFS(rooms2));

console.log("BFS: ", canVisitAllRoomsBFS(rooms1));
console.log("BFS: ", canVisitAllRoomsBFS(rooms2));
