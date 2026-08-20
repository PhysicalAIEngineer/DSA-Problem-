// Brute Force Code & Optimal Code
class Solution {
public:
    // recursive function to check whether the square string can be partitioned into numbers whose sum equals num
    bool check(int i, int current_sum, string& s, int num,
              vector<vector<int>>& dp) {
        // base case: if all digits have been processed return true only if the accumulated sum equals num
        if (i == s.length()) {
            return current_sum == num;
        }
        // prune the recursion if the current sum already exceeds the target value
        if (current_sum > num) {
            return false;
        }
        // return the previously computed result for this state if available
        if (dp[i][current_sum] != -1) {
            return dp[i][current_sum];
        }
        // store whether a valid partition exists
        bool possible = false;
        // try every possible substring starting at index i
        for (int j = i; j < s.length(); j++) {
            // convert the substring s[i...j] into an integer
            int addend = stoi(s.substr(i, j - i + 1));
            // recursively check the remaining part after adding the current number
            possible = possible || check(j + 1, current_sum + addend, s, num, dp);
            // if a valid partition is found memoize and return immediately
            if (possible) {
                dp[i][current_sum] = 1;
                return true;
            }
        }
        // memoize the result for the current state
        dp[i][current_sum] = possible ? 1 : 0;
        // return whether a valid partition exists
        return possible;
    }
    // return the punishment number from 1 to n
    int punishmentNumber(int n) {
        // store the final punishment number
        int punishment_number = 0;
        // check every number from 1 to n
        for (int num = 1; num <= n; num++) {
            // compute the square of the current number
            int square_num = num * num;
            // convert the square into a string so it can be partitioned
            string s = to_string(square_num);
            // DP table for memoization: dp[index][current_sum]
            vector<vector<int>> dp(s.length(), vector<int>(num + 1, -1));
            // if the square can be partitioned into numbers whose sum equals num, add the square to the answer
            if (check(0, 0, s, num, dp)) {
                punishment_number += square_num;
            }
        }
        // return the total punishment number
        return punishment_number;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)