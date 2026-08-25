// Brute Force Code & Optimal Code
class Solution {
public:
    void solve(vector<int>& candidates, int target,
               vector<int>& curr, vector<vector<int>>& result,
               int idx) {
        // if the remaining target becomes negative the current combination cannot be valid since all candidate values are positive adding more elements will only make the target smaller.
        if (target < 0) {
            return;
        }
        // if the remaining target becomes 0 the current combination adds up exactly to the target.
        if (target == 0) {
            // store a copy of the current combination.
            result.push_back(curr);
            return;
        }
        // try choosing every candidate starting from idx.
        for (int i = idx; i < candidates.size(); i++) {
            // skip duplicate values at the same recursion level if the first 1 has already started a branch at this level, the second 1 should not start another identical branch.
            if (i > idx && candidates[i] == candidates[i - 1]) {
                continue;
            }
            // choose candidates[i].
            curr.push_back(candidates[i]);
            // recursively process the remaining candidate pass i + 1 because every element can be used at most once.
            solve(candidates,target - candidates[i],curr,
                  result,i + 1);
            // backtrack and remove the chosen element so that we can try another candidate.
            curr.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates,
                                        int target) {
        // sort the candidates sorting places duplicate values next to each other which allows us to easily skip duplicate branches.
        sort(candidates.begin(), candidates.end());
        // store all valid combinations.
        vector<vector<int>> result;
        // store the combination currently being constructed.
        vector<int> curr;
        // start backtracking from index 0.
        solve(candidates, target, curr, result, 0);
        // return all unique combinations whose sum is equal to target.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)