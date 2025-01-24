# PROBLEM #802 - FIND EVENTUAL SAFE STATES

# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i
#   - Meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges.
# A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We need to check each node in the graph and determine if a loop is created or not --> The node can lead back to itself through it's adjacent node paths
# If there is a loop present, the node is not deemed safe
# If we do not find a loop, we reach a terminal node, we know that the node is safe

# We need a way to check each node and update if it is a possible loop or a path to a terminal node
#   - Initialize the array with a neutral value (I would use (0) since it is small to store)

# We need a function to check each node status and return a value to determined if it is a loop or not
#   - Update the values in our array to be either visited/loop or safe/terminal

# We need to traverse all adjacent nodes of each node --> RECURSION --> DFS
#   - Call the same function to check each node on subsequent adjancent nodes
#   - If we reach a terminal node, we know that path is safe
#   - If no adjacent nodes create a loop, that node is then deemed safe
#   - We can set the status in the array so that if we encounter that node as a later adjacent node, we already know it is a loop or safe!

# ---------------------------------------------------------------------------------------------------------------------------


def eventualSafeNodes(graph: list[int]) -> list[int]:
    # The length of the grid represents the total number of nodes we have
    nodes = len(graph)

    # Initialize an array with default values to represent each node of the grid --> Again by index
    status = [0] * nodes

    print(f"Status Intialized: {status}")

    # Initialize our result array to store all of the indexes of nodes that do not form a loop --> Safe nodes
    result: list[int] = []

    for index in range(nodes):
        if not dfs(graph, index, status):
            result.append(index)

    print(f"\nCompleted Result: {result}\n")
    return result


# Create a function to perform our loop search action --> A DFS of the nodes and their adjacent nodes
def dfs(graph: list[list[int]], index: int, status: list[int]) -> bool:
    # This function will visit each node and update it's value as either visited (potentially a loop) or safe (no loop created/terminal node)
    #   - I use (1) to desginated a visited node and (-1) to designate a safe node --> Remember, the array was initialized with (0) as the initial value of every index
    #   - These checks are used for the adjacent nodes of the current node --> If they have already been visited through our dfs function, their values will be set
    if status[index] == 1:
        return True  # A loop has been found since this node has already been visited
    if status[index] == -1:
        return False  # We have already visited this node and determined that it is a terminal node --> No loop can be formed

    # We set our index value for this node to visited on the first visit to this node --> Would've been (0) if it passed prior two checks
    status[index] = 1

    # Move through each adjacent node for the current node of the graph --> graph[0] represents the first nested array with adjacent nodes within
    for node in graph[index]:
        print(f"Status Array Update: {status}")
        # If we return True at any point through iterating through adjacent nodes --> We have found a loop and know this index is not 'safe'
        if dfs(graph, node, status):

            return True

    # We set our index value for this node to safe since we have not been able to find a loop through this node
    status[index] = -1

    print(f"Status Array Update: {status}")

    # Return false here because terminal nodes will reach this condition on their first visit, therefore we need to also return False immediately for these nodes
    return False


# ---------------------------------------------------------------------------------------------------------------------------

# Refactored for a nested function --> Less arguments to pass to dfs and overall slightly cleaner
#   - Comments are not replicated since functionality is identical


def eventualSafeNodesRefactor(graph: list[list[int]]) -> list[int]:
    nodes = len(graph)
    status = [0] * nodes
    result: list[int] = []

    def dfs(index: int) -> bool:
        if status[index] == 1:
            return True

        if status[index] == -1:
            return False

        status[index] = 1

        for node in graph[index]:
            if dfs(node):
                return True

        status[index] = -1
        return False

    for index in range(nodes):
        if not dfs(index):
            result.append(index)

    return result


eventualSafeNodes(
    [[1, 2], [2, 3], [5], [0], [5], [], []]
)  # Expected Output: [2, 4, 5, 6]
eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []])  # Expected Output: [4]
