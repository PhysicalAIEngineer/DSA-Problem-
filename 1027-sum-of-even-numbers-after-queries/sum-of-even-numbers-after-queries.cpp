// Optimal Code
class Solution {
public:
    vector<int> sumEvenAfterQueries(
        vector<int>& nums,
        vector<vector<int>>& queries
    ) {
        // calculate the initial sum of all even numbers
        int sum_even = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                sum_even += num;
            }
        }
        // store the answer after each query
        vector<int> result;
        // process every query
        for (auto& query : queries) {
            // extract value and index
            int val = query[0];
            int idx = query[1];
            // if the current element is even remove its contribution from the current even sum
            if (nums[idx] % 2 == 0) {
                sum_even -= nums[idx];
            }
            // apply the update
            nums[idx] += val;
            // if the updated element is even add its contribution back
            if (nums[idx] % 2 == 0) {
                sum_even += nums[idx];
            }
            // store the current even sum
            result.push_back(sum_even);
        }
        // return the even sums after all queries
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)