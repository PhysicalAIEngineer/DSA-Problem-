# Brute Force Code & Optimal Code 
class Solution:
    def maxCollectedFruits(self, grid: list[list[int]]) -> int:
        # step 1 : calculate the grid dimensions
        # calculate the total number of rows in the grid since the grid is an n x n square matrix the number of rows and columns is the same.
        n = len(grid)
        # step 2: create the memoization tables
        # create a 2D memoization table 't' with: n rows & n columns initially, every cell contains -1. for the second and third children: t[i][j] stores the maximum number of fruits that can be collected starting from cell (i, j) by following that child's allowed movement directions -1 means that the state has not been calculated yet use the same table for both children because their
        # valid regions do not overlap:
        # 1. second child -> cells above the main diagonal (i < j).
        # 2. third child  -> cells below the main diagonal (i > j).
        # diagonal entries are marked as 0 by child1Collect().
        t = [[-1] * n for _ in range(n)]
        # first child : collect fruits along the main diagonal
        # first child starts at the top-left corner (0, 0) and moves diagonally down-right. its path is: (0, 0) -> (1, 1) -> (2, 2) -> ... -> (n-1, n-1) therefore, it collects all fruits along the main diagonal this child does not need recursion or memoization because its path is fixed.
        def child1Collect():
            # initialize the total number of fruits collected by the first child to 0 add the fruits from every diagonal cell.
            ans = 0
            # iterate through all row indices of the grid since this is a square matrix, grid[i][i] represents the diagonal cell in row 'i'.
            for i in range(n):
                # collect fruits from the diagonal cell add the number of fruits present in the current diagonal cell (i, i) to the total ans stores the cumulative fruits collected by the first child.
                ans += grid[i][i]
                # mark the diagonal cell as collected set the current diagonal cell to 0.
                grid[i][i] = 0
                # mark the corresponding memoization enty as 0
                # since the diagonal has already been collected by the first child, the other children cannot collect any additional fruits from these cells setting t[i][i] = 0 also prevents these states from being treated as uncomputed states.
                t[i][i] = 0
            # return the total number of fruits collected along the main diagonal.
            return ans
        # second child : collect fruits above the main diagonal 
        # second child starts at the top-right corner: (0, n - 1) it moves downward through the upper triangular region.
        # allowed movements:
        # 1. down-left  -> (i + 1, j - 1)
        # 2. down       -> (i + 1, j)
        # 3. down-right -> (i + 1, j + 1)
        # second child must stay strictly above the main diagonal, meaning: i < j it cannot enter or cross the main diagonal.
        def child2Collect(i, j):
            # base case 1: outside the grid
            # check whether the current position is outside the boundaries of the grid.
            # i < 0  -> above the first row.
            # i >= n -> below the last row.
            # j < 0  -> left of the first column.
            # j >= n -> right of the last column.
            # if any condition is true, the position is invalid return 0 because an invalid position cannot contribute any additional fruits.
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            # base case 2: destination cell 
            # check whether the current position is the bottom-right destination cell (n - 1, n - 1) this cell belongs to the main diagonal. first child has already collected the fruits from this cell and changed its value to 0 second child is not allowed to enter the main diagonal therefore, return 0.
            if i == n - 1 and j == n - 1:
                return 0
            # base case 3: do not enter or cross the diagonal 
            # check whether the current cell is on or below the main diagonal.
            # 1. i == j -> cell belongs to the main diagonal.
            # 2. i > j  -> cell is below the main diagonal.
            # second child is allowed to collect fruits only from cells strictly above the main diagonal therefore, if either condition is true, return 0 this ensures that the second child stays in the region where i < j.
            if i == j or i > j:
                return 0
            # step 1: check the memoization tables 
            # check whether we have already calculated the maximum fruits collectible starting from (i, j) if t[i][j] is not -1, the answer is already available. return the cached result instead of exploring the same state again this avoids repeated recursive calculations.
            if t[i][j] != -1:
                return t[i][j]
            # step 2: explore the three possible movements 
            # option 1: move down left
            # moving down-left means:
            # - row index increases by 1.
            # - column index decreases by 1.
            # next cell becomes (i + 1, j - 1) recursively calculate the maximum fruits that can be collected from that next cell add grid[i][j] because the second child also collects the fruits from the current cell store the total in 'leftcorner'.
            leftcorner = grid[i][j] + child2Collect(i + 1, j - 1)
            # option 2: move down
            # moving down means:
            # - row index increases by 1.
            # - column index remains unchanged.
            # next cell becomes (i + 1, j) recursively calculate the maximum fruits collectible from that next cell add the fruits from the current cell grid[i][j] store the total in 'middle'.
            middle = grid[i][j] + child2Collect(i + 1, j)
            # option 3: move down right 
            # moving down-right means:
            # - row index increases by 1.
            # - column index increases by 1.
            # next cell becomes (i + 1, j + 1) recursively calculate the maximum fruits collectible from that next cell add the fruits from the current cell grid[i][j] store the total in 'rightcorner'.
            rightcorner = grid[i][j] + child2Collect(i + 1, j + 1)
            # step 3: select the movement that collects the maximum fruits  explored all three possible movements:
            # 1. leftcorner  -> move down-left.
            # 2. middle      -> move down.
            # 3. rightcorner -> move down-right.
            # select the largest result using max() store the maximum number of fruits collectible from the current cell (i, j) in the memoization table this avoids recalculating this state in the future.
            t[i][j] = max(leftcorner, middle, rightcorner)
            # return the maximum fruits collectible starting from the current cell.
            return t[i][j]
        # third child : collect fruits below the main diagonal 
        # third child starts at the bottom-left corner: (n - 1, 0) it moves toward the right through the lower triangular region.
        # allowed movements:
        # 1. up-right   -> (i - 1, j + 1)
        # 2. right      -> (i, j + 1)
        # 3. down-right -> (i + 1, j + 1)
        # third child must stay strictly below the main diagonal, meaning: i > j it cannot enter or cross the main diagonal.
        def child3Collect(i, j):
            # base case 1: outside the grid
            # check whether the current position is outside the boundaries of the grid.
            # i < 0  -> above the first row.
            # i >= n -> below the last row.
            # j < 0  -> left of the first column.
            # j >= n -> right of the last column.
            # if the current position is invalid return 0 because it cannot contribute any fruits.
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            # base case 2: destination cell 
            # check whether we have reached the bottom-right destination cell (n - 1, n - 1) this cell belongs to the main diagonal first child has already collected its fruits third child is not allowed to enter the main diagonal therefore, return 0.
            if i == n - 1 and j == n - 1:
                return 0
            # base case 3: do not enter or cross the diagonal 
            # check whether the current cell is on or above the main diagonal.
            # 1. i == j -> The cell belongs to the main diagonal.
            # 2. j > i  -> The cell is above the main diagonal.
            # third child is allowed to collect fruits only from cells strictly below the main diagonal therefore, if either condition is true return 0 this ensures that the third child stays in the region where i > j.
            if i == j or j > i:
                return 0
            # step 1: check the memoization tables 
            # check whether we have already calculated the maximum fruits collectible starting from (i, j) if t[i][j] is not -1, the answer is already stored. return the cached result instead of exploring the same state again second child's states are above the diagonal, while the third child's states are below it therefore, both children can safely share the same memoization table.
            if t[i][j] != -1:
                return t[i][j]
            # step 2: explore the three possible movements 
            # option 1: move up right 
            # moving up-right means:
            # - row index decreases by 1.
            # - column index increases by 1.
            # next cell becomes (i - 1, j + 1) recursively calculate the maximum fruits collectible from that next cell add the fruits from the current cell grid[i][j] store the total in 'topcorner'.
            topcorner = grid[i][j] + child3Collect(i - 1, j + 1)
            # option 2: move right 
            # moving right means:
            # - row index remains unchanged.
            # - column index increases by 1.
            # next cell becomes (i, j + 1) recursively calculate the maximum fruits collectible from that next cell add the fruits from the current cell grid[i][j] store the total in 'right'.
            right = grid[i][j] + child3Collect(i, j + 1)
            # option 3: move down right 
            # moving down-right means:
            # - row index increases by 1.
            # - column index increases by 1.
            # next cell becomes (i + 1, j + 1) recursively calculate the maximum fruits collectible from that next cell add the fruits from the current cell grid[i][j] store the total in 'rightcorner'.
            rightcorner = grid[i][j] + child3Collect(i + 1, j + 1)
            # step 3: select the movement that collects the maximum fruits 
            # explored all three possible movements:
            # 1. topcorner   -> move up-right.
            # 2. right       -> move right.
            # 3. rightcorner -> move down-right.
            # select the largest result using max() store the maximum fruits collectible from the current cell in the memoization table.
            t[i][j] = max(topcorner, right, rightcorner)
            # return the maximum fruits collectible starting from the current cell.
            return t[i][j]
        # step 4: calculate the first child fruits 
        # call child1Collect() first child collects fruits from every cell along the main diagonal the collected fruits are added to firstChildScore all diagonal cells are also changed to 0 so that the other children cannot collect those fruits again.
        firstChildScore = child1Collect()
        # step 5: calculate the second child fruits 
        # start the second child from the top-right corner starting coordinates: i = 0 & j = n - 1 the second child explores the upper triangular region and selects the movement that collects the maximum fruits store the maximum fruits collected in secondChildScore.
        secondChildScore = child2Collect(0, n - 1)
        # step 6: calculate the third child fruits 
        # start the third child from the bottom-left corner starting coordinates: i = n - 1 & j = 0 the third child explores the lower triangular region and selects the movement that collects the maximum fruits store the maximum fruits collected in thirdChildScore.
        thirdChildScore = child3Collect(n - 1, 0)
        # step 7: calculate the total fruits collected 
        # add the fruits collected by all three children:
        # 1. firstChildScore  -> fruits from the main diagonal.
        # 2. secondChildScore -> Maximum fruits from the upper triangular region.
        # 3. thirdChildScore  -> Maximum fruits from the lower triangular region.
        # return the total number of fruits collected.
        return firstChildScore + secondChildScore + thirdChildScore

# Time Complexity : O(N)
# Space Complexity : O(N)