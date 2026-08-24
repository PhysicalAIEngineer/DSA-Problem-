// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of elements in nums
    int n;
    // store the minimum total cost found so far Initially, no permutation has been evaluated so use infinity.
    int minSum = INT_MAX;
    // store the permutation that produces the minimum total cost.
    vector<int> result;
    void solve(vector<int>& nums, vector<bool>& visited, vector<int>& temp,int total_sum) {
        // pruning: if the current cost is already greater than or equal to the best answer found so far this branch cannot produce a better answer.
        if (minSum <= total_sum) {
            return;
        }
        // base case: if all indices have been selected have created a complete permutation.
        if (temp.size() == n) {
            // permutation represents a cycle after reaching the last index, must return back to the first index add the cost of: last index -> first index
            total_sum += abs(temp.back() - nums[temp[0]]);
            // if this complete permutation has a smaller cost than the best answer, update the result.
            if (total_sum < minSum) {
                // store the new minimum cost
                minSum = total_sum;
                // store a copy of the current permutation
                result = temp;
            }
            return;
        }
        // try every index as the next element of the permutation.
        for (int i = 0; i < n; i++) {
            // only choose index i if it has not already been used.
            if (!visited[i]) {
                // choose index i mark it as used.
                visited[i] = true;
                // add index i to the current permutation
                temp.push_back(i);
                // calculate the cost of moving from the previous selected index to the current selected index
                // 1. temp[temp.size() - 2] -> previous index
                // 2. temp[temp.size() - 1] -> current index
                int cost = abs(temp[temp.size() - 2] - nums[temp[temp.size() - 1]]);
                // recursively select the remaining unused indices.
                solve(nums, visited, temp, total_sum + cost);
                // backtracking remove the current index from the permutation.
                temp.pop_back();
                // mark the index as unused again so it can be selected in another permutation.
                visited[i] = false;
            }
        }
    }
    vector<int> findPermutation(vector<int>& nums) {
        // store the number of elements
        n = nums.size();
        // track whether each index has already been used in the current permutation.
        vector<bool> visited(n, false);
        // start the permutation with index 0 fixing the first index to 0 helps obtain the lexicographically smallest result among permutations having the minimum cost.
        vector<int> temp = {0};
        // mark index 0 as already used
        visited[0] = true;
        // start the backtracking process initial cost is 0 because no movement has been made yet.
        solve(nums, visited, temp, 0);
        // return the permutation with the minimum total cost.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)