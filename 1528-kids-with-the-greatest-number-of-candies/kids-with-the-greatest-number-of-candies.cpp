// Brute Force Code & Optimal Code
class Solution {
public:
    // return whether each child can have the greatest number of candies after receiving all extra candies.
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        // find the maximum number of candies currently held by any child.
        int maxCandies = *max_element(candies.begin(), candies.end());
        // store the result for each child.
        vector<bool> result;
        // check every child's candy count.
        for (int candy : candies) {
            // calculate how many candies this child would have after receiving all extra candies.
            int newCandyCount = candy + extraCandies;
            // check whether this child would have at least as many candies as the child who currently has the most candies.
            if (newCandyCount >= maxCandies) {
                result.push_back(true);
            }
            else {
                result.push_back(false);
            }
        }
        // return the result for all children.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)