# Brute Force Code & Optimal Code
import heapq 
class Solution: 
    def longestSubarray(self, nums, limit): 
        # length of the array
        n = len(nums) 
        # max heap: store (-value, index) because Python has only min heap negative value makes the largest value appear at the top
        maxPq = [] 
        # min heap: store (value, index)
        minPq = [] 
        # sliding window pointers
        i = 0 
        j = 0 
        # store maximum valid window length
        maxLength = 0 
        # expand the window using j
        while j < n: 
            # add current element to max heap
            heapq.heappush(maxPq, (-nums[j], j))
            # add current element to min heap
            heapq.heappush(minPq, (nums[j], j)) 
            # check whether current window is invalid max value - min value must be <= limit
            while -maxPq[0][0] - minPq[0][0] > limit: 
                # temporary value this line is overwritten below
                i = min(-maxPq[0][0], minPq[0][0])  
                # move left pointer just after the index of the smaller-indexed extreme element
                i = min(maxPq[0][1], minPq[0][1]) + 1 
                # remove outdated elements from max heap whose index is outside the current window
                while maxPq and maxPq[0][1] < i: 
                    heapq.heappop(maxPq) 
                # remove outdated elements from min heap whose index is outside the current window
                while minPq and minPq[0][1] < i: 
                    heapq.heappop(minPq) 
            # current window [i...j] is valid update maximum window length
            maxLength = max(maxLength, j - i + 1) 
            # move right pointer forward
            j += 1 
        # return longest valid subarray length
        return maxLength

# Time Complexity : O(N)
# Space Complexity : O(N)