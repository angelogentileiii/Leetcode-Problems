# PROBLEM #684 - REDUNDANT CONNECTION

# In this problem, a tree is an undirected graph that is connected and has no cycles

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph

# Return an edge that can be removed so that the resulting graph is a tree of n nodes
#   - If there are multiple answers, return the answer that occurs last in the input.

# ---------------------------------------------------------------------------------------------------------------------------


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    # Initialize an adjacency list to represent the graph
    adj = {}

    # Depth-First Search (DFS) to check if there's a path from 'node' to 'target' --> If such a path exists, it means adding the new edge would form a cycle
    def dfs(node, target, visited):
        # Base case: If node is already visited, return False
        if node in visited:
            return False

        # Mark node as visited
        visited.add(node)

        print(f"Visited Set: {visited}")

        # If we reached the target node, a path exists
        if node == target:
            return True

        # Recursively visit all neighbors and check if any path leads to target
        return any(dfs(neighbor, target, visited) for neighbor in adj[node])

    # Iterate over each edge in the given input
    for n1, n2 in edges:

        # If both nodes already exist in the adj, check if adding (n1, n2) creates a cycle
        if n1 in adj and n2 in adj:

            # If DFS finds a path from n1 to n2, this edge is redundant
            if dfs(n1, n2, set()):

                # Return the redundant edge
                print(f"\n -- Result: {n1, n2} -- \n")

                return [n1, n2]

        # If no cycle was detected, add the edge to the adjacency list
        if n1 not in adj:
            adj[n1] = []  # Initialize adjacency list for node n1

        if n2 not in adj:
            adj[n2] = []  # Initialize adjacency list for node n2

        # Add the edge (since it's an undirected adj, add both directions (we can create paths in both directions))
        adj[n1].append(n2)
        adj[n2].append(n1)

        print(f"Adjacency Graph: {adj}")


findRedundantConnection([[1, 2], [1, 3], [2, 3]])
findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
