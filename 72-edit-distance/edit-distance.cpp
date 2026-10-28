// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization table: t[i][j] stores the minimum edit distance required to convert the first i characters of s1 into the first j characters of s2 -1 means that the state has not been calculated yet.
    vector<vector<int>> t;
    // recursive function:
    // m -> number of characters in the current prefix of s1.
    // n -> number of characters in the current prefix of s2.
    // returns the minimum number of operations required to transform s1[0 ... m-1] into s2[0 ... n-1].
    int solve(string& s1, string& s2, int m, int n) {
        // base case: if either prefix is empty, can no longer compare characters from both strings.
        if (m == 0 || n == 0) {
            // if s1's prefix is empty, insert all n characters from s2.
            // if s2's prefix is empty, delete all m characters from s1.
            // if both prefixes are empty, m + n is 0.
            return m + n;
        }
        // memoization: if this state has already been solved, return its stored minimum edit distance.
        if (t[m][n] != -1) {
            return t[m][n];
        }
        // case 1: last characters of both prefixes match.
        if (s1[m - 1] == s2[n - 1]) {
            // no operation is needed for these matching characters solve the remaining prefixes.
            t[m][n] = solve(s1, s2, m - 1, n - 1);
        } else {
            // case 2: last characters do not match must choose one of three operations:
            // 1. insert
            // 2. delete
            // 3. replace
            // each operation costs 1.
            // operation 1: Insert
            // insert the required character from s2 the remaining problem is to convert s1[0 ... m-1] into s2[0 ... n-2].
            int insertC = 1 + solve(s1, s2, m, n - 1);
            // operation 2: delete
            // delete the last character of s1 the remaining problem is to convert s1[0 ... m-2] into s2[0 ... n-1].
            int deleteC = 1 + solve(s1, s2, m - 1, n);
            // operation 3: replace
            // replace the last character of s1 with the last character of s2 both last characters are now accounted for.
            int replaceC = 1 + solve(s1, s2, m - 1, n - 1);
            // choose the operation with the minimum total cost.
            t[m][n] = min({insertC, deleteC, replaceC});
        }
        // return the computed answer it is cached for future calls to the same state.
        return t[m][n];
    }
    int minDistance(string s1, string s2) {
        // step 1: calculate the lengths of both strings.
        int m = s1.length();
        int n = s2.length();
        // step 2: initialize the memoization table.
        // there are (m + 1) possible prefix lengths for s1 and (n + 1) possible prefix lengths for s2.
        t.assign(m + 1, vector<int>(n + 1, -1));
        // Step 3: start recursion using both complete strings.
        return solve(s1, s2, m, n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)