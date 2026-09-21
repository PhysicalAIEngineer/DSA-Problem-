# Brute Force Code & Optimal Code
class Solution: 
    # count total subarrays having at most k distinct elements
    def slidingWindow(self, nums, k): 
        # frequency map of elements in current window
        mp = {} 
        # length of array
        n = len(nums) 
        # left and right pointers
        i = 0 
        j = 0 
        # total number of valid subarrays
        count = 0 
        # expand window using j
        while j < n: 
            # add nums[j] to the window
            mp[nums[j]] = mp.get(nums[j], 0) + 1 
            # if window has more than k distinct elements shrink it from the left
            while len(mp) > k: 
                # remove nums[i] from the window
                mp[nums[i]] -= 1 
                # if its frequency becomes 0 remove it from the map
                if mp[nums[i]] == 0: 
                    del mp[nums[i]] 
                # move left pointer forward
                i += 1 
            # all subarrays ending at j and starting from i to j are valid
            count += (j - i + 1) 
            # move right pointer forward
            j += 1 
        # return count of subarrays with at most k distinct elements
        return count 
    def subarraysWithKDistinct(self, nums, k):
        # exactly k distinct = (at most k) - (at most k - 1)
        return self.slidingWindow(nums, k) - self.slidingWindow(nums, k - 1)

# Time Complexity : O(N)
# Space Complexity : O(N)