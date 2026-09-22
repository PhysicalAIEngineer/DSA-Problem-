// Brute Force Code & Optimal Code
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        // length of the array
        int n = nums.size();
        // create a doubled array this helps us handle the circular nature of nums
        vector<int> temp(2 * n);
        // copy nums twice
        for (int i = 0; i < 2 * n; i++) {
            temp[i] = nums[i % n];
        }
        // total number of 1s in the array this will be the required window size
        int countones = accumulate(nums.begin(), nums.end(), 0);
        // sliding window pointers
        int i = 0;
        int j = 0;
        // number of 1s in the current window
        int currcount = 0;
        // maximum number of 1s found in any valid window
        int maxcount = 0;
        // traverse the doubled array
        while (j < 2 * n) {
            // if current element is 1 add it to the current window count
            if (temp[j] == 1) {
                currcount++;
            }
            // window size should not be greater than the total number of 1s
            if (j - i + 1 > countones) {
                // remove the leftmost element from the current window
                currcount -= temp[i];
                i++;
            }
            // store the maximum number of 1s present in any window of size countones
            maxcount = max(maxcount, currcount);
            // move right pointer forward
            j++;
        }
        // minimum swaps needed = total 1s - maximum 1s already present together
        return countones - maxcount;
    }
};

// Time Complexitey : O(N)
// Space Complexity : O(N)