# Brute Force Code & Optimal Code
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        # calculate the total number of rows in the grid 
        m = len(grid)
        # calculate the total number of columns in the grid 
        n = len(grid[0])
        # define the modulo values 
        mod = 10 ** 9 + 7
        # create the memoization tables 
        # each memoization entry stores pairs : t[i][j] = (maximum product, minimum product) these values represent the maximum and minimum products among all valid paths from cell(i, j) to the destination store both values because negative numbers can reverse the effect of multiplication : 1. negative * maximum -> potentially minimum & 2. negative * minimum -> potentially maximum so, memoization prevents us from calculating the same cell maximum and minimum products multiple times 
        t = [[None] * n for _ in range(m)]
        # define the recursive function
        # solve (i, j) calculates two values : 1. maximum product from cell (i, j) to destination & 2. minimum product from cell (i, j) to destination and i represent the current row index & j represents the current column index so can move only in two directions down -> (i + 1, j) & right -> (i, j + 1)
        def solve(i, j):
            # base case : destination reached
            # check whether the current position is the bottom-right destination cell the destination coordinates are: (m - 1, n - 1) if reach the destination, there are no more movements to make therefore the product of the remaining path is simply the values of the destination cell itself both the maximum and minimum product are equal because there is only one remaining values return tuples (maximum product, minimum product)
            if i == m - 1 and j == n - 1:
                return (grid[i][j], grid[i][j])
            # check the memoization tables 
            # if t[i][j] is not None, it means that both values have already been calculated and stored return the cached tuples immediately instead of exploring the same subproblem agai this avoids repeated recursive calculations.
            if t[i][j] is not None:
                return t[i][j]
            # intialize maximum and minimum values 
            # intialize maxval with negative infinity this ensures that any valid product will be greater than the initial maximum value continuously update maxval whenever discover larger product
            maxval = float("-inf")
            # ntialize minval with positive infinity this ensures that any valid product will be smaller than the initial minimum value will continuously update minval whenever discover smaller product
            minval = float("inf")
            # option 1: move down
            # check whether moving down is possible next row is i + 1 if i + 1 < m the next row exits inside the grid 
            if i + 1 < m:
                # recursively calculate the maximum and minimum product from the cell directly below solve(i + 1, j) return tuples containing: 1. downmax -> maximum product from the cell below to the destination & 2. downmin -> minimum product from the cell below to the destination unpacj the retuned tuple into these two variables 
                downmax, downmin = solve(i + 1, j)
                # calculate the maximum product though down 
                # multiply the current cell values by both : downmax & downmin why do muliply by both values 1.if grid[i][j] is positive : multiplying by downmax may produce the maximum & multiplying by downmin may produce the minimum therefore must consider both possibilities maxval stores the largest product found so far
                maxval = max(maxval, grid[i][j] * downmax, grid[i][j] * downmin)
                # calculate the minimum product though down 
                # again multiply the current cell value by both the maximum and minimum products below select the smallest result using min() minval stores the smallest product found so far
                minval = min(minval, grid[i][j] * downmax, grid[i][j] * downmin)
            # option 2: move right
            # check whether moving right is possible next row is j + 1 if j + 1 < n the next row exits inside the grid
            if j + 1 < n:
                # recursively calculate the maximum and minimum product from the cell directly below solve(i, j + 1) return tuples containing: 1. rightmax -> maximum product from the cell below to the destination & 2. rightmin -> minimum product from the cell below to the destination unpacj the retuned tuple into these two variables 
                rightmax, rightmin = solve(i, j + 1)
                # calculate the maximum product though right
                # multiply the current cell values by both : rightmax & rightmin consider both because a negative current cell value can turn the minimum product into the maximum product compare all possible products and retain the largest values in maxval so, maxval may already contain a larger product obtained by moving down
                maxval = max(maxval, grid[i][j] * rightmax, grid[i][j] * rightmin)
                # store both result in the memoization tables 
                # after exploring all valid directions : 1. maxval contains the maximum product from (i, j). & 2. minval contains the minimum product from (i, j). and store both values together as tuples t[i][j] = (maximum product, minimum product) this allows us reuse both results if anohter recursive path reaches the same cell
                minval = min(minval, grid[i][j] * rightmax, grid[i][j] * rightmin)
            # store both result in the memoization tables 
            # after exploring all valid directions : 1. maxval contains the maximum product from (i, j). & 2. minval contains the minimum product from (i, j). and store both values together as tuples t[i][j] = (maximum product, minimum product) this allows us reuse both results if anohter recursive path reaches the same cell
            t[i][j] = (maxval, minval)
            # return the maximum and minimum products calculated for the current cell
            return t[i][j]
        # start the recursion
        # start calculating the maximum and minimum products from the top-left corner of the grid. so, starting cell coordinates are (0, 0) 1. maxprod -> Maximum product among all valid paths from the starting cell to the destination 2. minprod -> minimum product among all valid paths from the starting cell to the destination so, only need maxprod for the final answer, but calculate minProd because it is necessary for handling negative numbers correctly.
        maxprod, minprod = solve(0, 0)
        # check whether the maximum product is negative
        # problem requires a non-negative maximum product if maxprod is negative, every possible path has negative product thefore no non negative product path exists return -1 as required by the problem
        if maxprod < 0:
            return -1
        # return the final answer 
        return maxprod % mod

# Time Complexity : O(N)
# Space Complexity : O(N)