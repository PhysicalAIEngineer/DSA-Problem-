# Brute Force Code
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine both arrays into one array
        merged = nums1 + nums2
        # sort the combined array this makes it easy to find the middle element
        merged.sort()
        # total number of element 
        n = len(merged)
        # if the total number of element is odd there is exactly one middle element
        if n % 2 == 1:
            # middle index is n // 2
            return float(merged[n // 2])
        # if the total number of element is even there are two middle eleement
        else:
            # index of the left middle element
            middle1 = merged[(n // 2) - 1]
            # index of the right middle element
            middle2 = merged[n // 2]
        # median is the average of the two middle  element
        return (middle1 + middle2) / 2

# Time Complexity : O(N)
# Space Complexity : O(N)