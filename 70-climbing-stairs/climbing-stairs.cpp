// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization array: t[i] stores the number of distinct ways to climb exactly i stairs value of -1 means that the answer has not been calculated yet size 46 supports indices from 0 to 45.
    vector<int> t;
    // recursive helper function that returns the number of ways to climb exactly n stairs.
    int solve(int n) {
        // base case 1: if there are 0 stairs, there is exactly 1 way to stay where are take no steps.
        if (n == 0) {
            return 1;
        }
        // base cases 2 and 3: if n == 1, there is 1 way: take one 1-step move. if n == 2, there are 2 ways:  1. take two 1-step moves. or 2. take one 2-step move.
        if (n == 1 || n == 2) {
            return n;
        }
        // memoization check: if t[n] is not -1 have already calculated the answer for n stairs, so return the cached result.
        if (t[n] != -1) {
            return t[n];
        }
        // recursive case: the final move to stair n must be either: 1. 1-step move from stair n - 1. number of ways: solve(n - 1)  2. 2-step move from stair n - 2. number of ways: solve(n - 2) these possibilities are distinct, so add their counts.
        int a = solve(n - 1);
        int b = solve(n - 2);
        // store the calculated answer so future calls can reuse it without repeating the recursive calculations.
        t[n] = a + b;
        // return the total number of distinct ways to climb n stairs.
        return t[n];
    }
    int climbStairs(int n) {
        // initialize all 46 positions to -1, indicating that their answers have not been calculated yet.
        t.assign(46, -1);
        // start the recursive calculation for the original problem.
        return solve(n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)