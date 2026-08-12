// Brute Force Code & Optimal Code 
class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        // number of element in the array
        int n = nums.size();
        // LIS[i] stores the length of the longest strictly increasing subsequence that ends at index i every element by itself froms increasing subsequence of length 1
        vector<int> LIS(n ,1);
        // LDS[i] stores the length of the longest strictly decreasing subsequence that start at index i every element by itself forms decreasing subsequence of length 1
        vector<int> LDS(n, 1);
        // Calcualte LIS for every index
        for (int i = 0; i < n; i++) {
            // check every element before index i
            for (int j = i - 1; j >= 0; j--) {
                // if nums[i] is greater than nums[j] then nums[i] can be added after the increasing subsequence ending at j
                if (nums[i] > nums[j]) {
                    // extend the increasing subsequnce
                    // LIS[j] = best increasing subsequence ending at j + 1 
                    LIS[i] = max(LIS[i], LIS[j] + 1);
                }
            }
        }
        // calcaulte LDS for every index 
        for (int i = n - 1; i >= 0; i--) {
            // check every element after index i 
            for (int j = i + 1; j < n; j++) {
                // if nums[i] is greater than nums[j] then nums[j] can be the next element in the decreasing part of the mountains
                if (nums[i] > nums[j]) {
                    // extend the decreasing subsequence
                    // LDS[j] = best decreasing subsequence starting at j + 1 
                    LDS[i] = max(LDS[i], LDS[j] + 1);
                }
            }
        }
        // assume that may need to remove all n element reduce this values whenever find better mountain
        int minRemovals = n;
        // try every index as the possible peak of the mountain
        for (int i = 0; i < n; i++) {
            // valid mountain must have
            // 1. least one element before the peak
            // 2. least one element after the peak
            // LIS[i] > 1 means there is an increasing part before the peak
            // LDS[i] > 1 means there is an decreasing part after the peak
            if(LIS[i] > 1 && LDS[i] > 1)
                // calculate how many element can be keep if nums[i] is the peak so left side LIS[i] and right side LDS[i] therefore peak nums[i] is counted in both so subtract 1. total element kept : LIS[i] + LDS[i] - 1 
                minRemovals = min(minRemovals, n - LIS[i] - LDS[i] + 1);
        }
        // return the minimum number of elements that must be removed to create mountains array
        return minRemovals;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)