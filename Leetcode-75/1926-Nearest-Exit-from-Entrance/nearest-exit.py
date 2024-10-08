# Problem #1926 - NEAREST EXIT FROM ENTRANCE IN MAZE

# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
# You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. 
# You cannot step into a cell with a wall, and you cannot step outside the maze. 
# Your goal is to find the nearest exit from the entrance. 
# An exit is defined as an empty cell that is at the border of the maze. 
# The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

#---------------------------------------------------------------------------------------------------------------------------

# Immediately thing BREADTH FIRST SEARCH --> SHORTEST PATH (aka nearest exit)
    # Utilize a QUEUE --> FIFO order
    # Track the cells we have visited
    # Add next coordinates to the Queue to process

#---------------------------------------------------------------------------------------------------------------------------
from collections import deque

def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # Represents four possible movement directions (up, down, left, right)
    entrance = (entrance[0], entrance[1]) # Convert the entrance to a tuple
    queue = deque([entrance]) # Add entrance to the queue for our BFS
    visited = set([entrance]) # Used to keep track of cells visited without duplicates
    step = 0 # Initialized to track number of steps taken --> Return value if exit found

    # Our BFS loop --> Runs until the queue is empty
    # Each iteration represents attempting one step in every direction
    while queue:
        stepLength = len(queue)
        
        for _ in range(stepLength):
            # For each node, we check if it is located on the perimeter of the matrix
            node = queue.popleft()

            if (node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1) and node != entrance:
                return step # Return current count for shortest answer
            
            # For each node, we check all four directions of movement possible
            for dir in directions:
                newDir = (node[0] + dir[0], node[1] + dir[1]) # Add each direction to the original coordinates (Movement to new space)
                # Here we check threw things:
                    # The cell has not been already visited
                    # The new coordinates are within the bounds of the maze
                    # The new cell is an open path (Represent by the '.' element)
                if newDir not in visited and 0 <= newDir[0] < len(maze) and 0 <= newDir[1] < len(maze[0]) and maze[newDir[0]][newDir[1]] == '.':
                    # If yes to all, add cell to the visited set and add to queue for further exploration
                    visited.add(newDir)
                    queue.append(newDir)

        # After processing all nodes per level, increase step counter to indicate one more step into the maze completed
        step += 1
    
    # If no exit is found through loop, we exit and return -1
    return -1

maze1 = [
    ["+","+",".","+"],
    [".",".",".","+"],
    ["+","+","+","."]
]

maze2 = [
    ["+", ".", "+", "+", "+", "+", "+"],
    ["+", ".", "+", ".", ".", ".", "+"],
    ["+", ".", "+", ".", "+", ".", "+"],
    ["+", ".", ".", ".", ".", ".", "+"],
    ["+", "+", "+", "+", ".", "+", "."],
]

print(nearestExit(maze1, [1,2])) # Expect 1
print(nearestExit(maze2, [0,1])) # Expect 7

