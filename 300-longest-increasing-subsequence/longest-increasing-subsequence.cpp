// Brute Force Code & Optimal Code
class Solution {
public:
    // 2D memoization table: t[prev_index][curr_index] stores the length of the longest increasing subsequence that can be built by considering elements starting from curr_index, given that the previously selected element is at prev_index a value of -1 means that this state has not been calculated yet.
    vector<vector<int>> t;
    // recursive helper function:
    // prev_index = index of the previously selected element -1 means that no element has been selected yet.
    // curr_index = index of the element currently being considered.
    // Returns the maximum length of an increasing subsequence that can be formed from nums[curr_index:] while preserving increasing order.
    int longest_increasing_subsequence(vector<int>& nums, int prev_index,int curr_index, int n) {
        // base case: if curr_index reaches n, we have processed every element no more elements can be added, so return 0.
        if (curr_index == n) {
            return 0;
        }
        // memoization check: use the memoization table only when prev_index is a valid array index because the table has no separate row for -1 if this state has already been calculated, return the stored answer instead of repeating the recursive work.
        if (prev_index != -1 && t[prev_index][curr_index] != -1) {
            return t[prev_index][curr_index];
        }
        // option 1: Take the current element.
        // initially, assume we do not take the current element if taking it is valid, we will calculate its result below.
        int take_current_element = 0;
        // select nums[curr_index] if either:
        // 1. prev_index == -1: no element has been selected yet, so any element can be the first element of the increasing subsequence.
        // 2. nums[curr_index] > nums[prev_index]: current element is strictly greater than the previously selected element, so taking it preserves the strictly increasing order.
        if (prev_index == -1 || nums[curr_index] > nums[prev_index]) {
            // take the current element:
            // 1. add 1 because nums[curr_index] becomes part of the increasing subsequence.
            // 2. update prev_index to curr_index because the current element is now the most recently selected element.
            // 3. move to curr_index + 1 to process the next element.
            take_current_element = 1 + longest_increasing_subsequence(nums,curr_index, curr_index + 1, n);
        }
        // option 2: skip the current element do not include nums[curr_index] in the subsequence since we did not select this element, prev_index remains unchanged. simply move to the next array index.
        int skip_current_element = longest_increasing_subsequence(nums,prev_index, curr_index + 1, n);
        // calculate the better result from the take and skip choices.
        int answer = max(take_current_element, skip_current_element);
        // store the result only if prev_index is valid do not store the state where prev_index == -1 because this implementation reserves no separate row for that state.
        if (prev_index != -1) {
            t[prev_index][curr_index] = answer;
        }
        // return the maximum length obtainable from the current state.
        return answer;
    }
    int lengthOfLIS(vector<int>& nums) {
        // store the total number of elements in the input array.
        int n = nums.size();
        // create a 2D memoization table with n rows and n columns initially, every entry is -1, meaning it has not been calculated.
        t.assign(n, vector<int>(n, -1));
        // start at index 0 with prev_index = -1 this means no element has been selected yet, so the first element of the subsequence can be chosen from anywhere in the array while preserving the original element order.
        return longest_increasing_subsequence(nums, -1, 0, n);
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N^2)