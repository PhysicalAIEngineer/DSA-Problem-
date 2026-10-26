// Brute Force Code & Optimal Code
class Solution {
public:
    // 2D memoization table: t[prev_index][curr_index] stores the maximum length of a chain that can be built by considering pairs starting at curr_index, given that the previously selected pair is at prev_index. value of -1 means that the state has not been calculated yet prev_index can also be -1, meaning no pair has been selected but we do not store that state in the table.
    vector<vector<int>> t;
    // recursive helper function:
    // prev_index = index of the previously selected pair -1 means that no pair has been selected yet.
    // curr_index = index of the pair currently being considered.
    // returns the maximum length of a valid pair chain that can be formed from pairs[curr_index:] given the previous pair.
    int lis(vector<vector<int>>& pairs, int prev_index, int curr_index, int n) {
        // base case: if curr_index reaches n, all pairs have been considered there are no more pairs to add, so return 0.
        if (curr_index == n) {
            return 0;
        }
        // memoization check: if prev_index is valid and this state has already been calculated, return the stored answer this avoids repeatedly solving the same subproblems.
        if (prev_index != -1 && t[prev_index][curr_index] != -1) {
            return t[prev_index][curr_index];
        }
        // option 1: take the current pair.
        // initially, assume that we do not select the current pair if the current pair can be added to the chain, update this variable with the length obtained by selecting it.
        int take_current_pairs = 0;
        // pair has the form [start, end] can select the current pair if:
        // 1. prev_index == -1: no pair has been selected yet, so the current pair can be the first pair in the chain.
        // 2. pairs[curr_index][0] > pairs[prev_index][1]: current pair's start is strictly greater than the previous pair's end, so the chain condition is satisfied.
        if (prev_index == -1 || pairs[curr_index][0] > pairs[prev_index][1]) {
            // select the current pair:
            // - add 1 because this pair contributes one element to the chain.
            // - update prev_index to curr_index because the current pair becomes the last pair selected in the chain.
            // - continue considering pairs from curr_index + 1.
            take_current_pairs = 1 + lis(pairs, curr_index, curr_index + 1, n);
        }
        // option 2: skip the current pair.
        // do not include the current pair in the chain since we did not select it, prev_index remains unchanged move to the next pair and check whether a longer chain can be formed without selecting the current pair.
        int skip_current_pairs = lis(pairs, prev_index, curr_index + 1, n);
        // return the maximum chain length possible from this state.
        // compare:
        // - take_current_pairs: chain length when selecting the pair.
        // - skip_current_pairs: chain length when skipping the pair.
        int result = max(take_current_pairs, skip_current_pairs);
        // store the result if prev_index is valid this allows the answer to be reused if the same state is encountered again.
        if (prev_index != -1) {
            t[prev_index][curr_index] = result;
        }
        // return the maximum chain length for this state.
        return result;
    }
    int findLongestChain(vector<vector<int>>& pairs) {
        // store the total number of pairs in the input list.
        int n = pairs.size();
        // sort the pairs in lexicographical order: first by the starting value, then by the ending value.
        sort(pairs.begin(), pairs.end());
        // create a 2D memoization table with n rows and n columns initially, every entry is -1, meaning the state has not been calculated yet.
        t.assign(n, vector<int>(n, -1));
        // start from the first pair with no previously selected pair prev_index = -1 means the first pair in the chain can be chosen from any pair, provided the remaining pairs satisfy the chain condition.
        return lis(pairs, -1, 0, n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)