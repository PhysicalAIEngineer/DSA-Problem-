# Brute Force Code & Optimal Code
class Solution:
    def find_first_position(self, nums: list[int], target: int) -> int:
        # initialize the left boundary of the binary search as index 0 is the first element of the array.
        left = 0
        # initialize the right boundary of the binary search as len(nums) - 1 is the index of the last element.
        right = len(nums) - 1
        # store the index of the first occurrence of target initially, assume target does not exist in the array if target is never found, result will remain -1.
        result = -1
        # continue binary search while the search range is valid when left becomes greater than right, no elements remain to search.
        while left <= right:
            # calculate the middle index of the current search range this formula avoids calculating (left + right) directly.
            mid = left + (right - left) // 2
            # check whether the middle element equals the target.
            if nums[mid] == target:
                # found an occurrence of target store its index as a possible first occurrence.
                result = mid
                # search further in the left half there might be another occurrence of target at an index smaller than the current mid.
                right = mid - 1
            # if the middle element is greater than target the target can only exist in the left half this works because the array is sorted in ascending order.
            elif nums[mid] > target:
                # move the right boundary to the element immediately before the middle index.
                right = mid - 1
            # if the middle element is smaller than target the target can only exist in the right half.
            else:
                # move the left boundary to the element immediately after the middle index.
                left = mid + 1
        # return the first occurrence found if target does not exist, return -1.
        return result
    def find_last_position(self, nums: list[int], target: int) -> int:
        # initialize the left boundary of the binary search.
        left = 0
        # initialize the right boundary of the binary search.
        right = len(nums) - 1
        # store the index of the last occurrence of target initially, assume target does not exist in the array.
        result = -1
        # continue binary search while the search range is valid.
        while left <= right:
            # calculate the middle index of the current search range.
            mid = left + (right - left) // 2
            # check whether the middle element equals the target.
            if nums[mid] == target:
                # found an occurrence of target store its index as a possible last occurrence.
                result = mid
                # search further in the right half there might be another occurrence of target at an index greater than the current mid.
                left = mid + 1
            # if the middle element is greater than target the target can only exist in the left half.
            elif nums[mid] > target:
                # move the right boundary to the element immediately before the middle index.
                right = mid - 1
            # if the middle element is smaller than target the target can only exist in the right half.
            else:
                # move the left boundary to the element immediately after the middle index.
                left = mid + 1
        # return the last occurrence found if target does not exist, return -1.
        return result
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # perform binary search to find the first occurrence of target in the sorted array.
        left = self.find_first_position(nums, target)
        # perform another binary search to find the last occurrence of target in the sorted array.
        right = self.find_last_position(nums, target)
        # return both positions in the required format: [first occurrence, last occurrence] if target does not exist: left = -1 and right = -1, so the result becomes [-1, -1].
        return [left, right]

# Time Complexity : O(NlogN)
# Space Complexity : O(N)