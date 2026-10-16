// Brute Force Code & Optimal Code
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        // total number of elements in both arrays
        int m = nums1.size();
        int n = nums2.size();
        // pointer for traversing nums1
        int left = 0;
        // pointer for traversing nums2
        int right = 0;
        // store the maximum valid distance
        int maximum_distance = 0;
        // traverse both arrays
        while (left < m && right < n) {
            // if the current pair is invalid move left to find a smaller value in nums1
            if (nums1[left] > nums2[right]) {
                left++;
            }
            // otherwise, the pair is valid update the maximum distance and extend the window
            else {
                maximum_distance = max(maximum_distance, right - left);
                right++;
            }
        }
        // return the maximum valid distance
        return maximum_distance;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)