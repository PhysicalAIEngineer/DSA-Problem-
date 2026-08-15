// Brute Force Code & Optimal Code
class Solution {
public:
    // vector to store all valid parenthesis combinations
    vector<string> result;
    // backtracking function to generate valid parenthesis combinations
    void solve(int n, string current, int open_count, int close_count) {
        // if the current string contains 2 * n characters store it as a valid answer
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        // add an opening parenthesis if there are still opening brackets available
        if (open_count < n) {
            solve(n,current + '(',open_count + 1,close_count);
        }
        // add a closing parenthesis only if it does not make the string invalid
        if (close_count < open_count) {
            solve(n,current + ')',open_count,close_count + 1);
        }
    }
    // generate all valid parenthesis combinations
    vector<string> generateParenthesis(int n) {
        // clear any previous results
        result.clear();
        // start backtracking with an empty string and zero opening and closing parentheses
        solve(n, "", 0, 0);
        // return all valid combinations
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)