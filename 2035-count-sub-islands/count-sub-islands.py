# Brute Force Code & Optimal Code
class Solution:
    # DFS helper function explores one complete island in grid2 and checks whether that entire island is also present in grid1.
    def checkSubIsland(self, grid1: list[list[int]], grid2: list[list[int]], i: int, j: int) -> bool:
        # check whether moved outside the grid going outside the grid does NOT make the island invalid so return true
        if i < 0 or i >= len(grid1) or j < 0 or j >= len(grid1[0]):
            return True
        # only care about land cells in grid2 if this cell is water in grid2 there is nothing more to check from this path return True because water does not make the current grid2 island invalid.
        if grid2[i][j] != 1:  
            return True
        # mark the current grid2 cell as visited change 1 -> -1 so that we not visit the same cell again
        grid2[i][j] = -1 
        # check whether the correpsoding cell in grid1 is also land if grid2 has land(1) for this to be valid sub-island
        # 1. True -> grid1 also has land
        # 2. False -> grid2 has water
        result = (grid1[i][j] == 1)
        # explore all four neighbouring cells every land cell beloning to this grid2 island must also belong to land in grid1
        # 1. explore down
        result = result & self.checkSubIsland(grid1, grid2, i + 1, j)
        # 2. explore up   
        result = result & self.checkSubIsland(grid1, grid2, i - 1, j)  
        # 3. explore right
        result = result & self.checkSubIsland(grid1, grid2, i, j + 1)
        # 4. explore left   
        result = result & self.checkSubIsland(grid1, grid2, i, j - 1)   
        # return whether the complete island is contained inside grid1
        return result
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # store the total number of sub islands
        subIslands = 0
        # number of rows in grid2
        m = len(grid2)  
        # number fo column in grid2
        n = len(grid2[0])  
        # traverse evey cel of grid2
        for i in range(m):
            for j in range(n):
                # if find an unvisited land cell in grid2 it represents the beginning of new island checkSubIsland() explores the complete island and tells us wheter it is also completey contained in grid1
                if grid2[i][j] == 1 and self.checkSubIsland(grid1, grid2, i, j):
                    # entire island from grid2 exists inside grid1
                    subIslands += 1
        # return the total number of sub islands
        return subIslands

# Time Complexity : O(N)
# Space Complexity : O(N)