# Brute Force Code & Optimal Code
class Solution:
    def DFS(self, stones, index, visited):
        # mark the current stone as visited
        visited[index] = True
        # check all stones to find connected stones
        for i in range(self.n):
            # check if the stone is unvisited and shares the same row or column as the current stones
            if (not visited[i] and (stones[i][0] == stones[index][0] or stones[i][1] == stones[index][1])):
                # visit all connected stone using DFS
                self.DFS(stones, i, visited)
    def removeStones(self, stones: list[list[int]]) -> int:
        # store the total number of stones
        self.n = len(stones)
        # track with stone have been visited
        visited = [False] * self.n
        # count the number of connected components
        count = 0
        # traverse all stones
        for i in range(self.n):
            # skip stones that are already visited
            if visited[i]:
                continue 
            # explore all stones connected to the current stone 
            self.DFS(stones, i, visited)
            # increment the count after completing one component
            count += 1
        # maximum removalble stones =  total stones - connected components
        return self.n - count 

# Time Complexity : O(N)
# Space Complexity : O(N)