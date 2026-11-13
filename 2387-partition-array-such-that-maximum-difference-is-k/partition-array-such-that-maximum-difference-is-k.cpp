// Brute Force Code & Optimal Code
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        // sort the array in ascending order after sorting, smaller elements appear first and larger elements appear later.
        sort(nums.begin(), nums.end());
        // store the total number of elements in the array.
        int n = nums.size();
        // store the smallest element of the current partition since the array is sorted, the first element is the smallest element of the first partition.
        int minval = nums[0];
        // initialize the partition count to 1 at least one partition is required because the array contains elements.
        int count = 1;
        // traverse all elements of the sorted array.
        for (int i = 0; i < n; i++) {
            // calculate the difference between:
            // 1. nums[i] -> current element.
            // 2. minval  -> smallest element in the current partition.
            // if this difference is greater than k the current element cannot be included in the existing partition because the array is sorted, nums[i] is the largest element encountered so far.
            if (nums[i] - minval > k) {
                // current element cannot fit in the existing partition. therefore, start a new partition and increase the total partition count.
                count++;
                // update minval to the current element it becomes the smallest element of the newly created partition.
                minval = nums[i];
            }
        }
        // return the minimum number of partitions required.
        return count;
    }
};

// Time Complexity : O(Nlong)
// Space Complexity : O(N)