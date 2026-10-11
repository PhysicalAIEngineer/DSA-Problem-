// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        // find the minimum and maximum elements
        int minimum_elements = *min_element(nums.begin(), nums.end());
        int maximum_elements = *max_element(nums.begin(), nums.end());
        // store the frequency of each number
        unordered_map<int, int> frequency;
        // count the frequency of each number
        for (int num : nums) {
            frequency[num]++;
        }
        // start filling the array from index 0
        int i = 0;
        // place numbers in sorted order from minimum to maximum
        for (int num = minimum_elements; num <= maximum_elements; num++) {
            // Repeat the number while its frequency is greater than 0
            while (frequency[num] > 0) {
                nums[i] = num;
                i++;
                // decrease the frequency after placing the number
                frequency[num]--;
            }
        }
        // return the sorted array
        return nums;
    }
};

// Time Complexity : O(1)
// Space Complexity : O(1)