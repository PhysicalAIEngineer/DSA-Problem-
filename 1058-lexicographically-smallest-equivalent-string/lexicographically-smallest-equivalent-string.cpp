// Brute Force Code & Optimal Code
class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        // build an adjacency list to represent character equivalences if s1[i] and s2[i] are equivalent, add an edge between them since equivalence is bidirectional, add both directions characters connected through a path belong to the same group.
        vector<vector<char>> adj(26);
        for (int i = 0; i < s1.size(); i++) {
            char u = s1[i];
            char v = s2[i];
            adj[u - 'a'].push_back(v);
            adj[v - 'a'].push_back(u);
        }
        // DFS explores all characters equivalent to curr and returns the lexicographically smallest character in its component visited prevents revisiting characters and entering an infinite loop because the graph may contain cycles.
        function<char(char, vector<int>&)> DFS =
            [&](char curr, vector<int>& visited) -> char {
                // convert the current character to an index from 0 to 25 and mark it as visited.
                // 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
                visited[curr - 'a'] = 1;
                // initially, assume the current character is the smallest character in its equivalence group.
                char minChar = curr;
                // explore every character directly equivalent to curr.
                for (char v : adj[curr - 'a']) {
                    // visit a neighboring character only if it has not already been explored.
                    if (visited[v - 'a'] == 0) {
                        // recursively explore the neighbor's component and get its smallest equivalent character.
                        char smallest = DFS(v, visited);
                        // keep the lexicographically smaller character.
                        minChar = min(minChar, smallest);
                    }
                }
                // return the smallest character found in this component.
                return minChar;
            };
        // stores the final answer.
        string result = "";
        // replace each character in baseStr with the smallest character from its equivalence group.
        for (char ch : baseStr) {
            // create a fresh visited array for this DFS traversal.
            vector<int> visited(26, 0);
            // find the smallest equivalent character and append it.
            result += DFS(ch, visited);
        }
        // return the final string.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)