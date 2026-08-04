# Optimal Code
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # store the number of elements in nums1
        m = len(nums1)
        # store the number of elements in nums2
        n = len(nums2)
        # total number of elements if both arrays were combined
        size = m + n
        # find the two middle positions
        idx1 = (size // 2) - 1
        idx2 = size // 2
        # variables to store the two middle elements
        element1 = -1
        element2 = -1
        # pointer for nums1
        i = 0
        # pointer for nums2
        j = 0
        # represents the current position in the imaginary merged array
        k = 0
        # compare elements from both arrays and process them in sorted order
        while i < m and j < n:
            # if nums1 has the smaller element take the element from nums1
            if nums1[i] < nums2[j]:
                # if this is the first middle position store the element
                if k == idx1:
                    element1 = nums1[i]
                # if this is the second middle position store the element
                if k == idx2:
                    element2 = nums1[i]
                # move nums1 pointer forward
                i += 1
            else:
                # otherwise, take the element from nums2
                if k == idx1:
                    element1 = nums2[j]
                # if this is the second middle position store the element
                if k == idx2:
                    element2 = nums2[j]
                # move nums2 pointer forward
                j += 1
            # move to the next position in the imaginary merged array
            k += 1
        # if nums2 is exhausted process the remaining elements of nums1
        while i < m:
            # check if the current element is one of the middle elements
            if k == idx1:
                element1 = nums1[i]
            if k == idx2:
                element2 = nums1[i]
            # move nums1 pointer forward
            i += 1
            # move to the next merged position
            k += 1
        # if nums1 is exhausted process the remaining elements of nums2
        while j < n:
            # check if the current element is one of the middle elements
            if k == idx1:
                element1 = nums2[j]
            if k == idx2:
                element2 = nums2[j]
            # move nums2 pointer forward
            j += 1
            # move to the next merged position
            k += 1
        # if the total number of elements is odd there is only one middle element. element2 contains that middle element.
        if size % 2 == 1:
            return element2
        # if the total number of elements is even there are two middle elements.
        # median = average of the two middle elements.
        return (element1 + element2) / 2.0

# Time Complexity : O(N)
# Space Complexity : O(N)