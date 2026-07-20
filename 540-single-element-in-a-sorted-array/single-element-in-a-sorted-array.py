# Optimal Code
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # store the total number of elements
        n = len(nums)
        # initialize the binary search boundaries
        left = 0
        right = n - 1
        # perform binary search
        while left < right:
            # find the middle index
            mid = left + (right - left) // 2
            # check whether the number of elements from mid to right is even
            is_even = (right - mid) % 2 == 0
            # if the middle element matches the next element
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                # if the right side contains an even number of elements the single element must be on the right side
                if is_even:
                    left = mid + 2
                # otherwise, it lies on the left side
                else:
                    right = mid - 1
            # if the middle element matches the previous element
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                # if the right side contains an even number of elements, the single element lies on the left side
                if is_even:
                    right = mid - 2
                # otherwise, it lies on the right side
                else:
                    left = mid + 1
            # if the middle element matches neither neighbor it is the required single element
            else:
                return nums[mid]
        # when the search space is reduced to one element, return it
        return nums[left]

# Time Complexity : O(Nlog)
# Space Complexity : O(N)
