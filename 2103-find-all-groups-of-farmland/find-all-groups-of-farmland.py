# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # number of rows in the farmland matrix
        self.m = 0
        # number of column in the farmland matrix
        self.n = 0
        # store the final farmland groups
        self.result = []
        # four possible movements directions
        self.directions = [
            [0, 1], # right
            [0, -1], # left
            [1, 0], # down
            [-1, 0], # up
        ]
    def DFS(self, land, i, j, r2, c2):
        # mark the current farmland cell as visited changing 1 to 0 prevents us from visiting the same farmland cell agins
        land[i][j] = 0
        # update the bottom right corner of the current farmland groups
        # - r2 stores the largest row found so far
        # - c2 stores the largest column found so far
        r2[0] = max(r2[0], i)
        c2[0] = max(c2[0], j)
        # explore all four direction cells
        for direction in self.directions:
            # calculate the neighbouring row
            new_i = i + direction[0]
            # calculate the neighbouring column
            new_j = j + direction[1]
            # check three condition
            # 1. row is inside the matrix
            # 2. column is inside the matrix
            # 3. neighbouring cell is farmland
            if (0 <= new_i < self.m and 0 <= new_j < self.n and land[new_i][new_j] == 1):
                # continue DFS from the neighboring farmland cell
                self.DFS(land, new_i, new_j, r2, c2)
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # number of rows
        self.m = len(land)
        # number of columns
        self.n = len(land[0])
        # clear the result list
        self.result = []
        # visit every cell in matrix
        for i in range(self.m):
            for j in range(self.n):
                # if find an unvisited farmland cell it represents the start of a new farmland group
                if land[i][j] == 1:
                    # current cell is the top left corner of this farmland group
                    r1 = i
                    c1 =  j
                    # initially the bottom right corner is unknown list are used so the DFS can modifiy these values directly
                    r2 = [-1]
                    c2 = [-1]
                    # use DFS to visit every connected farmland cell in this group DFS will also find the largest row and largest column
                    self.DFS(land, i, j, r2, c2)
                    # store the four corner of the farmland group: [top row, left column, bottom row, right column]
                    self.result.append([r1, c1, r2[0], c2[0]])
        # return all farmland groups
        return self.result 

# Time Complexity : O(N)
# Space Complexity : O(N)