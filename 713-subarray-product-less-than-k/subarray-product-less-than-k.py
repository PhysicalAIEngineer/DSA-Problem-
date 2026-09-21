# Brute Force Code & Optimal Code
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # if k <= 1 no positive product can be less than k
        if k <= 1:
            return 0
        # length of array
        n = len(nums)
        # total number of valid subarray
        count = 0
        # left and right pointer of sliding window
        left = 0
        right = 0
        # product of current window
        product = 1
        # expand window using right pointer
        while right < n:
            # include nums[right] in the window
            product *= nums[right]
            # if product becomes >= k shrink window from the left
            while product >= k:
                # remove nums[left] from product
                product //= nums[left]
                # move left pointer forward
                left += 1
            # all subarrays ending at right and staring from left to right are valid
            count += (right - left) + 1
            # move right pointer forward
            right += 1
        # return total number of valid subarray
        return count  

# Time Complexity : O(N)
# Space Complexity : O(1)