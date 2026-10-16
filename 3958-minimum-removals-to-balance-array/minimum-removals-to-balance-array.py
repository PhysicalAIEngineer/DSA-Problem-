# Brute Force Code & Optimal Code 
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # total number of elements in the array
        n = len(nums)
        # sort the array so that the minimum and maximum elements of window are at its ends
        nums.sort()
        # initalize the current minimum and maximum elements
        maximum_element = nums[0]
        minimum_element = nums[0]
        # variable to store the length of the logest valid subarray
        longest_length = 1
        # initilize two pointer 
        # left -> beginning of nums
        left = 0
        # right -> ends of nums
        right = 0
        # traverse the array using the right pointer
        while right < n:
            # update the current maximum and minimum elements of the window
            maximum_element = nums[right]
            minimum_element = nums[left]
            # shrink the window until its satisfies the required condition
            while left < right and maximum_element > k * minimum_element:
                left += 1
                minimum_element = nums[left]
            # update the logest valid window found so far
            longest_length = max(longest_length, right - left + 1)
            # expand the window
            right += 1
        # minimum removals equal the total number of elements minus the longest valid subarray
        return n - longest_length

# Time Complexity : O(N)
# Space Complexity : O(1)