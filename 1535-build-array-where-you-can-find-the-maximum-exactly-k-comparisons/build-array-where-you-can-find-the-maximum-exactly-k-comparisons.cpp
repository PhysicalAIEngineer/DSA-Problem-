// Brute Force Code & Optimal Code
class Solution {
public:
    // modulo value required by the problem the number of valid arrays can become extremely large so take every result modulo 10^9 + 7.
    const int mod = 1e9 + 7;
    // 3D memoization table: t[index][searchcost][maxsofar] stores the number of ways to fill the remaining positions of the array.
    // 1. index: index of the next position to fill.
    // 2. searchcost: number of times a new maximum has been found so far.
    // 3. maxsofar: largest value encountered in the array so far.
    // dimensions:
    // 1. n + 1: indices from 0 to n.
    // 2. k + 1: search costs from 0 to k.
    // 3. m + 1: maximum values from 0 to m.
    // initially, every state contains -1, meaning it has not
    // been calculated yet.
    vector<vector<vector<int>>> t;
    // recursive helper function:
    // solve(index, searchcost, maxsofar) returns the number of ways to complete the array so that the final search cost is exactly k given the current state.
    int solve(int index, int searchcost, int maxsofar, int n, int m, int k) {
        // prune impossible states: if the search cost has already exceeded k, this state cannot produce a valid array.
        if (searchcost > k) {
            return 0;
        }
        // base case: if index == n, all n positions have been filled check whether the total search cost is exactly k if it is, the completed array is valid, so return 1 to count this array as one way otherwise, return 0 because the array is invalid.
        if (index == n) {
            return (searchcost == k) ? 1 : 0;
        }
        // memoization check: the state is determined by all three values: index, searchcost, and maxsofar if a cached answer exists, return it instead of recalculating all possible continuations.
        if (t[index][searchcost][maxsofar] != -1) {
            return t[index][searchcost][maxsofar];
        }
        // initialize the number of valid ways from this state will add the number of ways produced by choosing each possible value for the current array position.
        int number_valid = 0;
        // try every possible value from 1 through m each array element must be between 1 and m, inclusive.
        for (int i = 1; i <= m; i++) {
            // case 1: current value creates a new maximum.
            // if i > maxsofar, this value is larger than every value encountered earlier.
            // therefore:
            // - search cost increases by 1.
            // - new maximum becomes i.
            // - move to the next index and count all valid ways to complete the array from this updated state.
            if (i > maxsofar) {
                number_valid += solve(index + 1, searchcost + 1, i, n, m, k);
            }
            else {
                // case 2: current value does not create a new maximum.
                // if i <= maxsofar, the current value is not larger than the maximum encountered so far.
                // therefore:
                // - search cost remains unchanged.
                // - maxsofar remains unchanged.
                // - move to the next index and count all valid ways to complete the array from this state.
                number_valid += solve(index + 1, searchcost,  maxsofar, n, m, k
                );
            }
            // keep the accumulated number of ways within the required modulo range.
            number_valid %= mod;
        }
        // cache the result: after trying every possible value from 1 to m,
        // number_valid contains the total number of valid completions from the current state, modulo mod store it so future calls to this same state can reuse the answer.
        t[index][searchcost][maxsofar] = number_valid;
        // return the number of valid ways from this state.
        return number_valid;
    }
    int numOfArrays(int n, int m, int k) {
        // no valid array can have more than n maximum discoveries also, because all values are positive and n > 0, the search cost cannot be zero for a nonempty array.
        if (k > n || k == 0) {
            return 0;
        }
        // create a 3D memoization table every entry is initialized to -1, meaning not calculated.
        t.assign(n + 1, vector<vector<int>>(k + 1, vector<int>(m + 1, -1)));
        // start building the array from the first position.
        // 1. index = 0: no positions have been filled yet.
        // 2. searchcost = 0: no new maximum has been discovered yet.
        // 3. maxsofar = 0: initial maximum is 0 because all allowed values are positive integers from 1 to m.
        // return the number of arrays of length n whose search cost is exactly k.
        return solve(0, 0, 0, n, m, k);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)