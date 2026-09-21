# Brute Force Code & Optimal Code
class Solution:
    def maxSubarrayLength(self, nums, k):
        # length of the array
        n = len(nums)
        # frequency map mp[x] = number of times * appears in current window
        mp = {}
        # left and right pointer
        i = 0
        j = 0
        # maximum valid subarray length
        result = 0
        # expand window using j
        while j < n:
            # add nums[j] to the current window
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            # if the frequency of nums[j] becomes greater than k shrink the window form the left
            while i < j and mp[nums[j]] > k:
                # remove nums[i] from the frequency map
                mp[nums[i]] -= 1
                # move left pointer forward
                i += 1
            # current window valid update maximum length
            result = max(result, j - i + 1)
            # move right pointer forward
            j += 1
        # return maximum valid subarray length
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)