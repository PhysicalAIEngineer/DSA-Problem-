# Brute Force Code & Optimal Code
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # store the size of the square grid
        n = len(grid)
        # store the total number of row column pairs that are exactly equal
        count = 0
        # dictionary to store the how many times each row appears in the grid 
        mp = {}
        # step 1: store the frequency of every rows
        for row in range(n):
            # convert the current row into tuple so it can be used as dictionary key
            currentrow = tuple(grid[row])
            # increase the frequency of this row if the row has not appeared before get(currentrow, 0) return 0
            mp[currentrow] = mp.get(currentrow, 0) + 1
        # step 2: generate evey column and check whether it matches any sorted row
        for column in range(n):
            # store the values in the current values
            temp = []
            # traverse every row to bulid column c
            for row in range(n):
                # add the element at row r and column c
                temp.append(grid[row][column])
            # convert the column into tupls so it can be used as dictionary key
            temp = tuple(temp)
            # if this column matches one or more rows add the number of matching rows to count
            count += mp.get(temp, 0)
        # return the total number of equal row column pairs
        return count 

# Time Complexity : O(N)
# Space Complexity : O(N)