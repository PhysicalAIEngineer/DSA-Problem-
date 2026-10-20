# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # initialize the count variable
        self.count = 1
    def DFS(self, rooms, u, visited):
        # mark the current room as visited
        visited[u] = True
        # visit all rooms whose keys are available in the current room
        for node in rooms[u]:
            # if the room has not been visited, explore it using DFS
            if not visited[node]:
                self.DFS(rooms, node, visited)
    def canVisitAllRooms(self, rooms):
        # total number of rooms
        n = len(rooms)
        # initialize all rooms as unvisited
        visited = [False] * n
        # start DFS from room 0 because it is initially accessible
        self.DFS(rooms, 0, visited)
        # check whether every room has been visited
        for x in visited:
            if x == False:
                # return False if any room cannot be visited
                return False
        # return True if all rooms are visited
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)