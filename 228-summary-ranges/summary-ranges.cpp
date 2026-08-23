// Optimal Code
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // number of elements in the array
        int n = nums.size();
        // if the array is empty, there are no ranges to return
        if (n == 0) {
            return {};
        }
        // store the final list of ranges
        vector<string> result;
        // start processing from the first element
        int i = 0;
        // continue until every element is processed
        while (i < n) {
            // store the first number of the current range
            int start = nums[i];
            // keep moving forward while the numbers are consecutive
            while (i + 1 < n && nums[i] + 1 == nums[i + 1]) {
                i++;
            }
            // if the starting and ending numbers are different create a range such as "0->2"
            if (start != nums[i]) {
                result.push_back(
                    to_string(start) + "->" + to_string(nums[i])
                );
            }
            // otherwise, the range contains only one number
            else {
                result.push_back(to_string(start));
            }
            // move to the next unprocessed number
            i++;
        }
        // return all summarized ranges
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)