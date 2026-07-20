# Optimal Code
class Solution:
    # find the minimum element (pivot) in the rotated sorted array
    def findPivot(self, nums: list[int]):
        # intialize the binary search boundaries
        left = 0
        right = len(nums) - 1
        # perform binary search
        while left < right:
            # find the middle index
            mid = left + (right - left) // 2
            # if the middle element is greater than the  rightmost element the minimum must be in the right half
            if nums[mid] > nums[right]:
                # discard the left half including mid
                left = mid + 1
            # otherwise the minimum is at mid or somewhere in the left half
            else:
                right = mid
        # left pointer now points to the minium element
        return nums[left]
    # return the minimum element in the rotated sorted array 
    def findMin(self, nums: List[int]) -> int:
        # find and return the pivot element
        return self.findPivot(nums)
        
# Time Complexity : O(Nlog)
# Space Complexity : O(1)