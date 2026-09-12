# Brute Force Code & Optimal Code
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # total number of elements in the array
        n = len(nums)
        # count of odd numbers inside the current window
        odd_count = 0
        # number of valid subarrays ending at the current right index
        count = 0
        # total number of nice subarrays
        result = 0
        # left and right pointers of the sliding window
        left = 0
        right = 0
        # expand the window using the right pointer
        while right < n:
            # if the current element is odd add it to the odd-number count
            if nums[right] % 2 != 0:
                odd_count += 1
                # new odd number changes the possible starting positions, so reset count
                count = 0
            # shrink the window while it contains exactly k odd numbers
            while odd_count == k:
                # current window is valid can also remove leading even numbers and still have exactly k odd numbers each such choice creates another valid subarray.
                count += 1
                # if the left element is odd removing it reduces the odd count
                if nums[left] % 2 == 1:
                    odd_count -= 1
                # move the left pointer forward
                left += 1
            # every valid starting position found above creates a nice subarray ending at right
            result += count
            # move the right pointer forward
            right += 1
        # return the total number of subarrays containing exactly k odd numbers
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)