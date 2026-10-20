// Brute Force Code & Optimal Code
class Solution {
public:
    // initialize the count variable
    int count = 1;
    void DFS(vector<vector<int>>& rooms, int u, vector<bool>& visited) {
        // mark the current room as visited
        visited[u] = true;
        // visit all rooms whose keys are available in the current room
        for (int node : rooms[u]) {
            // if the room has not been visited, explore it using DFS
            if (!visited[node]) {
                DFS(rooms, node, visited);
            }
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        // total number of rooms
        int n = rooms.size();
        // initialize all rooms as unvisited
        vector<bool> visited(n, false);
        // start DFS from room 0 because it is initially accessible
        DFS(rooms, 0, visited);
        // check whether every room has been visited
        for (bool x : visited) {
            if (x == false) {
                // return false if any room cannot be visited
                return false;
            }
        }
        // return true if all rooms are visited
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)