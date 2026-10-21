# Brute Force Code & Optimal Code
class Solution:
    def allPathsSourceTarget(self, adj: list[list[int]]) -> list[list[int]]:
        # stores all valid paths from the source code (0) to the target node(n - 1)
        result = []
        def DFS(start, temp):
            # add the current node to the current path
            temp.append(start)
            # base case : if reach the last node (target) have found complete path from source to target
            if start == len(adj) - 1:
                # store copy of the current path in result 
                result.append(temp.copy())
            else:
                # recursive case : explore every neighours of the current node each neighours represents a possible next step along path toward the target
                for x in adj[start]:
                    # recurively explore the path though neighour x the current path is passed so that x can be added to it during the next DFS call
                    DFS(x, temp)
            # backtracking : remove the current node from the path after exploring all possibilities starting from this node this restores temp to its previous state so that other branches can be exlored independenlty
            temp.pop()
        # start DFS from each neighbours of node 0 initally temp contain [0] because every valid path must start at node 0 DFS then explores paths beginning with each neighbours
        for x in adj[0]:
            # create fresh path starting from the source code
            temp = [0]
            # explore all paths that begin with nieghbor x
            DFS(x, temp)
        # return all paths that start at node 0 and end at node n - 1
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)