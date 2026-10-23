// Brute Force Code & Optimal Code
class Solution {
public:
    // stores previously calculated Fibonacci numbers initially, every position contains -1, meaning the value has not been calculated yet t[i] stores the Fibonacci number F(i) size 31 supports indices from 0 to 30.
    vector<int> t;
    // recursive helper function to calculate F(n).
    int solve(int n) {
        // base case: first two Fibonacci numbers are F(0) = 0 and F(1) = 1 if n is 0 or 1, return n directly because no further recursion is required.
        if (n <= 1) {
            return n;
        }
        // memoization check: if t[n] is not -1, F(n) has already been calculated return the stored result instead of recalculating it this avoids repeatedly solving the same subproblems.
        if (t[n] != -1) {
            return t[n];
        }
        // recursive case: the fibonacci recurrence relation is:
        // F(n) = F(n - 1) + F(n - 2) calculate the two preceding fibonacci numbers add them, and store the result in t[n].
        t[n] = solve(n - 1) + solve(n - 2);
        // return the calculated fibonacci number.
        return t[n];
    }
    int fib(int n) {
        // create a vector of size 31 to store previously calculated fibonacci numbers initially, every position contains -1.
        t.assign(31, -1);
        // start the recursive calculation for the input n.
        return solve(n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)