// PROBLEM #684 - REDUNDANT CONNECTION

// In this problem, a tree is an undirected graph that is connected and has no cycles

// You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added
// The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed
// The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph

// Return an edge that can be removed so that the resulting graph is a tree of n nodes
//   - If there are multiple answers, return the answer that occurs last in the input.

// ---------------------------------------------------------------------------------------------------------------------------

// THOUGHTS

// My initial thought was to create an adjacency list where each key is the current node and each value is the adjacent node list
//   - Being an undirected graph, each adjacent node must be added to both keys --> if [1,2] then 1: [2] and 2: [1]
// We can use a helper function to determine if there is a path from the current node to the target node in our graph --> Path between two nodes
//   - We can use a set to track which nodes have been visited in the recursive calls so we can avoid infinite loops due to the undirected graph
//       - VERY IMPORTANT FOR UNDIRECTED GRAPH --> Once we visited a node, we cannot add it to the set again within the recursive call
//   - If we find a path in any of the adjacent nodes of our current node (recursive calls) --> We have found a redundant path which can be removed
//   - If not, we add that edge to the list and continue our processing

// There is a more efficient solution using the Union-Find structure --> Efficiently finds cycles within the graph
//  - Something I have not learned, at this time, but will research to build that solution

// ---------------------------------------------------------------------------------------------------------------------------

function findRedundantConnection(edges: number[][]): [number, number] {
    // Initialize an adjacency list to represent the graph
    // Each key is a node, and its value is the list of adjacent nodes
    const adj: { [key: number]: number[] } = {};

    /**
     * Depth-First Search (DFS) to check if there's a path from `node` to `target`.
     * If such a path exists, adding a new edge would form a cycle.
     */
    function dfs(node: number, target: number, visited: Set<number>): boolean {
        // Base case: If the node has already been visited, return false to avoid infinite loops
        if (visited.has(node)) return false;

        // Mark the node as visited in our set
        //  - This will trigger the condition above recursively so we do not fall into an infinite loop
        visited.add(node);

        console.log(`Visited Set: [${Array.from(visited)}]`);

        // If we reached the target node, a path exists
        if (node === target) return true;

        // Recursively visit all neighbors and check if any path leads to the target
        //  - Use the some method (similar to any) which returns once any recursive call returns 'true'
        //      - could also use a for loop with a conditional to return 'true' --> would require a return statement outside the loop to verify the return type condition
        return adj[node].some((neighbor) => dfs(neighbor, target, visited));
    }

    // Iterate over each edge in the given input --> Separating the node from it's adjacent node (n1, n2)
    for (const [n1, n2] of edges) {
        // If both nodes already exist in the adjacency list, check if adding (n1, n2) creates a cycle
        if (adj[n1] !== undefined && adj[n2] !== undefined) {
            // If DFS finds a path from n1 to n2, this edge is redundant
            //  - This will be the edge we can remove
            if (dfs(n1, n2, new Set())) {
                console.log(`\n -- Result: [${n1}, ${n2}] -- \n`);
                return [n1, n2];
            }
        }

        // If no cycle was detected, add the edge to the adjacency list
        if (!adj[n1]) adj[n1] = []; // Initialize adjacency list for node n1
        if (!adj[n2]) adj[n2] = []; // Initialize adjacency list for node n2

        // Add the edge (since it's an undirected graph, add both directions)
        adj[n1].push(n2);
        adj[n2].push(n1);

        console.log(`Adjacency Graph:`, adj);
    }

    // This should never occur but satisfies the return type for the function
    return [-1, -1];
}

findRedundantConnection([
    [1, 2],
    [1, 3],
    [2, 3],
]);
findRedundantConnection([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 4],
    [1, 5],
]);
