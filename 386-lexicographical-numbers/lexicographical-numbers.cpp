// Brute Force Code & Optimal Code
class Solution {
public:
    // recursive function to generate numbers in lexicographical order
    void solve(int current, int n, vector<int>& result) {
        // stop if the current number exceeds n
        if (current > n) {
            return;
        }
        // add the current number to the result
        result.push_back(current);
        // try appending digits from 0 to 9
        for (int next_digit = 0; next_digit <= 9; next_digit++) {
            // create the next number by appending next_digit to current
            int next_num = current * 10 + next_digit;
            // no need to continue if the number exceeds n
            if (next_num > n) {
                return;
            }
            // recursively generate the next lexicographical number
            solve(next_num, n, result);
        }
    }
    // return numbers from 1 to n in lexicographical order
    vector<int> lexicalOrder(int n) {
        // store the final lexicographical order
        vector<int> result;
        // start DFS from every leading digit from 1 to 9
        for (int num = 1; num <= 9; num++) {
            solve(num, n, result);
        }
        // return the result
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)