# Problem #841 - KEYS AND ROOMS

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
# Your goal is to visit all the rooms. 
# However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it.
# Each key has a number on it, denoting which room it unlocks, and 
# you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

#---------------------------------------------------------------------------------------------------------------------------

# This is a problem about traversal --> We need to traverse the rooms and pickup keys to travers addt. rooms
    # Either use BFS or DFS --> TRAVERSAL TECHNIQUES

# Step 1: Start at Room 0 (index 0) and use keys found in room to unlock other room
# Step 2: Track Visited rooms --> To know where we have been
# Step 3: After traversal, check if all rooms are visited 

#---------------------------------------------------------------------------------------------------------------------------

# DEPTH FIRST SOLUTION
def canVisitAllRoomsDFS(rooms: list[int]) -> bool:
    visited = [False] * len(rooms) # Initialize a list to track rooms visited (Make all False to start)

    def dfsTravers(room):
        visited[room] = True # Mark the current room as visited
        for key in rooms[room]: # Explore the rooms for the keys within this room
            if not visited[key]: # If it hasn't been visited, visit it via recursion
                dfsTravers(key)

    # Begin at room 0 --> Base case
    dfsTravers(0)

    # Check if all rooms have been visited using all method
    return all(visited)

# BREADTH FIRST SOLUTION
from collections import deque

def canVisitAllRoomsBFS(rooms: list[int]) -> bool:
    visited = [False] * len(rooms)
    queue = deque([0]) # Queue for BFS search beginning with Room 0
    visited[0] = True # Mark Room 0 as visited

    while queue: # Loop for BFS
        room = queue.popleft() # Grab the next room to process
        for key in rooms[room]: # For each key in the room, visit the children rooms
            if not visited[key]: # If they haven't been visited, proceed with the following
                visited[key] = True
                queue.append(key) # Add the room to the queue to explore it's keys
    
    # Checks if all values are true in parameter --> Check rooms visited
    return all(visited)


rooms1 = [[1],[2],[3],[]] # Expect True
rooms2 = [[1,3],[3,0,1],[2],[0]] # Expect False

print('BFS: ', canVisitAllRoomsBFS(rooms1))
print('BFS: ', canVisitAllRoomsBFS(rooms2))

print('DFS: ', canVisitAllRoomsDFS(rooms1))
print('DFS: ', canVisitAllRoomsDFS(rooms2))