// Brute Force Code & Optimal Code
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        // try every possible person as the judge
        for (int person = 1; person <= n; person++) {
            // count how many people trust the current person
            int trusted_by = 0;
            // track whether the current person trusts someone
            bool trusts_someone = false;
            // check every trust relationship
            for (auto& relation : trust) {
                int a = relation[0];
                int b = relation[1];
                // if the current person trusts someone they cannot be the judge
                if (a == person) {
                    trusts_someone = true;
                }
                // count how many people trust the current person
                if (b == person) {
                    trusted_by++;
                }
            }
            // judge must:
            // 1. trust nobody
            // 2. be trusted by every other person
            if (!trusts_someone && trusted_by == n - 1) {
                return person;
            }
        }
        // no judge exists
        return -1;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)