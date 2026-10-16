# Brute Force Code & Optimal Code
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        # total number of elements in both arrays
        m = len(nums1)
        n = len(nums2)
        # pointer for traversing nums1
        left = 0
        # pointer for traversing nums2
        right = 0
        # variable to store the maximum valid distance
        maximum_distance = 0
        # traverse both arrays
        while left < m and right < n:
            # if the current pair is invalid (nums1[left] > nums2[right]), move the left pointer to find a smaller value in nums1
            if nums1[left] > nums2[right]:
                left += 1
            # otherwise, the current pair is valid update the maximum distance and try extending the distance by moving the right pointer
            else:
                maximum_distance = max(maximum_distance,right - left)
                right += 1
        # return the maximum valid distance
        return maximum_distance

# Time Complexity : O(N)
# Space Complexity : O(N)