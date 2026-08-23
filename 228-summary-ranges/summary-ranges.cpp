// Brute Force Code & Optimal Code
class Solution {
public:
    // convert consecutive numbers into ranges and return them as strings.
    vector<string> summaryRanges(vector<int>& nums) {
        // store the final list of ranges.
        vector<string> result;
        // start processing from the first element.
        int i = 0;
        // continue until every number has been processed.
        while (i < nums.size()) {
            // store the first number of the current range.
            int start = nums[i];
            // store the current consecutive number.
            int current = nums[i];
            // start checking from the next element.
            int j = i + 1;
            // continue while there are more elements to check.
            while (j < nums.size()) {
                // check whether the next number is consecutive with the current number.
                if (nums[j] == current + 1) {
                    // extend the current range.
                    current = nums[j];
                    // move to the next element.
                    j++;
                }
                else {
                    // gap means the current range has ended.
                    break;
                }
            }
            // if the range contains only one number store only that number.
            if (start == current) {
                result.push_back(to_string(start));
            }
            else {
                // if the range contains multiple consecutive numbers store it as "start->end".
                result.push_back(to_string(start) + "->" + to_string(current));
            }
            // continue from the first element that was not part of the current range.
            i = j;
        }
        // return all summarized ranges.
        return result;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)