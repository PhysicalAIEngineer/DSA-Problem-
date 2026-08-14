// Optimal Code
class Solution {
public:
    vector<int> sumEvenAfterQueries(
        vector<int>& nums,
        vector<vector<int>>& queries
    ) {
        // store the answer after processing each query
        vector<int> answer;
        // process every query
        for (auto& query : queries) {
            // extract value and index
            int value = query[0];
            int index = query[1];
            // update the value at the given index
            nums[index] = nums[index] + value;
            // calculate the sum of all even numbers
            int even_sum = 0;
            for (int num : nums) {
                // add only even numbers
                if (num % 2 == 0) {
                    even_sum += num;
                }
            }
            // store the even sum after this query
            answer.push_back(even_sum);
        }
        // return the answer for all queries
        return answer;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)