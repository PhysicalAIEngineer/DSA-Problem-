// Brute Force Code & Optimal Code
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        // store the total number of elements
        int n = nums.size();
        // stores the frequency of elements in the left subarray
        unordered_map<int, int> mp1;
        // stores the frequency of elements in the right subarray
        unordered_map<int, int> mp2;
        // initially, all elements belong to the right subarray
        for (int num : nums) {
            mp2[num]++;
        }
        // try every possible index as the partition point
        for (int i = 0; i < n; i++) {
            // current element
            int num = nums[i];
            // move the current element from the right subarray to the left subarray
            mp1[num]++;
            mp2[num]--;
            // calculate the size of the left subarray left subarray = nums[0 ... i]
            int n1 = i + 1;
            // calculate the size of the right subarray right subarray = nums[i + 1 ... n-1]
            int n2 = n - i - 1;
            // check if 'num' is dominant in the left subarray and also dominant in the right subarray an element is dominant if: frequency * 2 > subarray size
            if (mp1[num] * 2 > n1 && mp2[num] * 2 > n2) {
                // found the smallest valid partition index
                return i;
            }
        }
        // no valid partition index was found
        return -1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)