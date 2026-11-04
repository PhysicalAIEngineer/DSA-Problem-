#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    int maxCollectedFruits(vector<vector<int>>& grid) {

        // Step 1: Calculate the grid dimensions.
        // Since the grid is an n x n square matrix,
        // the number of rows and columns is the same.
        int n = grid.size();

        // Step 2: Create the memoization table.
        // Create a 2D memoization table 't' with n rows
        // and n columns, initially filled with -1.
        //
        // For the second and third children:
        // t[i][j] stores the maximum number of fruits
        // that can be collected starting from cell (i, j).
        //
        // -1 means that the state has not been calculated yet.
        //
        // We use the same table for both children because
        // their valid regions do not overlap:
        //
        // 1. Second child -> cells above the main diagonal (i < j).
        // 2. Third child  -> cells below the main diagonal (i > j).
        //
        // Diagonal entries are marked as 0 by child1Collect().
        vector<vector<int>> t(n, vector<int>(n, -1));


        // --------------------------------------------------
        // First Child: Collect fruits along the main diagonal.
        // --------------------------------------------------

        // The first child starts at the top-left corner (0, 0)
        // and moves diagonally down-right.
        //
        // Its path is:
        // (0, 0) -> (1, 1) -> (2, 2) -> ... -> (n-1, n-1)
        //
        // Therefore, it collects all fruits along the main diagonal.
        //
        // This child does not need recursion or memoization
        // because its path is fixed.

        auto child1Collect = [&]() -> int {

            // Initialize the total number of fruits collected
            // by the first child to 0.
            int ans = 0;

            // Iterate through all row indices of the grid.
            // Since this is a square matrix, grid[i][i]
            // represents the diagonal cell in row i.
            for (int i = 0; i < n; i++) {

                // Collect fruits from the diagonal cell.
                // Add the number of fruits present in the
                // current diagonal cell (i, i) to the total.
                ans += grid[i][i];

                // Mark the diagonal cell as collected.
                // Set the current diagonal cell to 0.
                grid[i][i] = 0;

                // Mark the corresponding memoization entry as 0.
                //
                // Since the diagonal has already been collected
                // by the first child, the other children cannot
                // collect any additional fruits from these cells.
                //
                // Setting t[i][i] = 0 also prevents these states
                // from being treated as uncomputed states.
                t[i][i] = 0;
            }

            // Return the total number of fruits collected
            // along the main diagonal.
            return ans;
        };


        // --------------------------------------------------
        // Second Child: Collect fruits above the main diagonal.
        // --------------------------------------------------

        // The second child starts at the top-right corner:
        // (0, n - 1).
        //
        // It moves downward through the upper triangular region.
        //
        // Allowed movements:
        //
        // 1. Down-left  -> (i + 1, j - 1)
        // 2. Down       -> (i + 1, j)
        // 3. Down-right -> (i + 1, j + 1)
        //
        // The second child must stay strictly above the main
        // diagonal, meaning i < j.
        //
        // It cannot enter or cross the main diagonal.

        function<int(int, int)> child2Collect =
            [&](int i, int j) -> int {

            // Base Case 1: Outside the grid.
            //
            // Check whether the current position is outside
            // the boundaries of the grid.
            //
            // i < 0  -> Above the first row.
            // i >= n -> Below the last row.
            // j < 0  -> Left of the first column.
            // j >= n -> Right of the last column.
            //
            // If any condition is true, the position is invalid.
            // Return 0 because an invalid position cannot
            // contribute any additional fruits.
            if (i < 0 || i >= n || j < 0 || j >= n) {
                return 0;
            }

            // Base Case 2: Destination cell.
            //
            // Check whether the current position is the
            // bottom-right destination cell (n - 1, n - 1).
            //
            // This cell belongs to the main diagonal.
            // The first child has already collected its fruits
            // from this cell and changed its value to 0.
            //
            // The second child is not allowed to enter
            // the main diagonal.
            if (i == n - 1 && j == n - 1) {
                return 0;
            }

            // Base Case 3: Do not enter or cross the diagonal.
            //
            // Check whether the current cell is on or below
            // the main diagonal.
            //
            // 1. i == j -> Cell belongs to the main diagonal.
            // 2. i > j  -> Cell is below the main diagonal.
            //
            // The second child is allowed to collect fruits
            // only from cells strictly above the main diagonal.
            //
            // Therefore, if either condition is true, return 0.
            if (i == j || i > j) {
                return 0;
            }

            // Step 1: Check the memoization table.
            //
            // Check whether we have already calculated the
            // maximum fruits collectible starting from (i, j).
            //
            // If t[i][j] is not -1, the answer is already available.
            // Return the cached result instead of exploring
            // the same state again.
            if (t[i][j] != -1) {
                return t[i][j];
            }

            // Step 2: Explore the three possible movements.

            // Option 1: Move down-left.
            //
            // Moving down-left means:
            // - Row index increases by 1.
            // - Column index decreases by 1.
            //
            // Next cell becomes (i + 1, j - 1).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell.
            //
            // Add grid[i][j] because the second child also
            // collects the fruits from the current cell.
            int leftcorner =
                grid[i][j] + child2Collect(i + 1, j - 1);


            // Option 2: Move down.
            //
            // Moving down means:
            // - Row index increases by 1.
            // - Column index remains unchanged.
            //
            // Next cell becomes (i + 1, j).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell and add the fruits from
            // the current cell grid[i][j].
            int middle =
                grid[i][j] + child2Collect(i + 1, j);


            // Option 3: Move down-right.
            //
            // Moving down-right means:
            // - Row index increases by 1.
            // - Column index increases by 1.
            //
            // Next cell becomes (i + 1, j + 1).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell and add the fruits from
            // the current cell grid[i][j].
            int rightcorner =
                grid[i][j] + child2Collect(i + 1, j + 1);


            // Step 3: Select the movement that collects
            // the maximum number of fruits.
            //
            // We explored all three possible movements:
            //
            // 1. leftcorner  -> Move down-left.
            // 2. middle      -> Move down.
            // 3. rightcorner -> Move down-right.
            //
            // Select the largest result using max().
            //
            // Store the maximum number of fruits collectible
            // from the current cell (i, j) in the memoization table.
            t[i][j] = max({leftcorner, middle, rightcorner});

            // Return the maximum fruits collectible
            // starting from the current cell.
            return t[i][j];
        };


        // --------------------------------------------------
        // Third Child: Collect fruits below the main diagonal.
        // --------------------------------------------------

        // The third child starts at the bottom-left corner:
        // (n - 1, 0).
        //
        // It moves toward the right through the lower triangular region.
        //
        // Allowed movements:
        //
        // 1. Up-right   -> (i - 1, j + 1)
        // 2. Right      -> (i, j + 1)
        // 3. Down-right -> (i + 1, j + 1)
        //
        // The third child must stay strictly below the main
        // diagonal, meaning i > j.
        //
        // It cannot enter or cross the main diagonal.

        function<int(int, int)> child3Collect =
            [&](int i, int j) -> int {

            // Base Case 1: Outside the grid.
            //
            // Check whether the current position is outside
            // the boundaries of the grid.
            //
            // i < 0  -> Above the first row.
            // i >= n -> Below the last row.
            // j < 0  -> Left of the first column.
            // j >= n -> Right of the last column.
            //
            // If the current position is invalid, return 0
            // because it cannot contribute any fruits.
            if (i < 0 || i >= n || j < 0 || j >= n) {
                return 0;
            }

            // Base Case 2: Destination cell.
            //
            // Check whether we have reached the bottom-right
            // destination cell (n - 1, n - 1).
            //
            // This cell belongs to the main diagonal.
            // The first child has already collected its fruits.
            //
            // The third child is not allowed to enter
            // the main diagonal.
            if (i == n - 1 && j == n - 1) {
                return 0;
            }

            // Base Case 3: Do not enter or cross the diagonal.
            //
            // Check whether the current cell is on or above
            // the main diagonal.
            //
            // 1. i == j -> The cell belongs to the main diagonal.
            // 2. j > i  -> The cell is above the main diagonal.
            //
            // The third child is allowed to collect fruits
            // only from cells strictly below the main diagonal.
            //
            // Therefore, if either condition is true, return 0.
            if (i == j || j > i) {
                return 0;
            }

            // Step 1: Check the memoization table.
            //
            // Check whether we have already calculated the
            // maximum fruits collectible starting from (i, j).
            //
            // If t[i][j] is not -1, the answer is already stored.
            // Return the cached result instead of exploring
            // the same state again.
            //
            // The second child's states are above the diagonal,
            // while the third child's states are below it.
            //
            // Therefore, both children can safely share
            // the same memoization table.
            if (t[i][j] != -1) {
                return t[i][j];
            }

            // Step 2: Explore the three possible movements.

            // Option 1: Move up-right.
            //
            // Moving up-right means:
            // - Row index decreases by 1.
            // - Column index increases by 1.
            //
            // Next cell becomes (i - 1, j + 1).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell and add the fruits from
            // the current cell grid[i][j].
            int topcorner =
                grid[i][j] + child3Collect(i - 1, j + 1);


            // Option 2: Move right.
            //
            // Moving right means:
            // - Row index remains unchanged.
            // - Column index increases by 1.
            //
            // Next cell becomes (i, j + 1).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell and add the fruits from
            // the current cell grid[i][j].
            int right =
                grid[i][j] + child3Collect(i, j + 1);


            // Option 3: Move down-right.
            //
            // Moving down-right means:
            // - Row index increases by 1.
            // - Column index increases by 1.
            //
            // Next cell becomes (i + 1, j + 1).
            //
            // Recursively calculate the maximum fruits collectible
            // from that next cell and add the fruits from
            // the current cell grid[i][j].
            int rightcorner =
                grid[i][j] + child3Collect(i + 1, j + 1);


            // Step 3: Select the movement that collects
            // the maximum number of fruits.
            //
            // We explored all three possible movements:
            //
            // 1. topcorner   -> Move up-right.
            // 2. right       -> Move right.
            // 3. rightcorner -> Move down-right.
            //
            // Select the largest result using max().
            //
            // Store the maximum fruits collectible from
            // the current cell in the memoization table.
            t[i][j] = max({topcorner, right, rightcorner});

            // Return the maximum fruits collectible
            // starting from the current cell.
            return t[i][j];
        };


        // --------------------------------------------------
        // Step 4: Calculate the first child's fruits.
        // --------------------------------------------------

        // Call child1Collect() first.
        //
        // The first child collects fruits from every cell
        // along the main diagonal.
        //
        // The collected fruits are added to firstChildScore.
        //
        // All diagonal cells are also changed to 0 so that
        // the other children cannot collect those fruits again.
        int firstChildScore = child1Collect();


        // --------------------------------------------------
        // Step 5: Calculate the second child's fruits.
        // --------------------------------------------------

        // Start the second child from the top-right corner.
        //
        // Starting coordinates:
        // i = 0
        // j = n - 1
        //
        // The second child explores the upper triangular region
        // and selects the movement that collects the maximum fruits.
        //
        // Store the maximum fruits collected in secondChildScore.
        int secondChildScore = child2Collect(0, n - 1);


        // --------------------------------------------------
        // Step 6: Calculate the third child's fruits.
        // --------------------------------------------------

        // Start the third child from the bottom-left corner.
        //
        // Starting coordinates:
        // i = n - 1
        // j = 0
        //
        // The third child explores the lower triangular region
        // and selects the movement that collects the maximum fruits.
        //
        // Store the maximum fruits collected in thirdChildScore.
        int thirdChildScore = child3Collect(n - 1, 0);


        // --------------------------------------------------
        // Step 7: Calculate the total fruits collected.
        // --------------------------------------------------

        // Add the fruits collected by all three children:
        //
        // 1. firstChildScore  -> Fruits from the main diagonal.
        // 2. secondChildScore -> Maximum fruits from the upper
        //                       triangular region.
        // 3. thirdChildScore  -> Maximum fruits from the lower
        //                       triangular region.
        //
        // Return the total number of fruits collected.
        return firstChildScore + secondChildScore + thirdChildScore;
    }
};