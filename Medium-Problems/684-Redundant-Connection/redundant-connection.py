# PROBLEM #684 - REDUNDANT CONNECTION

# In this problem, a tree is an undirected graph that is connected and has no cycles

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph

# Return an edge that can be removed so that the resulting graph is a tree of n nodes
#   - If there are multiple answers, return the answer that occurs last in the input.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# My initial thought was to create an adjacency list where each key is the current node and each value is the adjacent node list
#   - Being an undirected graph, each adjacent node must be added to both keys --> if [1,2] then 1: [2] and 2: [1]
# We can use a helper function to determine if there is a path from the current node to the target node in our graph --> Path between two nodes
#   - We can use a set to track which nodes have been visited in the recursive calls so we can avoid infinite loops due to the undirected graph
#       - VERY IMPORTANT FOR UNDIRECTED GRAPH --> Once we visited a node, we cannot add it to the set again within the recursive call
#   - If we find a path in any of the adjacent nodes of our current node (recursive calls) --> We have found a redundant path which can be removed
#   - If not, we add that edge to the list and continue our processing

# There is a more efficient solution using the Union-Find structure --> Efficiently finds cycles within the graph
#   - Something I have not learned, at this time, but will research to build that solution

# ---------------------------------------------------------------------------------------------------------------------------


# DFS SOLUTION
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    # Initialize an adjacency list to represent the graph --> Key = Node, Val: Adjacency List to that Node
    adj = {}

    # Depth-First Search (DFS) to check if there's a path from 'node' to 'target' --> If such a path exists, it means adding the new edge would form a cycle
    def dfs(node, target, visited):
        # Base case: If node is already visited, return False --> Avoid those infinite loops
        if node in visited:
            return False

        # Mark node as visited by adding it to our set --> Being a set will avoid adding the node again for the undirected portion of the graph
        #   - Undirected meaning that the adjacent nodes can be in both directions --> 1 to 2 and 2 to 1
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

            # If DFS finds a path from n1 to n2, this edge is redundant --> It had already existed
            #   - Using a set here avoids infinite loops in our dfs search --> dfs could go back and forth because the graph is undirected
            if dfs(n1, n2, set()):

                # Return the redundant edge
                print(f"\n -- Result: {n1, n2} -- \n")

                return [n1, n2]

        # If no cycle was detected, add the edge to the adjacency list
        if n1 not in adj:
            adj[n1] = []  # Initialize adjacency list for node n1

        if n2 not in adj:
            adj[n2] = []  # Initialize adjacency list for node n2

        # Could also use the "setdefault" method here --> adj.setdefault(n1, []).append(n2)
        #   - A more pythonic solution and would be one line per node --> Would combine the conditional and the append line for each

        # Add the edge (since it's an undirected adj, add both directions (we can create paths in both directions))
        adj[n1].append(n2)
        adj[n2].append(n1)

        print(f"Adjacency Graph: {adj}")


findRedundantConnection([[1, 2], [1, 3], [2, 3]])
findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
