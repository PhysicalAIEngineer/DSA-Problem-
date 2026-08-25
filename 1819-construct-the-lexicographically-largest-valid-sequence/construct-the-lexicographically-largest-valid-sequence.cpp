// Brute Force Code & Optimal Code
class Solution {
public:
    bool solve(int i, int n, vector<int>& result, vector<bool>& used) {
        // base case: if i reaches the end of the result array every required number has been placed successfully since always try numbers from largest to smallest the first complete valid sequence found is the lexicographically largest sequence.
        if (i >= result.size()) {
            return true;
        }
        // if the current position is already occupied by the second occurrence of a previous number skip this position and move forward.
        if (result[i] != -1) {
            return solve(i + 1, n, result, used);
        }
        // try every number from largest to smallest trying larger numbers first helps us find the lexicographically largest sequence first.
        for (int num = n; num >= 1; num--) {
            // if this number has already been placed it cannot be used again.
            if (used[num]) {
                continue;
            }
            // TRY
            // mark the current number as used.
            used[num] = true;
            // place the first occurrence at index i.
            result[i] = num;
            // number 1 appears only once in the sequence.
            if (num == 1) {
                // continue filling the next position.
                if (solve(i + 1, n, result, used)) {
                    return true;
                }
            } else {
                // for numbers greater than 1 the two occurrences must be exactly num positions apart.
                int j = i + num;
                // second position must:
                // 1. be inside the result array.
                // 2. be currently empty.
                if (j < result.size() && result[j] == -1) {
                    // place the second occurrence of num.
                    result[j] = num;
                    // continue filling the remaining positions.
                    if (solve(i + 1, n, result, used)) {
                        return true;
                    }
                    // backtrack remove the second occurrence because this placement did not lead to a solution.
                    result[j] = -1;
                }
            }
            // UNDO / BACKTRACK
            // mark the number as unused so another placement can be tried in a different branch.
            used[num] = false;
            // remove the first occurrence from the current position.
            result[i] = -1;
        }
        // none of the available numbers can produce a valid sequence from this position.
        return false;
    }
    vector<int> constructDistancedSequence(int n) {
        // required sequence contains:
        // - one occurrence of 1
        // - two occurrences of every number from 2 to n
        // total length = 2 * n - 1.
        // initially every position is empty and represented by -1.
        vector<int> result(2 * n - 1, -1);
        // used[num] tells us whether number num has already been placed in the sequence size is n + 1 so that numbers can be accessed directly using their values.
        vector<bool> used(n + 1, false);
        // start backtracking from the first position.
        solve(0, n, result, used);
        // return the lexicographically largest valid sequence.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)