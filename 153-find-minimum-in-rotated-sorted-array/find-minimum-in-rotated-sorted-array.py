class Solution:
    def findPivot(self, nums: list[int]):
        # intialize the left boundary of the binary search initially search starts from the first elements
        left = 0
        # initalize the right boundary of the binary search len(nums) - 1 represents the index of the last elements
        right = len(nums) - 1
        # continue binary search while the search range contains more than one element onece left == right both pointer indicates the minimum elements
        while left < right:
            # calcualte the middle index of the current search range using the formula avoids directly adding left and right
            mid = left + (right - left) // 2
            # compare the middle element with the rightmost element if nums[mid] > nums[right] the middle element belongs to the left larget position of the rotated array therefore the minimum element must be to the right of mid
            if nums[mid] > nums[right]:
                # discard the left portions including nums[mid] cannot be the minimum because it is geater than nums[right] move the left boundary immediately after mid
                left = mid + 1
            else:
                # if nums[mid] <= nums[right] the minimum element must be at mid or somewhere to its left keep mid in the search range because nums[mid] itself could be the minimum element move the right bounary to mid
                right = mid
        # binary search ends when left == right both pointer now point to the index of the minimum element return the minimum values from the array
        return nums[left]
    def findMin(self, nums: list[int]) -> int:
        # findpivot perfrom binary search and return the minimum values not its index
        return self.findPivot(nums)

# Time Complexity : O(NlogN)
# Space Complexity : O(N)