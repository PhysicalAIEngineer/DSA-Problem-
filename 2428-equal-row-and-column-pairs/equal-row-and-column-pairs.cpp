// Brute Force Code & Optimal Code
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        // store the size of the square grid
        int n = grid.size();
        // store the total number of row column pairs that are exactly equal
        int count = 0;
        // map store how many times each row appears in the grid 
        map<vector<int>, int>mp;
        // step 1: store the frequncy of every row
        for (int row = 0; row < n; row++){
            // increase the frequency of the current row
            mp[grid[row]]++;
        }
        // step 2: generate every column and check whether it matches any sorted row
        for (int column = 0; column < n; column++) {
            // store the values of the current column
            vector<int> temp;
            // traverse every row to bulid column
            for (int row = 0; row < n; row++) {
                // add the element at row and column
                temp.push_back(grid[row][column]);
            }
            // check whether this column matches one or more rows if the column exists in the map 
            count += mp[temp];
        }
        // return the total number of equal row column pairs
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)